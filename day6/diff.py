def load(filename):
    return [int(line.strip()) for line in open(filename)]

step1 = load("day6/out.1")
step2 = load("day6/out.2")

print max(a for a, b in zip(step1, step2) if a == b)
