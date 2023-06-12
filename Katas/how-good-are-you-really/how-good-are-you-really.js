function betterThanAverage(classPoints, yourPoints) {
  const avg = (classPoints.reduce((sum, n) => sum + n) + yourPoints) / (classPoints.length + 1)
  return yourPoints > avg;
}