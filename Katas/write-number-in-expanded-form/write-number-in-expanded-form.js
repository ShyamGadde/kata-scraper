function expandedForm(num) {
  const digits = Array.from(String(num), Number).reverse()
  return digits.map((n, i) => n * 10 ** i).filter(n => n !== 0).reverse().join(' + ');
}