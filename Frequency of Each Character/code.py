s = input("Enter string: ")

for ch in s:
    if s.index(ch) == s.rindex(ch) or s.index(ch) == s.index(ch):
        print(ch, "=", s.count(ch))
