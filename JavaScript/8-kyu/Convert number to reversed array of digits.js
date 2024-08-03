// Convert number to reversed array of digits
// Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

// Example(Input => Output):
// 35231 => [1,3,2,5,3]
// 0 => [0]

function digitize(n) {
  let arr = [];
  if (n ==0){
    arr.push(0);
    return arr;
  }
  while(n>0){
    let ost = n % 10;
    arr.push(ost);
    n = Math.floor(n/10)
  }
  return arr
}

console.log(digitize(3652));
