import subprocess
from pathlib import Path

DB_PATH = str(Path.home()) + "\\stopme.json"
result = subprocess.run(f"del {DB_PATH}")