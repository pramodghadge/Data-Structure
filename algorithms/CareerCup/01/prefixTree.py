class PreFixTree(object):
    def __init__(self):
        self.d = dict()

    def add(self, name, number):
        d = self.d

        for i in name:
            if i not in d:
                d[i] = dict()
            d = d[i]

        if 'CellNumber' in d:
            d['CellNumber'].append(number)
        else:
            d['CellNumber'] = [number]

    def get_Number(self, name):
        d = self.d

        for i in name:
            if i not in d:
                return 0
            else:
                d = d[i]

        if 'CellNumber' not in d:
            return 0
        else:
            return d['CellNumber']



if __name__ == '__main__':
    t = PreFixTree()
    t.add("Pramod Ghadge", '732-762-4434')
    t.add("Priyanka Ghadge", '732-889-1322')

    print t.get_Number("Priyanka Ghadge")