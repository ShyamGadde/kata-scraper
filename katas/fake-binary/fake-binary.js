function fakeBin(x){
  return x.toString().split('').map(n=>n<5?0:1).join('');
}