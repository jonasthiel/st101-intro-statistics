#Given that the probability of one head is p, return the probability of
#two flips resulting in two heads

def f(p):
    return p ** 2

#Return the probability of exactly one head in three flips

def f(p):
    return 3 * p * (1 - p) ** 2

#Return the probability of flipping one head each from two coins
#One coin has a probability of heads of p1 and the other of p2

def f(p1,p2):
    return p1 * p2

#Two coins have probabilities of heads of p1 andd p2
#The probability of selecting the first coin is p0
#Return the probability of a flip landing on heads

def f(p0,p1,p2):
    return p0 * p1 + (1 - p0) * p2