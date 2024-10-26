// Description:
// You will be given an array a and a value x. All you need to do is check whether the provided array contains the value.

// Array can contain numbers or strings. X can be either.

// Return true if the array contains the value, false if not.
function check(a, x) {
    for(let element of a){
        if(element==x){
            return true;
        }
    }
    return false;
  }
  console.log(check([0,0,'a'], 3));