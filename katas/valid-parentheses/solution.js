function validParentheses(parens) {
  const stack = [];
  for (const paren of parens) {
    if (paren === "(") stack.push(paren);
    else if (stack.at(-1) === "(") stack.pop();
    else return false;
  }
  return stack.length === 0;
}