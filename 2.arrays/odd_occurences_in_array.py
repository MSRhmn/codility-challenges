# Find value that occurs in odd number of elements


def odd_occurences_in_array(arr):
    """
    This is a function which takes an array of elements.
    Returns an odd number in those elements.
    """
    n = len(arr)

    for i in range(0, n):
        count = 0
        for j in range(0, n):
            if arr[i] == arr[j]:
                count += 1
        if count % 2 != 0:
            return arr[i]

    return None


def main():
    array_of_elements = [9, 3, 5, 9, 5, 9, 3, 8, 9]
    print(
        f" Odd number in {array_of_elements} is: {odd_occurences_in_array(array_of_elements)}"
    )


if __name__ == "__main__":
    main()
