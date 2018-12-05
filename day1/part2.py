import sys
from itertools import cycle

changes = [int(line) for line in open("day1/input")]

current = 0
seen = set()

for change in cycle(changes):
    current += change
    if current in seen:
        print current
        sys.exit(0)
    seen.add(current)
