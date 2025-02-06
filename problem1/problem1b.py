def main():
    with open('input.txt', 'r') as file:
        left_col, right_col = zip(*(line.split() for line in file))

    frequency = {}

    for x, y in zip(right_col, left_col):
        if x not in frequency:
            frequency[x] = 0
        elif x in frequency:
            frequency[x] += 1

        if y not in frequency:
            frequency[y] = 0
        elif y in frequency:
            frequency[y] += 1

    print(sum((int(key) * int(value)) for (key, value) in frequency.items()))
    return


if __name__ == "__main__":
    main()