def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

cells = [
    tuple(map(int, line.strip().split(", ")))
    for line in open("day6/input")
]

max_x = max(x for x, y in cells)
max_y = max(y for x, y in cells)

points = ((x, y) for x in range(max_x + 1) for y in range(max_y + 1))

safe_points = [
    point
    for point in points
    if sum(distance(point, cell) for cell in cells) < 10000
]

print safe_points

# print "-" * max_x
# for y in range(max_y + 1):
#     for x in range(max_x + 1):
#         if (x, y) in safe_points:
#             print "#",
#         else:
#             print " ",
#     print "|"
# print "-" * max_x

print len(safe_points)
