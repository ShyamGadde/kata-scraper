String.prototype.toAlternatingCase = function () {
    return this.split('').map(ch => ch === ch.toLowerCase() ? ch.toUpperCase() : ch.toLowerCase()).join('')
}