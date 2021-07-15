from ibapi.contract import Contract




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

#Ocotber VIX Contract Object
october_vixFuture_contract = Contract()
october_vixFuture_contract.symbol = 'VXK1'
october_vixFuture_contract.secType = 'FUT'
october_vixFuture_contract.tradingClass = 'VX'
october_vixFuture_contract.exchange = 'CFE'
october_vixFuture_contract.currency = 'USD'
october_vixFuture_contract.lastTradeDateOrContractMonth = '20211020'

november_vixFuture_contract = Contract()
november_vixFuture_contract.symbol = 'VXK1'
november_vixFuture_contract.secType = 'FUT'
november_vixFuture_contract.tradingClass = 'VX'
november_vixFuture_contract.exchange = 'CFE'
november_vixFuture_contract.currency = 'USD'
november_vixFuture_contract.lastTradeDateOrContractMonth = '20211117'

contract_list = [july_vixFuture_contract, august_vixFuture_contract, september_vixFuture_contract, october_vixFuture_contract, november_vixFuture_contract]
