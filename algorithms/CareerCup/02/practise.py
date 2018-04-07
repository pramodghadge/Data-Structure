class LinkedNode(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class DoubleLinkedList(object):
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


    def delete(self, target):
        node = self.head
        last = None
        while node is not None:
            if node.value == target:
                if last is None:
                    self.head = self.head.next
                else:
                    last,next = node.next
            else:
                last = node
                node = node.next

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node.value
            node = node.next

    def pop(self):
        val = self.head.value
        self.head = self.head.next
        return val


    def __repr__(self):
        return 'Reverse Linked List[' + ','.join(map(str,self)) + ']'

class LinkedList(object):
    def __init__(self):
        self.head = None

    def add(self, value):
        self.head = LinkedNode(value, self.head)

    def pop(self):
        if self.head is None:
            raise ValueError("Linked List is empty")
        val = self.head.value
        self.head = self.head.next
        return val

    def remove(self, target):
        node = self.head
        last= None
        while node is not None:
            val = node.value
            if val == target:
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
        while node is not None:
            yield node.value
            node = node.next

    def __repr__(self):
        return "Linked list:["+ ','.join(map(str, self)) + ']'

    def addAtEnd(self, val):
        node =self.head
        last = None
        while node is not None:
            last = node
            node = node.next

        newNode = LinkedNode(val, None)
        if last is None:
            self.head = newNode
        else:
            last.next = newNode
        return True

    def nthValue(self, n):
        if n < 0:
            return 0
        i = 0
        node = self.head
        while node is not None and i < n:
            node = node.next
            i += 1
        if node:
            return node.value
        return None

def deleteNode(node):
    while node is not None:
        previousNode = node.next
        node = None
        node = previousNode

    print node.value

def insertNthLocation(node, n, value):
    if node is None:
        return False

    idx = 0
    last = None
    while node is not None and idx < n:
        last=node
        node = node.next
        idx += 1

    if node is None:
        return False

    if last is None:
        node = LinkedNode(value, node)
        print node
    else:
        last.next = LinkedNode(value, node)

    return True

def maintainSortedList(node, value):
    last = None
    while node is not None and node.value > value:
        last = node
        node = node.next

    if last is None:
        node = LinkedNode(value, node)
    else:
        last.next = LinkedNode(value, node)

def appendList(node1, node2):
    if node1 is None and node2 is None:
        return None
    if node1 is None:
        return node2
    if node2 is None:
        return node1

    last = None
    node = node1
    while node is not None:
        last = node
        node = node.next

    last.next = node2

    return node1

def splitList(node1):
    node = node1
    p1 = node
    p2 = node
    nd1 = None
    nd2 = None
    while p2 is not None:
        nd1 = LinkedNode(p1.value, nd1)
        if p2.next is None:
            nd2 = p1.next
            break
        p1 = p1.next
        p2 = p2.next.next



    return nd1, nd2

def removeDuplication(node):
    if node is None:
        return None
    last = node
    node = node.next
    while node is not None:
        if last.value == node.value:
            tmp = node.next
            while last.value == tmp.value:
                tmp = tmp.next
            last.next = tmp
            last = tmp
            node = tmp.next
        else:
            last = node
            node = node.next

def reverseList(aNode):
    if aNode is None:
        return None

    # prev = aNode
    # curr = aNode.next
    curr = aNode
    prev = None
    while curr is not None:
        nextNode = curr.next
        curr.next = prev
        prev = curr
        curr = nextNode

    return prev
    # return aNode



if __name__ == '__main__':
    ll = LinkedList()
    ll.add(1)
    ll.add(2)
    ll.add(3)
    ll.add(5)
    # print ll.pop()
    # print ll.remove(3)
    # ll.addAtEnd(1)
    print ll
    # print ll.nthValue(1)
    # print ll
    # print insertNthLocation(ll.head, 3, 4)
    maintainSortedList(ll.head, 4)
    print ll
    # ll.deleteAllNode()
    # print ll.head.value
    # print ll.head.next.value
    # deleteNode(ll.head)
    l = LinkedList()
    l.add(5)
    l.add(4)
    l.add(3)
    l.add(2)
    print ll, l
    node = appendList(ll.head, l.head)
    # while node is not None:
    #     print node.value
    #     node = node.next


    nd1, nd2 = splitList(node)
    print 'First List'
    while nd1 is not None:
        print nd1.value
        nd1 = nd1.next

    print 'Second List'
    while nd2 is not None:
        print nd2.value
        nd2 = nd2.next

    dup = LinkedList()
    dup.add(1)
    dup.add(2)
    dup.add(3)
    dup.add(3)
    dup.add(3)
    dup.add(4)
    dup.add(5)
    print dup
    node = dup.head
    removeDuplication(node)

    print 'Reversing'
    print dup
    nd = reverseList(dup.head)
    while nd is not None:
        print nd.value
        nd = nd.next


    dl = DoubleLinkedList()
    dl.add(1)
    dl.add(2)
    dl.add(3)
    dl.add(4)
    dl.add(5)
    dl.add(6)
    print dl2
    print dl.pop()
    print dl