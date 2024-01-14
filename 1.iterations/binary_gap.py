# Find longest sequence of zeros in binary representation of an integer.


def into_binary(n):
    """This function takes takes an integer as argument and converts it into binary"""
    binary = ""
    while n > 0:
        remainder = n % 2
        binary = str(remainder) + binary
        n //= 2
    return binary


def main():
    int_value = int(input("Enter an integer value: "))
    binary_string = into_binary(int_value)

    current_gap = 0
    max_gap = 0

    for digit in binary_string:
        if digit == "0":
            current_gap += 1
        elif digit == "1":
            if current_gap > max_gap:
                max_gap += current_gap
                current_gap = 0

    print(f"The longest binary gap in {int_value} is: {max_gap}")


if __name__ == "__main__":
    main()
