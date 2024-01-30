import itertools


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def main() -> None:
    # Test data
    data = [1, 2, 3, 4, 5]

    # TODO
    perms = list(itertools.permutations(data))

    filtered_permutations = [perm for perm in perms if is_prime(perm[0])]

    chained_permutations = list(itertools.chain(*filtered_permutations))

    print(chained_permutations)

    # Print the sum of the chained permutations
    print("Sum of chained permutations:", sum(chained_permutations))


if __name__ == "__main__":
    main()
