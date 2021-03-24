"""
Followed the pseudo code provided in the assignment file.
"""
import numpy as np
import pandas as pd

a = 0 
b = 31 
R = 32

M = 50
N = 50

eps = 0.0000000000000001
H = []
p_s = []

with open('images/IA.txt') as f:
    referenceImage = f.readlines()[5:]

imageNames = ['IB1.txt', 'IB2.txt', 'IB3.txt', 'IB4.txt', 'IB5.txt', 'IB6.txt', 'IB7.txt', 'IB8.txt', 'IB9.txt', 'IB10.txt']

for image in imageNames: 
    with open ('images/' + image) as f:
        currImage = f.readlines()[4:]

        # this should all be 0's, but there was an error "divide by zero encountered in log2"
        # so I'm replacing them with very small values really close to 0 instead, the eps variable.
        # C = np.zeros((R, R))
        C = np.empty([R,R])
        C.fill(eps)
        for i in range (M):
            for j in range (N): 
                K = int(referenceImage[i].split()[j])
                L = int(currImage[i].split()[j])
                C[K][L] = C[K][L] + 1
        P = C / (M*N)
        H.append(-1 * sum(P.flatten() * np.log2(P.flatten())))
        

MaxH = max(H)
for currH in H:
    p_s.append(1 - (currH/MaxH))

p_s_np = np.asarray(p_s)
smax = np.argmax(p_s_np)

PFrame = pd.DataFrame(P)

print("Probs Matrix: \n", PFrame)
print("Entropy Matrix: \n", H)
print("Similarity Measures: \n", p_s)
print("Index of most similar image: ", smax)
