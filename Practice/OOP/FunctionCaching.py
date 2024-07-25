import time
from functools import lru_cache
# Decorator to wrap a function with a memorizing callable that saves up to the maxsize most recent calls.
# It can save time when an expensive or I/O bound function is periodically called with the same arguments.


@lru_cache(maxsize=32)
def some_work(n):
    time.sleep(n)
    return n


@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


if __name__ == '__main__':
    print("Running Some Work")
    some_work(3)
    print("Running Some Work")
    # some_work(4)
    print("Running Some Work")
    # some_work(5)
    print("Done Calling Again")
    some_work(3)
    # some_work(5)
    print("Called Again")
    print(some_work.cache_info())
    print()

    print([fib(n) for n in range(16)])
    print(fib.cache_info())
