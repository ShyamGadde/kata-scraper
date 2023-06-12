function adjacentElementsProduct(array) {
  let res = -Infinity;
  for (let i = 1, n = array.length; i < n; i++) {
    res = Math.max(res, array[i - 1] * array[i]);
  }
  return res;
}