from cs50 import get_int

def main():
    height = get_height()

    for row in range(1, height + 1):

        spaces = " " * (height - row)
        hashes = "#" * row
        gap = "  "

        print(f"{spaces}{hashes}{gap}{hashes}")


def get_height():
    while True:
        try:
            n = get_int("Height: ")
            if n >= 1 and n <= 8:
                return n
        except ValueError:
            pass


if __name__ == "__main__":
    main()
