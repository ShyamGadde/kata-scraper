function createPhoneNumber(numbers){
  numbers = numbers.join('');
  return `(${numbers.slice(0, 3)}) ${numbers.slice(3, 6)}-${numbers.slice(6)}`
}