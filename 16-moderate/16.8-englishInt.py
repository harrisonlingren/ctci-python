def englishInt(num):
    ones = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven',
            'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    orders = ['', '', 'thousand', 'million', 'billion', 'trillion']

    isNegative = (num < 0)

    # split number into an array of chunks less than 1000
    def splitIntoChunks(n):
        numChunks = 1
        n2 = n
        while n > 1000:
            numChunks += 1
            n //= 1000

        chunks = {}
        for i in range(numChunks,0,-1):
            chunks[i-1] = n2 % 1000
            n2 //= 1000
        return chunks

    # evaluate number chunk
    def evalNum(digits):
        if len(digits) == 3:
            return evalHundred(digits)
        if len(digits) == 2:
            return evalTen(digits)
        if len(digits) == 1:
            return ones[digits[0]]
        return None

    # hundreds case
    def evalHundred(digits):
        return (ones[digits[0]] + ' ' + 'hundred ' + evalNum(digits[1:]))

    # tens case
    def evalTen(digits):
        if digits[0] == 1:
            return ones[ int(str(digits[0]) + str(digits[1])) ]
        else:
            return tens[digits[0]] + ' ' + ones[digits[1]]

    # build answer from parts

    c = splitIntoChunks(abs(num))
    order = len(c)
    englishI = ''
    for chunknum, chunk in c.items():
        d = []
        for c in str(chunk):
            d.append(int(c))

        englishI += evalNum(d)
        if order > 1:
            englishI +=  ' ' + orders[order] + ' '
        order -= 1

    if isNegative:
        englishI = 'negative ' + englishI

    return englishI

print(englishInt(int(input('number to convert:  '))))


# TODO: issues with numbers over 999,999 that contain zeros
