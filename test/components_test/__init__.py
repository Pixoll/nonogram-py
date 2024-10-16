from pathlib import Path
from shutil import copytree

project_root = Path(__file__).resolve().parent.parent.parent.as_posix()
copytree(project_root + "/assets", project_root + "/test/assets", dirs_exist_ok=True)
