from database_access import spread_dictionary
from ibapi.wrapper import EWrapper
from ibapi.client import EClient
import pandas as pd
import threading
import time
# import pymysql
import datetime

spread_values = list(spread_dictionary.values())



column_name = ['DateTime','Bid Price', 'Ask Price', 'Bid Size', 'Ask Size']

spread_date_list = list(spread_dictionary.keys())

dict_index = [*range(len(spread_date_list))]

fut_frame = pd.DataFrame(columns=column_name)

marketDataFut = { date: {key: None for key in column_name} for date in spread_date_list}


class spreaData(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)
        
    time = datetime.datetime.now()
    for i in dict_index:
        marketDataFut[spread_date_list[i]]['DateTime'] = time.strftime("%Y-%m-%d %H:%M:%S")
        

    def tickPrice(self, reqId, tickType, price, attrib):

        if tickType == 66:
            for i in dict_index:
                if reqId == i:
                    marketDataFut[spread_date_list[i]]['Bid Price'] = price

        elif tickType == 67:
            for i in dict_index:
                if reqId == i:
                    marketDataFut[spread_date_list[i]]['Ask Price'] = price

    def tickSize(self, reqId, tickType, size):

        if tickType == 69:
            for i in dict_index:
                if reqId == i:
                    marketDataFut[spread_date_list[i]]['Bid Size'] = size

        elif tickType == 70:
            for i in dict_index:
                if reqId == i:
                    marketDataFut[spread_date_list[i]]['Ask Size'] = size

def run_loop():
    app.run()

app = spreaData()
app.connect('127.0.0.1', 7497, 136)

thread = threading.Thread(target=run_loop, daemon=True)
thread.start()

time.sleep(1)

app.reqMarketDataType(3)

def dataRequest():
    for i in dict_index:
        app.reqMktData(i, spread_values[i], '', False, False, [])

dataRequest()

time.sleep(1)

app.disconnect()


spread_frame = pd.DataFrame.from_dict({(i): marketDataFut[i]
for i in marketDataFut.keys()},
orient='index')

print(spread_frame)

# connection = pymysql.connect(host='localhost:3306',
#                              user='root',
#                              password='Dm5zttia!',
#                              db='spread_futures')


spread_frame.to_csv('spread_data.csv', index=True)

