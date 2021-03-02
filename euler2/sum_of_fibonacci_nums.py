"""Module that calculates the sum of whatever fibonacci numbers you care about"""

def fibonacci():
    last, current = 0, 1
    print(f"Fib(0) is {last}", f"Fib(1) is {current}", sep='\n')
    for i in range(2, 10):
        last, current = current, current+last
        print(f"Fib({i}) is {current}")

if __name__ == "__main__":
    fibonacci()