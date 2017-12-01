class LinkedNode(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, value):
        node = LinkedNode(value)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def remove(self, target):
        if self.head is None:
            return False

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
        if self.head is None:
            raise ValueError('Linked list is empty')

        value = self.head.value
        self.head = self.head.next
        return value

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

    def checkInfinite(self):
        p1 = p2 = self.head
        while p1 != None and p2 != None:
            if p2.next == None:
                return False
            p1 = p1.next
            p2 = p2.next.next

            if p1 == p2:
                return True
        return False



    def __repr__(self):
        return 'LinkedList:['+','.join(map(str, self))+']'

if __name__ == '__main__':
    l = LinkedList()
    l.add(10)
    l.add(11)
    print(l)
    l.remove(10)
    print l
    l.add(10)
    print l
    print l.pop()
    print l
    print l.checkInfinite()