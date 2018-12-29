import re


def parse_line(line):
    (x, y, dx, dy) = re.match("position=<\s*(-?\d+),\s*(-?\d+)> velocity=<\s*(-?\d+),\s*(-?\d+)>", line).groups()
    return int(x), int(y), int(dx), int(dy)


def parse(filename):
    state = []
    for line in open(filename):
        state.append(parse_line(line.strip()))
    return state


def render(state):
    points = {(x, y) for (x, y, dx, dy) in state}
    min_x = min(x for (x, y) in points)
    max_x = max(x for (x, y) in points)
    min_y = min(y for (x, y) in points)
    max_y = max(y for (x, y) in points)

    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if (x, y) in points:
                print "#",
            else:
                print " ",
        print


def evolve(state):
    return [(x + dx, y + dy, dx, dy) for (x, y, dx, dy) in state]


def measure(state):
    points = {(x, y) for (x, y, dx, dy) in state}
    min_x = min(x for (x, y) in points)
    max_x = max(x for (x, y) in points)
    min_y = min(y for (x, y) in points)
    max_y = max(y for (x, y) in points)

    return (max_x - min_x) * (max_y - min_y)


def find_smallest_evolution(initial):
    state = initial
    volume = measure(state)

    while True:
        next_state = evolve(state)
        next_volume = measure(next_state)
        if next_volume < volume:
            state = next_state
            volume = next_volume
        else:
            return state


if __name__ == "__main__":
    state = parse("input")
    evo = find_smallest_evolution(state)
    render(evo)
