function switcheroo(x){
  return x.split('').map(char => {
    if (char === 'a') return 'b';
    if (char === 'b') return 'a';
    return char;
  }).join('');
}