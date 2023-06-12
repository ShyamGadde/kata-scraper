function DNAStrand(dna){
  //your code here
  output = "";
  for (let i = 0; i < dna.length; i++) {
    switch (dna[i]) {
        case "A":
          output += "T";
          break;  
        case "T":
          output += "A";
          break;
        case "C":
          output += "G";
          break;
        case "G":
          output += "C";
          break;
    }
  }
  return output;
}