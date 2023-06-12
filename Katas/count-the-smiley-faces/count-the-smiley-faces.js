//return the total number of smiling faces in the array
function countSmileys(arr) {
  return arr.filter(str => str.match(/^[:;][-~]?[)D]$/)).length;
}