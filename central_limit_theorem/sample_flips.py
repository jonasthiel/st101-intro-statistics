#Write a function sample that simulates N sets of coin flips and
#returns a list of the proportion of heads in each set of N flips
#It may help to use the flip and mean functions that you wrote before

import random
from math import sqrt
from plotting import *

def mean(data):
    return float(sum(data))/len(data)

def variance(data):
    mu=mean(data)
    return sum([(x-mu)**2 for x in data])/len(data)

def stddev(data):
    return sqrt(variance(data))


def flip(N):
    return [random.random()>0.5 for x in range(N)]

def sample(N):
    samples = []
    for i in range(N):
        samples.append(mean(flip(N)))
    return samples

N=1000
outcomes=sample(N)
histplot(outcomes,nbins=30)

print(mean(outcomes))
print(stddev(outcomes))