function generateShape(integer){
  return Array.from({length: integer}, () => '+'.repeat(integer)).join('\n')
}