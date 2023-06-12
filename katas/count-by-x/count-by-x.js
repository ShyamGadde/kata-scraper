function countBy(x, n) {
  const arr = new Array(n).fill(0);
  return arr.map((n, i) => (i + 1) * x);
}