wordSeperator = '\n'

class PreFixTree(object):
    def __init__(self):
        self.tree = {}

    def add(self, word):
        d = self.tree
        for alph in word:
            if alph not in d:
                d[alph] = {}
            d = d[alph]

        if wordSeperator in d:
            return False

        d[wordSeperator] = None
        return True

    def __contains__(self, item):
        d = self.tree
        for alph in item:
            if alph not in d:
                return False
            d = d[alph]

        return wordSeperator in d

def reverse(node):
    if not node:
        return
    childs = node.keys()
    for alph in childs:
        d = node[alph]
        reverse(d)
        print alph


if __name__ == '__main__':
    tree = PreFixTree()
    print tree.add('Pramod')
    print tree.add('Pram')
    tree.add('ant')
    # print 'Pramod' in tree
    # print tree.tree
    reverse(tree.tree)



