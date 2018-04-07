class LinkedNode(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList(object):
    def __init__(self):
        self.head = None

    def add(self, value):
        self.head = LinkedNode(value, self.head)
        return True

    def remove(self, target):
        node = self.head
        last = None
        while node:
            if node.value == target:
                if last is None:
                    self.head = self.head.next
                else:
                    last.next = node.next
                return True
            else:
                last = node
                node = node.next
        return False

    def pop(self):
        value = self.head.value
        self.head = self.head.next
        return value

    def __iter__(self):
        node =self.head
        while node:
            yield node.value
            node = node.next

    def __repr__(self):
        return 'Linked List:[' + ','.join(map(str, self)) + ']'

def printReverse(node):
    if not node:
        return
    printReverse(node.next)
    print node.value

def checkloop(node):
    p1 = p2 = node
    while p1 is not None and p2 is not None:
        if p2.next is None:
            return False
        p1 = p1.next
        p2 = p2.next.next
        if p1 == p2:
            return True
    return False

if __name__ == '__main__':
    ll = LinkedList()
    ll.add(4)
    ll.add(6)
    ll.add(9)
    # print ll.pop()
    # print ll.remove(4)
    print ll
    printReverse(ll.head)
    print checkloop(ll.head)