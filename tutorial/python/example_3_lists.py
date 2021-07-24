#!/usr/bin/env python

# create a list and print
nums = [1,2,3,4,5]
print(f"num list: {nums}")

# get the first number
print(f"nums[0]: {nums[0]}")

# get the 4th number
print(f"nums[3]: {nums[3]}")

'''
Notice indexing is 0-based!
First number is accessed using 0, second using 1, etc.
'''
# slice a list - slice after index 3 to the end
result = nums[3:]
print(f"nums[3:] - {result}")

# slice including index 3 to the end
result = nums[-3:]
print(f"nums[-3:] - {result}")

# slice first 3 items
result = nums[:3]
print(f"nums[:3] - {result}")

# slice a subset of items
result = nums[2:4]
print(f"nums[2:4] - {result}")

# put 2 lists together
nums1 = [1,2,3,4,5]
nums2 = [6,7,8,9,10]

all_nums = nums1 + nums2
print(f"concatenating 2 lists together: {all_nums}")

# Lets change the first number
nums[0] = 6
print(f"changing index 0: {nums}")

# list of characters
letters = ['a','b','c','d','e']

# list of unsorted numbers
values = [6,33,88,34,56,234,6,2,345]
print(f"unsorted values: {values}")

# sort the values
values = sorted(values)
print(f"sorted values: {values}")

# growing a list
# creating an empty list
items = []

# setting size to 3 and populating it
items[0:2] = [1,2,3]
print(f"items:{items}")

