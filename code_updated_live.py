# In order for the code to work need to run setup.py found in ../TWS API/source/pythonclient
# For set up to run need to have python wheels installed on system 
# Using wheels for IBAPI can be found https://stackoverflow.com/questions/57618117/installing-the-ibapi-package answer 
# Replacing python3 in command line with just python

#importing IBAPI pythonclient components for application
from os import write
from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
#threading and time to control the process of the app and csv to write csv files
import threading
import time
import csv
# imported pandas in order to convert dictionary of price to panda and eventually to excel(in progress)
#import pandas as pd


#converting dataframe to Excel Object (commented out)
#writer = pd.ExcelWriter('demo.xlsx', engine = 'xlsxwritter')
#main_df.to_excel(writer, sheet_name='Sheet1', index=False)
#writer.save()

#creating multiple dictionaries for each month, to be latter added to a list and saved as cvs file
may_data_dictionary = {'Date': 20210519,
                       'Bid Size': 0,
                       'Bid Price': 0,
                       'Ask Size': 0,
                       'Ask Price': 0,
                       'Last Price': 0,
                       'Volume': 0}

june_data_dictionary = {'Date': 20210616,
                        'Bid Size': 0,
                        'Bid Price': 0,
                        'Ask Size': 0,
                        'Ask Price': 0,
                        'Last Price': 0,
                        'Volume': 0}

july_data_dictionary = {'Date': 20210721,
                        'Bid Size': 0,
                        'Bid Price': 0,
                        'Ask Size': 0,
                        'Ask Price': 0,
                        'Last Price': 0,
                        'Volume': 0}

august_data_dictionary = {'Date': 20210818,
                          'Bid Size': 0,
                          'Bid Price': 0,
                          'Ask Size': 0,
                          'Ask Price': 0,
                          'Last Price': 0,
                          'Volume': 0}

september_data_dictionary = {'Date': 20210915,
                             'Bid Size': 0,
                             'Bid Price': 0,
                             'Ask Size': 0,
                             'Ask Price': 0,
                             'Last Price': 0,
                             'Volume': 0}

#List to put dictionaries into
dicts = [may_data_dictionary, june_data_dictionary, july_data_dictionary, august_data_dictionary, september_data_dictionary] 

