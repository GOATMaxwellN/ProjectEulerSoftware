"""Module that calculates the sum of whatever fibonacci numbers you care about"""

def fibonacci():
    last, current = 0, 1
    print(f"Fib(0) is {last}", f"Fib(1) is {current}", sep='\n')
    for i in range(2, 10):
        last, current = current, current+last
        print(f"Fib({i}) is {current}")

def sum_of_even_fib_nums(upperbound):
    sum = 0
    last, current = 0, 1
    while current < upperbound:
        last, current = current, current+last
        if current % 2 == 0:
            sum += current
    return sum

if __name__ == "__main__":
    pass