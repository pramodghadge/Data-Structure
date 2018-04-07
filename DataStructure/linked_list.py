class LinkedNode(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList(object):
    def __init__(self):
        self.head = None

    def add(self, value):
        self.head = LinkedNode(value, self.head)

    def remove(self, target):
        if self.head is None:
            raise ValueError('Linked list is empty')

        node = self.head
        last = None
        while node:
            if node.value == target:
                if last is None:
                    self.head = self.head.next
                else:
                    last.next = node.next
                return True
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

    def __repr__(self):
        return 'LinkedList:['+','.join(map(str, self))+']'


if __name__ == '__main__':
    l = LinkedList()
    print l
    l.add(10)
    l.add(11)
    l.add(12)
    print l
    l.remove(11)
    print l
    print l.pop()
    print l
    print l.pop()
    print l
