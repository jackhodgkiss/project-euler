#!/usr/bin/env python3
from typing import Callable, Sequence


def main() -> None:
    mod_filter: Callable[[int], bool] = \
        lambda number: number % 3 == 0 or number % 5 == 0
    numbers: Sequence = range(1, 1_000)
    answer: int = sum(filter(mod_filter, numbers))
    print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
