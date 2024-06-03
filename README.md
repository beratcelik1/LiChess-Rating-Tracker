# Lichess Rating Tracker

## Overview
This project fetches and displays information about the top 50 classical chess players from Lichess.org. It includes functionalities to list the top players, print the rating history for the top player over the last 30 days, and generate a CSV file with the rating history for the top 50 players for the last 30 days.

## Features
- List the usernames of the top 50 classical chess players.
- Print the rating history for the top player in classical chess over the last 30 calendar days.
- Generate a CSV file showing the rating history for each of the top 50 players over the last 30 days.

## Requirements
- Python 3.x
- Requests library (`pip install requests`)

## Installation

Clone the repository:
    ```
    git clone https://github.com/beratcelik1/lichess-rating-tracker.git
    ```

## Usage

1. **List Top 50 Classical Chess Players**
    ```python
    from chess_players_rating_tracker import print_top_50_classical_players

    print_top_50_classical_players()
    ```

2. **Print Rating History for the Top Player**
    ```python
    from chess_players_rating_tracker import print_last_30_day_rating_for_top_player

    print_last_30_day_rating_for_top_player()
    ```

3. **Generate CSV for Top 50 Players' Ratings**
    ```python
    from chess_players_rating_tracker import generate_rating_csv_for_top_50_classical_players

    generate_rating_csv_for_top_50_classical_players()
    ```

## Running Tests
This project includes tests to ensure the correctness of the implemented functions. To run the tests, execute the following command:
```python
from chess_players_rating_tracker import run_tests

run_tests()
```

## Code Overview

### Functions

- **fetch_data(url: str) -> Optional[Dict]**
  - Helper function to fetch data from a given URL.
  - Returns a JSON response if the request is successful, otherwise returns None.

- **fetch_top_50_classical_players() -> List[Dict]**
  - Fetches the top 50 classical chess players from the Lichess API.
  - Returns a list of dictionaries containing player information.

- **fetch_rating_history(username: str) -> Optional[List[Dict]]**
  - Fetches the rating history for a specific player from the Lichess API.
  - Returns a list of dictionaries containing the player's rating history.

- **print_top_50_classical_players() -> None**
  - Prints the usernames of the top 50 classical chess players.

- **generate_last_30_days_rating(points: List[List[int]], start_date: datetime.date, end_date: datetime.date) -> Dict[str, Optional[int]]**
  - Generates the rating history for the last 30 days using a deque.
  - Takes the rating points, start date, and end date as inputs.
  - Returns a dictionary with dates as keys and ratings as values.

- **print_last_30_day_rating_for_top_player() -> None**
  - Prints the rating history for the top classical chess player over the last 30 days.

- **generate_rating_csv_for_top_50_classical_players() -> None**
  - Generates a CSV file showing the rating history for each of the top 50 players over the last 30 days.
  - The CSV includes the player's username and their ratings for each day in the last 30 days.

- **run_tests() -> None**
  - Runs tests to validate the functionality of the script.
  - Includes tests for fetching top players, fetching rating history, generating rating history for the last 30 days, and edge cases.

## Key Assumptions

- If a player does not play on a given day, their rating remains the same as the last known rating.

## Explanation of Empty Cells in the CSV

In the generated CSV file, you may notice that some cells are empty. This is because the Lichess rating history for some players might not cover all the last 30 days. Here are the possible reasons for the empty cells:

1. **Recent Start**: Some players have only recently started playing classical chess games on Lichess. For instance:
   - If a player started playing 5 days ago, the initial 25 cells will be empty for the days before they started playing.

2. **Irregular Play**: Some players may not have played every day within the last 30 days. In such cases, their rating remains the same as the last known rating until they play again. These cells will not be empty but will show the last known rating.

The code fills in the rating for each day by looking back to find the last known rating. For example:

- **Player C**: Played games on May 1st, May 5th, and May 10th. Their rating history will show:
  - May 1st: 1500 (rating on May 1st)
  - May 2nd: 1500 (last known rating from May 1st)
  - May 3rd: 1500 (last known rating from May 1st)
  - May 4th: 1500 (last known rating from May 1st)
  - May 5th: 1510 (rating on May 5th)
  - May 6th: 1510 (last known rating from May 5th)
  - May 7th: 1510 (last known rating from May 5th)
  - May 8th: 1510 (last known rating from May 5th)
  - May 9th: 1510 (last known rating from May 5th)
  - May 10th: 1520 (rating on May 10th)

### How the Code Searches Back for the Last Known Rating

To handle cases where a player has not played on a specific day, the code uses the following approach:

- It maintains a deque (double-ended queue) of sorted rating dates and their corresponding ratings.
- For each day in the last 30 days, it checks if the player has a rating for that specific day.
- If there is no rating for the day, the code looks back through the deque to find the last known rating and uses that value.

This approach ensures that the CSV file accurately reflects the available data while adhering to the key assumption that if a player doesn't play on a given day, their rating remains the same as the last known rating.

The presence of empty cells or repeated ratings is thus a normal occurrence and reflects the real-world scenario of varying player activity levels.

## License

This project is licensed under the MIT License.
