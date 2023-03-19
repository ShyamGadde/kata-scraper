function towerBuilder(nFloors) {
  const result = [];
  for (let i = 0; i < nFloors; i++) {
    let spaces = ' '.repeat(nFloors - i - 1)
    result.push(`${spaces}${'*'.repeat(i * 2 + 1)}${spaces}`);
  }
  return result;
}