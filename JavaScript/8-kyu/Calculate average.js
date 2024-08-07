// Description:
// Write a function which calculates the average of the numbers in a given list.

// Note: Empty arrays should return 0.

function findAverage(array) {
    let count = 0;
    if(array.length!=0){
        array.forEach(element => {
            count+=element;
        });
        return count/array.length;
    }
    else return 0
  }

  console.log(findAverage([1,2,3,4]));