function isPythagoreanTriple(integers) {
  integers.sort((a, b) => a - b);
  [ a, b, c ] = integers;
  return a ** 2 + b ** 2 === c ** 2;
}