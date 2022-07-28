# DESCRIPTION:
# There was a test in your class and you passed it. Congratulations!
# But you're an ambitious person. You want to know if you're better than the average student in your class.
#
# You receive an array with your peers' test scores. Now calculate the average and compare your score!
#
# Return True if you're better, else False!
#
# Note:
# Your points are not included in the array of your class's points. For calculating the average point you may add your point to
# the given array!
def better_than_average(class_points, your_points):
    count_person = 0
    class_p = 0
    for i in class_points:
        class_p+=i
        count_person+=1
    if ((class_p/count_person)>your_points):
        return False
    else: return True
# print(better_than_average([12, 23, 34, 45, 56, 67, 78, 89, 90], 69))
