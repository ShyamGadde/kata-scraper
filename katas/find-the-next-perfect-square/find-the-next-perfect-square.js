function findNextSquare(sq) {
  const sqrt = Math.sqrt(sq);
  if (Number.isInteger(sqrt)) {
    return Math.pow(sqrt + 1, 2);
  } else {
    return -1;
  }
}