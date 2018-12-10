import re
from collections import deque


def solve(players_count, last_marble):
    current_player = 0

    state = deque([])
    players = [0] * players_count

    for i in range(last_marble):
        if i != 0 and i % 23 == 0:
            state.rotate(7)
            players[current_player] += i + state.pop()
            state.rotate(-1)
        else:
            state.rotate(-1)
            state.append(i)

        current_player = (current_player + 1) % players_count

    return max(score for score in players)


with open('../input/day9.txt', 'r') as f:
    players, last_marble = tuple(map(int, re.findall(r"[\d]+", f.readline())))

print("Part One: %d" % solve(players, last_marble))
print("Part Two: %d" % solve(players, last_marble * 100))
