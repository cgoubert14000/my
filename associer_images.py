#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=======================================================================
 ASSOCIER_IMAGES.py  -  prend TOUTES les images d'un dossier, quel que
                        soit leur nom, et en fait un planning pret
=======================================================================

 Le probleme :
   le bot cherche "01.jpg", "02.jpg"... mais tes fichiers s'appellent
   humour_noir_couple_20261012_1likes_577164508518853291
   -> impossible de faire le lien en se fiant au nom.

 La solution :
   ce script REGARDE LE CONTENU des fichiers (et non leur nom), garde
   tout ce qui est vraiment une image, en fait des copies propres
   numerotees 01.jpg, 02.jpg... et ecrit un planning qui va avec.

 UTILISATION :

   python associer_images.py                  -> analyse, ne touche a rien
   python associer_images.py --preparer       -> cree les copies + planning_auto.txt
   python associer_images.py --preparer --limite 20     -> les 20 premieres
   python associer_images.py --preparer --ordre date    -> tri par date d'ajout
   python associer_images.py --preparer --ordre hasard  -> ordre aleatoire

 ENSUITE, on programme avec le planning genere :

   python programmer.py "demain" --planning planning_auto.txt --par-jour 5 --limite 20 --test

 Qui est pris ? TOUS les fichiers d'images du ou des dossiers detectes
 (images/, image/, ...), y compris ceux qui n'ont AUCUNE extension.
 Qui est ignore ? le texte, les .zip, les .json, le CREDITS.txt, les
 fichiers illisibles, et les copies deja generees par ce script.

 Ce script ne SUPPRIME et ne MODIFIE JAMAIS tes fichiers d'origine :
 il se contente d'ajouter des copies.
=======================================================================
"""

import os
import re
import sys
import json
import random
import hashlib
import argparse
import datetime

DOSSIER = os.path.dirname(os.path.abspath(__file__))

# Dossiers ou l'on va chercher les images
CANDIDATS = ("images", "image", "Images", "Image", "photos", "photo")

# --- reconnaissance par le CONTENU (les 32 premiers octets) ---------
SIGNATURES = (
    (b"\xff\xd8\xff", "jpg"),
    (b"\x89PNG\r\n\x1a\n", "png"),
    (b"GIF87a", "gif"),
    (b"GIF89a", "gif"),
    (b"BM", "bmp"),
    (b"II*\x00", "tiff"),
    (b"MM\x00*", "tiff"),
)
RIFF = b"RIFF"
WEBP = b"WEBP"
IPTC = b"ftyp"

# extensions connues qui ne sont JAMAIS des images : on ne les ouvre meme pas
EXT_A_JETER = (".zip", ".rar", ".7z", ".txt", ".md", ".json", ".ini", ".db",
               ".py", ".exe", ".lnk", ".url", ".csv", ".log", ".bak", ".tmp",
               ".html", ".htm", ".xml", ".pdf", ".mp4", ".mkv", ".mov")

# ce que Facebook accepte comme image
EXT_FACEBOOK = ("jpg", "jpeg", "png", "gif", "bmp", "tif", "tiff", "webp")

HASHTAGS_DEFAUT = "#humour #humoriste #drole #rire #humournoir"


# ---------------------------------------------------------------------
# Affichage
# ---------------------------------------------------------------------
def titre(txt):
    print()
    print("=" * 66)
    print(" " + txt)
    print("=" * 66)


def ok(txt):
    print("  [OK]  " + txt)


def ko(txt):
    print("  [X]   " + txt)


def info(txt):
    print("        " + txt)


# ---------------------------------------------------------------------
# Reconnaissance d'une image par son contenu
# ---------------------------------------------------------------------
def type_reel(chemin, lire_pillow=True):
    """Retourne l'extension reelle ('jpg', 'png'...) ou None."""
    try:
        with open(chemin, "rb") as f:
            tete = f.read(32)
    except Exception:
        return None

    if len(tete) < 12:
        return None

    for sig, ext in SIGNATURES:
        if tete.startswith(sig):
            return ext

    if tete[:4] == RIFF and tete[8:12] == WEBP:
        return "webp"

    if tete[4:8] == IPTC:
        marque = tete[8:12]
        if marque in (b"heic", b"heix", b"hevc", b"mif1", b"msf1", b"avif"):
            return "heic"

    # dernier recours : Pillow, s'il est installe (valide aussi le fichier)
    if lire_pillow:
        try:
            from PIL import Image
            with Image.open(chemin) as im:
                im.verify()
            f = (im.format or "").lower()
            return {"jpeg": "jpg"}.get(f, f) or None
        except ImportError:
            return None
        except Exception:
            return None

    return None


