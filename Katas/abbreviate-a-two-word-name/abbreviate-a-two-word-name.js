function abbrevName(name) {
  return name.split(' ').map(name => name[0].toUpperCase()).join('.');
}