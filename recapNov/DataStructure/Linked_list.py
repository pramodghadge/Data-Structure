class LinkedNode(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList(object):
    def __init__(self):
        self.head = None

    def add(self, val):
        self.head = LinkedNode(val, self.head)

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
        return 'Linked List:[' +','.join(map(str,self))+']'


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



if __name__ == '__main__':
    ll = LinkedList()
    print ll

    ll.add(2)
    ll.add(3)
    ll.add(4)
    ll.add(5)

    print ll

    ll.remove(3)

    print ll
    ll.remove(5)
    print ll
    ll.add(10)
    ll.add(12)
    print ll
    print ll.checkInfinite()
    print ll.pop()
    print ll