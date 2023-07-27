import random
import string


def generate_id() -> str:
    return "".join(random.choices(string.ascii_uppercase, k=12))


class Person:
    def __init__(self, name: str, address: str) -> None:
        self.id = generate_id()
        self.name = name
        self.address = address
        self.email_address = []


def main() -> None:
    person = Person(name="Rodrigo", address="123 Main St")
    print(person)

if __name__ == "__main__":
    main()