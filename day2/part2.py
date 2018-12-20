from itertools import combinations

codes = [line.strip() for line in open("input")]

for a, b in combinations(codes, 2):
    if sum(c1 != c2 for (c1, c2) in zip(a, b)) == 1:
        print "".join([c1 for (c1, c2) in zip(a, b) if c1 == c2])
