#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=======================================================================
 VERIFIER_IMAGES.py  -  "pourquoi le bot ne trouve pas mes images ?"
=======================================================================

 Le programmateur cherche chaque image dans le dossier indique par
 config.json (par defaut : images/), avec EXACTEMENT le nom ecrit
 dans planning.txt ("IMAGE: 01.jpg").

 Ce script compare les deux et te dit pourquoi ca ne colle pas :

   1. le dossier images/ n'est pas la ou le bot le cherche
   2. les images sont dans un SOUS-dossier (ZIP mal extrait :
      images/images/01.jpg, ou fb_auto/fb_auto/images/01.jpg)
   3. l'extension ne correspond pas (01.png au lieu de 01.jpg)
   4. la numerotation ne correspond pas (1.jpg au lieu de 01.jpg)
   5. le nom a un suffixe (01 (1).jpg, 01 - Copie.jpg)

 UTILISATION :
   python3 verifier_images.py              -> diagnostic seul (ne touche a rien)
   python3 verifier_images.py --corriger   -> corrige ce qui peut l'etre

 Ce script ne SUPPRIME jamais une image, et n'ecrase jamais un fichier
 existant. Sous Windows, tape "python" au lieu de "python3".
=======================================================================
"""

import os
import sys
import json
import re
import shutil
import argparse

DOSSIER = os.path.dirname(os.path.abspath(__file__))

# Tout ce qui peut etre une image
EXT_IMAGES = (".jpg", ".jpeg", ".jfif", ".png", ".webp", ".gif",
              ".bmp", ".tif", ".tiff", ".heic", ".avif")

# Noms de dossiers qui, ailleurs sur le disque, peuvent contenir
# les images du bot
NOMS_DOSSIERS_IMAGES = ("images", "image", "photos", "photo",
                        "pictures", "pics", "img")

# Reconnaissance par le contenu : tes fichiers peuvent n'avoir AUCUNE
# extension (ex : humour_noir_couple_20261012_1likes_577164508518853291).
SIGNATURES = (
    (b"\xff\xd8\xff", "jpg"),
    (b"\x89PNG\r\n\x1a\n", "png"),
    (b"GIF87a", "gif"),
    (b"GIF89a", "gif"),
    (b"BM", "bmp"),
    (b"II*\x00", "tiff"),
    (b"MM\x00*", "tiff"),
)
EXT_A_JETER = (".zip", ".rar", ".7z", ".txt", ".md", ".json", ".ini", ".db",
               ".py", ".exe", ".lnk", ".url", ".csv", ".log", ".bak", ".tmp",
               ".html", ".htm", ".xml", ".pdf", ".mp4", ".mkv", ".mov")

IGNORES = ("__pycache__", "node_modules", "logs", "$recycle.bin",
           "appdata", "windows", "program files", "system volume information")

FICHIERS_BOT = ("programmer.py", "planning.txt", "config.json")


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
# Lecture de config.json et planning.txt
# ---------------------------------------------------------------------
def charger_config():
    chemin = os.path.join(DOSSIER, "config.json")
    if not os.path.exists(chemin):
        ko("config.json introuvable a cote de ce script.")
        info("Es-tu bien dans le dossier fb_auto (celui de programmer.py) ?")
        sys.exit(1)
    try:
        with open(chemin, encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        ko("config.json illisible : " + str(e))
        sys.exit(1)


def lire_planning(chemin):
    """Retourne [(nom_image, actif)] dans l'ordre du fichier."""
    if not os.path.exists(chemin):
        ko("%s introuvable." % os.path.basename(chemin))
        sys.exit(1)

    posts, courant = [], None
    with open(chemin, encoding="utf-8") as f:
        for brute in f:
            ligne = brute.rstrip("\n").rstrip("\r")
            nu = ligne.strip()

            if ligne.startswith("#"):
                continue

            if nu.upper().startswith("=== POST") and nu.endswith("==="):
                if courant:
                    posts.append(courant)
                courant = {"image": "", "actif": True}
                continue

            if courant is None:
                continue

            haut = nu.upper()
            if haut.startswith("IMAGE:"):
                courant["image"] = nu.split(":", 1)[1].strip()
            elif haut.startswith("ACTIF:"):
                val = nu.split(":", 1)[1].strip().lower()
                courant["actif"] = val not in ("non", "no", "false", "0")

    if courant:
        posts.append(courant)

    return [(p["image"], p["actif"]) for p in posts if p["image"]]


