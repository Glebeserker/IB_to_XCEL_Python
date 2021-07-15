# In order for the code to work need to run setup.py found in ../TWS API/source/pythonclient
# For set up to run need to have python wheels installed on system 
# Using wheels for IBAPI can be found https://stackoverflow.com/questions/57618117/installing-the-ibapi-package answer 
# Replacing python3 in command line with just python

#importing IBAPI pythonclient components for application
from os import write
from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import ComboLeg, Contract
#threading and time to control the process of the app and csv to write csv files
import threading
import time
import csv
from contracts import contract_list
# imported pandas in order to convert dictionary of price to panda and eventually to excel(in progress)
#import pandas as pd


#converting dataframe to Excel Object (commented out)
#writer = pd.ExcelWriter('demo.xlsx', engine = 'xlsxwritter')
#main_df.to_excel(writer, sheet_name='Sheet1', index=False)
#writer.save()

#creating multiple dictionaries for each month, to be latter added to a list and saved as cvs file




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

october_data_dictionary = {'Date': 20211020,
                             'Bid Size': 0,
                             'Bid Price': 0,
                             'Ask Size': 0,
                             'Ask Price': 0,
                             'Last Price': 0,
                             'Volume': 0}

november_data_dictionary = {'Date': 20211117,
                             'Bid Size': 0,
                             'Bid Price': 0,
                             'Ask Size': 0,
                             'Ask Price': 0,
                             'Last Price': 0,
                             'Volume': 0}

#List to put dictionaries into
dicts = [august_data_dictionary, september_data_dictionary, october_data_dictionary, november_data_dictionary] 

#IB constructor class to send and recieve data
class IBapi(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)
    def tickPrice(self, reqId, tickType, price, attrib):
        
        file = open('C:\IB-Script\price.txt', 'r+')
        # ask price if statement for each month
        if tickType == 2: 
            if reqId == 0:
                text_ask = str(price)
                august_data_dictionary['Ask Price'] = text_ask
            elif reqId == 1:
                text_ask = str(price)
                september_data_dictionary['Ask Price'] = text_ask
            elif reqId == 2: 
                text_ask = str(price)
                october_data_dictionary['Ask Price'] = text_ask
            elif reqId == 3:
                text_ask = str(price)
                november_data_dictionary['Ask Price'] = text_ask
            else: 
                print('Incorrect reqId') 
    
        elif tickType == 4: 
            
            if reqId == 0:
                text_lastPrice = str(price)
                august_data_dictionary['Last Price'] = text_lastPrice
            elif reqId == 1:
                text_lastPrice = str(price)
                september_data_dictionary['Last Price'] = text_lastPrice
            elif reqId == 2:
                text_lastPrice = str(price)
                october_data_dictionary['Last Price'] = text_lastPrice
            elif reqId == 3:
                text_lastPrice = str(price)
                november_data_dictionary['Last Price'] = text_lastPrice
            else:
                print('Incorrect reqId')
                

        elif tickType == 1: 
    
            if reqId == 0:
                text_bidPrice = str(price)
                august_data_dictionary['Bid Price'] = text_bidPrice
            elif reqId == 1:
                text_bidPrice = str(price)
                september_data_dictionary['Bid Price'] = text_bidPrice
            elif reqId == 2:
                text_bidPrice = str(price)
                october_data_dictionary['Bid Price'] = text_bidPrice
            elif reqId == 3:
                text_bidPrice = str(price)
                november_data_dictionary['Bid Price'] = text_bidPrice
            else:
                print('Incorrect reqId')
        
        
        
    # function to call size parameters of things
    def tickSize(self, reqId, tickType, size):
        
        if tickType == 0: 
            
            if reqId == 0:
                
                text_bidSize = str(size)
                august_data_dictionary['Bid Size'] = text_bidSize
            elif reqId == 1:
                
                text_bidSize = str(size)
                september_data_dictionary['Bid Size'] = text_bidSize
            elif reqId == 2:
                
                text_bidSize = str(size)
                october_data_dictionary['Bid Size'] = text_bidSize
            elif reqId == 3:
                text_bidSize = str(size)
                november_data_dictionary['Bid Size'] = text_bidSize
            else: 
                print('Incorrect reqId')
                
            
        elif tickType == 3:
           
            if reqId == 0:
                text_askSize = str(size)
                august_data_dictionary['Ask Size'] = text_askSize
            elif reqId == 1:
                text_askSize = str(size)
                september_data_dictionary['Ask Size'] = text_askSize 
            elif reqId == 2:
                text_askSize = str(size)
                october_data_dictionary['Ask Size'] = text_askSize 
            elif reqId == 3:
                text_askSize = str(size)
                november_data_dictionary['Ask Size'] = text_askSize
            else:
                print('Incorrect reqId')
                  
        elif tickType == 8:
           
            if reqId == 0:
                
                text_volume = str(size)
                august_data_dictionary['Volume'] = text_volume
            elif reqId == 1:
               
                text_volume = str(size)
                september_data_dictionary['Volume'] = text_volume
            elif reqId == 2:
                
                text_volume = str(size)
                october_data_dictionary['Volume'] = text_volume
            elif reqId == 3:
                
                text_volume = str(size)
                november_data_dictionary['Volume'] = text_volume
                
        elif tickType == 5:
            
            if reqId == 0:
                
                text_lastSize = str(size)
                august_data_dictionary['Last Size'] = text_lastSize
            elif reqId == 1:
                
                text_lastSize = str(size)
                september_data_dictionary['Last Size'] = text_lastSize
            elif reqId == 2:
                
                text_lastSize = str(size)
                october_data_dictionary['Last Size'] = text_lastSize
            elif reqId == 3:
                
                text_lastSize = str(size)
                november_data_dictionary['Last Size'] = text_lastSize
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

# 1) Live Data
# 2) Frozen
# 3) Delayed
# 4) Delayed Frozen
#Request Market Data as 3 = Delayed since using paper account at the moment 
app.reqMarketDataType(1)


# Requesting Market Data for Euro to Usd ask price 1 = unique identifier, contract info, string for genericTickList (https://interactivebrokers.github.io/tws-api/classIBApi_1_1EClient.html#a7a19258a3a2087c07c1c57b93f659b63)
# boolean value if want a one-time snap shot, boolean value for regulatory snapshot, [] = mktDataOptions TagValue.
app.reqMktData(0, contract_list[1], '', False, False, [])
app.reqMktData(1, contract_list[2], '', False, False, [])
app.reqMktData(2, contract_list[3], '', False, False, [])
app.reqMktData(3, contract_list[4], '', False, False, [])




time.sleep(1) #Sleep interval to allow time for incoming price data

# Calling disconnect, otherwise the infinite loop occurs
app.disconnect()
