from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LAUNCHERS = (
    "CONFIGURER.bat",
    "PLANIFIER.bat",
    "ENVOYER_PLANNING.bat",
    "LANCER_BOT.bat",
)


def test_windows_launchers_are_ascii_with_crlf_line_endings() -> None:
    for filename in LAUNCHERS:
        data = (ROOT / filename).read_bytes()
        data.decode("ascii")
        assert b"\n" in data
        assert data.count(b"\n") == data.count(b"\r\n")


def test_planner_runs_python_and_propagates_its_exit_code() -> None:
    script = (ROOT / "PLANIFIER.bat").read_text(encoding="ascii")

    assert '".venv\\Scripts\\python.exe" -m facebook_bot plan' in script
    assert 'set "BOT_RESULT=%ERRORLEVEL%"' in script
    assert "exit /b %BOT_RESULT%" in script
