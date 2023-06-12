function printerError(s) {
  let errors = 0;
  for (ch of s) if (ch > 'm') errors++;
  return `${errors}/${s.length}`;
}