#IB constructor class to send and recieve data
class IBapi(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)
    def tickPrice(self, reqId, tickType, price, attrib):
        
        file = open('C:\IB-Script\price.txt', 'r+')
        # ask price if statement for each month
        if tickType == 2: 
            if reqId == 1:
                print('May ask price is: ', price)
                text_ask = str(price)
                may_data_dictionary['Ask Price'] = text_ask
            elif reqId == 2:
                print('June ask price is: ', price)
                text_ask = str(price)
                june_data_dictionary['Ask Price'] = text_ask
            elif reqId == 3:
                print('July ask price is: ', price)
                text_ask = str(price)
                july_data_dictionary['Ask Price'] = text_ask
            elif reqId == 4: 
                print('August ask price is: ', price)
                text_ask = str(price)
                august_data_dictionary['Ask Price'] = text_ask
            elif reqId == 5:
                print('Septemeber ask price is: ', price)
                text_ask = str(price)
                september_data_dictionary['Ask Price'] = text_ask
            else: 
                print('Incorrect reqId') 
    
        elif tickType == 4: 
            if reqId == 1:
                print('May last price was: ', price)
                text_lastPrice = str(price)
                may_data_dictionary['Last Price'] = text_lastPrice
            elif reqId == 2:
                print('June last price was: ', price)
                text_lastPrice = str(price)
                june_data_dictionary['Last Price'] = text_lastPrice
            elif reqId == 3:
                print('July last price was: ', price)
                text_lastPrice = str(price)
                july_data_dictionary['Last Price'] = text_lastPrice
            elif reqId == 4:
                print('August last price was: ', price)
                text_lastPrice = str(price)
                august_data_dictionary['Last Price'] = text_lastPrice
            elif reqId == 5:
                print('Septemeber last price was: ', price)
                text_lastPrice = str(price)
                september_data_dictionary['Last Price'] = text_lastPrice
            else:
                print('Incorrect reqId')
                

        elif tickType == 1: 
            if reqId == 1:
                print('May bid price is: ', price)
                text_bidPrice = str(price)
                may_data_dictionary['Bid Price'] = text_bidPrice
            elif reqId == 2:
                print('June bid price is: ', price)
                text_bidPrice = str(price)
                june_data_dictionary['Bid Price'] = text_bidPrice
            elif reqId == 3:
                print('July bid price is: ', price)
                text_bidPrice = str(price)
                july_data_dictionary['Bid Price'] = text_bidPrice
            elif reqId == 4:
                print('August bid price is: ', price)
                text_bidPrice = str(price)
                august_data_dictionary['Bid Price'] = text_bidPrice
            elif reqId == 5:
                print('September bid price is: ', price)
                text_bidPrice = str(price)
                september_data_dictionary['Bid Price'] = text_bidPrice
            else:
                print('Incorrect reqId')
        
        
        
    # function to call size parameters of things
    def tickSize(self, reqId, tickType, size):
        
        if tickType == 0: 
            if reqId == 1:
                print("May bid size is:", size)
                text_bidSize = str(size)
                may_data_dictionary['Bid Size'] = text_bidSize
            elif reqId == 2:
                print("June bid size is: ",size)
                text_bidSize = str(size)
                june_data_dictionary['Bid Size'] = text_bidSize
            elif reqId == 3:
                print('July bid size is: ', size)
                text_bidSize = str(size)
                july_data_dictionary['Bid Size'] = text_bidSize
            elif reqId == 4:
                print('August bid size is: ', size)
                text_bidSize = str(size)
                august_data_dictionary['Bid Size'] = text_bidSize
            elif reqId == 5:
                print('Septmeber bid size is: ', size)
                text_bidSize = str(size)
                september_data_dictionary['Bid Size'] = text_bidSize
            else: 
                print('Incorrect reqId')
                
            
        elif tickType == 3:
            if reqId == 1:
                print("May ask size is: ", size)
                text_askSize = str(size)
                may_data_dictionary['Ask Size'] = text_askSize
            elif reqId == 2:
                print('June ask size is: ', size)
                text_askSize = str(size)
                june_data_dictionary['Ask Size'] = text_askSize
            elif reqId == 3:
                print('July ask size is: ', size)
                text_askSize = str(size)
                july_data_dictionary['Ask Size'] = text_askSize 
            elif reqId == 4:
                print('August ask size is: ', size)
                text_askSize = str(size)
                august_data_dictionary['Ask Size'] = text_askSize 
            elif reqId == 5:
                print('September ask size is: ', size)
                text_askSize = str(size)
                september_data_dictionary['Ask Size'] = text_askSize
            else:
                print('Incorrect reqId')
                  
        elif tickType == 8:
            if reqId == 1:
                print("May volume is: ", size)
                text_volume = str(size)
                may_data_dictionary['Volume'] = text_volume
            elif reqId == 2:
                print('June volume is: ', size)
                text_volume = str(size)
                june_data_dictionary['Volume'] = text_volume
            elif reqId == 3:
                print('July volume is: ', size)
                text_volume = str(size)
                july_data_dictionary['Volume'] = text_volume
            elif reqId == 4:
                print('August volume is: ', size)
                text_volume = str(size)
                august_data_dictionary['Volume'] = text_volume
            elif reqId == 5:
                print('Septemeber volume is: ', size)
                text_volume = str(size)
                september_data_dictionary['Volume'] = text_volume
                
        elif tickType == 5:
            if reqId == 1:
                print("May last size was: ", size)
                text_lastSize = str(size)
                may_data_dictionary['Last Size'] = text_lastSize
            elif reqId == 2:
                print('June last size was: ', size)
                text_lastSize = str(size)
                june_data_dictionary['Last Size'] = text_lastSize
            elif reqId == 3:
                print('July last size was: ', size)
                text_lastSize = str(size)
                july_data_dictionary['Last Size'] = text_lastSize
            elif reqId == 4:
                print('August last size was: ', size)
                text_lastSize = str(size)
                august_data_dictionary['Last Size'] = text_lastSize
            elif reqId == 5:
                print('Septemeber last size was: ', size)
                text_lastSize = str(size)
                september_data_dictionary['Last Size'] = text_lastSize
        data_columns = ['Date', 'Bid Price', 'Bid Size', 'Ask Price', 'Ask Size', 'Last Price', 'Last Size', 'Volume']
        with open('C:\Ib-Script\LiveData.csv', 'r+') as ofile:
            writer = csv.DictWriter(ofile, fieldnames=data_columns)
            writer.writeheader()
            for data in dicts:
                writer.writerow(data)
        


