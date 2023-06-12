function getCount(str) {
  let count = 0

  for (let char of str) {
    switch(char) {
      case 'a':
      case 'e':
      case 'i':
      case 'o':
      case 'u':
        count++;
    }
  }

  return count;
}