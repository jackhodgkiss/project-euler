def main():
    def is_mult(left, right): return left % right == 0
    multiples = [number for number in range(
        3, 1_000) if is_mult(number, 3) or is_mult(number, 5)]
    answer = sum(multiples)
    print(f'Answer: {answer}')


if __name__ == '__main__':
    main()
