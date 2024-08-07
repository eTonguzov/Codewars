// Description:
// There was a test in your class and you passed it. Congratulations!

// But you're an ambitious person. You want to know if you're better than the average student in your class.

// You receive an array with your peers' test scores. Now calculate the average and compare your score!

// Return true if you're better, else false!

// Note:
// Your points are not included in the array of your class's points. Do not forget them when calculating the average score!

function betterThanAverage(classPoints, yourPoints) {
    let count_person = 0
    let class_p = 0
    classPoints.forEach(element => {
        class_p+=element;
        count_person+=1;
    });
    if ((class_p/count_person)>yourPoints){
        return false
    }
    else return true
  }
  