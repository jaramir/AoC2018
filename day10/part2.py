from part1 import measure, evolve, parse


def find_smallest_evolution(initial):
    state = initial
    time = 0
    volume = measure(state)

    while True:
        next_state = evolve(state)
        next_volume = measure(next_state)
        if next_volume < volume:
            state = next_state
            volume = next_volume
            time += 1
        else:
            return time


if __name__ == "__main__":
    state = parse("input")
    time = find_smallest_evolution(state)
    print time
