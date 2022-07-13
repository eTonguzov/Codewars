# DESCRIPTION:
# Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.
#
# Note: input will never be an empty string
def fake_bin(x):
    # zero = str(x)
    num = list(x)
    new = []
    res = ''
    for i in num:
        # int(i)
        if int(i)>=5: new.append('1')
        else: new.append('0')
    for x in new:
        res +=x

    return res
print(fake_bin('2312'))