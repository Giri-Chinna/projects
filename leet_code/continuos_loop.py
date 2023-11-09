import time

signal = [
    ('red', 4),
    ('green', 4),
    ('yellow', 2)
]

i=0
while True:
    color = signal[i][0]
    print(color)
    time.sleep(signal[i][1])

    if i == len(signal) -1:
        i = 0
    else:
        i += 1

"""Alternative way"""
from itertools import cycle

light = cycle(signal)
while True:
    c,s = next(light)
    print(c)
    time.sleep(s)
