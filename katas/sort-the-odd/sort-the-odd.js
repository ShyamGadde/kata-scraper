function sortArray(array) {
  const odds = array.filter(n => n % 2);
  odds.sort((a, b) => a - b)
  return array.map(n => n % 2 ? odds.shift() : n);
}