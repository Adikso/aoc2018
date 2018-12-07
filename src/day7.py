import re
import string
from collections import OrderedDict, defaultdict


def process(points):
    depends = defaultdict(set)

    for (dependency, target) in points:
        if dependency not in depends:  # dependency would not show as target when its first element
            depends[dependency] = set()

        depends[target].add(dependency)

    return OrderedDict(sorted(depends.items()))


def part_one(points):
    visited = []
    depends = process(points)
    size = len(depends.keys())

    while len(visited) < size:
        for target in depends.keys():
            if depends[target].issubset(set(visited)):
                visited.append(target)
                del depends[target]
                break

    return ''.join(visited)


def part_two(points):
    alphabet = string.ascii_uppercase

    visited = []
    depends = process(points)
    size = len(depends.keys())

    queue = {}
    total = 0

    while len(visited) < size:
        for target in list(queue.keys()):
            time = queue[target]
            if time == 0:
                visited.append(target)
                del queue[target]

        for target in list(depends.keys()):
            if depends[target].issubset(set(visited)) and len(queue) < 5:
                queue[target] = 60 + alphabet.index(target) + 1
                del depends[target]

        for target in queue.keys():
            queue[target] -= 1

        total += 1

    return total - 1


def main():
    with open('../input/day7.txt', 'r') as f:
        points = [tuple(re.findall(r" ([A-Z]) ", line)) for line in f]

    print("Part One: %s" % part_one(points))
    print("Part Two: %s" % part_two(points))


if __name__ == '__main__':
    main()
