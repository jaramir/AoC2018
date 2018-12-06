from collections import defaultdict

def parse_event(event):
    return int(event[15:17]), event[19:].strip()

def get_events_by_guard(events):
    events_per_guard = defaultdict(list)
    current_guard = None
    for event in events:
        minute, description = parse_event(event)
        if description.startswith("Guard"):
            current_guard = description.split()[1][1:]
        else:
            events_per_guard[current_guard].append(event)
    return dict(events_per_guard)

def get_nights_worked(events):
    nights_worked = defaultdict(int)
    for event in events:
        minute, description = parse_event(event)
        if description.startswith("Guard"):
            nights_worked[description.split()[1][1:]] +=1
    return dict(nights_worked)

def get_sleep_patterns(events_per_guard):
    sleep_patterns = {}
    for guard in events_per_guard:
        sleep_patterns[guard] = get_sleep_pattern(events_per_guard[guard])
    return sleep_patterns

def get_sleep_pattern(events):
    sleep_pattern = [0] * 60
    nap_started = None
    for event in events:
        minute, description = parse_event(event)
        if description == "falls asleep":
            nap_started = minute
        else: # wakes up
            for index in range(nap_started, minute):
                sleep_pattern[index] += 1
    return sleep_pattern

def get_max_times_asleep(sleep_patterns):
    max_times_asleep = {}
    for guard in sleep_patterns:
        max_times_asleep[guard] = max(sleep_patterns[guard])
    return max_times_asleep

def get_asleep_probability(nights_worked, max_times_asleep):
    asleep_probability = {}
    for guard in max_times_asleep:
        asleep_probability[guard] = max_times_asleep[guard] * 1.0 / nights_worked[guard]
    return asleep_probability

if __name__ == '__main__':
    events = sorted([line for line in open('day4/input')])
    events_per_guard = get_events_by_guard(events)
    sleep_patterns = get_sleep_patterns(events_per_guard)
    nights_worked = get_nights_worked(events)
    max_times_asleep = get_max_times_asleep(sleep_patterns)
    asleep_probability = get_asleep_probability(nights_worked, max_times_asleep)

    print " " * 43,
    for i in range(60):
        print "%2s" % i,
    print
    for guard in sorted(asleep_probability, key=asleep_probability.get, reverse=True):
        print "%4s slept %2s times over %2s nights. p: %.2f" % (guard, max_times_asleep[guard],  nights_worked[guard], asleep_probability[guard]),
        for times in sleep_patterns[guard]:
            if times == 0:
                print "  ",
            else:
                print "%2s" % times,
        print
    print

    target_guard = sorted(asleep_probability, key=asleep_probability.get, reverse=True)[0]
    target_minute = sleep_patterns[target_guard].index(max_times_asleep[target_guard])
    print target_guard, "*", target_minute, int(target_guard) * target_minute
