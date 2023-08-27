def explode(s):
  return "".join(digit * int(digit) for digit in s)