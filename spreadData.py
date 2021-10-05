from spread_contracts import spread_combos
import pandas as pd
from ibapi.client import EClient
from ibapi.wrapper import EWrapper
import threading
import time as tm

#csv modules import 
from csv import DictWriter


column_name = ['Spread Dates', 'Bid Price', 'Ask Price', 'Bid Size', 'Ask Size']

spread_date_list = ['Oct 21/Nov 21', 'Oct 21/Dec 21', 'Oct 21/Jan 22', 'Nov 20/Dec 20', 'Nov 20/Jan 21', 'Dec 20/Jan 21']

length_of_spread = 0
for key in spread_combos:
    length_of_spread += 1
print(length_of_spread)    
reqIdBool = list(range(length_of_spread))
print(reqIdBool)
spread_incom_data = { id: {key: None for key in column_name} for id in reqIdBool}


spread_frame = pd.DataFrame(columns= column_name)

for item in spread_incom_data:
    spread_incom_data[item]['Spread Dates'] = spread_date_list[item]
    
    
class SpreadData(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self,self)
        #price ticks
        
    def tickPrice(self, reqId, tickType, price, attrib):
        if tickType == 67:
            for i in reqIdBool:
                if reqId == i:
                    spread_incom_data[reqIdBool[i]]['Ask Price'] = price
                    
        elif tickType == 66:
            for i in reqIdBool:
                if reqId == i:
                    spread_incom_data[reqIdBool[i]]['Bid Price'] = price      
        
    def tickSize(self, reqId, tickType, size):
        if tickType == 69:
            for i in reqIdBool:
                if reqId == i:
                    spread_incom_data[reqIdBool[i]]['Bid Size'] = size
                        
        elif tickType == 70:
            for i in reqIdBool:
                    if reqId == i:
                        spread_incom_data[reqIdBool[i]]['Ask Size'] = size

def run_app():
    app.run()
    
app = SpreadData()
app.connect('127.0.0.1', 7496, 'UNIQUE ID HERE')

api_thread = threading.Thread(target=run_app, daemon=True)
api_thread.start()

tm.sleep(1)


app.reqMarketDataType(1)

def MarketRequest():
    for i in reqIdBool:
        app.reqMktData(i, spread_combos[i], '', False, False, [])
        
        
MarketRequest()

tm.sleep(1)

app.disconnect

intermediate_frame = pd.DataFrame.from_dict({(i): spread_incom_data[i] for i in spread_incom_data.keys()}, orient='index')

intermediate_frame.columns = ['Dates', 'BidPrice', 'AskSize', 'Bid Size', 'AskSize']

print(intermediate_frame)

intermediate_frame.to_csv('PATH TO CSV FILE HERE', mode='a', index=False, header='False')
