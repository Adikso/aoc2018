import string

with open('../input/day5.txt', 'r') as f:
    input = f.read().rstrip()


# No brain solution
def count(data):
    good_pass = False
    pass_count = 0

    while not good_pass:
        for letter in string.ascii_lowercase:
            before = len(data)
            data = data.replace(letter + letter.upper(), "").replace(letter.upper() + letter, "")

            pass_count = pass_count + 1 if len(data) == before else 0

            if pass_count == len(string.ascii_lowercase):
                return before, data


amount, data = count(input)  # Save result of first elimination
print("Part One: %d" % amount)
print("Part Two: %d" % min(count(data.replace(letter, "").replace(letter.upper(), ""))[0] for letter in string.ascii_lowercase))
