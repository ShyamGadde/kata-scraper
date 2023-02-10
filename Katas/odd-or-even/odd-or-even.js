function oddOrEven(array) {
   return array.reduce((acc, curVal) => acc + curVal, 0) % 2 ? "odd" : "even";
}