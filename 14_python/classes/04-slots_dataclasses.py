import timeit
from dataclasses import dataclass
from functools import partial
from statistics import median


@dataclass(slots=False)
class Person:
    name: str
    address: str
    email: str


@dataclass(slots=True)
class PersonSlots:
    name: str
    address: str
    email: str


@dataclass(slots=False)
class Employee:
    dept: str


@dataclass(slots=True)
class EmployeeSlots:
    dept: str


def get_set_delete(person: Person | PersonSlots):
    person.address = "123 Main St"
    person.address
    del person.address


def main():
    person = Person("John", "123 Main St", "john@doe.com")
    person_slots = PersonSlots("John", "123 Main St", "john@doe.com")
    no_slots = median(timeit.repeat(partial(get_set_delete, person), number=1000000))
    slots = median(timeit.repeat(partial(get_set_delete, person_slots), number=1000000))
    print(f"No slots: {no_slots}")
    print(f"Slots: {slots}")
    print(f"% performance improvement: {(no_slots - slots) / no_slots:.2%}")


if __name__ == "__main__":
    main()