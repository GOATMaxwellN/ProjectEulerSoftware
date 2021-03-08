"""CLI with some fibonacci calculating tools"""
import argparse
import os
import sys

def create_file(tail):
    """Creates a file in order to write the results of the desired calculation"""
    head, tail = os.path.split(tail)
    # checks if directories listed exist
    if not os.path.exists(head):
        sys.exit(f"{head}: Directory does not exist or is not relative to current directory. "
                   "Create the directory or use the absolute path. It may also be that the filename "
                   "doesn't conform to file naming conventions")
    elif tail == '':
        sys.exit("FILE must not end with a slash. The last component of the path should be the filename.")
    # gets rid of any extensions placed by user and replaces with '.txt'
    tail = tail.split('.')[0]
    tail += '.txt'
    f = open(os.path.join(head,tail), "w")
    return f

def fibonacci(args):
    """Used by the 'list' subparser. Writes all desired fibonacci terms and their values to either
    sys.stdout or a created file if user requested one"""
    if args.file is not None:
        file = create_file(args.file)
    else:
        file = sys.stdout
    last, current = 0, 1
    print(f"Fib(0) is {last}", f"Fib(1) is {current}", sep='\n', file=file)
    if args.max_term:
        for cur_term in range(2, args.n+1):
            last, current = current, current+last
            if filter_value(args, current):
                print(f"Fib({cur_term}) is {current}")
    elif args.max_num:
        cur_term = 2
        while current+last < args.n:
            last, current = current, current+last
            if filter_value(args, current):
                print(f"Fib({cur_term}) is {current}")
            cur_term += 1
    # close file if one was created
    if args.file:
        file.close()

def filter_value(args, fib_value):
    """Makes sure fibonacci terms and values calculated conform to user's wants. Currently only 
    able to filter by if the fibonacci value is a multiple of requested numbers"""
    if not args.divisible_by:
        return True
    for i in args.divisible_by:
        if fib_value % i == 0:
            return True
    return False

def nth_fibonacci(args):
    """Prints out value of requested fibonacci term"""
    if args.max_term == 0:
        return print(0)
    last, current = 0, 1
    for i in range(2, args.max_term+1):
        last, current = current, current+last
    print(current)

def sum_of_fibs(args):
    """Adds up all fibonacci values that conform to user's wants and prints out the sum"""
    if args.file is not None:
        file = create_file(args.file)
    else:
        file = sys.stdout
    last, current = 0, 1
    calculated_sum = 1
    if args.max_term:
        for i in range(2, args.n+1):
            last, current = current, current+last
            if filter_value(args, current):
                calculated_sum += current
    elif args.max_num:
        while current+last < args.n:
            last, current = current, current+last
            if filter_value(args, current):
                calculated_sum += current
    # close the file if one was created
    if args.file:
        file.close()
    # print the sum
    print(f'The sum is {calculated_sum}')

def sum_of_even_fibs(args):
    """Efficient way to find sum of even fibonaccis"""
    if args.file is not None:
        file = create_file(args.file)
    else:
        file = sys.stdout
    sum = 10
    last, current = 2, 8
    while True:
        new_current = 4*current+last
        if new_current < args.n:
            last, current = current, new_current
            sum += new_current
        else:
            break
    print('Sum:', sum, file=file)
    return

def list_even_fibs(args):
    """Efficient way to list sum of even fibonaccis"""
    if args.file is not None:
        file = create_file(args.file)
    else:
        file = sys.stdout
    last, current = 2, 8
    print(last, current, sep='\n', file=file)
    while True:
        new_current = 4*current+last
        if new_current < args.n:
            last, current = current, new_current
            print(new_current, file=file)
        else:
            return


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CLI with few tools")
    subparsers = parser.add_subparsers()

    # 'sum' and 'list' subparsers share the same arguments, so this parent parser will be inherited by those two subparsers
    list_sum_parent_parser = argparse.ArgumentParser(add_help=False)
    list_sum_parent_parser.add_argument('n', type=int, 
                             help='Depending on if -mt or -mn is selected, this determines the last fibonacci\
                                   term to go up to, or the biggest fibonacci value to stay below.')
    group = list_sum_parent_parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-mt', '--max-term', action='store_true',
                        help='Uses n to go through all fibonacci values up to the nth term. F(0) to F(n).')
    group.add_argument('-mn', '--max-num', action='store_true',
                        help='Uses n to go through all fibonacci values with a value less than n. F(0) to F(?) > n')
    list_sum_parent_parser.add_argument('-db', '--divisible-by', type=int, nargs='+', default=[],
                                        help='Only prints the Fibonacci values that are divisible by the numbers passed into this argument')
    list_sum_parent_parser.add_argument('-f', '--file', type=str, default=None,
                                        help='Creates text file called FILE. Fibonacci terms will be written to\
                                        FILE instead of the command line. FILE can be an existing path, but the last\
                                        component of the path will be the filename. Any extensions to FILE\
                                        will be stripped away, the end result will always be FILE.txt.\
                                        WARNING: if FILE already exists, all of its contents will be deleted\
                                        before writing the terms')
    
    parser_list = subparsers.add_parser('list', parents=[list_sum_parent_parser], description='Lists all the fibonacci terms, up to F(n)')
    parser_list.set_defaults(func=fibonacci)

    parser_nth_fibonacci = subparsers.add_parser('nth_fibonacci', description='Given n, returns F(n).')
    parser_nth_fibonacci.add_argument('n', type=int, help='The fibonacci term you want')
    parser_nth_fibonacci.set_defaults(func=nth_fibonacci)

    parser_sum = subparsers.add_parser('sum', parents=[list_sum_parent_parser], description='Adds up all the calculated Fibonacci terms')
    parser_sum.set_defaults(func=sum_of_fibs)

    parser_sum_of_even_fibs = subparsers.add_parser(
        'sum_of_even_fibs', description='Efficient way to calculate sum of even fibonacci values up to n')
    parser_sum_of_even_fibs.add_argument('n', type=int)
    parser_sum_of_even_fibs.add_argument('-f', '--file', type=str, default=None)
    parser_sum_of_even_fibs.set_defaults(func=sum_of_even_fibs)

    parser_list_even_fibs = subparsers.add_parser(
        'list_even_fibs', description='Efficient way to list even fibonacci values up to n'
    )
    parser_list_even_fibs.add_argument('n', type=int)
    parser_list_even_fibs.add_argument('-f', '--file', type=str, default=None)
    parser_list_even_fibs.set_defaults(func=list_even_fibs)

    args = parser.parse_args()
    args.func(args)
