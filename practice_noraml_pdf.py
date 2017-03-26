import random as random
import math as math
import matplotlib.pyplot as plt
from collections import Counter

def bernoulli_trial(p):
    return 1 if random.random() < p else 0

def binominal(n,p):
    return sum(bernoulli_trial(p) for _ in range(n))



#    mu =  p * n
#    sigma = math.sqrt(n * p * (1-p))

#    xs = range(min(data, max(data) + 1 )
#    ys = [normal_cdf(i + 0.5, mu, sigma) - normal_cdf(i -)]

data = [binominal(100, 0.75) for _ in range(10000)]
histgram = Counter(data)
print(histgram.keys())
print(histgram.values())
