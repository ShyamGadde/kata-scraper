function calculateYears(principal, interestRate, taxRate, desired) {
  let years = 0
  while (principal < desired) {
    let interest = principal * interestRate
    interest -= interest * taxRate
    principal += interest
    years++
  }
  
  return years
}