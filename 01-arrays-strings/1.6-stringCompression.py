def stringCompression(s):
    outp = ''

    # index counters
    i = 0
    j = 0
    isBlock = True

    while i < len(s):
        isBlock = True
        while isBlock:
            if j >= len(s):
                outp += s[i] + str(j-i)
                i = j
                break
            if s[i] == s[j]:
                j += 1
            else:
                isBlock = False
                outp += s[i] + str(j-i)
                i = j
    return outp if len(outp) < len(s) else s

teststr = input('input string to compress:  ')
print(stringCompression(teststr))
