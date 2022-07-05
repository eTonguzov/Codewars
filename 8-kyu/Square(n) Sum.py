# DESCRIPTION:
# Complete the square sum function so that it squares each number passed into it and then sums the results together.
#
# For example, for [1, 2, 2] it should return 9 because 1^2 + 2^2 + 2^2 = 9.
def square_sum(numbers):
    count = 0
    new_list = []
    for i in numbers:
        i**=2
        new_list.append(i)
        count+=i
    return count
#print(square_sum([1, 2, 3]))