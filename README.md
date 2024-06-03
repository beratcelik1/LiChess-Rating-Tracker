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
    cd lichess-rating-tracker
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

# Code Overview

## Functions

- `fetch_data(url: str) -> Optional[Dict]`: Helper function to fetch data from a given URL.
- `fetch_top_50_classical_players() -> List[Dict]`: Fetches the top 50 classical chess players.
- `fetch_rating_history(username: str) -> Optional[List[Dict]]`: Fetches the rating history for a specific player.
- `print_top_50_classical_players() -> None`: Prints the usernames of the top 50 classical chess players.
- `generate_last_30_days_rating(points: List[List[int]], start_date: datetime.date, end_date: datetime.date) -> Dict[str, Optional[int]]`: Generates rating history for the last 30 days using a deque.
- `print_last_30_day_rating_for_top_player() -> None`: Prints the rating history for the top player in the last 30 days.
- `generate_rating_csv_for_top_50_classical_players() -> None`: Generates a CSV file for the top 50 players' ratings over the last 30 days.
- `run_tests() -> None`: Runs tests to validate the functionality of the script.

## Example

Here is an example of how you might use the script:

```python
if __name__ == "__main__":
    print_top_50_classical_players()
    print_last_30_day_rating_for_top_player()
    generate_rating_csv_for_top_50_classical_players()
    run_tests()
```

# CSV File Structure

The generated CSV file `top_50_players_ratings.csv` will have the following structure:

- The first column will be the player’s username.
- The 2nd column will be the player’s rating 30 days ago.
- The 32nd column will be the player’s rating today.
- Each row will represent one player, and each column will represent a date within the last 30 days, starting from 30 days ago to today.

## Key Assumptions

- If a player does not play on a given day, their rating remains the same as the last known rating.

## License

This project is licensed under the MIT License.
