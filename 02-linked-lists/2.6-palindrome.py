from Stack import Stack
from LinkedList import LinkedList

def palindrome(LL):
    checker = Stack()

    n = LL.getHead().getNext()
    while n.hasNext():
        checker.push(n.getVal())
        n = n.getNext()

    checker.push(n.getVal())

    n = LL.getHead().getNext()
    while not checker.isEmpty() and n.hasNext():
        if n.getVal() != checker.pop():
            return False
        n = n.getNext()
    return True

_ll = LinkedList()

listSize = int(input('size of list:  '))
for _ in range(0,listSize):
    _ll.add(int(input('next number to add:  ')))

print(palindrome(_ll))
