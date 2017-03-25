import random
def random_kid():
    return random.choice(["boy","girl"])


both_girl = 0
older_girls = 0
either_girl = 0

random.seed(0)

for _ in range(10000):
    younger = random_kid()
    older = random_kid()
    if older == "girl":
        older_girls += 1
    if older == "girl" and younger == "girl":
        both_girl += 1
        either_girl =+ 1

print(both_girl)
print(older_girls)
