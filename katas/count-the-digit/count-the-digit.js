function nbDig(n, d) {
  const squares = Array(n + 1).fill(1).map((v, i) => i * i);
  const regex = new RegExp(`${d}`, 'g');
  return squares.reduce((count, n) => count += (`${n}`.match(regex) || []).length, 0)
}