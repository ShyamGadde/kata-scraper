function solve(s){
  let uppercase = 0;
  let lowercase = 0;
  let numbers = 0;
  let special = 0;

  for(let i = 0; i < s.length; i++){
    if(s[i] >= 'A' && s[i] <= 'Z'){
      uppercase++;
    } else if(s[i] >= 'a' && s[i] <= 'z'){
      lowercase++;
    } else if(s[i] >= '0' && s[i] <= '9'){
      numbers++;
    } else {
      special++;
    }
  }

  return [uppercase, lowercase, numbers, special];
}