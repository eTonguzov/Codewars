# DESCRIPTION:
# Complete the solution so that it reverses the string passed into it.
#
# 'world'  =>  'dlrow'
# 'word'   =>  'drow'

def solution(string):
    x = list(string)
    x.reverse()
    StrX = "".join(x)#Здесь "" - между элементами списка вставляется строка "", пустая строка. В нашем случае вставляется пустая строка
    return StrX
#################
# # Other solution
# def solution(str):
#    return str[::-1]#str[start:stop:step] синтаксис срезов.
# print(solution("World"))
