var capitals = function (word) {
 // Write your code here
  const result = []
  
  for (let i = 0; i < word.length; i++) 
    if (word[i].toUpperCase() === word[i]) result.push(i)
  
  return result 
};