import re
from functools import reduce


class Node:
    def __init__(self):
        self.metadata = []
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)


sum_metadata = 0


def process(numbers):
    global sum_metadata

    child_amount = numbers.pop(0)
    metadata_amount = numbers.pop(0)

    node = Node()

    for i in range(child_amount):
        node.add_child(process(numbers))

    node.metadata = numbers[:metadata_amount]
    sum_metadata += reduce(lambda a, b: a + b, node.metadata)
    del numbers[:metadata_amount]

    return node


def part2(root):
    if len(root.children) == 0:
        return reduce(lambda a, b: a + b, root.metadata)

    sum = 0
    for entry_id in root.metadata:
        if entry_id != 0 and entry_id <= len(root.children):
            sum += part2(root.children[entry_id - 1])

    return sum


with open('../input/day8.txt', 'r') as f:
    numbers = list(map(int, re.findall(r"[\d]+", f.readline())))

node = process(numbers)
print(sum_metadata)
print(part2(node))
