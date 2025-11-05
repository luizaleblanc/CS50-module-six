from cs50 import get_float


def main():
    dollars = get_change_owed()
    cents = round(dollars * 100)

    coin_count = 0

    coin_count += cents // 25
    cents = cents % 25

    coin_count += cents // 10
    cents = cents % 10

    coin_count += cents // 5
    cents = cents % 5

    coin_count += cents

    print(coin_count)


def get_change_owed():
    while True:
        try:
            dollars = get_float("Change owed: ")
            if dollars >= 0:
                return dollars
        except ValueError:
            pass


if __name__ == "__main__":
    main()
