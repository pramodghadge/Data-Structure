'''
Returns the zero based index of the first occurrence of any character of str2 in str1
Inp0ut:
str1="adf6ysh"
str2="123678"

output: 3
'''

def findfirstoccurenceIndex(mystr1, mystr2):
    mySet = set(mystr1)
    for i,v in enumerate(mystr2):
        if v in mySet:
            return i

if __name__ == '__main__':
    str1 = "adf6ysh"
    str2 = "123678"
    print findfirstoccurenceIndex(str1,str2)