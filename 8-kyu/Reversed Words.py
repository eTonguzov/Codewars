# DESCRIPTION:
# Complete the solution so that it reverses all of the words within the string passed in.
#
# Example(Input --> Output):
#
# "The greatest victory is that which requires no battle" --> "battle no requires which that is victory greatest The"
def reverse_words(s):
    a = " ".join(reversed(s.split()))

    return a

# print(reverse_words("hello world!"))

