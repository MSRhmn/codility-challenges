# Find the missing element in a given permutation


def perm_missing_elem(arr):
    """
    Given a permutation array with missing element it returns that element.
    """
    # Sum of the current array elements
    current_elem_sum = 0

    for i in arr:
        current_elem_sum += i

    # Apply arithmetic progression to sum of actual array
    n = len(arr) + 1
    sum_of_elem = n * (n + 1) // 2
    missing_elem = sum_of_elem - current_elem_sum
    return missing_elem


def main():
    A = [2, 3, 1, 5]
    print(perm_missing_elem(A))


if __name__ == "__main__":
    main()
