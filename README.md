# HMM-Based Cell Association for Optimizing MTC Device Connectivity in 5G Networks

In the context of 5G networks, the efficient management of resources is crucial due to the massive number of connected devices, especially for Machine-Type Communication (MTC) devices. These devices, which typically involve low-power, low-latency communication, require optimized cell selection and channel availability strategies to maintain reliable and efficient communication in a dense network environment. This project applies Hidden Markov Models (HMM) to address these challenges.

By modeling the system as a probabilistic process, HMMs allow us to predict the most likely sequence of states (e.g., cell selection) based on observed data. The project leverages HMM to analyze the cell selection process and estimate the channel availability in a 5G network with a varying number of MTC devices. The use of the HMM enables better understanding and optimization of resource allocation, which is vital for ensuring the performance and scalability of the network.

The project includes implementations of various algorithms, such as the forward and backward algorithms for state probability computation, the Baum-Welch algorithm for parameter estimation (essential for adaptive learning in dynamic environments), and the Viterbi algorithm for decoding the most probable state sequence. These algorithms are applied to real-world observational data, and the results are visualized to help better understand the network's behavior as the number of MTC devices changes.

Ultimately, this project aims to provide a more efficient approach for managing cell selection and channel availability in the rapidly growing 5G network, where the density of MTC devices can pose significant challenges to system performance.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Setup and Requirements](#setup-and-requirements)
3. [Results and Visualizations](#results-and-visualizations)


## Project Overview

The project uses HMMs to model the cell selection process and determine the channel availability for varying numbers of MTC devices. The key algorithms used in this project include:

- **Forward Algorithm**: Computes the forward probabilities (state probabilities over time).
- **Backward Algorithm**: Computes the backward probabilities (backward recursion).
- **Baum-Welch Algorithm**: Used to estimate the parameters of the HMM.
- **Viterbi Algorithm**: Finds the most likely sequence of states.
- **Visualization**: Generates plots to visualize the results, including state probabilities, cell selection trends, and channel availability.



## Setup and Requirements

Before running the scripts, make sure to install the required libraries.

### Requirements:
- Python 3.x
- pandas
- numpy
- matplotlib
- seaborn

You can install the dependencies using `pip`:

```bash
pip install pandas numpy matplotlib seaborn
```

## References
1. Balapuwaduge, Indika & Li, Frank. (2019). Hidden Markov Model based Machine Learning for mMTC Device Cell Association in 5G Networks. 