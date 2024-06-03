import requests
import datetime
import csv
from collections import deque
from typing import List, Dict, Optional
from unittest.mock import patch

# Helper function to fetch data from a given URL
def fetch_data(url: str) -> Optional[Dict]:
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data from {url}: {response.status_code}")
        return None

# Fetch the top 50 classical chess players
def fetch_top_50_classical_players() -> List[Dict]:
    url = "https://lichess.org/api/player/top/50/classical"
    data = fetch_data(url)
    return data['users'] if data else []

# Fetch the rating history for a specific player
def fetch_rating_history(username: str) -> Optional[List[Dict]]:
    url = f'https://lichess.org/api/user/{username}/rating-history'
    return fetch_data(url)

# Print the usernames of the top 50 classical chess players with ranking
def print_top_50_classical_players() -> None:
    players = fetch_top_50_classical_players()
    for index, player in enumerate(players, start=1):
        print(f"{index}- {player['username']}")

# Generate rating history for the last 30 days using a deque
def generate_last_30_days_rating(points: List[List[int]], start_date: datetime.date, end_date: datetime.date) -> Dict[str, Optional[int]]:
    rating_dates = {datetime.date(year, month + 1, day): rating for year, month, day, rating in points}
    sorted_dates = sorted(rating_dates.items())
    
    last_known_rating = None
    rating_history = {}
    stack = deque(sorted_dates)

    # Iterate over each day in the last 30 days
    for single_date in (start_date + datetime.timedelta(n) for n in range((end_date - start_date).days + 1)):
        while stack and stack[0][0] <= single_date:
            last_known_rating = stack.popleft()[1]
        rating_history[single_date.isoformat()] = last_known_rating

    return rating_history

# Print the rating history for the top player in the last 30 days
def print_last_30_day_rating_for_top_player() -> None:
    players = fetch_top_50_classical_players()
    if not players:
        print("No players found.")
        return
    
    top_player = players[0]['id']
    history_data = fetch_rating_history(top_player)

    if not history_data:
        print(f"No rating history found for {top_player}.")
        return

    classical_history = next((item for item in history_data if item['name'] == 'Classical'), None)
    if not classical_history:
        print(f"No classical rating history for {top_player}.")
        return

    today = datetime.date.today()
    start_date = today - datetime.timedelta(days=30)
    rating_history = generate_last_30_days_rating(classical_history['points'], start_date, today)
    
    formatted_rating_history = ", ".join(f"{date}: {rating}" for date, rating in sorted(rating_history.items()))
    print(f"{top_player}, {{{formatted_rating_history}}}")

# Generate CSV for the top 50 players' ratings over the last 30 days
def generate_rating_csv_for_top_50_classical_players() -> None:
    players = fetch_top_50_classical_players()
    if not players:
        print("No players found.")
        return

    today = datetime.date.today()
    start_date = today - datetime.timedelta(days=30)

    with open('top_50_players_ratings.csv', 'w', newline='') as csvfile:
        fieldnames = ['username'] + [(start_date + datetime.timedelta(days=n)).isoformat() for n in range(31)]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for player in players:
            username = player['id']
            history_data = fetch_rating_history(username)

            if not history_data:
                print(f"No rating history found for {username}.")
                continue

            classical_history = next((item for item in history_data if item['name'] == 'Classical'), None)
            if not classical_history:
                print(f"No classical rating history for {username}.")
                continue

            rating_history = generate_last_30_days_rating(classical_history['points'], start_date, today)
            ratings_row = {'username': username}
            for single_date in (start_date + datetime.timedelta(n) for n in range(31)):
                date_str = single_date.isoformat()
                ratings_row[date_str] = rating_history[date_str]

            writer.writerow(ratings_row)

