function sumArray(array) {
  if (array === null || array === undefined) return 0;
  array.sort((a, b) => a - b);
  array.pop();
  array.shift();
  return array.reduce((sum, n) => sum + n, 0);
}