import json

# Function to load JSON data from a file
def load_json_data(filename):
    with open(filename, 'r') as file:
        return json.load(file)

# Function to calculate hero statistics and generate the required JSON data
def generate_hero_statistics(hero_stats):
    hero_data = []

    for hero in hero_stats:
        hero_info = {
            "id": hero.get('id'),
            "name": hero.get('localized_name'),
            "pro_ban": hero.get('pro_ban', 0),
            "pro_win": hero.get('pro_win', 0),
            "pro_pick": hero.get('pro_pick', 0),
            "1_pick": hero.get('1_pick', 0),  # Herald picks
            "1_win": hero.get('1_win', 0),    # Herald wins
            "2_pick": hero.get('2_pick', 0),  # Guardian picks
            "2_win": hero.get('2_win', 0),    # Guardian wins
            "3_pick": hero.get('3_pick', 0),  # Crusader picks
            "3_win": hero.get('3_win', 0),    # Crusader wins
            "4_pick": hero.get('4_pick', 0),  # Archon picks
            "4_win": hero.get('4_win', 0),    # Archon wins
            "5_pick": hero.get('5_pick', 0),  # Legend picks
            "5_win": hero.get('5_win', 0),    # Legend wins
            "6_pick": hero.get('6_pick', 0),  # Ancient picks
            "6_win": hero.get('6_win', 0),    # Ancient wins
            "7_pick": hero.get('7_pick', 0),  # Divine picks
            "7_win": hero.get('7_win', 0),    # Divine wins
            "8_pick": hero.get('8_pick', 0),  # Immortal picks
            "8_win": hero.get('8_win', 0),    # Immortal wins
        }

        # Calculate total picks and total wins
        hero_info["total_picks"] = (
            hero_info["1_pick"] + hero_info["2_pick"] + hero_info["3_pick"] +
            hero_info["4_pick"] + hero_info["5_pick"] + hero_info["6_pick"] +
            hero_info["7_pick"] + hero_info["8_pick"] + hero_info["pro_pick"]
        )
        hero_info["total_wins"] = (
            hero_info["1_win"] + hero_info["2_win"] + hero_info["3_win"] +
            hero_info["4_win"] + hero_info["5_win"] + hero_info["6_win"] +
            hero_info["7_win"] + hero_info["8_win"] + hero_info["pro_win"]
        )

        # Calculate win rate per rank and average win rate
        hero_info["win_rate_per_rank"] = {
            "Herald": hero_info["1_win"] / hero_info["1_pick"] if hero_info["1_pick"] > 0 else 0,
            "Guardian": hero_info["2_win"] / hero_info["2_pick"] if hero_info["2_pick"] > 0 else 0,
            "Crusader": hero_info["3_win"] / hero_info["3_pick"] if hero_info["3_pick"] > 0 else 0,
            "Archon": hero_info["4_win"] / hero_info["4_pick"] if hero_info["4_pick"] > 0 else 0,
            "Legend": hero_info["5_win"] / hero_info["5_pick"] if hero_info["5_pick"] > 0 else 0,
            "Ancient": hero_info["6_win"] / hero_info["6_pick"] if hero_info["6_pick"] > 0 else 0,
            "Divine": hero_info["7_win"] / hero_info["7_pick"] if hero_info["7_pick"] > 0 else 0,
            "Immortal": hero_info["8_win"] / hero_info["8_pick"] if hero_info["8_pick"] > 0 else 0,
            "Pro": hero_info["pro_win"] / hero_info["pro_pick"] if hero_info["pro_pick"] > 0 else 0,
        }
        hero_info["average_win_rate"] = hero_info["total_wins"] / hero_info["total_picks"] if hero_info["total_picks"] > 0 else 0

        hero_data.append(hero_info)

    return hero_data

# Function to save JSON data to a file
def save_json_data(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"Hero statistics saved to {filename}")

# Main function to load data, process it, and save the results
def main():
    # Load hero data from JSON file
    hero_stats = load_json_data('hero_stats.json')

    # Generate hero statistics
    hero_statistics = generate_hero_statistics(hero_stats)

    # Save the resulting data to a new JSON file
    save_json_data(hero_statistics, 'hero_statistics.json')

if __name__ == "__main__":
    main()
