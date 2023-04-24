# your code goes here!
from time import sleep

def countdown(x):
    while x != 0:
        print(f'{x} SECOND(S)!')
        x-=1
    else:
        print("HAPPY NEW YEAR!")


def countdown_with_sleep(x):
    while x != 0:
        print(f'{x} SECOND(S)!')
        x-=1
        sleep(1)
    else:
        print("HAPPY NEW YEAR!")