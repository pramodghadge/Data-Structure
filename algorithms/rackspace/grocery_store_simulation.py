
class Customer(object):
    def __init__(self, cType, aTime, items):
        self.cType = cType
        self.arrivalTime = aTime
        self.holdingItems = items


    def __repr__(self):
        return "Customer Type {}, arrivalTime: {} " \
               "and holding {} items".format(self.cType,
                                             str(self.arrivalTime),
                                             str(self.holdingItems))

CashierBufferTime = 1

class Cashier(object):
    def __init__(self, isTrainer=False):
        self.isTrainer = isTrainer
        self.isOccupied = False
        self.customerCnt = 0
        self.noOfItemsToProcess = 0
        self.currentBusyTime = 0
        self.lastEventTime = 0
        self.currentEventTime = 0

    def OrderExecutionRate(self):
        return 0.5 if self.isTrainer else 1.0

    @property
    def busyTime(self):
        return self.currentBusyTime

    @busyTime.setter
    def busyTime(self, t):
        self.currentBusyTime = t

    def updateBusyTime(self):
        if not self.isOccupied:
            return
        tDiff = self.currentBusyTime - self.timeLapsed()
        if tDiff > 0 :
            self.currentBusyTime = tDiff
            self.updateLastEventTime(True)
        else:
            self.updateLastEventTime(False)

    def updateLastEventTime(self, flag=True):
        if flag:
            self.lastEventTime = self.currentEventTime


    def timeLapsed(self):
        return self.currentEventTime - self.lastEventTime


    def isTrainer(self):
        return self.isTrainer == True

    '''
    def updateCurrentBusyTime(lastArrivalTime, currentArrivalTime, currentBusyTime=0):
        if not currentBusyTime or not lastArrivalTime:
            return 0
        else:
            timeDiff = currentBusyTime-(currentArrivalTime-lastArrivalTime)
            if timeDiff > 0:
                return timeDiff
            return 0

    def updateItemCount(cashier, existingItemCnt, lastArrivalTime, currentArrivalTime):
        if not lastArrivalTime and not existingItemCnt:
            return 0
    
        timeDiff = currentArrivalTime-lastArrivalTime
        processRate=1
        if cashier == 0:
            processRate=0.5
    
    
        itemCnt = existingItemCnt - int(timeDiff * processRate)
        if itemCnt <= 0:
            return 0
        return itemCnt
    
    '''
    def updateInProcessItems(self):
        if not self.noOfItemsToProcess:
            return

        items = self.noOfItemsToProcess - int(self.timeLapsed()- self.OrderExecutionRate())
        self.noOfItemsToProcess = 0 if items <= 0 else items


    @property
    def customerCnt(self):
        return self.customerCnt

    @customerCnt.setter
    def customerCnt(self, cnt):
        self.customerCnt = cnt

    def hasActiveCustomer(self):
        return self.customerCnt is not None

    def checkOutSpeedPerItem(self):
        return 2 if self.isTrainer() else 1

    def busyFor(self):
        if self.hasActiveCustomer():
            return self.checkOutSpeedPerItem() * self.customer.holdingItems + CashierBufferTime
        else:
            return 0

    def CurrentItemCount(self):
        if self.hasActiveCustomer():
            return self.customer.holdingItems
        return 0

class GroceryStore(object):
    def __init__(self, noOfCashier):
        self.noOfCashier = noOfCashier
        self.isSomeOneInLine = False
        self.OrderQueue = []

    def isLineEmpty(self):
        return len(self.OrderQueue) == 0


    def parseFile(self):
        with open(self.fileName) as f:
            pass

def updateCustmerCount(count, cashierDict):
    cashierDict['Trainer']['currentBusyTime'] = count

# def updateCurrentBusyTime(lastArrivalTime, currentArrivalTime, noOfItems, currentBusyTime=0, isTrainer=True):
#     multiplier = 1
#     if isTrainer:
#         multiplier=2
#     t = (noOfCashiers * multiplier) - (currentArrivalTime - lastArrivalTime)
#     if not currentBusyTime:
#         return t
#     elif (currentBusyTime-t) < 0:
#         return 0
#     else:
#         return currentBusyTime-t

def updateCurrentBusyTime(lastArrivalTime, currentArrivalTime, currentBusyTime=0):
    if not currentBusyTime or not lastArrivalTime:
        return 0
    else:
        timeDiff = currentBusyTime-(currentArrivalTime-lastArrivalTime)
        if timeDiff > 0:
            return timeDiff
        return 0



