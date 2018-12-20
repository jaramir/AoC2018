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

if __name__ == '__main__':
    input = open('input').read()
    print len(react(input))
