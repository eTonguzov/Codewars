# DESCRIPTION:
# Given an array of integers.
#
# Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.
#
# If the input is an empty array or is null, return an empty array.
#
# Example
# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].
def count_positives_sum_negatives(arr):
    new_arg = []
    count_positive = 0
    sum_negative = 0
    if arr != []:
        for i in arr:
            if i>0:
                count_positive+=1
            elif i<0: sum_negative-=-i
            else: continue
        if count_positive > 0 or sum_negative < 0 or count_positive ==0 or sum_negative == 0 :
            new_arg.append(count_positive)
            new_arg.append(sum_negative)
    else: new_arg = arr
    return new_arg
# print(count_positives_sum_negatives([]))
