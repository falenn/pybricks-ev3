#!/usr/bin/env python
'''This is my big example progam
and this comment can go on and on and on
and on
'''
# Global variables 

count = 5     # int
time = 1.5    # float
name = "Curtis" # string
is_on = False # boolean
is_onn = 1    # int - but also is True


def area(width=1, height=1):
    '''Computes the area given a width and height'''
    print(F"begin area({width},{height})")
    return width * height
    


if __name__ == "__main__":
    print("My name is %s" % (name))

    print(F"5 + 5 = {5+5}")

    val = (50 - 5*6) / 4	
    print(val)

    val = 5 ** 2
    print(val)

    val = 17 % 3  # modulo
    print(val)

    val = 16 // 3
    print(val)

    ''' This is calculating the area of a rectangle width 5 * height 7'''
    val = 7 * 5
    print(val)

    width = 7
    height = 5
    #area = width * height

    val = area(width, height)
    print(val)

    print(area(4,4))



