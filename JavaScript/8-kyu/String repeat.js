/*DESCRIPTION:
Write a function that accepts an integer n and a string s as parameters, and returns a string of s repeated exactly n times.

Examples (input -> output)
6, "I"     -> "IIIIII"
5, "Hello" -> "HelloHelloHelloHelloHello"*/

function repeatStr (n, s) {
    let mass = []
    for(let x = 0; x < n; x++){
        mass.push(s)
    }
    let result = mass.join('');
    return result;
  }

  console.log(repeatStr(3, 'Egor'))