def md5(chemin):
    h = hashlib.md5()
    try:
        with open(chemin, "rb") as f:
            for bloc in iter(lambda: f.read(65536), b""):
                h.update(bloc)
        return h.hexdigest()
    except Exception:
        return None


def cle_naturelle(nom):
    """Tri 'humain' : 2.jpg avant 10.jpg."""
    parties = re.split(r"(\d+)", nom)
    return [(1, int(t)) if t.isdigit() else (0, t.lower()) for t in parties]


# ---------------------------------------------------------------------
# Dossiers a explorer
# ---------------------------------------------------------------------
def charger_config():
    chemin = os.path.join(DOSSIER, "config.json")
    if os.path.exists(chemin):
        try:
            with open(chemin, encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {}


def dossiers_source(cfg):
    """Tous les dossiers existants ou chercher des images."""
    trouves = []
    vu = set()

    def ajouter(nom):
        chemin = nom if os.path.isabs(nom) else os.path.join(DOSSIER, nom)
        cle = os.path.normcase(os.path.abspath(chemin))
        if cle in vu:
            return
        vu.add(cle)
        if os.path.isdir(chemin):
            trouves.append((nom, chemin))

    if cfg.get("DOSSIER_IMAGES"):
        ajouter(cfg["DOSSIER_IMAGES"])
    for nom in CANDIDATS:
        ajouter(nom)

    return trouves


def inventaire(chemins, ignorer_noms=(), deja_traites=()):
    """Liste (chemin, dossier, nom, type, taille) de toutes les images."""
    images, non_images, ignores = [], [], []
    vus_md5 = {}

    for etiquette, dossier in chemins:
        try:
            contenu = sorted(os.listdir(dossier))
        except Exception:
            continue

        for nom in contenu:
            chemin = os.path.join(dossier, nom)
            if not os.path.isfile(chemin):
                continue
            if nom.startswith(".") or nom.lower() == "desktop.ini":
                continue
            if nom in ignorer_noms:
                ignores.append((dossier, nom))
                continue
            if nom.lower().endswith(EXT_A_JETER):
                non_images.append((dossier, nom, "extension non-image"))
                continue

            type_ = type_reel(chemin)
            if not type_:
                non_images.append((dossier, nom, "contenu non reconnu"))
                continue

            empreinte = md5(chemin)

            # deja preparee lors d'un passage precedent ?
            if empreinte and empreinte in deja_traites:
                non_images.append((dossier, nom, "deja preparee (deja en ligne)"))
                continue

            # doublon strict : meme contenu deja vu
            if empreinte and empreinte in vus_md5:
                non_images.append(
                    (dossier, nom, "doublon de " + vus_md5[empreinte]))
                continue
            if empreinte:
                vus_md5[empreinte] = nom

            images.append({
                "chemin": chemin,
                "dossier": etiquette,
                "nom": nom,
                "type": type_,
                "taille": os.path.getsize(chemin),
                "md5": empreinte,
            })

    return images, non_images, ignores


# ---------------------------------------------------------------------
# Conversion (facultative, avec Pillow)
# ---------------------------------------------------------------------
def convertir_jpeg(source, cible):
    try:
        from PIL import Image
    except ImportError:
        return False
    try:
        im = Image.open(source)
        if im.mode in ("RGBA", "LA", "P") or "transparency" in im.info:
            im = im.convert("RGBA")
            fond = Image.new("RGB", im.size, (255, 255, 255))
            fond.paste(im, mask=im.split()[-1])
            im = fond
        else:
            im = im.convert("RGB")
        # on limite la largeur a 1440 px : inutile de publier plus gros
        if im.width > 1440:
            h = int(im.height * 1440 / im.width)
            im = im.resize((1440, h), Image.LANCZOS)
        im.save(cible, "JPEG", quality=92, optimize=True)
        return True
    except Exception:
        return False


def numero_libre(dossier, ext, depart=1):
    n = depart
    while True:
        nom = "%02d.%s" % (n, ext)
        if not os.path.exists(os.path.join(dossier, nom)):
            return n
        n += 1


# ---------------------------------------------------------------------
# Programme principal
# ---------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser(
        description="Fait un planning a partir de TOUTES les images d'un "
                    "dossier, sans se fier a leur nom.")
    ap.add_argument("--preparer", action="store_true",
                    help="Cree les copies numerotees + planning_auto.txt")
    ap.add_argument("--ordre", choices=("nom", "date", "hasard"), default="nom",
                    help="Ordre de publication (defaut : nom)")
    ap.add_argument("--limite", type=int, default=None,
                    help="Ne prendre que les N premieres images")
    ap.add_argument("--dossier", default=None,
                    help="Dossier des images (defaut : images/ ou image/)")
    ap.add_argument("--sortie", default=None,
                    help="Dossier ou ecrire les copies (defaut : celui du bot)")
    ap.add_argument("--planning", default="planning_auto.txt",
                    help="Nom du planning a ecrire")
    ap.add_argument("--hashtags", default=None,
                    help="Hashtags a utiliser (defaut : ceux de planning.txt)")
    ap.add_argument("--tout", action="store_true",
                    help="Reprendre aussi les images deja preparees "
                         "auparavant (creerait des doublons)")
    ap.add_argument("--oui", action="store_true",
                    help="Ne pas demander de confirmation")
    args = ap.parse_args()

    titre("ASSOCIER LES IMAGES AU PLANNING")

    cfg = charger_config()

    # --- ou chercher -------------------------------------------------
    if args.dossier:
        chemin = args.dossier if os.path.isabs(args.dossier) \
            else os.path.join(DOSSIER, args.dossier)
        if not os.path.isdir(chemin):
            ko("Dossier introuvable : " + chemin)
            sys.exit(1)
        chemins = [(args.dossier, chemin)]
    else:
        chemins = dossiers_source(cfg)

    if not chemins:
        ko("Aucun dossier d'images trouve (ni images/, ni image/).")
        info("Dossier du bot : " + DOSSIER)
        info("Dis-moi ou sont tes images : --dossier \"C:\\chemin\\vers\\images\"")
        sys.exit(1)

    print()
    print("  Dossiers explores :")
    for etiquette, chemin in chemins:
        n = len([f for f in os.listdir(chemin)
                 if os.path.isfile(os.path.join(chemin, f))])
        print("      %-12s %s  (%d fichiers)" % (etiquette + "/", chemin, n))

    # --- dossier de sortie -------------------------------------------
    nom_sortie = args.sortie or cfg.get("DOSSIER_IMAGES") or "images"
    dossier_sortie = nom_sortie if os.path.isabs(nom_sortie) \
        else os.path.join(DOSSIER, nom_sortie)

    chemin_planning = os.path.join(
        DOSSIER, os.path.basename(args.planning))

    # images deja preparees lors d'un passage precedent
    chemin_etat = os.path.join(DOSSIER, "images_traitees.json")
    deja_traites = set()
    if not args.tout and os.path.exists(chemin_etat):
        try:
            with open(chemin_etat, encoding="utf-8") as f:
                deja_traites = set(json.load(f).get("md5", []))
        except Exception:
            deja_traites = set()

    # les images deja listees dans ce planning ne sont pas reprises
    ignorer = set()
    if os.path.exists(chemin_planning):
        try:
            with open(chemin_planning, encoding="utf-8") as f:
                for ligne in f:
                    if ligne.strip().upper().startswith("IMAGE:"):
                        ignorer.add(ligne.split(":", 1)[1].strip())
        except Exception:
            pass

    # --- inventaire --------------------------------------------------
    titre("CE QU'IL Y A VRAIMENT DANS LES DOSSIERS")

    images, non_images, ignores = inventaire(chemins, ignorer, deja_traites)

    if not images and deja_traites:
        ko("Aucune NOUVELLE image a preparer.")
        info("%d image(s) de ce dossier ont deja ete preparees et sont"
             % len(deja_traites))
        info("deja listees dans %s." % os.path.basename(args.planning))
        info("Pour les reprendre quand meme (doublons possibles) :")
        info("      python associer_images.py --preparer --tout")
        sys.exit(0)

    if not images:
        ko("Aucune image valide trouvee.")
        info("Verifie que les fichiers sont bien la (et pas seulement")
        info("dans un ZIP non extrait).")
        if non_images:
            info("Fichiers ecartes :")
            for dossier, nom, raison in non_images[:10]:
                info("  %s (%s)" % (nom, raison))
        sys.exit(1)

    if args.ordre == "date":
        images.sort(key=lambda i: os.path.getmtime(i["chemin"]))
    elif args.ordre == "hasard":
        random.shuffle(images)
    else:
        images.sort(key=lambda i: cle_naturelle(i["nom"]))

    total_trouve = len(images)
    if args.limite:
        images = images[:args.limite]

    print()
    ok("%d image(s) valide(s) reconnue(s) d'apres leur CONTENU." % total_trouve)
    if args.limite and args.limite < total_trouve:
        info("On ne garde que les %d premieres (--limite)." % args.limite)

    types = {}
    for i in images:
        types[i["type"]] = types.get(i["type"], 0) + 1
    print()
    print("      formats : " + ", ".join(
        "%s x%d" % (t, n) for t, n in sorted(types.items())))

    print()
    print("  Ordre retenu (%s) :" % args.ordre)
    for n, i in enumerate(images, 1):
        if n > 12:
            print("      ... (+%d)" % (len(images) - 12))
            break
        nom = i["nom"]
        if len(nom) > 46:
            nom = nom[:43] + "..."
        print("      %2d. %-46s [%s] %s"
              % (n, nom, i["type"], i["dossier"] + "/"))

    if non_images:
        print()
        ko("%d fichier(s) ecarte(s) :" % len(non_images))
        for dossier, nom, raison in non_images[:10]:
            nom_affiche = nom if len(nom) <= 44 else nom[:41] + "..."
            print("      %-46s (%s)" % (nom_affiche, raison))
        if len(non_images) > 10:
            print("      ... (+%d)" % (len(non_images) - 10))

    if ignores:
        print()
        info("%d fichier(s) deja dans %s, donc non repris."
             % (len(ignores), os.path.basename(args.planning)))

    # --- hashtags ----------------------------------------------------
    hashtags = args.hashtags
    if not hashtags:
        for fichier in (cfg.get("FICHIER_PLANNING", "planning.txt"),):
            p = os.path.join(DOSSIER, fichier)
            if not os.path.exists(p):
                continue
            try:
                with open(p, encoding="utf-8") as f:
                    for ligne in f:
                        if ligne.strip().upper().startswith("HASHTAGS:"):
                            hashtags = ligne.split(":", 1)[1].strip()
                            break
            except Exception:
                pass
            if hashtags:
                break
    if not hashtags:
        hashtags = HASHTAGS_DEFAUT

    # --- simulation --------------------------------------------------
    if not args.preparer:
        titre("PLANIFICATION")
        print()
        info("Mode analyse : rien n'a ete ecrit.")
        info("Pour creer les copies numerotees et le planning :")
        info("      python associer_images.py --preparer")
        if args.limite:
            info("      python associer_images.py --preparer --limite %d"
                 % args.limite)
        print()
        info("Ensuite tu programmeras avec :")
        info('  python programmer.py "demain" --planning %s '
             "--par-jour 5 --limite 20 --test"
             % os.path.basename(args.planning))
        print()
        return

    # --- preparation -------------------------------------------------
    titre("PREPARATION DES FICHIERS")

    if not args.oui:
        print("  %d image(s) vont etre copiees dans :" % len(images))
        print("      " + dossier_sortie)
        rep = input("  Continuer ? (oui/non) > ")
        if rep.strip().lower() not in ("oui", "o", "yes", "y"):
            print("  Annule.\n")
            return

    os.makedirs(dossier_sortie, exist_ok=True)

    try:
        from PIL import Image  # noqa: F401
        pillow = True
    except ImportError:
        pillow = False

    if not pillow:
        print()
        info("Pillow n'est pas installe : les fichiers seront copies tels")
        info("quels (format d'origine conserve). Pour tout passer en JPEG :")
        info("      pip install pillow")

    correspondance = []
    copies, convertis, echecs = 0, 0, []
    numero = 1

    for i in images:
        source = i["chemin"]

        if pillow:
            ext = "jpg"
            numero = numero_libre(dossier_sortie, ext, numero)
            cible = os.path.join(dossier_sortie, "%02d.jpg" % numero)
            if convertir_jpeg(source, cible):
                convertis += 1
                nom_cible = os.path.basename(cible)
            else:
                if os.path.exists(cible):
                    os.remove(cible)
                echecs.append((i["nom"], "conversion impossible"))
                continue
        else:
            ext = i["type"] if i["type"] != "heic" else "jpg"
            numero = numero_libre(dossier_sortie, ext, numero)
            cible = os.path.join(dossier_sortie, "%02d.%s" % (numero, ext))
            nom_cible = os.path.basename(cible)
            try:
                import shutil
                shutil.copy2(source, cible)
                copies += 1
            except Exception as e:
                echecs.append((i["nom"], str(e)[:50]))
                continue

        correspondance.append((nom_cible, i["nom"], i["dossier"], i["type"]))
        numero += 1

    if not correspondance:
        ko("Aucun fichier n'a pu etre prepare.")
        sys.exit(1)

    # --- planning ----------------------------------------------------
    maintenant = datetime.datetime.now()
    lignes = [
        "# " + "=" * 68,
        "#  PLANNING GENERE AUTOMATIQUEMENT le %s"
        % maintenant.strftime("%d/%m/%Y a %Hh%M"),
        "#",
        "#  %d image(s) prises dans : %s"
        % (len(correspondance),
           ", ".join(e + "/" for e, _ in chemins)),
        "#  Copies pretes dans : %s/"
        % os.path.basename(os.path.normpath(dossier_sortie)),
        "#  Ordre : %s" % args.ordre,
        "#",
        "#  Le commentaire '# source :' indique d'ou vient chaque image.",
        "#  Pour ecarter une image : ajoute  ACTIF: non  dans son bloc.",
        "# " + "=" * 68,
        "",
    ]

    for n, (nom_cible, nom_source, etiquette, type_) in enumerate(
            correspondance, 1):
        lignes.append("")
        lignes.append("=== POST %d ===" % n)
        lignes.append("# source : %s/%s" % (etiquette, nom_source))
        lignes.append("IMAGE: %s" % nom_cible)
        lignes.append("TEXTE:")
        lignes.append("HASHTAGS: %s" % hashtags)

    lignes.append("")

    with open(chemin_planning, "w", encoding="utf-8") as f:
        f.write("\n".join(lignes))

    # on retient ce qui a ete prepare, pour ne jamais le refaire
    try:
        with open(chemin_etat, "w", encoding="utf-8") as f:
            json.dump({
                "md5": sorted({i["md5"] for i in images if i["md5"]}
                              | set(deja_traites)),
                "total": len({i["md5"] for i in images if i["md5"]}
                             | set(deja_traites)),
            }, f, indent=1)
    except Exception as e:
        print("  (etat non enregistre : %s)" % e)

    rapport = os.path.join(DOSSIER, "images_correspondance.txt")
    with open(rapport, "w", encoding="utf-8") as f:
        f.write("Correspondance des images (genere le %s)\n"
                % maintenant.strftime("%d/%m/%Y %H:%M"))
        f.write("=" * 70 + "\n\n")
        for nom_cible, nom_source, etiquette, type_ in correspondance:
            f.write("%-10s <=  %s/%s  [%s]\n"
                    % (nom_cible, etiquette, nom_source, type_))

    # --- bilan -------------------------------------------------------
    titre("TERMINE")

    print()
    ok("%d copie(s), %d converti(s) en JPEG." % (copies, convertis))
    print("      Images pretes  : " + dossier_sortie)
    print("      Planning ecrit : " + chemin_planning)
    print("      Correspondance : " + rapport)

    if echecs:
        print()
        ko("%d fichier(s) non traite(s) :" % len(echecs))
        for nom, err in echecs[:8]:
            info("%s (%s)" % (nom[:44], err))

    print()
    print("  ET MAINTENANT, REGARDE CE QUI SERA PUBLIE :")
    print()
    print('      python programmer.py "demain" --planning %s '
          "--par-jour 5 --limite 20 --test"
          % os.path.basename(args.planning))
    print()
    print("  Rien n'est envoye avec --test. Si l'apercu te plait, relance")
    print("  la MEME commande sans --test.")
    print()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nInterrompu.\n")
