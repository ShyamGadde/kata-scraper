function alphabetPosition(text) {
  return text.toUpperCase().split('').filter(char => char.charCodeAt() > 64 && char.charCodeAt() < 91).map(char => char.charCodeAt() - 64).join(' ')
}