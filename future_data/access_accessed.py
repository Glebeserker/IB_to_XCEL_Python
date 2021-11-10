import pyodbc

from ibapi.contract import Contract

#List to be used for data
dateList = []
realList = []
contractLists = []
#Establishing connection with MS Access Database
conn_str = (r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            r'DBQ=C:\IB-Script\Access_Data\MARKET2.accdb;')
conn = pyodbc.connect(conn_str)

cursor = conn.cursor()

#SQL COMMAND
sql = "select LastTradingDate from qVixFutures"
cursor.execute(sql)

#parseing through request to be stored and adjusted so data saved is a list of strings
for row in cursor.fetchall():
    realList.clear()
    dateList.append(str(row))
    for item in dateList:
        realList.append(item[2:10])

#Closing connection
cursor.close()
conn.close()
print('connection closed')

print(realList)

#Clearing the list for each time it is called up so there are no repeated dates        
contractLists.clear()        
#Function that creates a Contract
def ContractMaker(date, secType = 'FUT', currency="USD", exchane='CFE', symbol = 'VXK1', tradingClass = 'VX'):
    contrac = Contract()
    contrac.symbol = symbol
    contrac.secType = secType
    contrac.currency = currency
    contrac.exchange = exchane
    contrac.tradingClass = tradingClass
    contrac.lastTradeDateOrContractMonth = date
    return contrac
#Add objects to list to be used in future manipulation
for date in realList:
    contractLists.append(ContractMaker(date))
