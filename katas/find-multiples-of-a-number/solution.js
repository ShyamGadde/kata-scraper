function findMultiples(integer, limit) {
  return Array(Math.floor(limit / integer)).fill(0).map((_, i) => integer * (i + 1))
}