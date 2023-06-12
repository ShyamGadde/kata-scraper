function solution(nums){
  if (!nums) return [];
  return nums.sort((a,b) => a - b)
}