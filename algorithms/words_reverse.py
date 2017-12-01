def words_reverse(myStr):
    for i in myStr.split(' '):
        yield i[::-1]

if __name__ == '__main__':
    myStr = 'my name is Pramod'
    print ' '.join(list(words_reverse(myStr)))

