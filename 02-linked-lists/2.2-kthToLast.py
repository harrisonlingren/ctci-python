from LinkedList import LinkedList

def kthToLast(LL, k):
    size = len(LL)

    # sanity check
    if k > size:
        print('error: %s is larger than the list size' % k)
        return

    # search for value
    n = LL.getHead()
    for _ in range(0, size-k):
        if n.hasNext():
            n = n.getNext()

    return n.getVal()

_ll = LinkedList()

listSize = int(input('size of list:  '))
for _ in range(0,listSize):
    _ll.add(int(input('next number to add:  ')))

kth = int(input('element (from last) to check for:  '))
print('%s element from last: %s' % (kth, kthToLast(_ll, kth)))
