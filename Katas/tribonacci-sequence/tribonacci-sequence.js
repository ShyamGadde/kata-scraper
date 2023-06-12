function tribonacci(signature,n){
  if (n < 3) return signature.slice(0, n);
  for (let i = 3; i < n; i++) {
    signature.push(signature.at(-1) + signature.at(-2) + signature.at(-3));
  }
  return signature;
}