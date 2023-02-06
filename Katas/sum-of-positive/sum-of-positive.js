function positiveSum(arr) {
   let sum = 0; 
   
   arr.forEach((num)=>num>0?sum+=num:0); 
   
   return sum; 
   
}