from collections import defaultdict

def parse_event(event):
    return int(event[15:17]), event[19:].strip()

events = sorted([line for line in open('day4/input')])

events_per_guard = defaultdict(list)

current_guard = None

for event in events:
    minute, description = parse_event(event)

    if description.startswith("Guard"):
        current_guard = description.split()[1][1:]
    else:
        events_per_guard[current_guard].append(event)

events_per_guard = dict(events_per_guard)

minutes_slept = defaultdict(int)

for guard in events_per_guard:
    nap_started = None
    for event in events_per_guard[guard]:
        minute, description = parse_event(event)
        if description == "falls asleep":
            nap_started = minute
        else: # wakes up
            minutes_slept[guard] += minute - nap_started

minutes_slept = dict(minutes_slept)

guard_slept_more_minutes = sorted(minutes_slept.items(), lambda a, b: cmp(a[1], b[1]), reverse=True)[0][0]

sleep_pattern = [0] * 60
for event in events_per_guard[guard_slept_more_minutes]:
    minute, description = parse_event(event)
    if description == "falls asleep":
        nap_started = minute
    else: # wakes up
        for index in range(nap_started, minute):
            sleep_pattern[index] += 1

most_slept_minute = sleep_pattern.index(max(sleep_pattern))

print most_slept_minute * int(guard_slept_more_minutes)
