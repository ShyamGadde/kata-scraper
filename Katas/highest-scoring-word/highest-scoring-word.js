function high(x){
  const words = x.split(' ');
  const scores = words.map(word => Array.from(word)
                           .reduce((score, char) => score + char.charCodeAt() - 96, 0));
  return words[scores.indexOf(Math.max(...scores))];
}