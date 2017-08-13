def checkPermutation(s1, s2):
    if len(s1) != len(s2):
        return False

    chars = {}
    for c in s1:
        if c not in chars:
            chars[c] = 0
        chars[c] += 1

    for c in s2:
        if c not in chars:
            return False
        else:
            chars[c] -= 1
            if chars[c] < 0:
                return False
    return True

str1 = input('string 1:  ')
str2 = input('string 2:  ')
print(checkPermutation(str1, str2))
