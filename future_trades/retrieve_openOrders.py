from typing import OrderedDict
from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.order import *


import pandas as pd

import threading
import time

data_dict = {
    'OrderId': [] ,
    'LastTradeDate': [],
    'OrderPermId': [],
    'Exchange': [],
    'SecType': [],
    'LmtPrice': [],
    'Order Action': [],
    'Quantity': [],
    'Status': [],
}


class IBapi(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)

    def nextValidId(self, orderId):
        self.nextValidId = orderId
        self.start()


    def start(self):
        self.reqAllOpenOrders()
        
    def openOrder(self, orderId, contract: Contract, order: Order,
                    orderState):
            super().openOrder(orderId, contract, order, orderState)
            print("OpenOrder. PermId: ", order.permId, "ClientId:", order.clientId, " OrderId:", orderId, 
                   "Account:", order.account, "Symbol:", contract.symbol, "SecType:", contract.secType,
                   "Exchange:", contract.exchange, "Action:", order.action, "OrderType:", order.orderType,
                   "TotalQty:", order.totalQuantity, "CashQty:", order.cashQty, 
                   "LmtPrice:", order.lmtPrice, "AuxPrice:", order.auxPrice, "Status:", orderState.status, 'LastTradeDate:', contract.lastTradeDateOrContractMonth)
            
            
            data_dict['OrderId'].append(orderId)
            data_dict['LastTradeDate'].append(contract.lastTradeDateOrContractMonth)
            data_dict['OrderPermId'].append(order.permId)
            data_dict['Exchange'].append(contract.exchange)
            data_dict['SecType'].append(contract.secType)
            data_dict['LmtPrice'].append(order.lmtPrice)
            data_dict['Order Action'].append(order.action)
            data_dict['Quantity'].append(order.totalQuantity)
            data_dict['Status'].append(orderState.status)
            
    

def run_loop():
    app.run()

app = IBapi()
app.connect('127.0.0.1', 7497, 123)

# Start the socket in a thread
api_thread = threading.Thread(target=run_loop, daemon=True)
api_thread.start()

time.sleep(3)


data_dict = OrderedDict(data_dict)

df = pd.DataFrame.from_dict(data_dict)

print(df)

df.to_csv('open_orders.csv', index=False)


app.disconnect()
