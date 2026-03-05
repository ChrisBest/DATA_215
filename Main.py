from scripts.queries import merge_players_games, achievement_counts


def main():
    merged_data = merge_players_games()
    print("Merged Data:")
    print(merged_data.head())

    counts = achievement_counts()
    print("\nAchievement Counts:")
    print(counts.head())


if __name__ == "__main__":
    main()