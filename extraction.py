import requests
import json

# Function to fetch hero statistics from OpenDota API
def fetch_hero_stats():
    url = 'https://api.opendota.com/api/heroStats'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve data: {response.status_code}")
        return None

# Function to save hero data to a JSON file
def save_hero_data_to_json(hero_stats, filename='hero_stats.json'):
    with open(filename, 'w') as json_file:
        json.dump(hero_stats, json_file, indent=4)
    print(f"Hero data saved to {filename}")

# Main function to fetch and save hero data
def main():
    hero_stats = fetch_hero_stats()
    if hero_stats:
        save_hero_data_to_json(hero_stats)

if __name__ == "__main__":
    main()