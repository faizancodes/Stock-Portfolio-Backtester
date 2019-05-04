
#https://www.red-gate.com/simple-talk/sql/bi/historical-stock-prices-volumes-python-csv-file/

import pandas_datareader as web
import datetime
import math

start = datetime.datetime(2018, 1, 1)
end = datetime.datetime(2019, 4, 1)

accValue = 10000
capitalInStocks = 0
#stocks = [('MSFT', 10), ('AAPL', 10), ('PYPL', 10), ('V', 10), ('SBUX', 10), ('O', 10), ('DPK', 7), ('SPXU', 7), ('TWM', 8), ('SQQQ', 8)]
stocks = [['MSFT', 10], ['AAPL', 10], ['PYPL', 10], ['V', 10], ['SBUX', 10], ['O', 10], ['NKE', 10], ['MA', 10], ['STOR', 10], ['SPXU', 10]]

purchaseCosts = []
dates = []

for x in range(len(stocks)):
    df = web.DataReader(stocks[x][0], 'yahoo', start, end)
    path_out = 'C:\\Users\\faiza\\OneDrive\\Desktop\\pyTest\\'
    df.to_csv(path_out + '$' + stocks[x][0] + '.txt')
    classFile = open("C:\\Users\\faiza\\OneDrive\\Desktop\\pyTest\\$" + stocks[x][0] + '.txt', "r")
    closes = []

    for line in classFile:
        dates.append(line[0 : line.find(',')])
        adjClose = line
        for y in range(6):
            adjClose = adjClose[adjClose.find(',') + 1 : ]
        
        closes.append(adjClose.strip())
            
    sharesPurchased = math.floor(((stocks[x][1] / 100) * accValue) / float(closes[1]))
    purchaseCosts.append([sharesPurchased, sharesPurchased * float(closes[1])])
    capitalInStocks += sharesPurchased * float(closes[1])

cash = accValue - capitalInStocks
totalCapital = cash + capitalInStocks
portfolioValue = totalCapital

print(purchaseCosts)
print('Total Capital: $' + str(totalCapital))
print('Capital in Stocks: $' + str(capitalInStocks))
print()

classFile = open("C:\\Users\\faiza\\OneDrive\\Desktop\\pyTest\\$" + 'SPY' + '.txt', "r")
spy = []
perDiff = []

for line in classFile:
    adjClose = line
    for y in range(6):
        adjClose = adjClose[adjClose.find(',') + 1 : ]

    spy.append(adjClose.strip())
 
classFile = open("C:\\Users\\faiza\\OneDrive\\Desktop\\pyTest\\$" + 'SPXU' + '.txt', "r")
spxu = []

for line in classFile:
    adjClose = line
    for y in range(6):
        adjClose = adjClose[adjClose.find(',') + 1 : ]
    
    spxu.append(adjClose.strip())

counter = 3
diff = 0
totalProfit = []
z = 0

def getSMA(data, period):
    summ = 0
    for x in range(len(data) - period, len(data)):
        summ += float(data[x])

    return summ / period


for f in range((len(closes))):

    dailyProfit = []

    for x in range(len(stocks)):
        
        classFile = open("C:\\Users\\faiza\\OneDrive\\Desktop\\pyTest\\$" + stocks[x][0] + '.txt', "r")
        closes2 = []
        
        for line in classFile:
            adjClose = line
            for y in range(6):
                adjClose = adjClose[adjClose.find(',') + 1 : ]
            
            closes2.append(adjClose.strip())
        
        
        #Reconfigure long/short positions 

        if f >= 12 and x < 9 and float(closes2[counter - 1]) < getSMA(closes2, 12):
            
            if stocks[x][1] > 5 and stocks[len(stocks) - 1][1] < 25:
                
                stocks[x][1] = stocks[x][1] - 1
                stocks[len(stocks) - 1][1] = stocks[len(stocks) - 1][1] + 1

                sharesToSell = math.floor((0.01 * accValue) / float(closes2[counter - 1]))
                purchaseCosts[x][0] -= sharesToSell
                purchaseCosts[x][1] = purchaseCosts[x][1] - (sharesToSell * float(closes2[counter - 1]))

                sharesToBuy = math.floor((0.01 * accValue) / float(spxu[counter - 1]))
                purchaseCosts[len(stocks) - 1][0] += sharesToBuy
                purchaseCosts[len(stocks) - 1][1] = purchaseCosts[len(stocks) - 1][1] + (sharesToBuy * float(spxu[counter - 1]))

        elif f >= 20 and x < 9 and float(closes2[counter - 1]) > getSMA(closes2, 20):
            
            if stocks[x][1] < 11:
                
                stocks[x][1] = stocks[x][1] + 1
                stocks[len(stocks) - 1][1] = stocks[len(stocks) - 1][1] - 1

                sharesToSell = math.floor((0.01 * accValue) / float(spxu[counter - 1]))
                purchaseCosts[len(stocks) - 1][0] -= sharesToSell
                purchaseCosts[len(stocks) - 1][1] = purchaseCosts[len(stocks) - 1][1] - (sharesToSell * float(spxu[counter - 1]))

                sharesToBuy = math.floor((0.01 * accValue) / float(closes2[counter - 1]))
                purchaseCosts[x][0] += sharesToBuy
                purchaseCosts[x][1] = purchaseCosts[x][1] + (sharesToBuy * float(closes2[counter - 1]))
          
            
        diff = (purchaseCosts[x][0] * float(closes2[counter - 1])) - (purchaseCosts[x][1])
        dailyProfit.append(diff)

    counter += 1
    profitSum = 0

    #print(dailyProfit)
    #print()

    for num in dailyProfit:
        profitSum += num

    totalProfit.append([profitSum, ((totalCapital + profitSum) - totalCapital) / totalCapital * 100])

    if counter > len(closes2):
        break


def portfolioReturns():
    
    for x in range(len(totalProfit)):
        print(accValue + totalProfit[x][0])
    print()

    for x in range(len(totalProfit)):
        print(str(totalProfit[x][1]) + '%')
    print()

def spyReturns():
    
    df2 = web.DataReader('SPY', 'yahoo', start, end)
    path_out = 'C:\\Users\\faiza\\OneDrive\\Desktop\\pyTest\\'
    df2.to_csv(path_out + '$' + 'SPY' + '.txt')
    classFile = open("C:\\Users\\faiza\\OneDrive\\Desktop\\pyTest\\$" + 'SPY' + '.txt', "r")
    spy = []
    perDiff = []

    for line in classFile:
        adjClose = line
        for y in range(6):
            adjClose = adjClose[adjClose.find(',') + 1 : ]
        
        try:
            spy.append(float(adjClose.strip()))
        except:
            print('err')

    for x in range(len(spy)):
        perDiff.append((spy[x] - spy[0]) / spy[0] * 100)

    for num in perDiff:
        print(str(num) + '%')
    

portfolioReturns()
#printSPY()


print(purchaseCosts)
print()
print(stocks)


