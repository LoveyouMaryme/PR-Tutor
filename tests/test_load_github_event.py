from github_event_loader import load_github_event
import os


def test_load_github_event(monkeypatch, tmp_path):

    # 1. Créer un fichier JSON temporaire
    event_file = tmp_path / "event.json"

    event_file.write_text(
        '{"action": "synchronize", "number": 20}',
        encoding="utf-8"
    )

    # 2. Simuler GITHUB_EVENT_NAME
    monkeypatch.setenv(
        "GITHUB_EVENT_NAME",
        "pull_request"
    )

    # TODO 3 : simuler GITHUB_EVENT_PATH
    monkeypatch.setenv(
        "GITHUB_EVENT_PATH",
        str(event_file)
    )

    # TODO 4 : appeler load_github_event()
    event_name, payload = load_github_event()

    # TODO 5 : vérifier les valeurs retournées
    assert(event_name == "pull_request")
    assert(payload["action"] == "synchronize")
    assert(payload["number"] == 20 )