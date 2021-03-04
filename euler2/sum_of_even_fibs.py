"""Module that calculates the sum of whatever fibonacci numbers you care about"""
import argparse

def fibonacci():
    last, current = 0, 1
    print(f"Fib(0) is {last}", f"Fib(1) is {current}", sep='\n')
    for i in range(2, 10):
        last, current = current, current+last
        print(f"Fib({i}) is {current}")

def nth_fibonacci(args):
    last, current = 0, 1
    for i in range(2, args.n+1):
        last, current = current, current+last
    print(current)

def sum_of_even_fib_nums(upperbound):
    sum = 0
    last, current = 0, 1
    while current < upperbound:
        last, current = current, current+last
        if current % 2 == 0:
            sum += current
    return sum

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Module with lots of Fibonacci tools.")
    subparsers = parser.add_subparsers()

    parser_nth_fibonacci = subparsers.add_parser('nth_fibonacci', help='Given n, returns F(n).')
    parser_nth_fibonacci.add_argument('n', type=int)
    parser_nth_fibonacci.set_defaults(func=fibonacci)

    args = parser.parse_args()
    args.func(args)
