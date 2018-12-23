import numpy

def bfs(G, s):
    color = [0] * len(G)
    distance = [-1] * len(G)
    parent = [None] * len(G)
    Q = []

    color[s] = 1
    distance[s] = 0
    parent[s] = None

    Q.append(s)
    while Q:
        u = Q.pop()
        for v in G[u]:
            if color[v] == 0:
                color[v] = 1
                distance[v] = distance[u] + 1
                parent[v] = u
                Q.append(v)
        color[u] = 2

    return distance


def matrix_to_list(matrix):
    h, w = matrix.shape
    l = [[]] * h * w

    for y in range(h):
        for x in range(w):
            if matrix[y, x] == 1:
                sub = []

                if y + 2 < h and matrix[y + 2, x] == 1 and matrix[y + 1, x] in [2, 3]:
                    sub.append((y + 2) * w + x)

                if y - 2 >= 0 and matrix[y - 2, x] == 1 and matrix[y - 1, x] in [2, 3]:
                    sub.append((y - 2) * w + x)

                if x - 2 >= 0 and matrix[y, x - 2] == 1 and matrix[y, x - 1] in [2, 3]:
                    sub.append(y * w + x - 2)

                if x + 2 < w and matrix[y, x + 2] == 1 and matrix[y, x + 1] in [2, 3]:
                    sub.append(y * w + x + 2)

                l[y * w + x] = sub

    return l

def display(area, x1, y1, distances=None):
    oX = int(area.shape[1] / 2)
    oY = int(area.shape[0] / 2)

    rows = []
    for y in range(area.shape[0]):
        row = []
        for x in range(area.shape[1]):
            if x == x1 + oX and y == y1 + oY:
                row.append("\u001b[31m@ \u001b[0m")
                continue

            if x == oX and y == oY:
                row.append("X ")
                continue

            if area[y, x] == 1:
                if distances:
                    row.append((str(distances[y * area.shape[0] + x]) + "   ")[0:2])
                else:
                    row.append(".")
            elif area[y, x] == 0:
                row.append("\u001b[40;97m##\u001b[0m")
            elif area[y, x] == 2:
                row.append("||")
            elif area[y, x] == 3:
                row.append("--")
            else:
                row.append("  ")

        rows.append("".join(row))
    print("\n".join(rows))
    print("=" * 10)

def part_one(regex, start=0, area=None, x=0, y=0):
    if area is None:
        area = numpy.zeros((1000, 1000))

    oX = int(area.shape[1] / 2)
    oY = int(area.shape[0] / 2)

    if x == 0 and y == 0:
        area[oY, oX] = 1

    i = start
    while i < len(regex):
        if regex[i] == "N":
            y -= 1
            area[y + oY, x + oX] = 3
            y -= 1

        if regex[i] == "S":
            y += 1
            area[y + oY, x + oX] = 3
            y += 1

        if regex[i] == "E":
            x += 1
            area[y + oY, x + oX] = 2
            x += 1

        if regex[i] == "W":
            x -= 1
            area[y + oY, x + oX] = 2
            x -= 1

        if regex[i] in "NSEW":
            area[y + oY, x + oX] = 1

        if regex[i] == ")":
            return i

        if regex[i] == "(":
            while regex[i] != ")":
                i = part_one(regex, i + 1, area, x, y)

        if regex[i] == "|":
            return i

        i += 1

    if start == 0:
        return bfs(matrix_to_list(area), oY * area.shape[0] + oX)

    return len(regex)

def main():
    with open('../input/day20.txt', 'r') as f:
        regex = f.readline().strip()[1:-1]

    analysis = part_one(regex)

    print("Part One: %d" % max(analysis))
    print("Part Two: %d" % sum(int(x >= 1000) for x in analysis))


if __name__ == '__main__':
    main()
