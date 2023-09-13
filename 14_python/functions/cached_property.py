import statistics
from functools import cached_property
from typing import Iterable


class Dataset:
    def __init__(self, sequence_of_numbers : Iterable[float]) -> None:
        self._data = tuple(sequence_of_numbers)

    @cached_property
    def stdev(self):
        print("Computing stdev...")
        return statistics.stdev(self._data)
    

def main() -> None:
    data = Dataset([1, 2, 3, 4, 5])
    print(data.stdev)
    print(data.stdev)
    print(data.stdev)


if __name__ == "__main__":
    main()