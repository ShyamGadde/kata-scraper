function countPositivesSumNegatives(input) {
    return (input && input.length) ? [
      input.filter(n => n > 0).length,
      input.reduce((sum, n) => n < 0 ? sum + n : sum, 0)
    ] : [];
}