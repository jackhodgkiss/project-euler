#!/usr/bin/env python3
from itertools import takewhile
from typing import Generator


def fib_seq() -> Generator[int, None, None]:
    previous_term, current_term = 1, 1
    while True:
        yield current_term
        current_term = current_term + previous_term
        previous_term = current_term - previous_term


def main() -> None:
    fib_terms = takewhile(lambda term: term < 4_000_000, fib_seq())
    even_fib_terms = filter(lambda term: term % 2 == 0, fib_terms)
    answer: int = sum(even_fib_terms)
    print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
