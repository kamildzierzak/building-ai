import numpy as np


def generate(p1):
    # change this so that it generates 10000 random zeros and ones
    # where the probability of one is p1
    seq = np.random.choice([0, 1], p=[1-p1, p1], size=10000)
    return seq


def count(seq):
    total = 0
    countToFive = 0
    for i in seq:
        if (i == 1):
            countToFive = countToFive + 1
            if (countToFive >= 5):
                total = total + 1
        else:
            countToFive = 0
    return total


def main(p1):
    seq = generate(p1)
    return count(seq)


print(main(2/3))
