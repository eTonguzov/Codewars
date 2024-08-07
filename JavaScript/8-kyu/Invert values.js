// Description:
// Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.

// [1, 2, 3, 4, 5] --> [-1, -2, -3, -4, -5]
// [1, -2, 3, -4, 5] --> [-1, 2, -3, 4, -5]
// [] --> []
// You can assume that all values are integers. Do not mutate the input array.

function invert(lst) {
    let newArray = [];
    lst.forEach(element => {
        newArray.unshift(-element)
    });
    return newArray;
}
 console.log(invert([-1, -2, -3, -4, -5, 45]))


//  def invert(lst):
//     arr = []
//     for i in lst:
//         arr.append(i*(-1))
//     return arr
// print(invert([]))