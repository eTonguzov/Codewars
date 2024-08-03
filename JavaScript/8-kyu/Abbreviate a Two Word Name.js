// Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

// The output should be two capital letters with a dot separating them.

// It should look like this:

// Sam Harris => S.H

// patrick feeney => P.F

function abbrevName(name){

    const massive = name.split(" ");
    const resOne = massive[0].split('');
    const nameA = (resOne[0]).toUpperCase();
    const resTwo = massive[1].split('');
    const nameB = (resTwo[0]).toUpperCase();
    return nameA + "." + nameB;

}
console.log(abbrevName('egor tonguzov'))