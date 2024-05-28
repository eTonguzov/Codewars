// Write a function that removes the spaces from the string, then return the resultant string.

// Examples:

// Input -> Output
// "8 j 8   mBliB8g  imjB8B8  jl  B" -> "8j8mBliB8gimjB8B8jlB"
// "8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd" -> "88Bifk8hB8BB8BBBB888chl8BhBfd"
// "8aaaaa dddd r     " -> "8aaaaaddddr"

function noSpace(x){
    let newArr = x.split('');
    let massive = [];
    newArr.forEach(element => {
        if(element!=" "){
            massive.push(element)
        }
    });
    return massive.join('')
}

console.log(noSpace("fgf dgf    dgfd   dgdg gg gg"))
// let str = "8 jkj 99   lkl";

// let newArr = str.split('');

// console.log(newArr);
