function isVow(a){
  for (var i = 0; i < a.length; i++) {
    if (a[i] === 97 || a[i] === 101 || a[i] === 105 || a[i] === 111 || a[i] === 117) {
     a[i] = String.fromCharCode(a[i])
    }
  }
  return a;
}