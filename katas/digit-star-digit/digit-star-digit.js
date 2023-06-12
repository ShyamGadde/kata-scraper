function squareDigits(num){
  return +num.toString().split('').map(n => n * n).join('');
}