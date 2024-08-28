string = "Це приклад довгого рядка з багатьма словами"
words = string.split()
result = []
for word in words:
    if len(word) > 2:
        result.append(word[1:-1])
    else:
        result.append(word)
print(result)