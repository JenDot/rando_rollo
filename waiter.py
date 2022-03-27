"""A module to handle time.sleep() for reuse."""
import time, os

def waiter(*args):
    for arg in args:
        print(arg)
        time.sleep(0.20)
        # os.system('clear')
        time.sleep(0.2)
    return