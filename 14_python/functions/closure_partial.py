from dataclasses import dataclass
from functools import partial
from typing import Callable


@dataclass
class Customer:
    name: str
    age: int


def send_email_promotion(
    customers: list[Customer], is_eligible: Callable[[Customer], bool]
) -> None:
    for customer in customers:
        print(f"Checking {customer.name}")
        if is_eligible(customer):
            print(f"{customer.name} is eligible for promotion")
        else:
            print(f"{customer.name} is not eligible for promotion")


def is_eligible_for_promotion(customer: Customer, cutoff_age: int) -> bool:
    return customer.age > cutoff_age


def is_eligible_closure(cutoff_age: int) -> Callable[[Customer], bool]:
    def is_eligible(customer: Customer) -> bool:
        return customer.age > cutoff_age

    return is_eligible


def main() -> None:
    customers = [
        Customer("Alice", 25),
        Customer("Bob", 30),
        Customer("Charlie", 35),
        Customer("David", 40),
        Customer("Eve", 45),
        Customer("Frank", 50),
        Customer("Grace", 55),
        Customer("Holly", 60),
        Customer("Iris", 65),
    ]
    send_email_promotion(customers, is_eligible_closure(50))
    is_eligible_partial = partial(is_eligible_for_promotion, cutoff_age=50)
    send_email_promotion(customers, is_eligible_partial)


if __name__ == "__main__":
    main()