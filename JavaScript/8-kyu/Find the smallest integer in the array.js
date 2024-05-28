// Given an array of integers your solution should find the smallest integer.

// For example:

// Given [34, 15, 88, 2] your solution will return 2
// Given [34, -345, -1, 100] your solution will return -345
// You can assume, for the purpose of this kata, that the supplied array will not be empty.

function findSmallestInt(arr) {
    let small_elem = arr[0]//пусть первый эленет самый маленький
    arr.forEach(element => {
        if(element<small_elem){
            small_elem = element;
        }    
    });
    return small_elem;
  }

  console.log(findSmallestInt([1,5,6,6,3,5,3,2,52525,252,25,25,25,-5,-10000]))
