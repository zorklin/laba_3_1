string = "Це приклад довгого рядка з багатьма словами"
words = string.split()

result = []
for word in words:
    if len(word) > 1:
        result.append((word[1], word[-2]))
print(result)