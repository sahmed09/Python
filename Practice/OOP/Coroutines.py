"""Coroutines are generalization of subroutines. They are used for cooperative multitasking where a process
voluntarily yield (give away) control periodically or when idle in order to enable multiple applications
to be run simultaneously."""
# In Python, coroutines are similar to generators but with few extra methods and slight change in how we
# use yield statement. Generators produce data for iteration while coroutines can also consume data.

# When first value is sent to it, it checks for prefix and print name if prefix present.
# After printing name it goes through loop until it encounters name = (yield) expression again.
print("coroutine execution:")


# Python3 program for demonstrating coroutine execution:
def print_name(prefix):
    print(f"Searching prefix: {prefix}")
    while True:
        name = (yield)
        if prefix in name:
            print(name)


corou = print_name("Dear")  # calling coroutine, nothing will happen

# This will start execution of coroutine and Prints first line "Searching prefix..."
# and advance execution to the first yield expression
corou.__next__()

# sending inputs
corou.send("Atul")
corou.send("Dear Atul")
print()

# Python3 program for demonstrating closing a coroutine:
print("closing a coroutine:")


def print_name(prefix):
    print(f"Searching prefix: {prefix}")
    try:
        while True:
            name = (yield)
            if prefix in name:
                print(name)
    except GeneratorExit:
        print("Closing Coroutine")


corou = print_name("Dear")
corou.__next__()
corou.send("Atul")
corou.send("Dear Atul")
corou.close()
print()

print("Chaining coroutines for creating pipeline:")
# Coroutines can be used to set pipes. We can chain together coroutines and push data through pipe using send() method.
# An initial source(producer) which derives the whole pipe line.
# A sink, which is the end point of the pipe. A sink might collect all data and display it.

# program for demonstrating coroutine chaining :


def producer(sentence, next_coroutine):
    """
        Producer which just split strings and feed it to pattern_filter coroutine
    """
    tokens = sentence.split(" ")
    for token in tokens:
        next_coroutine.send(token)
    next_coroutine.close()


def pattern_filter(pattern="ing", next_coroutine=None):
    """
        Search for pattern in received token and if pattern got matched, send it to
        print_token() coroutine for printing
    """
    print(f"Searching for: {pattern}")
    try:
        while True:
            token = (yield)
            if pattern in token:
                next_coroutine.send(token)
    except GeneratorExit:
        print("Done with filtering!!")


def print_token():
    """
        Act as a sink, simply print the received tokens
    """
    print("I'm sink, i'll print tokens")
    try:
        while True:
            token = (yield)
            print(token)
    except GeneratorExit:
        print("Done with printing!!")


pt = print_token()
pt.__next__()
pf = pattern_filter(next_coroutine=pt)
pf.__next__()

sentence = "Bob is running behind a fast moving car"
producer(sentence, pf)
pt.close()
print()


# Extra:
def sercher():
    import time

    # 4 seconds time break
    book = "this is a book --- ."
    time.sleep(4)

    while True:
        text = (yield)
        if text in book:
            print("Your text is in the book.")
        else:
            print("Your text is not in the book.")


search = sercher()
print("Search Started")
next(search)
print("Next method run")
search.send("book")
input("Press any key ")  # next two block will not hold for 4 seconds and print immediately.
search.send("book")
input("Press any key ")
search.send("book")
search.close()
