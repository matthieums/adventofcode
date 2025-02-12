directions = [(-1, 0), (1, 0), (0, 1), (0, -1),
              (-1, -1), (1, -1), (1, 1), (-1, 1)]


def main():
    file_path = '/home/matthieu/adventofcode/problem4/input.txt'
    data = []

    # Open and read file into an appropriate data structure.
    with open(file_path, 'r') as file:
        for line in file:
            data.append(line.strip())

    target = 'XMAS'
    word_length = len(target)
    height = len(data)
    width = len(data[0])
    total = 0

    def search_from(row, col, dr, dc):
        for i in range(word_length):
            nr, nc = row + (i * dr), col + (i * dc)
            if not (0 <= nr < height and 0 <= nc < width) or data[nr][nc] != target[i]:
                return False
        return True

    for r in range(height):
        for c in range(width):
            if data[r][c] == 'X':
                for dr, dc in directions:
                    if search_from(r, c, dr, dc):
                        total += 1
    print(total)
    return total


if __name__ == '__main__':
    main()
