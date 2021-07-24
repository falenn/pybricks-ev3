#!/usr/bin/env python
'''Examples demonstrating while loop'''
from time import sleep, time


def while_number(count=5):
    '''while loop using a count'''
    while count > 0:
        print(F"me again: {count}")
        count = count -1
    print("Done!")

def while_boolean():
    '''demonstrates loop forever'''
    start = time()  # get the time since the start of the Epoch
    while(True):
        now = time() # get the time since the start of the Epoch
        print(F"Seconds have elapsed: {round(now - start,0)}") # diff
        sleep(1)
    

if __name__ == "__main__":
    while_number()
    while_number(20)
    while_boolean()
