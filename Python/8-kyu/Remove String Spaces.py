# DESCRIPTION:
# Simple, remove the spaces from the string, then return the resultant string.
def no_space(x):
    return x.replace(' ', '')#str.replace(old, new[, count]) Исходная строка остается неизменной.
                             # Новая строка – это копия исходной строки, в которой все вхождения старой подстроки заменены на новую

#print(no_space("q  w  e  r  t     y"))