function strCount(str, letter) {  
  return str.split('').reduce((count, char) => count += (char === letter) ? 1 : 0, 0)
}