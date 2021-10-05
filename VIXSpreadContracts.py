from ibapi.contract import Contract, ComboLeg
#Initial contracts for combo leg set up

#OCT(sell)combo
october_sell = ComboLeg()
october_sell.conId = 467524677
october_sell.ratio = 1
october_sell.action = 'SELL'
october_sell.exchange = 'CFE'

#NOV(sell) combo
november_sell = ComboLeg()
november_sell.conId = 472801223
november_sell.ratio = 1
november_sell.action = 'SELL'
november_sell.exchange = 'CFE'

#DEC(sell) combo
decem_sell = ComboLeg()
decem_sell.conId = 478139096
decem_sell.ratio = 1
decem_sell.action = 'SELL'
decem_sell.exchange = 'CFE'

#NOV(buy) combo
november_buy = ComboLeg()
november_buy.conId = 472801223
november_buy.ratio = 1
november_buy.action = 'BUY'
november_buy.exchange = 'CFE'

#DEC(buy) combo
decem_buy = ComboLeg()
decem_buy.conId = 478139096
decem_buy.ratio = 1
decem_buy.action = 'BUY'
decem_buy.exchange = 'CFE'

#JAN(buy) combo
jan = ComboLeg()
jan.conId = 484239821
jan.ratio = 1
jan.action = 'BUY'
jan.exchange = 'CFE'

# The original contract doesnt change, except for variable name,
# therefore need to set them up one by one

#OCT(sell) NOV(buy) spread
oct_nov_spread = Contract()
oct_nov_spread.symbol = 'VIX'
oct_nov_spread.currency = 'USD'
oct_nov_spread.exchange = 'CFE'
oct_nov_spread.secType = 'BAG'

#OCT(sell) DEC(buy) spread
oct_dec_spread = Contract()
oct_dec_spread.symbol = 'VIX'
oct_dec_spread.currency = 'USD'
oct_dec_spread.exchange = 'CFE'
oct_dec_spread.secType = 'BAG'

#OCT(sell) JAN(buy) spread
oct_jan_spread = Contract()
oct_jan_spread.symbol = 'VIX'
oct_jan_spread.currency = 'USD'
oct_jan_spread.exchange = 'CFE'
oct_jan_spread.secType = 'BAG'

#NOV(sell) DEC(buy) spread
nov_dec_spread = Contract()
nov_dec_spread.symbol = 'VIX'
nov_dec_spread.currency = 'USD'
nov_dec_spread.exchange = 'CFE'
nov_dec_spread.secType = 'BAG'

#NOV(sell) JAN(buy) spread
nov_jan_spread = Contract()
nov_jan_spread.symbol = 'VIX'
nov_jan_spread.currency = 'USD'
nov_jan_spread.exchange = 'CFE'
nov_jan_spread.secType = 'BAG'

#DEC(sell) JAN(buy) spread
dec_jan_spread = Contract()
dec_jan_spread.symbol = 'VIX'
dec_jan_spread.currency = 'USD'
dec_jan_spread.exchange = 'CFE'
dec_jan_spread.secType = 'BAG'


#Utilizing ComboLeg function to combine the legs to be used in the future for requesting data

#OCT NOV SPREAD COMBO
oct_nov_spread.comboLegs = []
oct_nov_spread.comboLegs.append(october_sell)
oct_nov_spread.comboLegs.append(november_buy)

#OCT DEC SPREAD COMBO
oct_dec_spread.comboLegs =[]
oct_dec_spread.comboLegs.append(october_sell)
oct_dec_spread.comboLegs.append(decem_buy)

#OCT JAN SPREAD COMBO
oct_jan_spread.comboLegs = []
oct_jan_spread.comboLegs.append(october_sell)
oct_jan_spread.comboLegs.append(jan)

#NOV DEC SPREAD COMBO
nov_dec_spread.comboLegs = []
nov_dec_spread.comboLegs.append(november_sell)
nov_dec_spread.comboLegs.append(decem_buy)

#NOV JAN SPREAD COMBO
nov_jan_spread.comboLegs = []
nov_jan_spread.comboLegs.append(november_sell)
nov_jan_spread.comboLegs.append(jan)

#DEC JAN SPREAD COMBO
dec_jan_spread.comboLegs = []
dec_jan_spread.comboLegs.append(decem_sell)
dec_jan_spread.comboLegs.append(jan)


spread_combos = [oct_nov_spread, 
                 oct_dec_spread, 
                 oct_jan_spread,
                 nov_dec_spread,
                 nov_jan_spread,
                 dec_jan_spread]

print(spread_combos)
