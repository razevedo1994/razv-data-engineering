import itertools
from dataclasses import dataclass


@dataclass
class Item:
    name: str
    weight: float


def main() -> None:
    # Counting
    for i in itertools.count(10):
        print(i)
        if i == 15:
            break

    # Repeating
    for i in itertools.repeat(10, 4):
        print(i)

    # Accumulate
    subtotals = [1, 4, 7, 8, 2, 3, 5, 6, 9, 10]
    for i in itertools.accumulate(subtotals):
        print(i)

    # Get all permutations of length 2
    items = ["a", "b", "c"]
    perms = itertools.permutations(items, 2)

    # Print the permutations
    for perm in perms:
        print(perm)

    # Print all permutations as a single list
    print(list(itertools.permutations(items)))

    # Combining different iterables
    for item in itertools.chain(items, range(5)):
        print(item)

    print(list(itertools.permutations(range(3), 2)))

    # Get all combinations of length 2 (order does not matter)
    print(list(itertools.combinations(items, 2)))

    # Itertools chain
    more_items = ["d", "e", "f"]
    all_items = itertools.chain(items, more_items)
    print(list(all_items))

    # Filter false
    iventory = [
        Item("laptop", 1.5),
        Item("phone", 0.5),
        Item("book", 1.0),
        Item("camera", 1.0),
        Item("headphones", 0.5),
        Item("charger", 0.5),
    ]

    # Filter out items with weight less than 1
    print(list(itertools.filterfalse(lambda x: x.weight < 1, iventory)))

    # Starmap
    print(list(itertools.starmap(lambda x, y: x * y, [(2, 6), (8, 4), (5, 3)])))


if __name__ == "__main__":
    main()
