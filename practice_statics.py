import random
def random_kid():
    return random.choice(["boy","girl"])


both_girls = 0
older_girl = 0
either_girl = 0

random.seed(0)

for _ in range(10000):
    younger = random_kid()
    older = random_kid()
    if older == "girl":
        older_girl += 1
    if older == "girl" and younger == "girl":
        both_girls += 1
    if older == "girl" or younger == "girl":
        either_girl += 1

print(both_girls)
print(older_girl)
print(either_girl)


def uniform_pdf(x):
    return 1 if x >=0 and x < 1 else 0

def uniform_cdf(x):
    "return the probability that a uniform random variable iss <=x"
    if x < 0: return 0
    elif x < 1: return x
    else: return 1
