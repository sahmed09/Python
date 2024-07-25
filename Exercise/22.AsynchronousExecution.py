import time
from concurrent.futures import ThreadPoolExecutor


def return_number(a):
    time.sleep(1)
    return a


print(return_number(6))

start = time.time()
with ThreadPoolExecutor(max_workers=3) as executor:  # max_workers=3 -> 3 number will be print at a time
    for result in executor.map(return_number, range(20)):
        print('Count: {0}'.format(result))
print('The total time is: {0}'.format(time.time() - start))
