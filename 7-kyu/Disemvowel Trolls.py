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
import re
def disemvowel(string_):
    list_znk = ['e', 'u', 'i' , 'o', '\n', 'O', 'E', 'U', 'I', ]
    for i in list_znk:
        string_=string_.replace(i, '')

    return string_
print(disemvowel("N ffns bt,Yr wrtng s amng th wrst 'v vr rad"))

