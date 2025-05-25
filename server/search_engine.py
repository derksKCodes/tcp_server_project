from typing import List
import requests
from pathlib import Path

def load_lines(filepath: str) -> list[str]:
    # Check if it's a URL
    if filepath.startswith("http://") or filepath.startswith("https://"):
        response = requests.get(filepath)
        if response.status_code == 200:
            return response.text.strip().splitlines()
        else:
            raise ValueError(f"Failed to load from URL: {filepath} (status {response.status_code})")
    else:
        # Load from local file
        with open(Path(filepath), "r", encoding="utf-8") as file:
            return file.read().strip().splitlines()

# def load_lines(filepath: str) -> List[str]:
#     with open(filepath, "r", encoding="utf-8") as file:
#         return [line.strip() for line in file]

def search_lines(query: str, lines: List[str]) -> List[str]:
    return [line for line in lines if line.strip() == query]
