function persistence(num) {
  let persistence = 0;
  while (num / 10 >= 1) {
    persistence++;
    num = Array.from(String(num), Number).reduce((prod, n) => prod * n);
  }
  return persistence;
}