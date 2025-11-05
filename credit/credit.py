from cs50 import get_string


def main():
    card_str = get_string("Number: ")
    length = len(card_str)

    if not is_luhn_valid(card_str):
        print("INVALID")
        return

    if length == 15 and card_str.startswith(("34", "37")):
        print("AMEX")

    elif length == 16 and card_str.startswith(("51", "52", "53", "54", "55")):
        print("MASTERCARD")

    elif (length == 13 or length == 16) and card_str.startswith("4"):
        print("VISA")

    else:
        print("INVALID")


def is_luhn_valid(number_str):
    total_sum = 0
    multiply_toggle = False

    for digit_char in reversed(number_str):
        digit = int(digit_char)

        if multiply_toggle:
            product = digit * 2
            total_sum += (product // 10) + (product % 10)
        else:
            total_sum += digit

        multiply_toggle = not multiply_toggle

    return (total_sum % 10) == 0


if __name__ == "__main__":
    main()
