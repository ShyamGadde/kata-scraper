function gimme (triplet) {
  const middleNumber = Array.from(triplet).sort((a, b) => a - b)[1];
  return triplet.indexOf(middleNumber);
}