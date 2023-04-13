function dirReduc(arr){
  let i = 0;
  while (i < arr.length) {
    if (arr[i] === 'NORTH' && arr[i + 1] === 'SOUTH' || arr[i] === 'SOUTH' && arr[i + 1] === 'NORTH') {
      arr.splice(i, 2);
      i = 0;
    } else if (arr[i] === 'EAST' && arr[i + 1] === 'WEST' || arr[i] === 'WEST' && arr[i + 1] === 'EAST') {
      arr.splice(i, 2);
      i = 0;
    } else {
      i++;
    }
  }
  return arr;
}