# from numba import jit  # pip install numba
import numpy as np
import time

x = np.arange(1000).reshape(100, 10)


# @jit(nopython=True)
def go_faster(a):  # Function is compiled and runs in machine code
    trace = 0.0
    for i in range(a.shape[0]):
        trace += np.tanh(a[i, i])
    return a + trace


# Do not repeat this. Compilation time is included in the execution time!
start = time.time()
go_faster(x)
end = time.time()
print('Elapsed (with compilation) = %s' % (end - start))

# Now the function is compiled, Re-time it executing from cache
start = time.time()
go_faster(x)
end = time.time()
print('Elapsed (after compilation) = %s' % (end - start))
