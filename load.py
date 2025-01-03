import json
import pandas as pd

# Function to load JSON data from a file
def load_json_data(filename):
    with open(filename, 'r') as file:
        return json.load(file)

# Function to display the hero statistics in a table
def display_hero_statistics(json_data):
    # Convert JSON data to a pandas DataFrame
    df = pd.DataFrame(json_data)
    
    # Display the DataFrame
    print(df)

# Main function to load data and display it
def main():
    # Load hero data from JSON file
    hero_statistics = load_json_data('hero_statistics.json')
    
    # Display the hero statistics
    display_hero_statistics(hero_statistics)

if __name__ == "__main__":
    main()