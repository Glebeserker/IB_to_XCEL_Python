from spread_contracts import spread_dict
from ibapi.wrapper import EWrapper
from ibapi.client import EClient
import pandas as pd
import threading
import time
import sys

spread_values = list(spread_dict.values())

dict_index = [*range(len(spread_dict))]

column_name = ['Bid Price', 'Ask Price', 'Bid Size', 'Ask Size']

spread_date_list = ['Nov21/Dec 21', 'Nov21/Jan 22', 'Nov21/Feb22', 'Dec21/Jan 22', 'Dec21/Feb22', 'Jan22/Feb22']

fut_frame = pd.DataFrame(columns=column_name)

marketDataFut = { date: {key: None for key in column_name} for date in spread_date_list}


class spreaData(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)

    def tickPrice(self, reqId, tickType, price, attrib):

        if tickType == 1:
            for i in dict_index:
                if reqId == i:
                    marketDataFut[spread_date_list[i]]['Bid Price'] = price

        elif tickType == 2:
            for i in dict_index:
                if reqId == i:
                    marketDataFut[spread_date_list[i]]['Ask Price'] = price

    def tickSize(self, reqId, tickType, size):

        if tickType == 0:
            for i in dict_index:
                if reqId == i:
                    marketDataFut[spread_date_list[i]]['Bid Size'] = size

        elif tickType == 3:
            for i in dict_index:
                if reqId == i:
                    marketDataFut[spread_date_list[i]]['Ask Size'] = size

def run_loop():
    app.run()

app = spreaData()
app.connect('127.0.0.1', 7496, 112)

thread = threading.Thread(target=run_loop, daemon=True)
thread.start()

time.sleep(1)

app.reqMarketDataType(1)

def dataRequest():
    for i in dict_index:
        app.reqMktData(i, spread_values[i], '', False, False, [])

dataRequest()

time.sleep(1)

app.disconnect()

spread_frame = pd.DataFrame.from_dict({(i): marketDataFut[i]
for i in marketDataFut.keys()},
orient='index')

spread_frame.to_csv('spread_data.csv', index=True)

