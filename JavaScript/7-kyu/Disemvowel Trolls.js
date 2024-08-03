// Trolls are attacking your comment section!

// A common way to deal with this situation is to remove all of the vowels from the trolls' comments, 
//neutralizing the threat.

// Your task is to write a function that takes a string and return a new string with all vowels removed.

// For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

// Note: for this kata y isn't considered a vowel.
function disemvowel(str) {
    let list_znk = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'];
    list_znk.forEach(element => {
        str=str.replaceAll(element, '')
    });
    return str;

    // let mass = str.split(' ');
    // for(let i = 0; i < mass.lenght; i ++){
    //     let new_mass = mass[i].split(''); //'T' 'h' 'i' ...
  }
  console.log(disemvowel("This website is for losers LOL!"))