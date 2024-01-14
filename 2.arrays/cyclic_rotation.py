# Rotate an array to the right by given number of steps


def cyclic_rotation(arr, p):
    """
    This function takes 2 arguments, array and a position.
    The position argument is responsible for the elements that will rotate.
    """

    n = len(arr)

    for i in range(p):
        last_item = arr[n - 1]
        for j in range(n - 1, 0, -1):
            arr[j] = arr[j - 1]
        arr[0] = last_item

    return arr


def main():
    array = [3, 4, 5, 8, 9, 11, 13]
    print(
        f"{array} is an array. Type a position value, which will rotate elements to right.\n"
    )
    position = int(input("Enter a position value: "))
    print(f"{array} -> {cyclic_rotation(array, position)}")


if __name__ == "__main__":
    main()
