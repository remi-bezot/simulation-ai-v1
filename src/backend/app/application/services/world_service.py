from typing import List, Dict, Any

# Stockage temporaire
_worlds: List[Dict[str, Any]] = []


def list_worlds() -> Dict[str, List[Dict[str, Any]]]:
    """Retourner la liste de tous les mondes."""
    return {"worlds": _worlds}


def create_world(data: Dict[str, Any]) -> Dict[str, Any]:
    """Créer un nouveau monde."""
    if not data.get("name"):
        raise ValueError("Le champ 'name' est obligatoire.")
    world = {
        "id": len(_worlds) + 1,
        "name": data["name"],
        "properties": data.get("properties", {}),
    }
    _worlds.append(world)
    return {"message": "Monde créé avec succès", "world": world}


def update_world(world_id: int, updates: Dict[str, Any]) -> Dict[str, Any]:
    """Mettre à jour un monde existant."""
    world = next((w for w in _worlds if w["id"] == world_id), None)
    if not world:
        raise ValueError(f"Monde avec l'ID {world_id} non trouvé.")
    for key, value in updates.items():
        if key in world:
            world[key] = value
    return {"message": "Monde mis à jour avec succès.", "world": world}


def delete_world(world_id: int) -> Dict[str, Any]:
    """Supprimer un monde par son ID."""
    global _worlds
    world = next((w for w in _worlds if w["id"] == world_id), None)
    if not world:
        raise ValueError(f"Monde avec l'ID {world_id} non trouvé.")
    _worlds = [w for w in _worlds if w["id"] != world_id]
    return {"message": f"Le monde avec l'ID {world_id} a été supprimé avec succès."}
