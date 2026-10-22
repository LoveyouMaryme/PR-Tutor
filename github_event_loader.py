import json
import os
from pathlib import Path


def load_github_event() -> tuple[str, dict]:

    # 1. Récupérer le nom de l'événement
    event_name = os.environ["GITHUB_EVENT_NAME"]

    # 2. Récupérer le chemin du fichier JSON
    event_path = os.environ["GITHUB_EVENT_PATH"]

    # 3. Lire le fichier et convertir son contenu en dict
    content = Path(event_path).read_text(encoding="utf-8")
    payload = json.loads(content)

    # 4. Retourner les deux valeurs
    return event_name, payload
