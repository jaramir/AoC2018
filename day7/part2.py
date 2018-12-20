def solve(dependants, base_cost=60, workers=5):
    def duration(task):
        return ord(task) - 64 + base_cost

    sequence = []
    outstanding_tasks = {dependency for dependency, dependant in dependants} | \
                        {dependant for dependency, dependant in dependants}

    started_tasks = {}

    def unsatified_dependencies(task):
        return [dependency
                for dependency, dependant in dependants
                if dependant == task
                and dependency not in sequence]

    t = 0

    while True:
        for task in started_tasks.keys():
            if started_tasks[task] == t:
                sequence.append(task)
                del started_tasks[task]

        available_workers = workers - len(started_tasks)

        unblocked_tasks = [task
                           for task in sorted(outstanding_tasks)
                           if len(unsatified_dependencies(task)) == 0
                           ][:available_workers]

        for task in unblocked_tasks:
            started_tasks[task] = t + duration(task)
            outstanding_tasks.remove(task)

        wip = "".join(started_tasks.keys())
        done = "".join(sequence)
        print "{t:4d} | {wip:5s} | {done}".format(**locals())

        if outstanding_tasks or started_tasks:
            t = min(started_tasks.values())
            continue
        else:
            return t

if __name__ == '__main__':
    print solve([
        (line[5], line[36])
        for line in open("input")
    ])
