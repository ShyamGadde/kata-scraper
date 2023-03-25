function order(words){
  const wordsArr = words.split(' ');
  const order = wordsArr.map(word => Number(word.split('').filter(n => parseInt(n))[0]));
  return wordsArr.sort((a, b) => order[wordsArr.indexOf(a)] - order[wordsArr.indexOf(b)]).join(' ');
}