/*Complete the solution so that it reverses the string passed into it.

'world'  =>  'dlrow'
'word'   =>  'drow' */

function solution(str){
  let splitString = str.split('');// ["h", "e", "l", "l", "o"]
  let reverseArray = splitString.reverse();//// ["o", "l", "l", "e", "h"]
  let joinArray = reverseArray.join('');//"olleh"
  return joinArray;
}
console.log(solution('Egor'))

