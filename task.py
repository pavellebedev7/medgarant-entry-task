import numpy as np
import time

FIRST = 1
LAST = 10
SIZE = 100000

numbers = list(np.random.randint(low=FIRST, high=LAST, size=SIZE))

# Initial algorithm
t0 = time.process_time()
for i, number in enumerate(numbers):
    number_is_in_tail = number in numbers[i + 1:]
    # Output for testing
    # print(number_is_in_tail)
elapsed_time0 = time.process_time() - t0
print(f'Initial algorithm time {elapsed_time0} s')

# Improved algorithm
t1 = time.process_time()
array = [0] * SIZE  # numbers present in the list
for index in range(len(numbers)):
    array[numbers[index] - 1] += 1
for index in range(len(numbers)):
    array[numbers[index] - 1] -= 1
    if array[numbers[index] - 1] == 0:
        number_is_in_tail = False
    else:
        number_is_in_tail = True
    # Output for testing
    # print(number_is_in_tail)
elapsed_time1 = time.process_time() - t1
print(f'Improved algorithm time {elapsed_time1} s')
