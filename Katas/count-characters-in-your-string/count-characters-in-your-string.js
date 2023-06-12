function count(string) {
  const result = {};
  for (char of string) {
    if (char in result) result[char]++;
    else result[char] = 1;
  }
  return result;
}