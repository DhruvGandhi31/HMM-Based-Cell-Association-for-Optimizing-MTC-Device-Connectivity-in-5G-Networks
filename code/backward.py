import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv('../Data/data_python_150.csv')

V = data['Observational states'].values

# Transition Probabilities
a = np.array(((0.54, 0.46), (0.49, 0.51)))

# Emission Probabilities
b = np.array(((0.16, 0.26, 0.58), (0.25, 0.28, 0.47)))


def backward(V, a, b):
    beta = np.zeros((V.shape[0], a.shape[0]))

    # setting beta(T) = 1
    beta[V.shape[0] - 1] = np.ones((a.shape[0]))

    # Loop in backward way from T-1 to
    # Due to python indexing the actual loop will be T-2 to 0
    for t in range(V.shape[0] - 2, -1, -1):
        for j in range(a.shape[0]):
            beta[t, j] = (beta[t + 1] * b[:, V[t + 1]]).dot(a[j, :])

    return beta


beta = backward(V, a, b)
print(beta)

plt.plot(beta)
plt.title("Backward Algorithm - State Probabilities Over Time")
plt.xlabel("Time Step")
plt.ylabel("Probability")
plt.legend(["State 1", "State 2"])  # Assuming two states
plt.show()
