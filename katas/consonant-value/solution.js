function solve(s) {
    const consonants = s.match(/[^aeiou]+/g);
    let highest = 0;
    for (const match of consonants) {
        let value = [...match].map(char => char.charCodeAt(0) - 'a'.charCodeAt(0) + 1).reduce((a, b) => a + b, 0);
        highest = Math.max(highest, value);
    }
    return highest;
}