from collections import defaultdict

def parse_event(event):
    return int(event[15:17]), event[19:].strip()

events = sorted([line for line in open('day4/input')])

events_per_guard = defaultdict(list)
nights_per_guard = defaultdict(int)

current_guard = None

for event in events:
    minute, description = parse_event(event)

    if description.startswith("Guard"):
        current_guard = description.split()[1][1:]
        nights_per_guard[current_guard] += 1
    else:
        events_per_guard[current_guard].append(event)

events_per_guard = dict(events_per_guard)
nights_per_guard = dict(nights_per_guard)

sleep_pattens = {}
max_per_guard = {}
sleepiness_per_guard = {}

for guard in events_per_guard:
    sleep_pattens[guard] = [0] * 60
    nap_started = None
    for event in events_per_guard[guard]:
        minute, description = parse_event(event)
        if description == "falls asleep":
            nap_started = minute
        else: # wakes up
            for idx in range(nap_started, minute):
                sleep_pattens[guard][idx] += 1

    max_per_guard[guard] = max(sleep_pattens[guard])
    sleepiness_per_guard[guard] = max_per_guard[guard] * 1.0 / nights_per_guard[guard]

sleepiest_guard = sorted(sleepiness_per_guard.items(), lambda a, b: cmp(a[1], b[1]), reverse=True)[0][0]
overworked_guard = sorted(max_per_guard.items(), lambda a, b: cmp(a[1], b[1]), reverse=True)[0][0]

def report_for(guard):
    max_times_slept = max(sleep_pattens[guard])
    sleepiest_minute = sleep_pattens[guard].index(max(sleep_pattens[guard]))
    code = int(guard) * sleepiest_minute
    nights_worked = nights_per_guard[guard]
    sleep_probability = max_times_slept * 1.0 / nights_worked
    sleep_patten = " ".join(map(str, sleep_pattens[guard]))
    print """slept {max_times_slept} times out of {nights_worked} nights {sleep_probability}
sleepiest minute: {sleepiest_minute}
code: {code}
{sleep_patten}
""".format(**locals())

print "sleepiest guard", sleepiest_guard
report_for(sleepiest_guard)

print "overworked guard", overworked_guard
report_for(overworked_guard)
