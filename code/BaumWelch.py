import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Forward algorithm


def forward(V, a, b, initial_distribution):
    alpha = np.zeros((V.shape[0], a.shape[0]))
    alpha[0, :] = initial_distribution * b[:, V[0]]

    for t in range(1, V.shape[0]):
        for j in range(a.shape[0]):
            alpha[t, j] = alpha[t - 1].dot(a[:, j]) * b[j, V[t]]
    return alpha

# Backward algorithm


def backward(V, a, b):
    beta = np.zeros((V.shape[0], a.shape[0]))
    beta[V.shape[0] - 1] = np.ones((a.shape[0]))

    for t in range(V.shape[0] - 2, -1, -1):
        for j in range(a.shape[0]):
            beta[t, j] = (beta[t + 1] * b[:, V[t + 1]]).dot(a[j, :])
    return beta

# Baum-Welch algorithm for training HMM


def baum_welch(V, a, b, initial_distribution, n_iter=100):
    M, T = a.shape[0], len(V)

    for n in range(n_iter):
        alpha = forward(V, a, b, initial_distribution)
        beta = backward(V, a, b)

        xi = np.zeros((M, M, T - 1))
        for t in range(T - 1):
            denominator = np.dot(
                np.dot(alpha[t, :].T, a) * b[:, V[t + 1]].T, beta[t + 1, :])
            for i in range(M):
                numerator = alpha[t, i] * a[i, :] * \
                    b[:, V[t + 1]].T * beta[t + 1, :].T
                xi[i, :, t] = numerator / denominator

        gamma = np.sum(xi, axis=1)
        a = np.sum(xi, 2) / np.sum(gamma, axis=1).reshape((-1, 1))

        gamma = np.hstack(
            (gamma, np.sum(xi[:, :, T - 2], axis=0).reshape((-1, 1))))
        denominator = np.sum(gamma, axis=1)
        for l in range(b.shape[1]):
            b[:, l] = np.sum(gamma[:, V == l], axis=1)

        b = np.divide(b, denominator.reshape((-1, 1)))

    return a, b

# Viterbi algorithm (decoding the most likely sequence)


def viterbi(V, a, b, initial_distribution):
    T = V.shape[0]
    M = a.shape[0]

    omega = np.zeros((T, M))
    omega[0, :] = np.log(initial_distribution * b[:, V[0]])

    prev = np.zeros((T - 1, M))

    for t in range(1, T):
        for j in range(M):
            probability = omega[t - 1] + np.log(a[:, j]) + np.log(b[j, V[t]])
            prev[t - 1, j] = np.argmax(probability)
            omega[t, j] = np.max(probability)

    S = np.zeros(T)
    last_state = np.argmax(omega[T - 1, :])
    S[0] = last_state

    backtrack_index = 1
    for i in range(T - 2, -1, -1):
        S[backtrack_index] = prev[i, int(last_state)]
        last_state = prev[i, int(last_state)]
        backtrack_index += 1

    return ["Cell A is selected" if s == 0 else "Cell B is selected" for s in np.flip(S)]

# Function to load data, initialize parameters, and run the algorithms


def process_data(number_of_devices):
    P_list = []
    res_cellA, res_cellB = [], []

    for number in number_of_devices:
        name = f'../Data/data_python_{number}.csv'
        data = pd.read_csv(name)
        V = data['Observational states'].values

        a = np.ones((2, 2)) / 2  # Initialize transition probabilities
        # Initialize emission probabilities
        b = np.array([[1, 3, 5], [2, 4, 6]])
        # Normalize emission probabilities
        b = b / np.sum(b, axis=1).reshape((-1, 1))
        initial_distribution = np.array([0.5, 0.5])

        alpha = forward(V, a, b, initial_distribution)
        Po = np.sum(alpha)
        Po_givenlambda = np.sum(Po)

        Pth = 0.15  # Threshold for probability
        print(baum_welch(V, a, b, initial_distribution, n_iter=100))

        P_list.append(Po_givenlambda)

        output = viterbi(V, a, b, initial_distribution)
        count_cellA = output.count("Cell A is selected")
        count_cellB = output.count("Cell B is selected")

        res_cellA.append(count_cellA)
        res_cellB.append(count_cellB)

        with open(f'../Output/output_{number}.txt', "w") as f:
            f.write("\n".join(output))

    return P_list, res_cellA, res_cellB

# Plotting the results


def plot_results(number_of_devices, P_list, res_cellA, res_cellB):
    P_available = [1 - p for p in P_list]

    plt.plot(number_of_devices, P_available,
             marker='X', linestyle='--', color='green')
    plt.title("Channel Availability for varying MTC device number")
    plt.grid(True)
    plt.axis([150, 600, 0.675, 0.875])
    plt.legend(['HMM based cell selection'], loc='upper right')
    plt.xlabel("Number of MTC devices")
    plt.ylabel("Channel Availability")
    plt.show()

    plt.plot(number_of_devices, res_cellA, 'r--',
             number_of_devices, res_cellB, 'b')
    plt.title("Frequency of selected cell for varying MTC device number")
    plt.grid(True)
    plt.axis([150, 600, 30, 420])
    plt.legend(['Cell A', 'Cell B'], loc='upper left')
    plt.xlabel("Number of MTC devices")
    plt.ylabel("Number of times cell selected")
    plt.show()


# Main execution
number_of_devices = [150, 250, 350, 450, 550, 600]
P_list, res_cellA, res_cellB = process_data(number_of_devices)
plot_results(number_of_devices, P_list, res_cellA, res_cellB)
