import numpy


def get_stats(entries: list):
    guards = {}

    current_guard = 0
    sleep_start = 0

    for entry in entries:
        minutes = int(entry[0][-2:])

        if entry[1] == "shift":
            current_guard = entry[2]
        elif entry[1] == "asleep":
            sleep_start = minutes
        elif entry[1] == "up":
            sleep_end = minutes

            if current_guard not in guards:
                guards[current_guard] = {"total": 0, "minutes": numpy.zeros(60)}

            guards[current_guard]["total"] += sleep_end - sleep_start
            guards[current_guard]["minutes"][sleep_start:sleep_end] += 1

    return sorted(guards.items(), key=lambda x: x[1]["total"], reverse=True)


def part_one(stats):
    return stats[0][0] * numpy.argmax(stats[0][1]["minutes"])


def part_two(stats):
    top_value = top_minute = top_guard = -1

    for (id, entry) in stats:
        most_common = numpy.argmax(entry["minutes"])

        if entry["minutes"][most_common] > top_value:
            top_minute = most_common
            top_value = entry["minutes"][most_common]
            top_guard = id

    return top_guard * top_minute


def main():
    with open('../input/day4.txt', 'r') as f:
        entries = []
        for line in f:
            entry = [line[1:17], line[line.rfind(" ") + 1:].rstrip()]

            if "Guard" in line:
                entry.append(int(line[line.find("#") + 1:line.find(" ", line.find("#") + 1)]))

            entries.append(entry)

    entries.sort(key=lambda x: x[0])
    stats = get_stats(entries)

    print("Part One: %d\nPart Two: %d" % (part_one(stats), part_two(stats)))


if __name__ == '__main__':
    main()
