// write the function isAnagram
var isAnagram = function(test, original) {
  if(test.length !== original.length) return false;
  test = test.toLowerCase().split("").sort();
  original = original.toLowerCase().split("").sort();
  for(let i=0; i<test.length; i++){
    if(test[i] !== original[i]) return false;
  }
  return true;
};