"""
Project Euler #1

This CLI will efficiently calculate the sum of multiples of whatever
integer you wish, within any range you wish.  

Given two integers, it will add up their sum of multiples, without any 
duplicate multiples in the mix.
"""

import argparse
from math import floor

def validate_range(range):
    if range[0] < 1:
        print('Error: Start of the range cannot be smaller than 1')
        return False
    elif range[0] > range[1]:
        print('Error: Start of the range cannot be larger than end of the range')
        return False
    elif range[1] < range[0]:
        print('Error: End of the range cannot be smaller than start of the range')
        return False

    return True


def som(num, args):
    # If range starts at 1, first term will be the number we are trying to find the som of
    if args.range[0] == 1:
        first_term = num
    else:
        # Find the closest first term equal or above the lowerbound of the range
        first_term = (args.range[0] // num) * num

        # Equation above for first_term might fall below the range, so add 1 after the floor division. 
        # Ex. (10 // 3) * 3 = 9   |  9 < 10
        # ((10 // 3) + 1) * 3 = 12   | 12 > 10
        if first_term < args.range[0]:
            first_term = ((args.range[0] // num) + 1) * num
    
    last_term = (args.range[1] // num) * num
    amount_of_terms = get_amount_of_terms(first_term, last_term, num)

    sum_of_multiples = floor( ((first_term + last_term) / 2) * amount_of_terms)
    return sum_of_multiples

def get_amount_of_terms(first_term, last_term, difference):
    # solves for amount of terms using this equation. 
    # (amount of terms = x, first_term = a, last_term = b, difference = d)
    # b = a + (x - 1) * a
    last_term -= first_term  # b = (x - 1) * d
    last_term /= difference  # b = (x - 1)
    last_term += 1           # b = x
    amount_of_terms = floor(last_term)  # Floor it just in case

    return amount_of_terms


def som_for_two(args):
    # som for the lcm of the two numbers will contain all
    # of their shared multiples, which we will subtract.
    lcm = get_lcm(args.nums[0], args.nums[1])

    num1 = som(args.nums[0], args)
    num2 = som(args.nums[1], args)
    lcm_mults = som(lcm, args)

    return num1 + num2 - lcm_mults


def get_gcd(a, b):
    # Uses Euclidean algorithm
    while b:
        a, b = b, a%b
    return a


def get_lcm(x, y):
    # x*y = lcm * gcd  which means...
    # (x*y) // gcd = lcm
    lcm = (x * y) // get_gcd(x, y)
    return lcm

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Calculate sum of multiples of the given integer(s)",
        formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('nums', type=int, nargs='+',
                        help='Integer with which to find the sum of their multiples')

    parser.add_argument('--range', '-r', type=int, nargs=2, metavar=('start', 'end'), required=True,
                        help='Range in which to look for multiples (inclusive).\n'
                            'If start < 1, start will be changed to 1. ' 
                            'If end < start, end will be changed to start + 1')

    args = parser.parse_args()

    if validate_range(args.range):
        if len(args.nums) == 1:
            print(som(args.nums[0], args))
        elif len(args.nums) == 2:
            print(som_for_two(args))
        else:
            print('Error: Maximum 2 numbers can have their multiples summed up')
    else:
        exit()
