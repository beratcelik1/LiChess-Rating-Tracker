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
