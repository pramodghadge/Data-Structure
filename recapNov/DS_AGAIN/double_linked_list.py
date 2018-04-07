class LinkedNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None


    def add(self, value):
        newNode = LinkedNode(value)
        if self.head is None:
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def pop(self):
        value = self.head.value
        self.head = self.head.next
        return value

    def remove(self, target):
        node = self.head
        last =None

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

    def __iter__(self):
        node = self.head

        while node:
            yield node.value
            node = node.next

    def __repr__(self):
        return 'Linked List:['+ ','.join(map(str, self)) + ']'


if __name__ == '__main__':
    ll = LinkedList()
    ll.add(10)
    ll.add(20)
    ll.add(30)
    print ll
    print ll.remove(10)
    print ll
