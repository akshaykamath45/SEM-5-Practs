import numpy as np


class Perceptron:
    def __init__(self, input_size):
        self.weights = np.random.rand(input_size)
        self.bias = np.random.rand(1)

    def activation(self, x):
        return 1 if x > 0 else 0

    def predict(self, X):
        summation = np.dot(X, self.weights) + self.bias
        return self.activation(summation)

    def train(self, X, y, learning_rate, epochs):
        for _ in range(epochs):
            for input, label in zip(X, y):
                pred = self.predict(input)
                error = label - pred
                self.weights += learning_rate * error * input
                self.bias += learning_rate * error


# This is a 5x4 matrix which resembles an L
# 10000
# 10000
# 10000
# 11111

# This is a 5x4 matrix which represents an M
# 10001
# 11011
# 10101
# 10001

# put L and M in a single array
input_data = np.array(
    [
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1],
    ]
)

labels = np.array([0, 1])  # 0 for L, 1 for M

perceptron = Perceptron(input_size=20)

perceptron.train(input_data, labels, learning_rate=0.1, epochs=100)

for x in input_data:
    pred = perceptron.predict(x)
    print(f"Input = {x}, Prediction -> {pred}")
    
    

# l = np.array([
#         [1, 0, 0],
#         [1, 0, 0],
#         [1, 0, 0],
#         [1, 1, 1]]).reshape((1, 12))

# m = np.array([
#         [1, 0, 1],
#         [1, 1, 1],
#         [1, 0, 1],
#         [1, 0, 1]]).reshape((1, 12))

# class Perceptron:
#     def _init_(self):
#         self.W = np.array([np.zeros(12)])
#     def fit(self, X, y, epoch=10):
#         for _ in range(epoch):
#             for i in range(len(X)):
#                 net = np.sum(X[i]*self.W)
#                 if net <= 0:
#                     y_hat = 0
#                 else:
#                     y_hat = 1
#                 dW = 0.5*(y[i] - y_hat)*X[i]
#                 self.W += dW
#         print(self.W)
#     def perdict(self, X):
#         net = np.sum(X*self.W)
#         return 0 if net <=0 else 1
# pr = Perceptron()
# pr.fit([l,l,l,l,l,m,m,m,m,m], [1,1,1,1,1,0,0,0,0,0])
# print(pr.perdict(l))
# print(pr.perdict(m))