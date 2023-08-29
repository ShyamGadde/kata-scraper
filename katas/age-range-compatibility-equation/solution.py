def dating_range(age):
    if age < 15:
        return f"{int(age - .1 * age)}-{int(age + .1 * age)}"
    return f"{age // 2 + 7}-{(age - 7) * 2}"