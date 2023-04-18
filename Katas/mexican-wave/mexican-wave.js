function wave(str){
  const result = []
  for (let i = 0, words = str.length; i < words; i++) {
    if (str[i] !== ' ') {
      let waveStr = str.slice(0, i) + str[i].toUpperCase() + str.slice(i + 1)
      result.push(waveStr)
    }
  }
  return result
}