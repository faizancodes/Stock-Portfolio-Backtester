
#https://www.red-gate.com/simple-talk/sql/bi/historical-stock-prices-volumes-python-csv-file/

import pandas_datareader as web
import datetime
import math
import matplotlib.pyplot as plt
import numpy as np
import numpy.random as nrand
import csv

startMonth = 5
startDay = 1
startYear = 2018

endMonth = 3
endDay = 9
endYear = 2020

start = datetime.datetime(startYear, startMonth, startDay)
end = datetime.datetime(endYear, endMonth, endDay)

accValue = 10000
startingCapital = accValue
capitalInStocks = 0


def testPortfolios():

    #stocks = [('MSFT', 10), ('AAPL', 10), ('PYPL', 10), ('V', 10), ('SBUX', 10), ('O', 10), ('DPK', 7), ('SPXU', 7), ('TWM', 8), ('SQQQ', 8)]

    '''
    stocks = [['AFL', 10], ['AJG', 10], ['AWK', 10], ['BAH', 10], ['BFAM', 10], 
            ['ELS', 10], ['GIB', 10], ['NEE', 10], ['RSG', 5], ['SBAC', 5], ['SUI', 5], ['QID', 5]]
    '''

    '''
    stocks = [['MSFT', 10], ['V', 10], ['PYPL', 10], ['SBUX', 10], ['WM', 10], 
            ['AMT', 10], ['ERUS', 10], ['GLD', 10], ['TMF', 5], ['VCLT', 5], ['UBT', 5], ['QID', 5]]
    '''

    '''
    stocks = [['MSFT', 8], ['V', 8], ['PYPL', 8], ['SBUX', 8], ['WM', 8], 
            ['AMT', 8], ['COST', 8], ['DIS', 8], ['ERUS', 8], ['GLD', 8], ['TMF', 5], ['VCLT', 5], ['UBT', 5], ['QID', 5]]
    '''

    '''
    stocks = [['TWTR', 10], ['NFLX', 15], ['FB', 10], ['BAC', 10], ['NVDA', 15], 
            ['MSFT', 10], ['JPM', 15], ['V', 15]]
    '''

    '''
    stocks = [['KO', 20], ['JNJ', 20], ['PG', 20], ['VZ', 15], ['AMT', 10], 
            ['WM', 10], ['QID', 5]]
    '''

    '''
    stocks = [['QQQ', 25], ['KBWP', 10], ['EDV', 10], ['XLRE', 10], ['GLD', 10], 
            ['TYD', 10],  ['VCLT', 10], ['ERUS', 10], ['QID', 5]]
    '''

    '''
    stocks = [['SBUX', 20], ['QQQ', 15], ['COST', 15], ['NVDA', 5], ['TCEHY', 10], 
            ['WM', 10],  ['MSG', 5], ['JNK', 5], ['VWOB', 5], ['LQD', 5], ['GLD', 5]]
    '''

    '''
    stocks = [['MSFT', 10], ['AAPL', 10], ['PYPL', 10], ['V', 10], ['SBUX', 10], ['O', 10], 
            ['NKE', 10], ['MA', 10], ['STOR', 10], ['QID', 10]]
    '''

    '''
    stocks = [['MSFT', 8], ['V', 8], ['PYPL', 7], ['SBUX', 7], ['COST', 6], ['WM', 7], 
            ['DIS', 6], ['AMT', 7], ['VRSK', 5], ['TWLO', 5], ['GLD', 5], ['TMF', 5], ['BTAL', 5], ['ZROZ', 5], ['TSLA', 4], ['ERUS', 5], ['YUM', 5]]
    '''

    '''
    stocks = [['MSFT', 9.09], ['AMT', 9.09], ['PYPL', 9.09], ['V', 9.09], ['SBUX', 9.09], ['YUM', 9.09], 
            ['NKE', 9.09], ['WM', 9.09], ['DIS', 9.09], ['TMF', 9.09], ['BTAL', 9.09]]
    '''

    '''
    stocks = [['MSFT', 8], ['WM', 7], ['PYPL', 7], ['V', 8], ['SBUX', 8], ['AMT', 7], 
            ['COST', 6], ['YUM', 5], ['DIS', 6], ['ERUS', 5], ['TMF', 5], ['BTAL', 5], ['GLD', 5], ['ZROZ', 4], ['TWLO', 5], ['VRSK', 5], ['TSLA', 4]]
    '''

    '''
    stocks = [['MSFT', 9], ['V', 9], ['SBUX', 9], ['DIS', 7], ['TWLO', 8], ['PYPL', 9], 
            ['GDXJ', 9], ['BTAL', 35], ['ERUS', 5]]
    '''

    '''
    stocks = [['APD', 6.25], ['ECL', 6.25], ['BLL', 6.25], ['EL', 6.25], ['AJG', 6.25], ['ELS', 6.25], 
            ['STE', 6.25], ['ZTS', 6.25], ['DHR', 6.25], ['WM', 6.25], ['FISV', 6.25], ['YUM', 6.25], ['SNPS', 6.25], ['MSFT', 6.25], ['WEC', 6.25], ['AWR', 6.25]]
    '''


    '''
    stocks = [['MSFT', 5], ['AAPL', 9.19], ['V', 20], ['SBUX', 19.82], ['DIS', 16.11], ['JPM', 5], ['UNH', 19.88], ['KO', 5]]
    '''

    '''
    stocks = [['MSFT', 5], ['COST', 5], ['V', 12.58], ['SBUX', 12.68], ['DIS', 5], ['JPM', 5], ['KO', 5], ['NKE', 5], ['STOR', 15], ['TLT', 14.73], ['BTAL', 15]]
    '''


