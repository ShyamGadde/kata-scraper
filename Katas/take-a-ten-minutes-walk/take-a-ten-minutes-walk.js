function isValidWalk(walk) {
  if (walk.length !== 10) return false;
  let vd = 0, hd = 0;
  walk.forEach(char => {
    switch (char) {
        case 'n':
          vd++;
          break;
        case 's':
          vd--;
          break;
        case 'e':
          hd++;
          break;
        case 'w':
          hd--;
          break;
    }
  })
  return vd === 0 && hd === 0;
}