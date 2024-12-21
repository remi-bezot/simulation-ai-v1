
import json

def to_json(data):
    """Convertir des données Python en JSON."""
    return json.dumps(data, indent=4, ensure_ascii=False)

