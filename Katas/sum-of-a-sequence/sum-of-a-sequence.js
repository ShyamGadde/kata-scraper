const sequenceSum = (begin, end, step) => {
    let sum = 0;
    for(; begin <= end; begin += step) {
        sum += begin;
    }

    return sum;
};