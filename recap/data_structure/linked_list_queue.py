class LinkedNode(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, value):
        node = LinkedNode(value, None)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def remove(self, target):
        if self.head is None:
            raise ValueError('Linked List is empty')
        last = None
        node = self.head
        while node:
            if target == node.value:
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
        node = self.head
        while node:
            yield node.value
            node = node.next

    def __repr__(self):
        return 'LinkedList:['+','.join(map(str,self))+']'

def print_reverse(node):
    if node is None:
        return
    print_reverse(node.next)
    print node.value


if __name__ == '__main__':
    ll = LinkedList()
    ll.add(10)
    ll.add(12)
    print ll
    print ll.pop()
    ll.add(14)
    ll.add(16)
    print ll
    ll.remove(14)
    print ll

    ll.add(17)
    ll.add(18)
    print ll
    print_reverse(ll.head)