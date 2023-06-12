function duplicateCount(text){
  text = text.toLowerCase();
  const chars = new Set();
  for (let i = 0; i < text.length; i++) {
    if (text.includes(text[i], i + 1)) chars.add(text[i]);
  }
  return chars.size;
}