# ---------------------------------------------------------------------
# Inventaire des images
# ---------------------------------------------------------------------
def est_une_image(chemin, nom):
    """Vrai si le fichier est une image (extension OU contenu)."""
    if nom.lower().endswith(EXT_IMAGES):
        return True
    if nom.lower().endswith(EXT_A_JETER):
        return False
    try:
        with open(chemin, "rb") as f:
            tete = f.read(32)
    except Exception:
        return False
    if len(tete) < 12:
        return False
    for sig, _ in SIGNATURES:
        if tete.startswith(sig):
            return True
    if tete[:4] == b"RIFF" and tete[8:12] == b"WEBP":
        return True
    if tete[4:8] == b"ftyp":
        return True
    return False


def lister_images(dossier, recursif=False):
    """Noms de fichiers images (chemins relatifs si recursif)."""
    trouves = []
    if not os.path.isdir(dossier):
        return trouves
    if recursif:
        for racine, dossiers, fichiers in os.walk(dossier):
            dossiers[:] = [d for d in dossiers
                           if d.lower() not in IGNORES
                           and not d.startswith(".")]
            for f in fichiers:
                if est_une_image(os.path.join(racine, f), f):
                    rel = os.path.relpath(os.path.join(racine, f), dossier)
                    trouves.append(rel)
    else:
        for f in os.listdir(dossier):
            chemin = os.path.join(dossier, f)
            if os.path.isfile(chemin) and est_une_image(chemin, f):
                trouves.append(f)
    return sorted(trouves)


def dossiers_avec_images(racine, profondeur=4, filtrer=False):
    """Tous les dossiers contenant des images, sous 'racine'."""
    trouves = []
    if not os.path.isdir(racine):
        return trouves
    base = os.path.abspath(racine).rstrip(os.sep).count(os.sep)

    for courant, dossiers, fichiers in os.walk(racine):
        dossiers[:] = [d for d in dossiers
                       if d.lower() not in IGNORES and not d.startswith(".")]

        n = sum(1 for f in fichiers
                if est_une_image(os.path.join(courant, f), f))
        if n and (not filtrer or dossier_pertinent(courant)):
            trouves.append((os.path.abspath(courant), n))

        if courant.count(os.sep) - base >= profondeur:
            dossiers[:] = []

    trouves.sort(key=lambda x: (-x[1], len(x[0])))
    return trouves


def dossier_pertinent(chemin):
    """Vrai si ce dossier, hors du dossier du bot, peut vraiment
    contenir les images du bot."""
    nom = os.path.basename(os.path.normpath(chemin)).lower()
    if nom in NOMS_DOSSIERS_IMAGES:
        return True
    parent = os.path.dirname(os.path.normpath(chemin))
    return any(os.path.exists(os.path.join(parent, f)) for f in FICHIERS_BOT)


# ---------------------------------------------------------------------
# Rapprochement attendu / present
# ---------------------------------------------------------------------
def ressemblance(attendu, present):
    """Retourne (bool, raison) si 'present' peut etre l'image 'attendu'."""
    ba, ea = os.path.splitext(attendu)
    bp, ep = os.path.splitext(present)

    if ba.lower() == bp.lower():
        if ea == ep:
            return True, "meme nom, mais dans un autre dossier"
        return True, "extension differente (%s au lieu de %s)" % (ep, ea)

    # 1.jpg au lieu de 01.jpg
    if ba.lower().lstrip("0") == bp.lower().lstrip("0") \
            and ba.lower() != bp.lower():
        return True, "numerotation differente (%s au lieu de %s)" % (bp, ba)

    # 01 (1).jpg, 01 - Copie.jpg, 01_final.jpg
    if bp.lower().startswith(ba.lower()):
        suffixe = bp[len(ba):]
        if re.match(r"^\s*[\(\[\-_.]", suffixe) or \
           suffixe.strip().lower().startswith(("copie", "copy", "final")):
            return True, "nom avec un suffixe (%s)" % bp

    return False, ""


def score_dossier(dossier, attendus):
    """(exact, souple) : combien d'images attendues sont dans ce dossier."""
    dispo = [os.path.basename(x) for x in lister_images(dossier, recursif=True)]
    bas = set(d.lower() for d in dispo)
    exact, souple = 0, 0
    for a in attendus:
        if a.lower() in bas:
            exact += 1
            continue
        for f in dispo:
            bon, _ = ressemblance(a, f)
            if bon:
                souple += 1
                break
    return exact, souple


