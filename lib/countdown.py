# your code goes here!
import time

def countdown(start):
    """Counts down from start to 1, then prints Happy New Year!"""
    while start > 0:
        print(f"{start} SECOND(S)!")
        start -= 1
    print("HAPPY NEW YEAR!")

def countdown_with_sleep(start):
    """Counts down from start to 1 with 1-second delays, then prints Happy New Year!"""
    while start > 0:
        print(f"{start} SECOND(S)!")
        start -= 1
        time.sleep(1)
    print("HAPPY NEW YEAR!")