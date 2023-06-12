function diamond(n){
  if (n % 2 === 0 || n < 1) return null;
  let result = '';
  for (let i = 1; i <= n; i += 2) {
    result += '*'.repeat(i).padStart((n + i) / 2);
    result += '\n';
  }
  for (let i = n - 2; i > 0; i -= 2) {
    result += '*'.repeat(i).padStart((n + i) / 2);
    result += '\n';
  }
  return result;
}