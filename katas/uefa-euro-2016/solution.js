function uefaEuro2016(teams, scores){
  let result = `At match ${teams[0]} - ${teams[1]}, `
  if (scores[0] > scores[1]) {
    result += `${teams[0]} won!`
  }
  else if (scores[0] < scores[1]) {
    result += `${teams[1]} won!`
  }
  else {
    result += `teams played draw.`
  }
  return result
}