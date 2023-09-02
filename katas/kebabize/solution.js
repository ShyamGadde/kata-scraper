function kebabize(str) {
  return str
    .replace(/([a-zA-Z0-9])([A-Z])/g, '$1-$2')
    .replace(/[^a-z-]/gi, '')
    .replace(/^-/, '')
    .toLowerCase();
}