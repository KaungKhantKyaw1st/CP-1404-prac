"""KKK"""
FILENAME = "wimbledon.csv"
COUNTRY_INDEX = 1
CHAMPION_INDEX = 2


def main():
    """Read data from file and display champions, win counts, and winning countries."""
    champion_to_win_count = {}
    records = read_file()
    display_champions(champion_to_win_count, records)
    display_winning_countries(records)


def display_winning_countries(records):
    """Display the countries that have won Wimbledon."""
    countries = {record[COUNTRY_INDEX] for record in records[1:]}  # Skip the header row
    print(f"These {len(countries)} countries have won Wimbledon: ")
    print(", ".join(sorted(countries)))


def display_champions(champion_to_win_count, records):
    """Display champions and the number of times they've won."""
    for record in records[1:]:  # Skip the header row
        champion = record[CHAMPION_INDEX]
        champion_to_win_count[champion] = champion_to_win_count.get(champion, 0) + 1
    print("Wimbledon Champions:")
    for champion, wins in champion_to_win_count.items():
        print(f"{champion} {wins}")


def read_file():
    """Open and read the file, returning the data as a list of lists."""
    with open(FILENAME, "r", encoding="utf-8-sig") as file:
        return [line.strip().split(",") for line in file]


main()