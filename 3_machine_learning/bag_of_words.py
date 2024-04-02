import numpy as np

data = [[1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 3, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1]]

def distance(row1, row2):
    sum = 0
    for i in range(len(row1)):
        sum += abs(row1[i] - row2[i])
    
    if sum > 0:
        return sum
    return np.inf

def all_pairs(data):
    dist = [[distance(sent1, sent2) for sent1 in data] for sent2 in data]
    return dist

def find_nearest_pair(data):
    N = len(data)
    dist = np.empty((N, N), dtype=float)
    dist = np.array(all_pairs(data))
    print(np.unravel_index(np.argmin(dist), dist.shape))

find_nearest_pair(data)
