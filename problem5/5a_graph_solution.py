RULES = '/home/matthieu/adventofcode/problem5/rules.txt'
UPDATES = '/home/matthieu/adventofcode/problem5/updates.txt'


def build_graph() -> dict:
    graph = {}

    with open(RULES, "r") as rules_file:
        for line in rules_file:
            number, prereq = line.strip().split('|')
            graph.setdefault(number, []).append(prereq)

    return graph


def build_updates_list() -> list:
    with open(UPDATES, "r") as updates_file:
        updates = [line.strip().split(',') for line in updates_file]
        return updates


def main() -> int:
    graph = build_graph()
    updates = build_updates_list()
    total = 0

    for update in updates:
        visited = set()
        valid = True
        for page in update:
            if any(neighbour in visited for neighbour in graph[page]):
                valid = False
                break
            visited.add(page)
        if valid:
            total += int(update[len(update) // 2])
    print(total)
    return total


main()
