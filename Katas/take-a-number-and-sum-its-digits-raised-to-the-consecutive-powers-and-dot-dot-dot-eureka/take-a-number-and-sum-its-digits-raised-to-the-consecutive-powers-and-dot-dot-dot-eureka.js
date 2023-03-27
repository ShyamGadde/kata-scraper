function sumDigPow(a, b) {
  const result = [];
  for (let i = a; i <= b; i++) {
    let testProp = Array.from(String(i), Number).reduce((acc, n, index) => acc + n ** (index + 1) , 0);
    if (testProp === i) result.push(i);
  }
  return result;
}