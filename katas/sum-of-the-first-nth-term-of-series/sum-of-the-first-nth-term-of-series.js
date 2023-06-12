function SeriesSum(n) {
  let denominator = 1;
  let result = 0;
  for (let i = 0; i < n; i++) {
    result += 1 / denominator;
    denominator += 3;
  }
  return result.toFixed(2);
}