#!/usr/bin/env python

'''
Comment about this function
This can be a long, multi-line comment
'''

'''
calculate_area
width as number
height as number
returns area or a rectangle (wdith * height) as number
'''
def calculate_area(width=0, height=0):	
    return width * height

# main function
if __name__ == "__main__":
    result = calculate_area(5,4)
    print(f"area:{result}")