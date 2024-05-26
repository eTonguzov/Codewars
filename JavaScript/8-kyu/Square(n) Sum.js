// Complete the square sum function so that it squares each number passed into it and then sums the results together.

// For example, for [1, 2, 2] it should return 9 because 

function squareSum(numbers){
    let count = 0;
    for(let x=0; x<numbers.length; x++){
        count= count + Math.pow(numbers[x],2);
    }
    return count;
}
let array = [1, 2, 5]
let a = squareSum(array)
console.log(a)