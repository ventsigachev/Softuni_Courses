import time
from decimal import Decimal


class store_results:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args):

        start = time.ctime()
        e_start = Decimal(time.time())
        result = self.func(*args)
        e_end = Decimal(time.time())
        end = time.ctime()
        timer = f" Started at: {start}, ended at: {end}.\n" \
                f"Execution time is {round(e_end - e_start, 10)} sec."

        with open("results.txt", "a") as file:
            file.write(f"Function '{self.func.__name__.upper()}'"
                       f" was called.{timer} Result: {result}\n\n")


@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


add(2, 2)
mult(6, 4)
