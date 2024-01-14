# Count minimal number of jumps from position X to Y


def frog_jmp(X, Y, D):
    """
    It solutions a frog distance reaching from point X to Y.
    D is the one time performace of the frog to make distance.

    """
    distance = Y - X

    if distance % D == 0:
        return distance // D
    return distance // D + 1


def main():
    coordinate_a = 11
    coordinate_b = 84
    jump = 12

    print(
        f"Little frog needs to make {frog_jmp(coordinate_a, coordinate_b, jump)} jumps to travel from {coordinate_a} to {coordinate_b} position."
    )


if __name__ == "__main__":
    main()
