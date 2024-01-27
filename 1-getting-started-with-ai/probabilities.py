import random

def main():
    
    dogsProb = 0.8
    catsProb = 0.1
    batsProb = 0.1

    favourite = 'dogs'
    if dogsProb <= random.random() < dogsProb + catsProb:
        favourite = "cats"
    if dogsProb + catsProb <= random.random() < dogsProb + catsProb + batsProb:
        favourite = "bats"

    print("I love " + favourite) 

main()
