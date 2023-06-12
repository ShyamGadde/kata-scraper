function isIsogram(str){
  const sortedArr = Array.from(str.toLowerCase()).sort()
  console.log(sortedArr);
  for (let i = 0; i < sortedArr.length - 1; i++) {
    if (sortedArr[i] === sortedArr[i + 1]) return false;
  }
  return true;
}