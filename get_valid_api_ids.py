# This is a standalone file to get valid IDs for NBA players API - do not call it from anywhere in the project
import requests
import time


min_number = 1
max_number = 3092
valid_ids = []
for current_id in range(min_number, max_number + 1):
    current_stats = {}
    url = f"https://www.balldontlie.io/api/v1/players/{current_id}"
    response = requests.get(url)
    current_player = response.json()
    current_stats["height_feet"] = current_player["height_feet"]
    current_stats["height_inches"] = current_player["height_inches"]
    current_stats["weight"] = current_player["weight_pounds"]
    current_stats["team id"] = current_player["team"]["id"]
    if None in current_stats.values():
        continue
    else:
        valid_ids.append(current_id)
    time.sleep(5)

print(valid_ids)
