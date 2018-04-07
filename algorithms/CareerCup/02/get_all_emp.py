def get_all_team_mates(boss, myCmp):
    allMates = set()

    if boss not in myCmp:
        return allMates

    currentLevel = [boss]

    while currentLevel:
        nextLevel = []
        for node in currentLevel:
            for mates in myCmp[node]:
                allMates.add(mates)
                if mates in myCmp:
                    nextLevel.append(mates)
        currentLevel = nextLevel

    return allMates

if __name__ == '__main__':
    myCmp = {
        1:[2,3,4],
        3:[5,6,7],
        5:[8,9,10]
    }

    print get_all_team_mates(2, myCmp)