def convertir_en_jpeg(source, cible):
    """Convertit une image (png/webp/gif...) en vrai JPEG.
    Retourne True si la conversion a reussi."""
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
        im.save(cible, "JPEG", quality=92)
        return True
    except Exception:
        return False


# ---------------------------------------------------------------------
# Programme principal
# ---------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser(
        description="Verifie que les images du planning sont bien dans "
                    "le dossier que le bot regarde.")
    ap.add_argument("--planning", default=None,
                    help="Fichier de planning (defaut : celui de config.json)")
    ap.add_argument("--corriger", action="store_true",
                    help="Corrige automatiquement ce qui peut l'etre")
    ap.add_argument("--oui", action="store_true",
                    help="Ne pas demander de confirmation")
    args = ap.parse_args()

    titre("VERIFICATION DES IMAGES")

    cfg = charger_config()

    dossier_images = os.path.join(DOSSIER, cfg.get("DOSSIER_IMAGES", "images"))
    nom_planning = args.planning or cfg.get("FICHIER_PLANNING", "planning.txt")
    chemin_planning = (nom_planning if os.path.isabs(nom_planning)
                       else os.path.join(DOSSIER, nom_planning))

    posts = lire_planning(chemin_planning)
    actifs = [n for n, a in posts if a and not n.lower().startswith("http")]

    print()
    print("  Dossier du bot      : " + DOSSIER)
    print("  Il cherche les images ICI :")
    print("      " + dossier_images)
    print("  Planning lu         : " + os.path.basename(chemin_planning))
    print("  Posts actifs        : %d (dont %d avec une image locale)"
          % (sum(1 for _, a in posts if a), len(actifs)))

    # --- 1. Le dossier existe-t-il, et que contient-il ? -----------
    titre("1. LE DOSSIER images/")

    if os.path.isdir(dossier_images):
        ok("Le dossier existe.")
    else:
        ko("CE DOSSIER N'EXISTE PAS.")
        info(dossier_images)

    presentes = lister_images(dossier_images)
    print()
    print("  %d image(s) trouvee(s) directement dedans." % len(presentes))
    for f in presentes[:15]:
        print("      " + f)
    if len(presentes) > 15:
        print("      ... (+%d)" % (len(presentes) - 15))

    if os.path.isdir(dossier_images) and not presentes:
        fichiers = [f for f in os.listdir(dossier_images)
                    if os.path.isfile(os.path.join(dossier_images, f))]
        if fichiers:
            info("Il y a des fichiers, mais aucune image :")
            info(", ".join(fichiers[:12]))
            for f in fichiers:
                if f.lower().endswith(".zip"):
                    print()
                    ko("ZIP NON EXTRAIT : " + f)
                    info("Clic droit dessus -> Extraire tout,")
                    info("puis deplace les images dans images/")
        else:
            info("Le dossier est VIDE.")

    # --- 2. Ou sont les images ailleurs ? -------------------------
    titre("2. OU SONT VRAIMENT TES IMAGES ?")

    if presentes and not actifs:
        info("(rien a chercher)")
    else:
        # a) sous le dossier du bot : ZIP extrait dans un sous-dossier
        candidats = dossiers_avec_images(DOSSIER, profondeur=4)
        # b) a cote du dossier du bot (Desktop, Downloads...)
        parent = os.path.dirname(DOSSIER.rstrip(os.sep))
        racine_disque = (not parent) or parent == DOSSIER \
            or re.match(r"^[A-Za-z]:[\\/]*$", parent) or parent == os.sep
        if not racine_disque:
            for chemin, n in dossiers_avec_images(parent, profondeur=3,
                                                  filtrer=True):
                if not os.path.abspath(chemin).startswith(
                        os.path.abspath(DOSSIER) + os.sep):
                    candidats.append((chemin, n))

        # on note chaque candidat selon le planning
        notes = []
        for chemin, n in candidats:
            exact, souple = score_dossier(chemin, actifs)
            dedans = os.path.abspath(chemin).startswith(
                os.path.abspath(DOSSIER) + os.sep)
            # a score egal, on prefere un dossier situe dans fb_auto
            notes.append((exact, souple, 0 if dedans else 1, n, chemin))
        notes.sort(key=lambda x: (-x[0], -x[1], x[2], len(x[4])))

        if not notes:
            ko("Aucune image trouvee nulle part autour du dossier du bot.")
            info("Verifie que tu as bien EXTRAIT le ZIP (clic droit ->")
            info("Extraire tout) : ouvrir l'apercu du ZIP ne suffit pas.")
        else:
            for exact, souple, _, n, chemin in notes[:6]:
                ici = os.path.abspath(chemin) == os.path.abspath(dossier_images)
                marque = "  <-- LE BOT CHERCHE ICI" if ici else ""
                print("  %4d image(s)  %s%s" % (n, chemin, marque))
                print("               dont %d sur les %d attendues "
                      "(+%d avec un autre nom)"
                      % (exact, len(actifs), souple))

            meilleur = notes[0][4]
            if os.path.abspath(meilleur) != os.path.abspath(dossier_images):
                print()
                ko("TES IMAGES NE SONT PAS DANS LE DOSSIER DU BOT.")
                info("Le bon dossier semble etre :")
                info("    " + meilleur)
                dedans = os.path.abspath(meilleur).startswith(
                    os.path.abspath(DOSSIER) + os.sep)
                if dedans:
                    info("-> c'est le cas classique du ZIP extrait dans un")
                    info("   sous-dossier. --corriger les remet au bon endroit.")
                else:
                    info("-> deplace les images a la main dans :")
                    info("   " + dossier_images)
                    info("   (ou change DOSSIER_IMAGES dans config.json)")

    # --- 3. Le planning et ses noms d'images -----------------------
    titre("3. PLANNING : LES NOMS D'IMAGES ATTENDUS")

    print()
    print("  %d post(s) au total, %d actif(s)." % (len(posts), len(actifs)))

    if not actifs:
        print()
        info("Aucun post actif dans le planning : rien a programmer.")
        return

    dispo_ici = lister_images(dossier_images)
    dispo_bot = lister_images(DOSSIER, recursif=True)

    manquants, a_corriger = [], []
    for nom in actifs:
        if nom in dispo_ici:
            continue
        manquants.append(nom)

        trouve = None
        for f in dispo_ici:                      # meme dossier, autre nom
            bon, raison = ressemblance(nom, f)
            if bon and f != nom:
                trouve = (f, dossier_images, raison)
                break

        if not trouve:                           # ailleurs dans fb_auto
            for rel in dispo_bot:
                f = os.path.basename(rel)
                bon, raison = ressemblance(nom, f)
                if bon:
                    trouve = (f, os.path.dirname(
                        os.path.join(DOSSIER, rel)), raison)
                    break

        if trouve:
            a_corriger.append((trouve[0], trouve[1], nom, trouve[2]))

    print()
    if not manquants:
        ok("Les %d images du planning sont TOUTES au bon endroit." % len(actifs))
        print()
        info("Tu peux lancer le bot :")
        info('  python programmer.py "demain" --par-jour 5 --limite 20 --test')
        return

    ko("%d image(s) du planning introuvable(s) sous ce nom exact :"
       % len(manquants))
    for m in manquants[:10]:
        print("      " + m)
    if len(manquants) > 10:
        print("      ... (+%d)" % (len(manquants) - 10))

    # --- 4. Pourquoi / comment reparer -----------------------------
    titre("4. POURQUOI, ET COMMENT REPARER")

    restants = [n for n in manquants
                if not any(c[2] == n for c in a_corriger)]

    if a_corriger:
        ok("%d de ces images existent, avec un nom ou une place "
           "differente :" % len(a_corriger))
        for present, ou, attendu, raison in a_corriger[:15]:
            lieu = os.path.relpath(ou, DOSSIER).replace("\\", "/")
            if len(lieu) > 24:
                lieu = "..." + lieu[-21:]
            print("      %-20s dans %-24s -> %s" % (present, lieu, attendu))
            print("      %-20s   %s" % ("", raison))
        if len(a_corriger) > 15:
            print("      ... (+%d)" % (len(a_corriger) - 15))

    if restants:
        print()
        ko("%d image(s) n'existent NULLE PART sous un nom approchant :"
           % len(restants))
        for r in restants[:10]:
            print("      " + r)
        info("Ces images ne sont pas dans le dossier du tout.")
        if not a_corriger:
            print()
            info("Autrement dit : tes images ne portent pas les noms")
            info("01.jpg, 02.jpg... ecrits dans le planning.")
            info("Si leurs noms sont quelconques (du genre")
            info("humour_noir_couple_20261012_1likes_577164508518853291),")
            info("il ne faut PAS les renommer : utilise plutot :")
            print()
            info("      python associer_images.py --preparer")
            print()
            info("Ce script prend toutes les images du dossier (sans tenir")
            info("compte du nom), en fait des copies 01.jpg, 02.jpg... et")
            info("ecrit un planning pret a publier.")
            print()
            info("Sinon, a la main :")
            info("  a) renommer les fichiers dans l'ordre : 01.jpg, 02.jpg...")
            info("  b) les mettre dans : " + dossier_images)
            info("  c) relancer un scraping : "
                 "python scraper.py \"funny cat\" 10")

    if not args.corriger:
        print()
        if a_corriger:
            info("Pour appliquer ces corrections automatiquement :")
        else:
            info("Pour un rapport detaille des fichiers presents :")
        info("      python verifier_images.py --corriger")
        info("(rien n'est supprime, rien n'est ecrase)")
        return

    # --- 5. Correction ---------------------------------------------
    titre("5. CORRECTION")

    if not a_corriger:
        info("Rien a corriger automatiquement.")
        return

    if not args.oui:
        rep = input("  Deplacer/renommer ces fichiers ? (oui/non) > ")
        if rep.strip().lower() not in ("oui", "o", "yes", "y"):
            print("  Annule.\n")
            return

    os.makedirs(dossier_images, exist_ok=True)

    deplaces, renommes, convertis, echecs = 0, 0, 0, []
    sans_conversion = []
    etiquette = os.path.basename(os.path.normpath(dossier_images)) + "/"

    for present, ou, attendu, raison in a_corriger:
        source = os.path.join(ou, present)
        cible = os.path.join(dossier_images, attendu)

        if not os.path.exists(source):
            continue
        if os.path.exists(cible):
            echecs.append((attendu, "deja present, non touche"))
            continue

        source_ext = os.path.splitext(source)[1].lower()
        aille_ici = os.path.abspath(ou) == os.path.abspath(dossier_images)

        converti = False
        if source_ext not in (".jpg", ".jpeg"):
            converti = convertir_en_jpeg(source, cible)

        try:
            if converti:
                os.remove(source)
                convertis += 1
                print("  converti : %-22s -> %s%s (vrai JPEG)"
                      % (present, etiquette, attendu))
                continue

            shutil.move(source, cible)
            if aille_ici:
                renommes += 1
                print("  renomme  : %-22s -> %s" % (present, attendu))
            else:
                deplaces += 1
                print("  deplace  : %-22s -> %s%s"
                      % (present, etiquette, attendu))
                if source_ext not in (".jpg", ".jpeg"):
                    sans_conversion.append((present, attendu))
        except Exception as e:
            echecs.append((present, str(e)[:60]))

    print()
    print("  %d deplace(s), %d converti(s), %d renomme(s), %d non traite(s)."
          % (deplaces, convertis, renommes, len(echecs)))
    for nom, err in echecs[:8]:
        info("%s : %s" % (nom, err))

    if sans_conversion:
        print()
        ko("%d fichier(s) renomme(s) en .jpg SANS conversion"
           % len(sans_conversion))
        info("(le contenu reste du png/webp : Facebook l'accepte en general)")
        info("Pour une vraie conversion : pip install pillow, puis annule")
        info("le renommage et relance ce script.")

    # sous-dossiers vides laisses derriere (ex: fb_auto/fb_auto/images)
    A_GARDER = ("images", "image", "reel", "reels", "logs")
    vides = []
    for racine, dossiers, fichiers in os.walk(DOSSIER, topdown=False):
        if os.path.abspath(racine) == os.path.abspath(DOSSIER):
            continue
        nom = os.path.basename(os.path.normpath(racine)).lower()
        parent = os.path.dirname(os.path.abspath(racine))
        if parent == os.path.abspath(DOSSIER) and nom in A_GARDER:
            continue
        if nom == "__pycache__":
            continue
        try:
            if not os.listdir(racine):
                os.rmdir(racine)
                vides.append(os.path.relpath(racine, DOSSIER))
        except Exception:
            pass
    if vides:
        print()
        info("Dossier(s) vide(s) laisse(s) par le deplacement, supprime(s) :")
        info(", ".join(vides))

    # --- Verification finale ---------------------------------------
    manquent_encore = [n for n in actifs
                       if not os.path.exists(os.path.join(dossier_images, n))]

    print()
    if manquent_encore:
        ko("Il reste %d image(s) du planning introuvable(s) :"
           % len(manquent_encore))
        for m in manquent_encore[:10]:
            print("      " + m)
        info("Celles-la ne sont pas dans le dossier du tout.")
    else:
        ok("TOUTES les images actives du planning sont maintenant en place.")

    print()
    info("Verifie avec un apercu (rien n'est envoye) :")
    info('  python programmer.py "demain" --par-jour 5 --limite 20 --test')
    print()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nInterrompu.\n")
