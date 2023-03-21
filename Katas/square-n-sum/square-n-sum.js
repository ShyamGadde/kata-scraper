function squareSum(numbers){
  return numbers.reduce((prodSum, n) => prodSum + n ** 2, 0);
}