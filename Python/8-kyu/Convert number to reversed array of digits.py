# DESCRIPTION:
# Convert number to reversed array of digits
# Given a random non-negative number, you have to return the digits of this number within an array in reverse order.
#
# Example(Input => Output):
# 348597 => [7,9,5,8,4,3]
# 0 => [0]
def digitize(n):
    arr = []
    if n == 0:
        arr.append(0)
        return arr
    while n > 0:
        ost = n % 10
        arr.append(ost)
        n//=10
    return arr
#print(digitize(0))
#Other solutions
# def digitize(n):
#     result = []
#     while n >= 1:
#         result.append(n%10)
#         n //= 10
#     return result

25//=10