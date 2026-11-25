file = open("sample.txt", "r")

text = file.read()

lines = text.splitlines()
words = text.split()
characters = len(text)

print("Lines:", len(lines))
print("Words:", len(words))
print("Characters:", characters)

file.close()
