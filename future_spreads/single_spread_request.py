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

spread_date_list = ['Nov21/Dec 21', 'Nov21/Jan 22', 'Nov21/Feb22', 'Dec21/Jan22', 'Dec21/Feb22', 'Jan22/Feb22']

fut_frame = pd.DataFrame(columns=column_name)


marketDataFut = { date: {key: None for key in column_name} for date in spread_date_list}

class SingleSpreadData(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self,self)
        
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
                    
                    
def run_app():
    app.run()
    
app = SingleSpreadData()
app.connect('127.0.0.1', 7496, 123)

thread = threading.Thread(target=run_app, daemon=True)
thread.start()

time.sleep(1)

app.reqMarketDataType(1)

contractId = int(sys.argv[1])

app.reqMktData(contractId, spread_values[contractId], '', False, False, [])

time.sleep(1)

app.disconnect()

#opening exsisting csv file
df = pd.read_csv('spread_data.csv')
row_to_be_changed = df.iloc[[contractId]]

df_dict = row_to_be_changed.to_dict()

for header in df_dict:
    for header2 in marketDataFut[spread_date_list[contractId]]:
        if header == header2:
            df_dict[header][contractId] = marketDataFut[spread_date_list[contractId]][header2]
            
new_df = pd.DataFrame.from_dict({(i): df_dict[i] for i in df_dict.keys()}, orient='columns')

print(new_df)
