# DESCRIPTION:
# Trolls are attacking your comment section!
#
# A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.
#
# Your task is to write a function that takes a string and return a new string with all vowels removed.
#
# For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
#
# Note: for this kata y isn't considered a vowel.or 'e' or 'u' or 'i' or 'o' or 'y'
def disemvowel(string_):
#     arr = []
#     for i in list(string_):
#         if i == ('a' or 'e'):
#             continue
#         else:arr.append(i)
#     string_ = str(arr)
#     return string_
# print(disemvowel("This website is for losers LOL!"))

# import codewars_test as test
# from solution import disemvowel
#
# @test.describe("Fixed Tests")
# def basic_tests():
#     @test.it("First fixed test")
#     def fixed_test_1():
#         test.assert_equals(disemvowel("This website is for losers LOL!"), "Ths wbst s fr lsrs LL!")