def run_tests() -> None:
    print("Running tests...")

    mock_players = {
        'users': [{'id': 'player1'}, {'id': 'player2'}, {'id': 'player3'}, {'id': 'player4'}, {'id': 'player5'},
                  {'id': 'player6'}, {'id': 'player7'}, {'id': 'player8'}, {'id': 'player9'}, {'id': 'player10'},
                  {'id': 'player11'}, {'id': 'player12'}, {'id': 'player13'}, {'id': 'player14'}, {'id': 'player15'},
                  {'id': 'player16'}, {'id': 'player17'}, {'id': 'player18'}, {'id': 'player19'}, {'id': 'player20'},
                  {'id': 'player21'}, {'id': 'player22'}, {'id': 'player23'}, {'id': 'player24'}, {'id': 'player25'},
                  {'id': 'player26'}, {'id': 'player27'}, {'id': 'player28'}, {'id': 'player29'}, {'id': 'player30'},
                  {'id': 'player31'}, {'id': 'player32'}, {'id': 'player33'}, {'id': 'player34'}, {'id': 'player35'},
                  {'id': 'player36'}, {'id': 'player37'}, {'id': 'player38'}, {'id': 'player39'}, {'id': 'player40'},
                  {'id': 'player41'}, {'id': 'player42'}, {'id': 'player43'}, {'id': 'player44'}, {'id': 'player45'},
                  {'id': 'player46'}, {'id': 'player47'}, {'id': 'player48'}, {'id': 'player49'}, {'id': 'player50'}]
    }

    mock_history = [
        {'name': 'Classical', 'points': [[2023, 3, 15, 1500], [2023, 3, 16, 1505], [2023, 3, 17, 1510]]}
    ]

    with patch('requests.get') as mock_get:
        # Mocking fetch_top_50_classical_players
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_players

        players = fetch_top_50_classical_players()
        assert len(players) == 50
        assert players == mock_players['users']
        print("Test fetch_top_50_classical_players passed")

        # Mocking fetch_rating_history
        mock_get.return_value.json.return_value = mock_history

        if players:
            username = players[0]['id']
            history_data = fetch_rating_history(username)
            assert 'points' in history_data[0]
            assert history_data == mock_history
            print("Test fetch_rating_history passed")

            # Test generate_last_30_days_rating
            points = mock_history[0]['points']
            today = datetime.date.today()
            start_date = today - datetime.timedelta(days=30)
            rating_history = generate_last_30_days_rating(points, start_date, today)
            assert len(rating_history) == 31
            for date, rating in rating_history.items():
                assert rating in [1500, 1505, 1510, None]
            print("Test generate_last_30_days_rating passed")

            # Test edge case: player without classical rating history
            mock_get.return_value.json.return_value = [{'name': 'Blitz', 'points': [[2023, 3, 15, 1500]]}]
            history_data = fetch_rating_history(username)
            classical_history = next((item for item in history_data if item['name'] == 'Classical'), None)
            assert classical_history is None
            print("Test edge case: player without classical rating history passed")

            # Test edge case: player who hasn't played in the last 30 days
            mock_get.return_value.json.return_value = [{'name': 'Classical', 'points': [[2023, 1, 1, 1600]]}]
            points = mock_get.return_value.json.return_value[0]['points']
            rating_history = generate_last_30_days_rating(points, start_date, today)
            for rating in rating_history.values():
                assert rating == 1600
            print("Test edge case: player who hasn't played in the last 30 days passed")

            # Test edge case: player who played exactly 30 days ago
            play_date = today - datetime.timedelta(days=30)
            mock_get.return_value.json.return_value = [{'name': 'Classical', 'points': [[play_date.year, play_date.month - 1 if play_date.month > 1 else 12, play_date.day, 1700]]}]
            points = mock_get.return_value.json.return_value[0]['points']
            rating_history = generate_last_30_days_rating(points, start_date, today)
            print(f"Expected: {1700}, Actual: {rating_history[start_date.isoformat()]}")
            assert rating_history[start_date.isoformat()] == 1700
            print("Test edge case: player who played exactly 30 days ago passed")

            # Test edge case: no players returned
            mock_get.return_value.json.return_value = {'users': []}
            players = fetch_top_50_classical_players()
            assert len(players) == 0
            print("Test edge case: no players returned passed")

    print("All tests completed.")


if __name__ == "__main__":
    print_top_50_classical_players()
    print_last_30_day_rating_for_top_player()
    generate_rating_csv_for_top_50_classical_players()
    run_tests()


