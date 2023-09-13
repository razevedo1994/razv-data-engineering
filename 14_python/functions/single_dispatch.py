from functools import singledispatch


@singledispatch
def add(x: int, y:int) -> int:
    return x + y


@add.register
def _(x: str, y: str) -> str:
    return f"{x} {y}"


@add.register
def _(x: list | set, y: list | set) -> list:
    return [*x, *y]


add.register(tuple, lambda x, y: (*x, *y))


def main() -> None:
    print(add(1, 2))
    print(add("Hello", "World"))
    print(add([1, 2, 3], [4, 5, 6]))
    print(add({1, 2, 3}, {4, 5, 6}))
    print(add((1, 2, 3), (4, 5, 6)))


if __name__ == "__main__":
    main()