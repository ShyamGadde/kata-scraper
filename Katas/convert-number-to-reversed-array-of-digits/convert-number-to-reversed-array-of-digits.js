function digitize(n) {
  return n.toString().split('').reverse().map(n => parseInt(n));
}