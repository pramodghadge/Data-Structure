def grep(line):
    while True:
        myString = yield
        if myString in line:
            yield myString
        else:
            yield 'Nothing'

if __name__ == '__main__':
    line = 'My name is Pramod'
    buffer = grep(line)
    buffer.next()
    for i in ['My', 'name', 'is','Pramod', 'Ghadge']:
        print buffer.send(i)

