function pipeFix(numbers){
  const result = [];
  
  for(let i = numbers[0]; i <= numbers.at(-1); i++) {
    result.push(i)
  }
  
  return result;
}