def updateItemCount(cashier, existingItemCnt, lastArrivalTime, currentArrivalTime):
    if not lastArrivalTime and not existingItemCnt:
        return 0

    timeDiff = currentArrivalTime-lastArrivalTime
    processRate=1
    if cashier == 0:
        processRate=0.5


    itemCnt = existingItemCnt - int(timeDiff * processRate)
    if itemCnt <= 0:
        return 0
    return itemCnt



def updateCashiers(customerType, arrivalTime, noOfItems, cashierDict):
    '''
        update busy total time to process customer
        update current customers in line for each cashier
        update items
        choose cashier based on customer type and existing data
        update busy total time for selected cashier to process customer
        update customer count for selected cashier
        find max busy time and return

    :param customerType:
    :param arrivalTime:
    :param noOfItems:
    :param cashierDict: dict holds cashiers details and associated attributes
        currentBusyTime=0,
        lastArrivalTime=0,
        totalNumberOfItems=0,
        noOfCustomers=0
    :return:
    '''

    data = []
    #update existing data based on new event
    maxTime = 0
    for cashier in cashierDict:
        #update total number of items per cashier
        updatedItemCount= updateItemCount(
                                cashier=cashier,
                                existingItemCnt=cashierDict[cashier]['totalNumberOfItems'],
                                lastArrivalTime=cashierDict[cashier]['lastArrivalTime'],
                                currentArrivalTime=arrivalTime,
                                )

        cashierDict[cashier]['totalNumberOfItems'] = updatedItemCount
        # update busy total time for each cashier based on lastArrivalTime  and current arrival time.
        updatedBusyTime = updateCurrentBusyTime(
                lastArrivalTime = cashierDict[cashier]['lastArrivalTime'],
                currentArrivalTime = arrivalTime,
                currentBusyTime = cashierDict[cashier]['currentBusyTime']
        )
        cashierDict[cashier]['currentBusyTime'] = updatedBusyTime
        cashierDict[cashier]['lastArrivalTime'] =  arrivalTime
        # update current customers in line for each cashier
        if not updatedBusyTime:
            cashierDict[cashier]['noOfCustomers'] = 0

        data.append((updatedItemCount, cashierDict[cashier]['noOfCustomers'],updatedBusyTime, cashier))

        print "Cashier:{0}, no of items Pending is:{1}".format(cashier, updatedItemCount)

        if updatedBusyTime > maxTime:
            maxTime = updatedBusyTime

    if len(data) > 1:
        if customerType == 'A':
            data.sort(key=lambda x: x[1])
        else:
            data.sort(key=lambda x: x[0])

    favCashierDetails=data[0]
    favCashier = favCashierDetails[3]
    #noOfItems
    # update busy total time for selected cashier to process customer
    muliplier = 1
    if favCashier == 0:
        muliplier = 2
    print 'customer:{0} goes to {1}'.format(str(idx), "Trainer cashier" if not favCashier else "Experienced cashier")

    cashierDict[favCashier]['currentBusyTime'] +=  muliplier * noOfItems + 1
    cashierDict[favCashier]['totalNumberOfItems'] += noOfItems
    cashierDict[favCashier]['noOfCustomers'] += 1

    if maxTime > cashierDict[favCashier]['currentBusyTime']:
        return maxTime

    return cashierDict[favCashier]['currentBusyTime']


if __name__ == '__main__':
    fileName = 'input.txt'
    noOfCashiers = 0
    cashierDict = dict()
    with open(fileName) as f:
        for idx, row in enumerate(f):
            row = row.strip()
            # print idx, row
            if idx == 0:
                noOfCashiers = int(row)
                if noOfCashiers == 1:
                    cashierDict[idx] = dict(
                        currentBusyTime = 0,
                        lastArrivalTime = 0,
                        totalNumberOfItems = 0,
                        noOfCustomers = 0
                    )

                elif noOfCashiers > 1:
                    for idx in range(noOfCashiers):
                        cashierDict[idx] = dict(
                            currentBusyTime=0,
                            lastArrivalTime=0,
                            totalNumberOfItems=0,
                            noOfCustomers=0
                        )
            else:
                customerType, arrivalTime, noOfItems = row.split()
                totaltime = updateCashiers(customerType, int(arrivalTime), int(noOfItems), cashierDict)
                print 'Check out will be completed in {0} minutes'.format(totaltime)


