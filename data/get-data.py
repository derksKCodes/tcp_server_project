import requests
from pathlib import Path

# Define the URL and data folder
url = "https://tests.quantitative-analysis.com/200k.txt"
data_folder = Path("data")
data_folder.mkdir(parents=True, exist_ok=True)  # Create 'data' folder if it doesn't exist

# Full path to the file
file_path = data_folder / "200k.txt"

# Download and save the file
response = requests.get(url)
if response.status_code == 200:
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(response.text)
    print(f"Data downloaded successfully to {file_path}")
else:
    print(f"Failed to download data. Status code: {response.status_code}")
