letters = []
counts = []

while (row := input()) != 'ФИНИШ':
    for letter in row:
        letter = letter.lower()
        if letter in letters:
            counts[letters.index(letter)] += 1
        else:
            letters.append(letter)
            counts.append(1)
print(min(letters[counts.index(max(counts))]))            
