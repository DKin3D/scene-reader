import sys
import time

st = 0.05


def txt(str):
    for letter in str:
        sys.stdout.write(letter)
        time.sleep(st)
        sys.stdout.flush()
        time.sleep(st)
    print()
