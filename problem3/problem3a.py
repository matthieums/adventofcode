def main():
    file_path = '/home/matthieu/adventofcode/problem3/input.txt'
    with open(file_path, 'r') as file:
        text = file.read()

    total = parseText(text)
    print(total)
    return


def parseText(text):
    """parse the hidden function within a string of text and execute them"""
    enableMultiplication = True
    maxIndex = len(text)
    total_sum = 0

    i = 0
    while i < maxIndex:

        # check if multiplication operation emerges
        if enableMultiplication and text[i] == 'm' and text[i + 1: i + 4] == 'ul(':
            i += 4
            extractIndex = i
            numbers = extractNumbers(text, extractIndex, maxIndex)

            if numbers:
                x, y = numbers
                total_sum += x * y
                continue

        # check if a do() emerges
        if not enableMultiplication and text[i] == 'd' and text[i+1: i+4] == 'o()':
            enableMultiplication = True
            i += 4
            continue

        # check if a don't() emerges
        elif text[i] == 'd' and text[i+1: i+7] == 'on\'t()':
            enableMultiplication = False
            i += 7
            continue

        i += 1

    return total_sum


def extractNumbers(text, start_index, end_index):
    """Extract numbers if found within the next indices"""
    symbols = [',', ')']
    res = []
    j = start_index

    for symbol in symbols:
        number = ''

        while text[j].isdigit() and j < end_index and len(number) < 3:
            number += text[j]
            j += 1

        if len(number) == 0 or text[j] != symbol:
            return None

        j += 1
        res.append(int(number))

    return (res)


if __name__ == "__main__":
    main()
