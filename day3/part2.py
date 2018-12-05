import re
import sys

def parse_claim(claim):
    id, left, top, width, height = re.sub('[ #@,x:]', ' ', claim).split()
    yield {
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

claims = {
    claim["id"]: set(to_areas(claim))
    for line in open('day3/input')
    for claim in parse_claim(line.strip())
}

for claim in claims:
    area = claims[claim]
    for other in claims:
        if other == claim:
            continue
        if len(area.intersection(claims[other])) > 0:
            break
    else:
        print claim
