def predict_age(*ages):
    return sum(map(lambda x: x*x, ages))**.5//2