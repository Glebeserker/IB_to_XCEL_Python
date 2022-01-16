import pyodbc

from ibapi.contract import Contract, ComboLeg

conn_str = (r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
           r'DBQ=D:\apptrial\work\Market4.accdb;')

conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

sqlCommand = 'SELECT Exparation, Conid From SpreadIDquery'

cursor.execute(sqlCommand)

data_fetched = cursor.fetchall()

# lists are saved inside a list [[expirationDate, ConId], ...]
lists = [list(rows) for rows in data_fetched]



class Constructors:
    def contracts(ID, action, ratio = 1, exchange = 'CFE'):
        contract = ComboLeg()
        contract.conId = ID
        contract.action = action
        contract.ratio = ratio
        contract.exchange = exchange 
        return contract
        
    def spreadContract(symbol='VIX', currency='USD', exchange='CFE', secType='BAG'):
        spreadContract = Contract()
        spreadContract.symbol = symbol
        spreadContract.currency = currency
        spreadContract.exchange = exchange
        spreadContract.secType = secType
        return spreadContract
        
buy_list = []
sell_list = []
combos_setup = []
values_list = []
values2 = []

combo_start = list(range(0, sum(list(range(0, len(lists)) ) ) ))


combos_setup.clear()
buy_list.clear()
sell_list.clear()
values_list.clear()

for i in lists:
    buy_list.append(Constructors.contracts(i[1], 'BUY'))
    sell_list.append(Constructors.contracts(i[1], 'SELL'))
    values_list.append(str(i[0]))

    
for j in combo_start:
    combos_setup.append(Constructors.spreadContract())
    combos_setup[j].comboLegs = []

for i in list(range(0, 3)):
    combos_setup[i].comboLegs.append(sell_list[0])
    combos_setup[i].comboLegs.append(buy_list[i+1])
    values2.append(values_list[0] + '/' + values_list[i+1])

    
for i in list(range(0, 2)):
    combos_setup[i+3].comboLegs.append(sell_list[1])
    combos_setup[i+3].comboLegs.append(buy_list[i+2])
    values2.append(values_list[1] + '/' + values_list[i+2])

for i in list(range(0, 1)):
    combos_setup[i+5].comboLegs.append(sell_list[2])
    combos_setup[i+5].comboLegs.append(buy_list[i+3])
    values2.append(values_list[2] + '/' + values_list[i+3])


spread_dictionary = {values2[i]: combos_setup[i] for i in range(len(values2))}

print(spread_dictionary)
        
    
    
    