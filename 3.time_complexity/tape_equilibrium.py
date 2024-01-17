# Minimize the value |(A[0] + ... + A[P-1]) - (A[P] + ... + A[N-1])|


def tape_equilibrium(arr):
    """
    Takes a non-empty array, declares 2 variable and calculates absolute difference between them.
    Lastly returns the minimal difference of two part of the array.
    """
    sum_of_left = arr[0]
    sum_of_right = 0

    for i in range(1, len(arr)):
        sum_of_right += arr[i]

    diff = abs(sum_of_left - sum_of_right)

    for P in range(1, len(arr) - 1):
        sum_of_left += arr[P]
        sum_of_right -= arr[P]

        new_diff = abs(sum_of_left - sum_of_right)
        if new_diff < diff:
            diff = new_diff

    return diff


def main():
    A = [3, 1, 2, 4, 3]
    print(tape_equilibrium(A))


if __name__ == "__main__":
    main()
