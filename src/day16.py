import re
import sys


def addr(regs, a, b, c): regs[c] = regs[a] + regs[b]
def addi(regs, a, b, c): regs[c] = regs[a] + b

def mulr(regs, a, b, c): regs[c] = regs[a] * regs[b]
def muli(regs, a, b, c): regs[c] = regs[a] * b

def banr(regs, a, b, c): regs[c] = regs[a] & regs[b]
def bani(regs, a, b, c): regs[c] = regs[a] & b

def borr(regs, a, b, c): regs[c] = regs[a] | regs[b]
def bori(regs, a, b, c): regs[c] = regs[a] | b

def setr(regs, a, b, c): regs[c] = regs[a]
def seti(regs, a, b, c): regs[c] = a

def gtir(regs, a, b, c): regs[c] = int(a > regs[b])
def gtri(regs, a, b, c): regs[c] = int(regs[a] > b)
def gtrr(regs, a, b, c): regs[c] = int(regs[a] > regs[b])

def eqir(regs, a, b, c): regs[c] = int(a == regs[b])
def eqri(regs, a, b, c): regs[c] = int(regs[a] == b)
def eqrr(regs, a, b, c): regs[c] = int(regs[a] == regs[b])


def part_one(entries):
    instrs = [addr, addi, mulr, muli,
              banr, bani, borr, bori,
              setr, seti, gtir, gtri,
              gtrr, eqir, eqri, eqrr]

    stats = {}

    how_many = 0
    for entry in entries:
        same_count = 0

        for instr in instrs:
            regs = entry["before"][:]
            instr(regs, *entry["instr"][1:])

            if entry["after"] == regs:
                same_count += 1

                if entry["instr"][0] not in stats:
                    stats[entry["instr"][0]] = {}

                if instr.__name__ not in stats[entry["instr"][0]]:
                    stats[entry["instr"][0]][instr.__name__] = 0

                stats[entry["instr"][0]][instr.__name__] += 1

        how_many += int(same_count >= 3)

    return how_many, stats


def part_two(stats, code):
    instrs = {}

    while stats:
        for key, value in sorted(stats.items()):
            was = False

            occurrences = {}
            for k, v in sorted(stats.items()):
                for x in v.keys():
                    if x not in occurrences:
                        occurrences[x] = {"count": 0, "occurs": []}

                    occurrences[x]["count"] += 1
                    occurrences[x]["occurs"].append(k)

            for k, v in occurrences.items():
                if v["count"] == 1:
                    instrs[v["occurs"][0]] = k
                    stats.pop(v["occurs"][0], None)
                    was = True

            if was:
                break

            if len(value) == 1:
                instrs[key] = list(value.values())[0]
                stats.pop(key, None)

    regs = [0, 0, 0, 0]
    for line in code:
        params = [int(x) for x in re.findall("[\d]+", line)]

        f = getattr(sys.modules[__name__], instrs[params[0]])
        f(regs, *params[1:])

    return regs[0]


def main():
    with open('../input/day16.txt', 'r') as f:
        full = f.read()
        tests = [re.findall(r"[\d]+", x) for x in full.split("\n\n")]

    entries = []

    for test in tests:
        if len(test) == 0:
            break

        numbers = [int(x) for x in test]
        entries.append({"before": numbers[0:4], "instr": numbers[4:8], "after": numbers[8:14]})

    how_many, stats = part_one(entries)
    print("Part One: %d" % how_many)

    code = full.split("\n\n\n\n")[1].splitlines()
    print("Part Two: %d" % part_two(stats, code))


if __name__ == '__main__':
    main()
