def exchange_money(budget, exchange_rate):
    res = budget / exchange_rate
    return res

def get_change(budget, exchanging_value):
    res = budget-exchanging_value
    return res

def get_value_of_bills(denomination, number_of_bills):

    res = denomination * number_of_bills
    return res

def get_number_of_bills(amount, denomination):
    res = int(amount / denomination)
    return res
    
def get_leftover_of_bills(amount, denomination):
    res = amount % denomination
    return res

def exchangeable_value(budget, exchange_rate, spread, denomination):
    imp = exchange_rate * (1 + spread / 100)
    res= budget / imp
    resf= int(res/denomination) * denomination
    return resf