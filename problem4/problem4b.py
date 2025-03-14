FILE_PATH = '/home/matthieu/adventofcode/problem4/input.txt'

CROSSDIRECTIONS = [
    [(-1, -1), (1, 1)],
    [(-1, 1), (1, -1)]
]


def main() -> int:
    data = load_data(FILE_PATH)
    count = count_valid(data)
    print(count)
    return count


def load_data(file_path: str) -> list:
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]


def count_valid(data: list):
    count = 0
    for i in range(1, len(data) - 1):
        for j in range(1, len(data[0]) - 1):
            if data[i][j] == 'A':
                if all(valid_line(data, line, i, j) for line in CROSSDIRECTIONS):
                    count += 1
    return count


def valid_line(data: list, line: list, i: int, j: int) -> bool:
    valid = True
    letters = set()
    for dr, dc in line:
        c = data[i+dr][j+dc]
        if c in 'MS' and c not in letters:
            letters.add(c)
        else:
            valid = False
            break
    return valid


main()
