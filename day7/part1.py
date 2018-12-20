def solve(dependants):
    sequence = []
    outstanding_tasks = {dependency for dependency, dependant in dependants} | \
                        {dependant for dependency, dependant in dependants}

    while outstanding_tasks:
        for task in sorted(outstanding_tasks):
            unsatified = [dependency
                for dependency, dependant in dependants
                if dependant == task
                and dependency not in sequence]

            if len(unsatified) > 0:
                continue

            sequence.append(task)
            outstanding_tasks.remove(task)
            break

    return "".join(sequence)

if __name__ == '__main__':
    print solve([
        (line[5], line[36])
        for line in open("input")
    ])
