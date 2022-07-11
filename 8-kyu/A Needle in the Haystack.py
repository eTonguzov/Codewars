# DESCRIPTION:
# Can you find the needle in the haystack?
#
# Write a function findNeedle() that takes an array full of junk but containing one "needle"
#
# After your function finds the needle it should return a message (as a string) that says:
#
# "found the needle at position " plus the index it found the needle, so:
#
# Example(Input --> Output)
#
# ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"] --> "found the needle at position 5"
# Note: In COBOL, it should return "found the needle at position 6"
def find_needle(haystack):
    count = 1
    for i in haystack:
        if i != 'needle':
            count+=1
        else: break
    return 'found the needle at position ' + str(count)
# print(find_needle([ 203, 139, 74, 246, 47, 246, 228, 201, 'needle', 260, 50, 30]))

