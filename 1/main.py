import math

def generate_data():
    X = [i * 0.1 for i in range(100)]
    Y = [math.sin(x) for x in X]
    return X, Y
X, Y = generate_data()
for x, y in zip(X, Y):
    print(f"X: {x:.2f}, Y: {y:.2f}")