stocks = [['MSFT', 6], ['V', 6], ['PYPL', 4], ['SBUX', 7], ['COST', 6], ['DIS', 5], ['NEE', 5], ['BTC-USD', 5],
          ['WM', 6], ['AMT', 6], ['VRSK', 4], ['TWLO', 4], ['TSLA', 4], ['GLD', 6], ['TMF', 4], ['BTAL', 5], ['ZROZ', 4], ['ERUS', 4], ['YUM', 5], ['DG', 4]]


purchaseCosts = []
dates = []
bitC = 1


for x in range(len(stocks)):
    
    if stocks[x][0] == 'BTC-USD':
        end = datetime.datetime(endYear, endMonth, endDay + 1)

    df = web.DataReader(stocks[x][0], 'yahoo', start, end)
    path_out = 'C:\\Users\\faiza\\OneDrive\\Desktop\\pyTest\\'
    df.to_csv(path_out + '$' + stocks[x][0] + '.txt')
    classFile = open("C:\\Users\\faiza\\OneDrive\\Desktop\\pyTest\\$" + stocks[x][0] + '.txt', "r")
    closes = []

    for line in classFile:
        if x == 1:
            dates.append(line[0 : line.find(',')])
        adjClose = line
        for y in range(6):
            adjClose = adjClose[adjClose.find(',') + 1 : ]
        
        closes.append(adjClose.strip())

    if stocks[x][0] == 'BTC-USD':
        sharesPurchased = (accValue * (stocks[x][1] / 100)) / float(closes[1])
        purchaseCosts.append([sharesPurchased, sharesPurchased * float(closes[1])])
        capitalInStocks += sharesPurchased * float(closes[1])
        bitC = 2
    else:
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

end = datetime.datetime(endYear, endMonth, endDay)

df = web.DataReader('SPY', 'yahoo', start, end)
path_out = 'C:\\Users\\faiza\\OneDrive\\Desktop\\pyTest\\'
df.to_csv(path_out + '$' + 'SPY' + '.txt')
classFile = open("C:\\Users\\faiza\\OneDrive\\Desktop\\pyTest\\$" + 'SPY' + '.txt', "r")


##Get SPY Prices

spy = []
spyDates = []
perDiff = []

for line in classFile:
    adjClose = line
    for y in range(6):
        adjClose = adjClose[adjClose.find(',') + 1 : ]

    spy.append(adjClose.strip())
    spyDates.append(line[0 : line.find(',')])
 

