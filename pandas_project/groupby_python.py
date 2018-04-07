
def get_mean(aList):
    return sum(aList) / len(aList)

def group_adjust(vals, groups, weights):
    countries = groups[0]
    states = groups[1]

    cities = None
    if len(groups) == 3:
        cities = groups[2]

    # countries
    # for idx, val in countries:






if __name__ == '__main__':
    pass