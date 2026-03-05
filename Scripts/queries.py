import pandas as pd
from scripts.config import read_csv_from_s3


def load_players():
    return read_csv_from_s3("gaming_data/players.csv")


def load_games():
    return read_csv_from_s3("gaming_data/games.csv")


def load_achievements():
    return read_csv_from_s3("gaming_data/achievements.csv")


def load_history():
    return read_csv_from_s3("gaming_data/history.csv")


def merge_players_games():
    players = load_players()
    history = load_history()

    merged = history.merge(players, on="playerid", how="left")
    return merged


def achievement_counts():
    history = load_history()

    result = (
        history.groupby("playerid")
        .size()
        .reset_index(name="achievement_count")
    )

    return result