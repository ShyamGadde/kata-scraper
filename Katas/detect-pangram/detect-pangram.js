function isPangram(string){
  const letters = new Set(string.trim().toLowerCase());
  return letters.size >= 26;
}