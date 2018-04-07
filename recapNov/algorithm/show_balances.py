def show_balance(daily_balance):

    noofDays = len(daily_balance)
    for day in range(noofDays-3, noofDays-1):
        print day, day+2
        balance_slice  = daily_balance[day: day+2]

        days_ago = noofDays - day
        print "slice starting %d days ago: %s" % (abs(days_ago), balance_slice)

if __name__ == '__main__':
    daily_balances = [107.92, 108.67, 109.86, 110.15]
    show_balance(daily_balances)