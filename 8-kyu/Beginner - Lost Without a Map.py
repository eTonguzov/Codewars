# DESCRIPTION:
# Given an array of integers, return a new array with each value doubled.
#
# For example:
#
# [1, 2, 3] --> [2, 4, 6]
def maps(a):
    new_list = []
    for i in a:
        i*=2
        new_list.append(i)
    return new_list
# print(maps([1, 2, 2]))