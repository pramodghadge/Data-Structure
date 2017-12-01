def show_balances(aBalanceList, aDaysAgo):
    for i in range(-aDaysAgo,-1):
        endIdx = i + 2
        if endIdx:
            slice = str(daily_balances[i:endIdx])
        else:
            slice = str(daily_balances[i:])

        print 'slice starting {0} days ago:{1}'.format(-i, slice)



if __name__ == '__main__':
    daily_balances = [107.92, 108.67, 109.86, 110.15]
    show_balances(daily_balances,4)