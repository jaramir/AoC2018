import re
from collections import Counter

def parse_claim(claim):
    id, left, top, width, height = re.sub('[ @,x:]', ' ', claim).split()
    return {
        'id': id,
        'left': int(left),
        'top': int(top),
        'width': int(width),
        'height': int(height)
    }

def to_areas(claim):
    for x in range(claim['left'], claim['left'] + claim["width"]):
        for y in range(claim['top'], claim['top'] + claim["height"]):
            yield (x, y)

claims = [parse_claim(line.strip()) for line in open('input')]

areas = [
    area
    for claim in claims
    for area in to_areas(claim)
]

print sum(count > 1 for (pos, count) in Counter(areas).items())
