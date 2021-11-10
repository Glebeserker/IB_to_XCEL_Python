from ibapi.contract import Contract, ComboLeg
#Initial contracts for combo leg set up


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

#Jan(sell) combo
jan_sell = ComboLeg()
jan_sell.conId = 484239821
jan_sell.ratio = 1
jan_sell.action = 'SELL'
jan_sell.exchange = 'CFE'


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
jan_buy = ComboLeg()
jan_buy.conId = 484239821
jan_buy.ratio = 1
jan_buy.action = 'BUY'
jan_buy.exchange = 'CFE'

#Feb(buy) combo
feb_buy = ComboLeg()
feb_buy.conId = 493119150
feb_buy.ratio = 1
feb_buy.action = 'BUY'
feb_buy.exchange = 'CFE'

# The original contract doesnt change, except for variable name,
# therefore need to set them up one by one


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

#Nov(sell) Feb(buy) spread
nov_feb_spread = Contract()
nov_feb_spread.symbol = 'VIX'
nov_feb_spread.currency = 'USD'
nov_feb_spread.exchange = 'CFE'
nov_feb_spread.secType = 'BAG'

#DEC(sell) JAN(buy) spread
dec_jan_spread = Contract()
dec_jan_spread.symbol = 'VIX'
dec_jan_spread.currency = 'USD'
dec_jan_spread.exchange = 'CFE'
dec_jan_spread.secType = 'BAG'

#Dec(sell) Feb(buy) spread
dec_feb_spread = Contract()
dec_feb_spread.symbol = 'VIX'
dec_feb_spread.currency = 'USD'
dec_feb_spread.exchange = 'CFE'
dec_feb_spread.secType = 'BAG'

#Jan(sell) Feb(buy) spread
jan_feb_spread = Contract()
jan_feb_spread.symbol = 'VIX'
jan_feb_spread.currency = 'USD'
jan_feb_spread.exchange = 'CFE'
jan_feb_spread.secType = 'BAG'


#Utilizing ComboLeg function to combine the legs to be used in the future for requesting data


#NOV DEC SPREAD COMBO
nov_dec_spread.comboLegs = []
nov_dec_spread.comboLegs.append(november_sell)
nov_dec_spread.comboLegs.append(decem_buy)

#NOV JAN SPREAD COMBO
nov_jan_spread.comboLegs = []
nov_jan_spread.comboLegs.append(november_sell)
nov_jan_spread.comboLegs.append(jan_buy)

#NOV FEB SPREAD COMBO
nov_feb_spread.comboLegs = []
nov_feb_spread.comboLegs.append(november_sell)
nov_feb_spread.comboLegs.append(feb_buy)

#DEC JAN SPREAD COMBO
dec_jan_spread.comboLegs = []
dec_jan_spread.comboLegs.append(decem_sell)
dec_jan_spread.comboLegs.append(jan_buy)

#DEC FEB SPREAD COMBO
dec_feb_spread.comboLegs = []
dec_feb_spread.comboLegs.append(decem_sell)
dec_feb_spread.comboLegs.append(feb_buy)

#JAN FEB SPREAD COMBO
jan_feb_spread.comboLegs = []
jan_feb_spread.comboLegs.append(jan_sell)
jan_feb_spread.comboLegs.append(feb_buy)



spread_dict = {'Nov21/Dec21': nov_dec_spread,
               'Nov21/Jan22': nov_jan_spread,
               'Nov21/Feb22': nov_feb_spread,
               'Dec21/Jan22': dec_jan_spread,
               'Dec21/Feb22': dec_feb_spread,
               'Jan22/Feb22': jan_feb_spread}
