"""Module that calculates the sum of whatever fibonacci numbers you care about"""
import argparse
import os
import sys

def create_file(tail):
    head, tail = os.path.split(tail)
    if not os.path.exists(head):
        sys.exit("{}: Directory does not exist.".format(head))
    elif tail == '':
        sys.exit("FILE must not end with a slash. The last component of the path should be the filename.")
    tail = tail.split('.')[0]
    tail += '.txt'
    f = open(os.path.join(head,tail), "w")
    return f

def fibonacci(args):
    if args.file is not sys.stdout:
        args.file = create_file(args.file)
    last, current = 0, 1
    print(f"Fib(0) is {last}", f"Fib(1) is {current}", sep='\n', file=args.file)
    for i in range(2, args.n+1):
        last, current = current, current+last
        print(f"Fib({i}) is {current}", file=args.file)
    args.file.close()

def nth_fibonacci(args):
    if args.n == 0:
        return print(0)
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

    parser_list = subparsers.add_parser('list', description='Lists all the fibonacci terms, up to F(n)')
    parser_list.add_argument('n', type=int, help='Is the last fibonacci term that the action will list')
    parser_list.add_argument('-f', '--file', type=str, default=sys.stdout,
                             help='Creates text file called FILE. Fibonacci terms will be written to\
                                   FILE instead of the command line. FILE can be a path, but the last\
                                   component of the path will be the filename. Any extensions to FILE\
                                   will be stripped away, the end result will always be FILE.txt.\
                                   WARNING: if FILE already exists, all of its contents will be deleted\
                                   before writing the terms')
    parser_list.set_defaults(func=fibonacci)

    parser_nth_fibonacci = subparsers.add_parser('nth_fibonacci', description='Given n, returns F(n).')
    parser_nth_fibonacci.add_argument('n', type=int, help='The fibonacci term you want')
    parser_nth_fibonacci.set_defaults(func=nth_fibonacci)

    args = parser.parse_args()
    args.func(args)
