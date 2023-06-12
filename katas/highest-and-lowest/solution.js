function highAndLow(numbers){
  const sortedNumbers = numbers.split(' ').sort((a, b) => a - b);
  return `${sortedNumbers.at(-1)} ${sortedNumbers[0]}`;
}