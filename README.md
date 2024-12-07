# HMM-Based Cell Association for Optimizing MTC Device Connectivity in 5G Networks

![Project Status](https://img.shields.io/badge/Status-Finished-blue)

## 🏆 Group Details 
**Group Number:** Gr13EC431  
**Group Members:**
- **Akula Mani Shanker** (202151016)
- **Arghadeep Dey** (202151027)
- **Gandhi Dhruv Vipulkumar** (202151053)
- **Nihal Vishwakarma** (202151099)
- **Vedant Bhagatsingh Patil** (202152330)

### Video Presentation
![Video](https://drive.google.com/file/d/1t2h9LBTbvVElQDtiWF7XLKHkXdq7ofgj/view)

### Mentor
**Dr. Bhupendra Kumar**

## 📚 Table of Contents
1. [Project Overview](#project-overview)
2. [Setup and Requirements](#setup-and-requirements)
3. [References](#references)




## 🚀 Project Overview

In 5G networks, efficient resource management is essential due to the large number of connected Machine-Type Communication (MTC) devices. These devices, with low-power and low-latency communication, need optimized cell selection and channel availability strategies to ensure reliable communication in dense environments. This project uses Hidden Markov Models (HMM) to address these challenges.

By treating the system as a probabilistic process, HMMs predict the most likely sequence of states (e.g., cell selection) from observed data, enabling better resource allocation. The project analyzes cell selection and channel availability for varying MTC device densities, aiming to enhance network performance and scalability.

Key algorithms include:

- **Forward Algorithm**: Calculates forward probabilities over time.  
- **Backward Algorithm**: Computes backward probabilities using recursion.  
- **Baum-Welch Algorithm**: Estimates HMM parameters.  
- **Viterbi Algorithm**: Determines the most likely state sequence.



## 🔧 Setup and Requirements

Before running the scripts, make sure to install the required libraries.

1. First clone the github repo

```bash
git clone https://github.com/DhruvGandhi31/HMM-Based-Cell-Association-for-Optimizing-MTC-Device-Connectivity-in-5G-Network.git
```

2. You can install the dependencies using `pip`:

```bash
pip install -r requirements.txt
```

3. Then run each python files in the code directory:

```bash
cd code
```

## 📬 References
1. Balapuwaduge, Indika & Li, Frank. (2019). Hidden Markov Model based Machine Learning for mMTC Device Cell Association in 5G Networks. 