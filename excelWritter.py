import access_accessed
from access_accessed import contractLists, realList

#importing necessery Interactive Broker API libraries
from ibapi.client import EClient
from ibapi.wrapper import EWrapper

#Regulatory imports
import os
import threading
import datetime
import time as tm
#Pandas import
import pandas as pd
import pyodbc
import csv



#List of column names to be used in pandas for transefring to access
columnNames = ['MarketDate', 'MarketTime','ExpirationDate', 'BidSize', 'BidPrice', 'AskSize', 'AskPrice', 'LastPrice', 'LastSize', 'Volume']

#A List of numbers based on length of contractLists to be used as boolean variable to match with reqId when pulling data 
reqIdBool = list(range(len(contractLists)))

#Setting up datetime variables 
time = datetime.datetime.now()

marketTime = int(time.strftime('%H%M%S'))
marketDate = int(time.strftime('%Y%m%d'))

#Empty dataframe created
pandaFrame= pd.DataFrame(columns=columnNames)

#creating dictionaries based on dates available in access_accessed
marketData = {  id: { key: None for key in columnNames} for id in reqIdBool}


#updating Expiration Date and datetime based on date
for date in marketData:
    marketData[date]['MarketDate'] = marketDate
    marketData[date]['MarketTime'] = marketTime
    marketData[date]['ExpirationDate'] = int(realList[date])

#indexing dictionaries for reqId
index_list = []
for i in marketData:
    index_list.append(i)
     

#IB constructor class to send and recieve data
class IBapi(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)
    #Ticks for Price Values
    def tickPrice(self, reqId, tickType, price, attrib):
        #Ask price tick 
        if tickType == 67:
            #For loop to change value inside the dictionary based on index of a nested dictionary 
            for i in reqIdBool:
                if reqId == i:
                    marketData[index_list[i]]['AskPrice'] = price
                    
        #Last Price tick
        elif tickType == 68:
            for i in reqIdBool:
                if reqId == i:
                    marketData[index_list[i]]['LastPrice'] = price
                        
        #Bid Price Tick
        elif tickType == 66:
            for i in reqIdBool:
                if reqId == i:
                    marketData[index_list[i]]['BidPrice'] = price
                    
    #Ticks for size values
    def tickSize(self, reqId, tickType, size):
        
        #Bid Size
        if tickType == 69:
            for i in reqIdBool:
                if reqId == i:
                    marketData[index_list[i]]['BidSize'] = size
                    
        #Ask Size
        elif tickType == 70:
            for i in reqIdBool:
                if reqId == i:
                    marketData[index_list[i]]['AskSize'] = size
                    
        #Last Size
        elif tickType == 71:
            for i in reqIdBool:
                if reqId == i:
                    marketData[index_list[i]]['LastSize'] = size
                    
        #Volume
        elif tickType == 74:
            for i in reqIdBool:
                if reqId == i:
                    marketData[index_list[i]]['Volume'] = size

#Function to run the request for data
def run_loop():
	app.run()
 
# calling up IBAPI class instance and connecting the app to local host server
app = IBapi()
app.connect('127.0.0.1', 7497, uniqueIdentifierHere #can be any positive integer)
app.nextOrderId = 0

#Start the socket in a thread
api_thread = threading.Thread(target=run_loop, daemon=True)
api_thread.start()

#Sleep interval to allow time for connection to server
tm.sleep(1) 

# Must use correct Market Data Type
# 1) Live Data
# 2) Frozen
# 3) Delayed
# 4) Delayed Frozen
app.reqMarketDataType(3)


def MarketRequest():
    for i in reqIdBool:
        app.reqMktData(i, contractLists[i], '', False, False, [])

MarketRequest()





#Sleep interval to allow time for incoming price data
tm.sleep(1) 


# Calling disconnect, otherwise the infinite loop occurs
app.disconnect()


#Saving marketData into pandas
frame = pd.DataFrame.from_dict({(i ): marketData[i]
                        for i in marketData.keys()
                        },
                       orient='index')



print(frame)
#Writting dataframe into excel

writer = pd.ExcelWriter('marketData.xlsx')

frame.to_excel(writer)

writer.save()
print('Excel Written')
