# DESCRIPTION:
# Write a function which calculates the average of the numbers in a given list.
#
# Note: Empty arrays should return 0.
def find_average(numbers):
    count = 0
    sum = 0
    for i in numbers:
        sum+=i
        count+=1
    return sum/count

# print(find_average([1,4,5,6,6,6]))
# Other soution
# return sum(array) / len(array) if array else 0