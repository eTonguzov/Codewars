// Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

// Note: input will never be an empty string

function fakeBin(x){
    let a = (x.toString()).split('');
    let result = '';
        a.forEach(element => {
            if(parseInt(element)<5){
                result+=0;
            } else result+=1;
        });
        return result;
}
console.log(fakeBin(14324234666));
