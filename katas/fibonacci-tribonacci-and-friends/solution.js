function Xbonacci(signature, n) {
  const x = signature.length;
  if (n <= x) {
    return signature.slice(0, n);
  }

  const result = [...signature];

  for (let i = x; i < n; i++) {
    let nextElement = 0;
    for (let j = 1; j <= x; j++) {
      nextElement += result[i - j];
    }
    result.push(nextElement);
  }

  return result;
}