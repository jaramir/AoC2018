def neighbours(cell):
    x, y = cell
    return {(x + 1, y),
            (x - 1, y),
            (x, y + 1),
            (x, y - 1)}

def contested(point, cells):
    for neighbour in neighbours(point):
        if neighbour in cells:
            return True
    else:
        return False

def step(families):
    new_families = []
    for index, cells in enumerate(families):
        next = set()
        others = set(cell
            for family in families
            for cell in family
            if families.index(family) != index)
        for cell in cells:
            next.add(cell)
            spawns = neighbours(cell)
            for spawn in spawns:
                if spawn in cells:
                    continue
                if spawn in next:
                    continue
                if not contested(spawn, others):
                    next.add(spawn)
        new_families.append(next)
    return new_families

def draw(families):
    cells = [cell for family in families for cell in family]

    for y in range(300):
        for x in range(300):
            if (x, y) in cells:
                print '#',
            else:
                print ' ',
        print
    print '-' * 500

def stat(families):
    for family in families:
        print len(family)
    print '-' * 100

if __name__ == '__main__':
    families = [
        [tuple(map(int, line.strip().split(", ")))]
        for line in open("input")
    ]

    for i in range(200):
        draw(families)
        stat(families)
        families = step(families)
