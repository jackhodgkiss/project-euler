#!/usr/bin/env python3
from collections import deque
import math
from typing import Deque, Generator


def factor_seq(number: int = 13195) -> Generator[int, None, None]:
    upper_limit: int = math.isqrt(number)
    smaller_factors: Deque = deque()
    for potential_factor in range(1, upper_limit):
        div_mod: tuple(int, int) = divmod(number, potential_factor)
        if div_mod[1] == 0:
            smaller_factors.append(potential_factor)
            yield div_mod[0]
    for factor in reversed(smaller_factors):
        yield factor


def is_prime(number: int = 541) -> bool:
    if number == 1:
        return False
    if number == 2 or number == 3:
        return True
    if number % 2 == 0:
        return False
    result: bool = True
    sieve_max_size: int = math.isqrt(number) + 1
    sieve: list[int] = [True] * (sieve_max_size // 2)
    for index, value in enumerate(sieve, 1):
        divisor: int = (index * 2) + 1
        if value:
            if number % divisor != 0:
                for mult_index in range(index - 1, len(sieve), divisor):
                    sieve[mult_index] = False
            else:
                result = False
                break
        else:
            for mult_index in range(index - 1, len(sieve), divisor):
                sieve[mult_index] = False
    return result


def main() -> None:
    answer: int = next(factor for factor in factor_seq(
        600851475143)if is_prime(factor))
    print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
