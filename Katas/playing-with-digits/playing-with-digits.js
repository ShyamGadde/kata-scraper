function digPow(n, p){
  const powerSum = Array.from(String(n), Number).reduce((sum, n) => sum + n ** p++, 0);
  const k = powerSum / n;
  return (Number.isInteger(k)) ? k : -1;
}