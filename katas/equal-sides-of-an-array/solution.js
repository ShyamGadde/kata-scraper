function findEvenIndex(arr) {
  let left = 0;
  let right = arr.reduce((sum, n) => sum + n);
  
  for (let i = 0; i < arr.length; i++) {
    right -= arr[i];
    if (left === right) return i;
    left += arr[i];
  }
  return -1;
}