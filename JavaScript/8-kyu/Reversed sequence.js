// Build a function that returns an array of integers from n to 1 where n>0.

// Example : n=5 --> [5,4,3,2,1]

const reverseSeq = n => {
    let a = [];
    for(let element = n; element>0; element--){
        a.push(element);
    }
    return a;
  };

  console.log(reverseSeq(5));