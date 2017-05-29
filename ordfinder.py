import itertools


rows = []
answer = []
correct_words = []

print("Indtast alle linjer, afslut med en blank linje:")
while True:
    inp = input()
    if inp == '':
        break
    else:
        rows.append(inp)

print("Indtast antal bogstaver pr. linje, afslut med en blank linje:")
while True:
    inp = input()
    if inp == '':
        break
    else:
        answer.append(int(inp))

cols = []
for i in range(len(rows[0])):
    cols.append([])
    for j in range(len(rows)):
        cols[i].append(rows[j][i])

for i in range(len(cols)):
    cols[i] = ''.join(cols[i])

words = list(itertools.product(*cols))

for i in range(len(words)):
    words[i] = ''.join(words[i])

words = list(set(words))

for i in range(len(words)):
    matches = [0] * 7
    for j in range(len(rows)):
        for k in range(len(rows[j])):
            if words[i][k] == rows[j][k]:
                matches[j] += 1
    if matches == answer:
        correct_words.append(words[i])

print("Følgende ord matcher: ")
for i in range(len(correct_words)):
    print(correct_words[i])

input("Tryk Enter for at afslutte...")
