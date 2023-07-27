import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_uppercase, k=12))


@dataclass
class Person:
    name: str
    address: str
    active: bool = True
    email_address: list[str] = field(default_factory=list)
    id: str = field(init=False, default_factory=generate_id)
    _search_string: str = field(init=False, repr=False)

    def __post_init__(self):
        self._search_string = f"{self.name} {self.address}"


def main() -> None:
    person = Person(name="Rodrigo", address="123 Main St")
    print(person)


if __name__ == "__main__":
    main()