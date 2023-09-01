function maxTriSum(numbers){
    let uniqueNumbers = [...new Set(numbers)];
    let firstLargest = -Infinity;
    let secondLargest = -Infinity;
    let thirdLargest = -Infinity;
    for (let i = 0; i < uniqueNumbers.length; i++) {
        if (uniqueNumbers[i] > firstLargest) {
            thirdLargest = secondLargest;
            secondLargest = firstLargest;
            firstLargest = uniqueNumbers[i];
        } else if (uniqueNumbers[i] > secondLargest) {
            thirdLargest = secondLargest;
            secondLargest = uniqueNumbers[i];
        } else if (uniqueNumbers[i] > thirdLargest) {
            thirdLargest = uniqueNumbers[i];
        }
    }
    return firstLargest + secondLargest + thirdLargest;
}