from dataclasses import dataclass
from typing import Callable


@dataclass
class Customer:
    name: str
    age: str


def send_email_promotion(
        customers: list[Customer], is_eligible: Callable[[Customer], bool]
    ) -> None:
    for customer in customers:
        print(f"Cheking {customer.name}")
        if is_eligible(customer):
            print(f"{customer.name} is eligible for promotion")
        else:
            print(f"{customer.name} is not eligible for promotion")

def is_eligible_for_promotion(customer: Customer) -> bool:
    return customer.age > 50


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
    send_email_promotion(customers, is_eligible_for_promotion)
    # send_email_promotion(customers, lambda customer: customer.age > 50)


if __name__ == "__main__":
    main()