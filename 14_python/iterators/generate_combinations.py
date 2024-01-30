from typing import Collection
import itertools


# This function calculates the average of a list of numbers
# Note: I'm using the Collection type hint here, which is a generic type hint
# for collections/iterables that support the len() function.
def calculate_average(numbers: Collection[int]) -> float:
    total = sum(numbers)
    return total / len(numbers)


def main() -> None:
    data = [1, 2, 3, 4, 5]

    perms = list(itertools.combinations(data, 2))

    # TODO
    averages: list[int] = [calculate_average(x) for x in perms]

    print("Averages of combinations:")
    for average in averages:
        print(average)


if __name__ == "__main__":
    main()
