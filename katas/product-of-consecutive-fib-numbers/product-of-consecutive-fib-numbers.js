function productFib(prod){
  let currVal = 0;
  const fibSeq = [0, 1];
  
  while (currVal < prod) {
    fibSeq.push(fibSeq.at(-1) + fibSeq.at(-2));
    currVal = fibSeq.at(-1) * fibSeq.at(-2);
  }
  return [fibSeq.at(-2), fibSeq.at(-1), currVal === prod];
}