##Get SQQQ Prices

classFile = open("C:\\Users\\faiza\\OneDrive\\Desktop\\pyTest\\$" + 'QID' + '.txt', "r")
spxu = []

for line in classFile:
    adjClose = line
    for y in range(6):
        adjClose = adjClose[adjClose.find(',') + 1 : ]
    
    spxu.append(adjClose.strip())


#Remove Extra Days for BTC Prices

classFileBTC = open("C:\\Users\\faiza\\OneDrive\\Desktop\\pyTest\\$BTC-USD.txt", "r")
rawBTC = []
btc = []

for line in classFileBTC:
    adjClose = line
    
    for y in range(6):
        adjClose = adjClose[adjClose.find(',') + 1 : ]

    rawBTC.append([line[0 : line.find(',')], adjClose.strip()])

for x in range(len(rawBTC)):
    if rawBTC[x][0] in spyDates:
        btc.append(rawBTC[x][1])
        
counter = 3
diff = 0
totalProfit = []
z = 0

def getSMA(data, period):
    
    summ = 0
    for x in range(len(data) - period, len(data)):
        summ += float(data[x])

    return summ / period


for f in range(len(spy)):

    dailyProfit = []

    for x in range(len(stocks)):
        
        classFile = open("C:\\Users\\faiza\\OneDrive\\Desktop\\pyTest\\$" + stocks[x][0] + '.txt', "r")
        closes2 = []
        
        for line in classFile:
            adjClose = line
            for y in range(6):
                adjClose = adjClose[adjClose.find(',') + 1 : ]
            
            closes2.append(adjClose.strip())
        
        
        smaDownCross = 50
        smaUpCross = 50

        '''
        #Reconfigure long/short positions 

        if f >= smaDownCross and x < 8 and float(closes2[counter - 1]) < getSMA(closes2, smaDownCross):
            
            if stocks[x][1] > 5 and stocks[len(stocks) - bitC][1] < 15:
                
                stocks[x][1] = stocks[x][1] - 1
                stocks[len(stocks) - bitC][1] = stocks[len(stocks) - bitC][1] + 1

                sharesToSell = math.floor((0.01 * accValue) / float(closes2[counter - 1]))
                purchaseCosts[x][0] -= sharesToSell
                purchaseCosts[x][1] = purchaseCosts[x][1] - (sharesToSell * float(closes2[counter - 1]))

                sharesToBuy = math.floor((0.01 * accValue) / float(spxu[counter - 1]))
                purchaseCosts[len(stocks) - bitC][0] += sharesToBuy
                purchaseCosts[len(stocks) - bitC][1] = purchaseCosts[len(stocks) - bitC][1] + (sharesToBuy * float(spxu[counter - 1]))

        elif f >= smaUpCross and x < 8 and float(closes2[counter - 1]) > getSMA(closes2, smaUpCross):
            
            if stocks[x][1] < 10 and stocks[len(stocks) - bitC][1] > 5:  
                
                stocks[x][1] = stocks[x][1] + 1
                stocks[len(stocks) - bitC][1] = stocks[len(stocks) - bitC][1] - 1

                sharesToSell = math.floor((0.01 * accValue) / float(spxu[counter - 1]))
                purchaseCosts[len(stocks) - bitC][0] -= sharesToSell
                purchaseCosts[len(stocks) - bitC][1] = purchaseCosts[len(stocks) - bitC][1] - (sharesToSell * float(spxu[counter - 1]))

                sharesToBuy = math.floor((0.01 * accValue) / float(closes2[counter - 1]))
                purchaseCosts[x][0] += sharesToBuy
                purchaseCosts[x][1] = purchaseCosts[x][1] + (sharesToBuy * float(closes2[counter - 1]))

        '''

        if stocks[x][0] == 'BTC-USD':
            try:
                diff = (purchaseCosts[x][0] * float(btc[counter - 1])) - (purchaseCosts[x][1])
                dailyProfit.append(diff)
            except:
                print()
        else:
            diff = (purchaseCosts[x][0] * float(closes2[counter - 1])) - (purchaseCosts[x][1])
            dailyProfit.append(diff)


    counter += 1
    profitSum = 0

    for num in dailyProfit:
        profitSum += num

    totalProfit.append([profitSum, ((totalCapital + profitSum) - totalCapital) / totalCapital * 100])

    if counter > len(spy):
        break


