from pathlib import Path
import json

class Config:
    def __init__(self, path=None):
        if path is None:
            # Go up one directory from 'server' to access 'config.json'
            path = Path(__file__).resolve().parent.parent / "config.json"
        with open(path, "r") as f:
            self.config = json.load(f)

    def get(self, key: str):
        return self.config.get(key)
