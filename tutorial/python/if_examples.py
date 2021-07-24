#!/usr/bin/env python
'''Python examples for Python Practice'''

def if_boolean_example(state=True):
    '''Demonstrates if statement with boolean'''
    if state:
        print("True!")
    else:
        print("False")

def if_number_example(val=0):
    '''example if using ints'''
    if val > 0:
        print(F"{val} is greater than 0")
    elif val == 0:
        print(F"{val} is zero!  Don't go negative")
    else:
        print("What are you doing!?")
    if val == 42:
        print("That's the answer to the universe!")




if __name__ == "__main__":
    if_boolean_example(True)
    if_boolean_example(False)

    if_number_example(23)
    if_number_example(0)
    if_number_example(-1)
    if_number_example(42)
