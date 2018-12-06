import re

def react(polymer):
    polymer = list(polymer.strip())
    i = 0
    while i < len(polymer) - 1:
        a = polymer[i]
        b = polymer[i + 1]
        if a.lower() == b.lower() and a != b:
            del polymer[i]
            del polymer[i]
            if i > 0: # lesson learned?
                i -= 1
        else:
            i += 1
    return "".join(polymer)

def units(polymer):
    return set(polymer.lower())

def filter(unit, polymer):
    return re.sub(unit, '', polymer, flags=re.IGNORECASE)

if __name__ == '__main__':
    input = open('day5/input').read()

    reacted = react(input)
    print len(reacted)

    for unit in units(reacted):
        print unit, len(react(filter(unit, reacted)))
