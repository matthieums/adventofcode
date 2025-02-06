def main(file):

    safe_count = 0

    with open(file, 'r') as input:
        for report in input:
            levels = list(map(int, report.split()))
            n = len(levels)

            if levels[0] < levels[1]:
                direction = 'increasing'
            elif levels[0] > levels[1]:
                direction = 'decreasing'
            else:
                continue

            is_safe = True

            for i in range(1, n):
                diff = abs(levels[i] - levels[i - 1])

                if diff < 1 or diff > 3:
                    is_safe = False
                    break

                if direction == 'increasing' and levels[i] <= levels[i - 1]:
                    is_safe = False
                    break

                if direction == 'decreasing' and levels[i] >= levels[i - 1]:
                    is_safe = False
                    break

            if is_safe:
                safe_count += 1

        print(safe_count)

if __name__ == "__main__":
    file_path = "/home/matthieu/adventofcode/problem2/input.txt"
    main(file_path)