dates2 = []
spyReturns2 = []
portfolioReturns2 = []
allData = []
spyR = []
portReturnsAnalysis = []
spyReturnsAnalysis = []

portfolioReturns2.append(0)
portReturnsAnalysis.append(0)


def portfolioReturns():
    
    '''
    for x in range(len(totalProfit)):
        print(accValue + totalProfit[x][0])
    print()
    '''

    for x in range(len(totalProfit)):
        #print(str(totalProfit[x][1]) + '%')
        portfolioReturns2.append(totalProfit[x][1])
        portReturnsAnalysis.append(totalProfit[x][1])

    print()


def spyReturns():

    global spyR

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
            print('')

    for x in range(len(spy)):
        perDiff.append((spy[x] - spy[0]) / spy[0] * 100)

    for num in perDiff:
        #print(str(num) + '%')
        spyR.append(str(num) + '%')
        spyReturns2.append(num)
        spyReturnsAnalysis.append(num)

    print()


def printDates():
    
    for date in dates:
        #print(date)
        
        dates2.append(date)

    print()


def printCode():
    
    for x in range(len(dates) - 1):
        allData.append([dates2[x], portfolioReturns2[x], spyReturns2[x]])

    for x in range(len(allData)):
        print("['" + str(allData[x][0]) + "', " + str(allData[x][1]) + ", "  + str(allData[x][2]) + "],")
    

def vol(returns):
    return np.std(returns)


def beta(returns, market):
    m = np.matrix([returns, market])
    return np.cov(returns, market)[0][1]/np.var(market)


def sharpe(returns, rf):
    volatility = returns.std()
    sharpe_ratio = (returns.mean() - rf) / volatility
    return sharpe_ratio


def treynorRatio(er, returns, market, rf):
    denom = beta(returns, market)
    return (er - rf) / denom


def prices(returns, base):
    # Converts returns into prices
    s = [base]
    for i in range(len(returns)):
        s.append(base * (1 + returns[i]))
    return np.array(s)


def dd(returns, tau):
    # Returns the draw-down given time period tau
    values = prices(returns, 100)
    pos = len(values) - 1
    pre = pos - tau
    drawdown = float('+inf')
    # Find the maximum drawdown given tau
    while pre >= 0:
        dd_i = (values[pos] / values[pre]) - 1
        if dd_i < drawdown:
            drawdown = dd_i
        pos, pre = pos - 1, pre - 1
    # Drawdown should be positive
    return abs(drawdown)


def average_dd_squared(returns, periods):
    # Returns the average maximum drawdown squared over n periods
    drawdowns = []
    for i in range(0, len(returns)):
        drawdown_i = math.pow(dd(returns, i), 2.0)
        drawdowns.append(drawdown_i)

    drawdowns = sorted(drawdowns)
    total_dd = abs(drawdowns[0])

    for i in range(1, periods):
        total_dd += abs(drawdowns[i])

    return total_dd / periods


def burkeRatio(er, returns, rf, periods):
    return (er - rf) / math.sqrt(average_dd_squared(returns, periods))


def informationRatio(returns, benchmark):
    diff = returns - benchmark
    return np.mean(diff) / vol(diff)


def lpm(returns, threshold, order):
    # This method returns a lower partial moment of the returns
    # Create an array he same length as returns containing the minimum return threshold
    threshold_array = np.empty(len(returns))
    threshold_array.fill(threshold)
    # Calculate the difference between the threshold and the returns
    diff = threshold_array - returns
    # Set the minimum of each to 0
    diff = diff.clip(min=0)
    # Return the sum of the different to the power of order
    return np.sum(diff ** order) / len(returns)


def omegaRatio(er, returns, rf, target=0):
    
    if lpm(returns, target, 1) == 0:
        return 20000

    return float((er - rf) / lpm(returns, target, 1))



