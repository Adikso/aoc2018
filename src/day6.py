import re
from collections import defaultdict


def distance(a, b):
    x1, y1 = a
    x2, y2 = b

    return abs(x1 - x2) + abs(y1 - y2)


def find_nearest_to(x, y):
    top_point = None
    top_value = 1000000

    for point in points:
        dist = distance((x, y), point)

        if dist < top_value:
            top_value = dist
            top_point = point
        elif dist == top_value:
            top_point = None

    return top_point


def get_infinite(r=10000):
    infinite = set()

    for p in [-r, r]:
        for y in range(max_top, max_bottom):
            infinite.add(find_nearest_to(p, y))

        for x in range(max_left, max_right):
            infinite.add(find_nearest_to(x, p))

    return filter(None, infinite)


def part_one():
    areas = defaultdict(set)

    for x in range(max_left, max_right):
        for y in range(max_top, max_bottom):
            top_point = find_nearest_to(x, y)

            if top_point:
                areas[top_point].add((x, y))

    for k in get_infinite():
        del areas[k]

    return max(len(p) for p in areas.values())


def part_two():
    in_region = 0

    for x in range(max_left, max_right):
        for y in range(max_top, max_bottom):
            if sum(distance((x, y), p) for p in points) < 10000:
                in_region += 1

    return in_region


with open('../input/day6.txt', 'r') as f:
    points = list(tuple(map(int, re.findall(r"[\d]+", line))) for line in f)

max_right = max(x for x, y in points)
max_left = min(x for x, y in points)

max_bottom = max(y for x, y in points)
max_top = min(y for x, y in points)

print("Part One: %d" % part_one())
print("Part Two: %d" % part_two())
