def clouser(myLine):
    def wrapper(myWord):
        if myWord in myLine:
            print '{0} exists'.format(myWord)
        else:
            print '{0} not exists'.format(myWord)
    return wrapper

if __name__ == '__main__':
    f = clouser('My name is Pramod')
    for i in ['My', 'name', 'is','Pramod', 'Ghadge']:
        f(i)