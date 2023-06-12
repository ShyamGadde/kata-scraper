function nbYear(p0, percent, aug, p) {
  let years = 0;
  percent /= 100;
  while (p0 < p) {
    p0 = Math.floor(p0 + p0 * percent + aug);
    years++;
  }
  return years;
}