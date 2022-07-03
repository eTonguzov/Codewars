# DESCRIPTION:
# Return the number (count) of vowels in the given string.
#
# We will consider a, e, i, o, u as vowels for this Kata (but not y).
#
# The input string will only consist of lower case letters and/or spaces.
def get_count(sentence):
    x = list(sentence)
    count = 0
    def get_count2():
        for i in x:
            if i == ('a', 'e', 'i', 'o', 'u'):
                nonlocal count
                count+= 1
            else: continue
    return count
print(get_count())


print(get_count(di))

