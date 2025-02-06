def main(file):
    safe_count = 0

    with open(file, 'r') as input:
        for report in input:
            levels = list(map(int, report.split()))
            n = len(levels)

            if is_valid(levels):
                safe_count += 1
                continue

            for i in range(n):
                modified_levels = levels[:i] + levels[i+1:]
                if is_valid(modified_levels):
                    safe_count += 1
                    break
    print(safe_count)
    return


def is_valid(levels):
    if levels[0] < levels[1]:
        direction = 'increasing'
    elif levels[0] > levels[1]:
        direction = 'decreasing'
    else:
        return False

    for i in range(1, len(levels)):
        diff = abs(levels[i] - levels[i - 1])
        if diff < 1 or diff > 3:
            return False
        if direction == 'increasing' and levels[i] <= levels[i - 1]:
            return False
        if direction == 'decreasing' and levels[i] >= levels[i - 1]:
            return False

    return True


if __name__ == "__main__":
    file_path = "/home/matthieu/adventofcode/problem2/input.txt"
    main(file_path)
