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
        node = self.head
        last = node
        while node:
            if node.value == target:
                if node == self.head:
                    self.head = self.head.next
                else:
                    last.next = node.next
                return True
            else:
                last = node
                node = node.next

    def pop(self):
        value = self.head.value
        self.head = self.head.next
        return value

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

    def __repr__(self):
        return 'LinkedList:['+','.join(map(str,self))+']'


def print_reverse(headNode):
    if headNode is None:
        return
    print_reverse(headNode.next)
    print headNode.value



if __name__ == '__main__':
    ll = LinkedList()
    ll.add(10)
    ll.add(12)
    ll.add(13)
    ll.add(14)
    ll.add(15)
    print ll.tail.value
    print ll.tail.next

    print ll
    ll.remove(10)
    print ll
    print_reverse(ll.head)
    # print ll.pop()

