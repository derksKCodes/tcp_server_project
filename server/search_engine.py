from typing import List

def load_lines(filepath: str) -> List[str]:
    with open(filepath, "r", encoding="utf-8") as file:
        return [line.strip() for line in file]

def search_lines(query: str, lines: List[str]) -> List[str]:
    return [line for line in lines if line.strip() == query]
