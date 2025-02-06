def main():
    with open('input.txt', 'r') as input:
        left_col = []
        right_col = []

        for line in input:
            numbers = line.split()
            first = numbers[0]
            second = numbers[1]
            left_col.append(first)
            right_col.append(second)

    left_col.sort()
    right_col.sort()

    res = []
    for x, y in zip(left_col, right_col):
        res.append(abs(int(x)-int(y)))

    print(sum(res))
    return

if __name__ == "__main__":
    main()


# Second solution
def main():
    with open('input.txt', 'r') as file:
        # Generator expression () >< list comprehension []
        left_col, right_col = zip(*(line.split() for line in file))

    left_col = sorted(map(int, left_col))
    right_col = sorted(map(int, right_col))

    print(right_col)

    total_diff = sum(abs(a - b) for a, b in zip(left_col, right_col))

    print(total_diff)
    return

if __name__ == "__main__":
    main()