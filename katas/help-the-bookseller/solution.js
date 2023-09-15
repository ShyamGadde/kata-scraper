function stockList(listOfArt, listOfCat){
  if(!listOfArt.length || !listOfCat.length) {
    return "";
  }
  
  const count = new Map();
  listOfCat.forEach(cat => count.set(cat, 0));
  
  listOfArt.forEach(stocklist => {
    [code, quantity] = stocklist.split(" ");
    if (count.has(code[0])) count.set(code[0], count.get(code[0]) + parseInt(quantity));
  })
  
  const res = [];
  count.forEach((value, key) => res.push(`(${key} : ${value})`));

  return res.join(" - ");
}