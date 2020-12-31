#Calculate the probability of a positive result given that
#p0=P(C)
#p1=P(Positive|C)
#p2=P(Negative|Not C)

def f(p0,p1,p2):
    return p0 * p1 + (1 - p0) * (1 - p2)