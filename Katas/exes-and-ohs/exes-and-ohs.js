function XO(str) {
  let countOs = 0, countXs = 0;
  for (let char of str) {
    if (char.toLowerCase() === 'x') countXs++;
    else if (char.toLowerCase() === 'o') countOs++;
  }
  return countOs === countXs;
}