def recursiveMultiply(num1, num2):
    def doMultiply(n1, n2, last):
        print(n1, n2)
        if n2 == 1:
            return n1

        # TODO: does not work for odd quotients
        if n2 % 2 != 0:
            n2 -= 1
            #n1 += n2

        key = '%s, %s' % (n1, n2)
        if key not in last:
            last[key] = doMultiply(n1, n2 >> 1, last) + doMultiply(n1, n2 >> 1, last)
        return last[key]

    history = {}
    return doMultiply(num1, num2, history)


testnum1 = int(input('number 1:  '))
testnum2 = int(input('number 2:  '))
print(recursiveMultiply(testnum1, testnum2))
