function openOrSenior(data){
  return data.map((person) => (person[0] >= 55 && person[1] > 7 ? "Senior" : "Open"));
}