printDates()

spyReturns()

portfolioReturns()


print(purchaseCosts)
print()
print(stocks)
print()


i = np.argmax(np.maximum.accumulate(portReturnsAnalysis) - portReturnsAnalysis) # end of the period
j = np.argmax(portReturnsAnalysis[:i]) # start of period

k = np.argmax(np.maximum.accumulate(spyReturnsAnalysis) - spyReturnsAnalysis) # end of the period
l = np.argmax(spyReturnsAnalysis[:k]) # start of period

portfolioMaxDrawdown = portReturnsAnalysis[j] - portReturnsAnalysis[i]
spyMaxDrawdown = spyReturnsAnalysis[l] - spyReturnsAnalysis[k]

betaCalc = beta(np.asarray(portReturnsAnalysis), np.asarray(spyReturnsAnalysis))
alpha = portReturnsAnalysis[len(portReturnsAnalysis) - 1] - (0.6 + betaCalc * (spyReturnsAnalysis[len(spyReturnsAnalysis) - 1] - 0.6))
sharpeRatio = sharpe(np.asarray(portReturnsAnalysis), 0.6)

e = np.mean(np.asarray(portReturnsAnalysis))
treynorR = treynorRatio(e, np.asarray(portReturnsAnalysis), np.asarray(spyReturnsAnalysis), 0.6)

burkeR = burkeRatio(e, np.asarray(portReturnsAnalysis), 0.6, 5)
infR = informationRatio(np.asarray(portReturnsAnalysis), np.asarray(spyReturnsAnalysis))

omgRatio = (omegaRatio(e, np.asarray(portReturnsAnalysis), 0.6)) / 200

portfolioRating = (((spyMaxDrawdown - portfolioMaxDrawdown) * 10) + (alpha * 10) - (betaCalc * 5) + (sharpeRatio * 5) + (infR * 5) + (omgRatio * 10) + (treynorR * 10) + (burkeR / 100)) / 100 * 5


print('Portfolio Max Drawdown:', str(portfolioMaxDrawdown) + '%')
print('SPY Max Drawdown:', str(spyMaxDrawdown) + '%')
print('Beta:', betaCalc)
print('Alpha:', alpha)
print('Sharpe Ratio:', sharpeRatio)
print('Information Ratio:', infR)
print('Omega Ratio:', omgRatio)
print('Treynor Ratio:', treynorR)
print('Burke Ratio:', burkeR)
print('Portfolio Rating:', portfolioRating)

#printCode()


with open('C:\\Users\\faiza\\OneDrive\\Desktop\\StockData\\2020Portfolio.csv', 'w') as f:
    
    for x in range(len(dates)):
        
        if x == 0:
            f.write('Date,Account Value,SPY Returns,Portfolio Returns' + '\n')
        elif x == 1:
            f.write(dates[x] + ',' + str(startingCapital) + ',' + spyR[x - 1] + ',' + '0%' + '\n')
        else:
            f.write(dates[x] + ',' + str(accValue + totalProfit[x - 2][0]) + ',' +  spyR[x - 1] + ',' + str(totalProfit[x - 2][1]) + '%' + '\n') 
    
    f.write('\n\n\n')
    f.write('Stock, Percentage of Portfolio\n')

    for x in range(len(stocks)):
        f.write(stocks[x][0] + ',' + str(stocks[x][1]) + '%\n')

    f.write('\n\n')
    f.write('Max Drawdown For Portfolio, ' + str(portfolioMaxDrawdown) + '%\n')
    f.write('Max Drawdown For SPY, ' + str(spyMaxDrawdown) + '%')

    f.write('\nBeta,' + str(betaCalc))
    f.write('\nAlpha,' + str(alpha))
    f.write('\nSharpe Ratio,' + str(sharpeRatio))
    f.write('\nInformation Ratio,' + str(infR))
    f.write('\nOmega Ratio,' + str(omgRatio))
    f.write('\nTreynor Ratio,' + str(treynorR))
    f.write('\nBurke Ratio,' + str(burkeR))
    f.write('\nPortfolio Rating,' + str(portfolioRating))
