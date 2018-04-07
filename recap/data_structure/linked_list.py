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
            raise ValueError('Linked List is empty')
        node = self.head
        last = None

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
        val = self.head.value
        self.head = self.head.next
        return val

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
    ll.add(11)
    ll.add(12)
    ll.add(13)
    ll.add(14)
    print ll
    print ll.pop()
    print ll

    node = ll.head

    print_reverse(node)
