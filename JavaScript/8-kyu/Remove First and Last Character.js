/*It's pretty straightforward.
Your goal is to create a function that removes the first and last characters of a string.
You're given one parameter, the original string.
You don't have to worry about strings with less than two characters.*/

function removeChar(str){
    let array = str.split('')
    delete array[0]
    delete array.pop() //удаляет последний элемент маасива
    let result = array.join('')
    return result;
   };

   console.log(removeChar("Egor"))