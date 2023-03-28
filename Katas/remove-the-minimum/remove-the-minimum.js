function removeSmallest(numbers) {
  let lowestRating = Math.min(...numbers);
  let ratingsCopy = Array.from(numbers);
  ratingsCopy.splice(numbers.indexOf(lowestRating), 1);
  return ratingsCopy;
}