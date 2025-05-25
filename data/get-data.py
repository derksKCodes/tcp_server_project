import requests
from pathlib import Path

# Define the URL and data folder
url = "https://tests.quantitative-analysis.com/200k.txt"


data_folder = Path(__file__).resolve().parent  # 'data' folder in the same directory as this script
data_folder.mkdir(parents=True, exist_ok=True)  


# Full path to the file
file_path = data_folder / "200k.txt"

if file_path.exists():
    print("200k.txt file already exists.")
    exit(0)  # Exit if the file already exists
else:
    print("200k.txt file does not exist, proceeding to download.")

# Download and save the file
response = requests.get(url)
if response.status_code == 200:
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(response.text)
    print(f"Data downloaded successfully to {file_path}")
else:
    print(f"Failed to download data. Status code: {response.status_code}")


# # Fetch the file content directly without downloading the file
# response = requests.get(url)
# if response.status_code == 200:
#     data = response.text
#     print("✅ Data read successfully from the URL.")
    
#     # Process each line (if needed)
#     lines = data.strip().splitlines()
#     for line in lines[:5]:  # Example: print the first 5 lines
#         print(line)
# else:
#     print(f"❌ Failed to fetch data. Status code: {response.status_code}")
