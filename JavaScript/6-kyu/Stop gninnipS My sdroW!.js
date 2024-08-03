// Write a function that takes in a string of one or more words, 
//and returns the same string, but with all words that have five or more letters reversed 
//(Just like the name of this Kata). Strings passed in will consist of only letters and spaces.
// Spaces will be included only when more than one word is present.

// Examples:

// "Hey fellow warriors"  --> "Hey wollef sroirraw" 
// "This is a test        --> "This is a test" 
// "This is another test" --> "This is rehtona test"
function spinWords(string){
    let resuleTemp = '';
    const massive = string.split(' '); // ["WOR" "WORLD"]
    //if(massive[0].length)
    for(let i = 0; i <massive.length; i++){
        //let resuleTemp = ''
        if((massive[i]).length>=5){
            let massivChar = massive[i].split('');//"W" 'O' 'R' 'L' 'D'
            resuleTemp = (massivChar.reverse()).join(''); //"D" 'L' 'R' "O" 'W'
            
        
        } else {
            resuleTemp = massive[i]
        }
        massive.splice(i,1,resuleTemp)

     }
    return massive.join(' ')
  }

  console.log(spinWords("Hey fellow warriors"))