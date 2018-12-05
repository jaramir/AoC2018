from collections import Counter

codes = [line.strip() for line in open("day2/input")]
counts = [Counter(code).values() for code in codes]
twos = sum(2 in count for count in counts)
threes = sum(3 in count for count in counts)
print twos * threes
