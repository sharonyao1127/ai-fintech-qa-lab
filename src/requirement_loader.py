from pathlib import Path


def load_requirement(path: str) -> str:
    """Load requirement text from a markdown file."""
    requirement_path = Path(path)
    if not requirement_path.exists():
        raise FileNotFoundError(f"Requirement file not found: {path}")
    return requirement_path.read_text(encoding="utf-8")
