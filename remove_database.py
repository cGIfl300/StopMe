import subprocess
from pathlib import Path

DB_PATH = str(Path.home()) + "\\stopme.json"
try:
    result = subprocess.run(f"del {DB_PATH}")
except FileNotFoundError:
    print("Aucune base de donnée à supprimer")
    exit()
print("La base de données à été supprimée avec succès")
