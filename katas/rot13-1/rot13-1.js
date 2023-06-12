function rot13(message){
  let cipherText = '';
  for (let char of message) {
    let charCode = char.charCodeAt(0);
    if (65 <= charCode && charCode <= 90 ) {
      let rot13Char = (charCode - 65 + 13) % 26;
      cipherText += String.fromCharCode(65 + rot13Char);
    }
    else if (97 <= charCode && charCode <= 122) {
      let rot13Char = (charCode - 97 + 13) % 26;
      cipherText += String.fromCharCode(97 + rot13Char);
    }
    else cipherText += char;
  }
  return cipherText;
}