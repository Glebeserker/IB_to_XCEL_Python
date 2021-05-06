# In order for the code to work need to run setup.py found in ../TWS API/source/pythonclient
# For set up to run need to have python wheels installed on system 
# Using wheels for IBAPI can be found https://stackoverflow.com/questions/57618117/installing-the-ibapi-package answer 
# Replacing python3 in command line with just python

#importing IBAPI pythonclient components for application
from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
#threading and time to control the process of the app
import threading
import time
# imported pandas in order to convert dictionary of price to panda and eventually to excel(in progress)
#import pandas as pd


#converting dataframe to Excel Object (commented out)
#writer = pd.ExcelWriter('demo.xlsx', engine = 'xlsxwritter')
#main_df.to_excel(writer, sheet_name='Sheet1', index=False)
#writer.save()

#setting IBAPI class object constructor method in order to call up for data and saving it in dictionary
class IBapi(EWrapper, EClient):
	def __init__(self):
		EClient.__init__(self, self)
		self.reqId_price_EUR_USD_dictionary = {} #dictionary to save price based on Id
	def tickPrice(self, reqId, tickType, price, attrib):
		self.reqId_price_EUR_USD_dictionary[reqId] = price #updates with every new price recieved
		if tickType == 2 and reqId == 1:
			print('The current ask price is: ', price)
			#converting price to string to be saved in .txt file to be sent to excel
			text_price = str(price)
			file = open("price.txt", "w")
			file.write(text_price)
			file.close

def run_loop():
	app.run()
# calling up IBAPI class instance and connecting the app to local host server
app = IBapi()
app.connect('127.0.0.1', 7497, 136)

#Start the socket in a thread
api_thread = threading.Thread(target=run_loop, daemon=True)
api_thread.start()

time.sleep(1) #Sleep interval to allow time for connection to server

#Create contract object
apple_contract = Contract()
apple_contract.symbol = 'AAPL'
apple_contract.secType = 'STK'
apple_contract.exchange = 'SMART'
apple_contract.currency = 'USD'
apple_contract.primaryExchange = "ISLAND"

#currency object
eurusd_contract = Contract()
eurusd_contract.symbol = 'EUR'
eurusd_contract.secType = 'CASH'
eurusd_contract.exchange = 'IDEALPRO'
eurusd_contract.currency = 'USD'

#Request Market Data as 3 = Delayed since using paper account at the moment 
app.reqMarketDataType(3)


# Requesting Market Data for Euro to Usd ask price 1 = unique identifier, contract info, string for genericTickList (https://interactivebrokers.github.io/tws-api/classIBApi_1_1EClient.html#a7a19258a3a2087c07c1c57b93f659b63)
# boolean value if want a one-time snap shot, boolean value for regulatory snapshot, [] = mktDataOptions TagValue.
app.reqMktData(1, eurusd_contract, '', False, False, [])


time.sleep(1) #Sleep interval to allow time for incoming price data

# Calling disconnect, otherwise the infinite loop occurs
app.disconnect()
