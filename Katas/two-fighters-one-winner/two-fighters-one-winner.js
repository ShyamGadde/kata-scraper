function declareWinner(fighter1, fighter2, firstAttacker) {
  const fighters = [fighter1, fighter2]
  let attacker = fighters[0].name === firstAttacker ? 0 : 1
  
  while (fighters[0].health > 0 && fighters[1].health > 0) {
    fighters[attacker ^ 1].health -= fighters[attacker].damagePerAttack
    attacker ^= 1
  }
  
  return fighters[0].health > 0 ? fighters[0].name : fighters[1].name
}