from string import punctuation

s = ''.join(input().split())
specials = str()
numbers = str()
forbid = punctuation
i = 0
while i < len(s):
    if s[i] in forbid or s[i].isdigit():
        if s[i].isdigit():
            numbers += s[i]
        else:
            specials += s[i]
        s = s.replace(s[i], '', 1)
        i-=1
    i+=1
print(specials + ''.join(sorted(numbers)) + ''.join(sorted(s, key=lambda a:a.lower())))