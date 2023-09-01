function incrementer(nums) { 
  return nums.map((n, i) => (n + i + 1) % 10);
}