# DESCRIPTION:
# Summation
# Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.
#
# For example:
#
# summation(2) -> 3
# 1 + 2
#
# summation(8) -> 36
# 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8

def summation(num):
    count = 0
    start = 0
    while(start<num):
        count+=count+1
        start+=1


    return count

print(summation(8))
        
