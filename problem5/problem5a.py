RULES = '/home/matthieu/adventofcode/problem5/rules.txt'
UPDATES = '/home/matthieu/adventofcode/problem5/updates.txt'


def load_data() -> tuple[dict, list]:
    prereqToNumber = dict()
    updates = list()

    with open(RULES, "r") as rules_file:
        for line in rules_file:
            number, prereq = line.strip().split('|')
            prereqToNumber.setdefault(number, []).append(prereq)

    with open(UPDATES, "r") as updates_file:
        updates = [line.strip().split(',') for line in updates_file]

    return prereqToNumber, updates


def read(data) -> int:
    valid = 0
    prereqDict, updatesList = data

    for update in updatesList:
        positions = {}
        n = len(update)
        interrupted = False

        for i, num in enumerate(update):
            positions[num] = i
            for requirement in prereqDict[num]:
                if requirement in positions and positions[requirement] < positions[num]:
                    interrupted = True
                    break
        if not interrupted:
            valid += int(update[n // 2])
    return valid


def main():
    data = load_data()
    print(read(data))
    return


main()