def run_loop():
	app.run()
# calling up IBAPI class instance and connecting the app to local host server
app = IBapi()
app.connect('127.0.0.1', 7496, 136)

#Start the socket in a thread
api_thread = threading.Thread(target=run_loop, daemon=True)
api_thread.start()

time.sleep(1) #Sleep interval to allow time for connection to server

#Create May VIX future object
may_vixFuture_contract = Contract()
may_vixFuture_contract.symbol = 'VXK1'
may_vixFuture_contract.secType = 'FUT'
may_vixFuture_contract.tradingClass = 'VX'
may_vixFuture_contract.exchange = 'CFE'
may_vixFuture_contract.currency = 'USD'
may_vixFuture_contract.lastTradeDateOrContractMonth = '20210519'

#Create June VIX future object
june_vixFuture_contract = Contract()
june_vixFuture_contract.symbol = 'VXK1'
june_vixFuture_contract.secType = 'FUT'
june_vixFuture_contract.tradingClass = 'VX'
june_vixFuture_contract.exchange = 'CFE'
june_vixFuture_contract.currency = 'USD'
june_vixFuture_contract.lastTradeDateOrContractMonth = '20210616'

#Create July VIX future object
july_vixFuture_contract = Contract()
july_vixFuture_contract.symbol = 'VXK1'
july_vixFuture_contract.secType = 'FUT'
july_vixFuture_contract.tradingClass = 'VX'
july_vixFuture_contract.exchange = 'CFE'
july_vixFuture_contract.currency = 'USD'
july_vixFuture_contract.lastTradeDateOrContractMonth = '20210721'

#Create August VIX future object
august_vixFuture_contract = Contract()
august_vixFuture_contract.symbol = 'VXK1'
august_vixFuture_contract.secType = 'FUT'
august_vixFuture_contract.tradingClass = 'VX'
august_vixFuture_contract.exchange = 'CFE'
august_vixFuture_contract.currency = 'USD'
august_vixFuture_contract.lastTradeDateOrContractMonth = '20210818'

#Create Septmeber VIX future object
september_vixFuture_contract = Contract()
september_vixFuture_contract.symbol = 'VXK1'
september_vixFuture_contract.secType = 'FUT'
september_vixFuture_contract.tradingClass = 'VX'
september_vixFuture_contract.exchange = 'CFE'
september_vixFuture_contract.currency = 'USD'
september_vixFuture_contract.lastTradeDateOrContractMonth = '20210915'

# 1) Live Data
# 2) Frozen
# 3) Delayed
# 4) Delayed Frozen
#Request Market Data as 3 = Delayed since using paper account at the moment 
app.reqMarketDataType(1)


# Requesting Market Data for Euro to Usd ask price 1 = unique identifier, contract info, string for genericTickList (https://interactivebrokers.github.io/tws-api/classIBApi_1_1EClient.html#a7a19258a3a2087c07c1c57b93f659b63)
# boolean value if want a one-time snap shot, boolean value for regulatory snapshot, [] = mktDataOptions TagValue.
app.reqMktData(1, may_vixFuture_contract, '', False, False, [])
app.reqMktData(2, june_vixFuture_contract, '', False, False, [])
app.reqMktData(3, july_vixFuture_contract, '', False, False, [])
app.reqMktData(4, august_vixFuture_contract, '', False, False, [])
app.reqMktData(5, september_vixFuture_contract, '', False, False, [])




time.sleep(1) #Sleep interval to allow time for incoming price data

# Calling disconnect, otherwise the infinite loop occurs
app.disconnect()
