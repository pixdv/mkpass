from pathlib import Path
from errors import OUTPUT_ERRORS


def get_output_path(
        path: str | Path,
        force: bool = False
) -> Path | str | None:
    p = Path(path)
    if p.parent.exists() or p.exists():
        return p
    elif not p.parent.exists() and force==True:
        try:
            parent_path = p.parent
            parent_path.mkdir(parents=True, exist_ok=True)
            return p
        except PermissionError:
            return OUTPUT_ERRORS["PermissionError"]
    elif not p.parent.exists() and force==False:
        return OUTPUT_ERRORS["FileExistsError"]
