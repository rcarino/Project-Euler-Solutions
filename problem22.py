file = open('names.txt', 'r')
names = []
for line in file:
    names += line.replace('"', '').lower().split(',')

names.sort()

scores = []
for i, name in enumerate(names):
    score = 0
    for c in name:
        score += ord(c) - 96
    score *= i + 1
    scores.append(score)

print sum(scores)
