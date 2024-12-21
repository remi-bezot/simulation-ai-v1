from sqlalchemy.ext.declarative import declarative_base
import os
import pkgutil
import importlib

# Déclare une base commune pour tous les modèles SQLAlchemy
Base = declarative_base()

# Chargement dynamique des modèles pour éviter les problèmes d'import manuel
__all__ = ["Base"]

# Chemin absolu du dossier contenant les modèles
current_dir = os.path.dirname(__file__)
module_prefix = __name__.rsplit(".", 1)[0]

# Parcours des fichiers dans le répertoire `models` pour importer automatiquement les modèles
for _, module_name, _ in pkgutil.iter_modules([current_dir]):
    module = importlib.import_module(f"{module_prefix}.{module_name}")
    for attr in dir(module):
        obj = getattr(module, attr)
        # Vérifie si l'objet est un modèle SQLAlchemy
        if hasattr(obj, "__tablename__") and hasattr(obj, "__table__"):
            globals()[attr] = obj
            __all__.append(attr)
