from collections import Counter

def mode(x):
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.iteritems() if count == max_count]

a = [1,2,3,4,5,2,3,5,2,4,6,2,3,4,6,6,2,3,52,3,52,2,3,5,2,3,6]

print(Counter(a))
