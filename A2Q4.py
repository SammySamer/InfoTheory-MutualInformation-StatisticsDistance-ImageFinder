import numpy as np
import pandas as pd

with open('echrate.txt') as f:
  lines = f.readlines()[9:374]


eps = 0.0000000000000001

x1 = np.empty([0,364])
x2 = np.empty([0,364])
x3 = np.empty([0,364])
x4 = np.empty([0,364])
x5 = np.empty([0,364])

for currLine in lines:
  splitLine = currLine.split()
  x1 = np.append(x1, int(splitLine[0]) / 10000)
  x2 = np.append(x2, int(splitLine[1]) / 10000)
  x3 = np.append(x3, int(splitLine[2]) / 10000)
  x4 = np.append(x4, int(splitLine[3]) / 10000)
  x5 = np.append(x5, int(splitLine[4]) / 10000)

def I_Dist(X,Y): 
  N = len(X)

  Xmin = np.amin(X)
  X = X - Xmin
  Xmax = max(X)
  X = X * (1-eps) / Xmax

  Ymin = min(Y)
  Y = Y - Ymin
  Ymax = max(Y)
  Y = Y * (1-eps) / Ymax

  M = np.floor(1 + np.log2(N) + 0.5).astype(int)
  u = np.floor(X*M).astype(int) + 1
  v = np.floor(Y*M).astype(int) + 1

  f = np.zeros((M,M))

  Zx = []
  Zy = [] 
  for k in range (1, M):
    Zx.append((2*k - 1) / (2*M))
  Zy = Zx  

  for i in range (N): 
    f[u[i] - 1][v[i] - 1] = f[u[i] - 1][v[i] - 1] + 1

  Pxy = (f / N) + eps
  Px = []
  Py = []

  for i in range (M):
    Px.append(sum(Pxy[:,i])) #columns
    Py.append(sum(Pxy[i]))   #rows

  Hx = -1 * sum(Px * np.log2(Px))
  Hy = -1 * sum(Py * np.log2(Py))
  Hxy = -1 * sum(Pxy.flatten() * np.log2(Pxy.flatten()))

  MI = Hx + Hy - Hxy
  Dist = 1 - (2 * MI / (Hx + Hy))

  return MI, Dist

echrate = [x1, x2, x3, x4, x5]
info = np.zeros((5,5))
dist = np.zeros((6,6))

for i in range (5):
  for j in range (5):
    info[i,j], dist[i,j] = I_Dist(echrate[i], echrate[j])

for i in range (5): 
  dist[i, 5] = sum(dist[i]) / 5
  dist[5, i] = sum(dist[:,i]) / 5
dist[5,5] = sum(dist[5])

infoFrame = pd.DataFrame(info)
distFrame = pd.DataFrame(dist)

print(infoFrame)
print(distFrame)
print()