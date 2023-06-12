function feast(beast, dish) {
  return beast[0] === dish[0] && beast.at(-1) === dish.at(-1)
}