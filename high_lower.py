import random


#Read the dictionary from world_indices.txt file
f = open('world_indice.txt', 'r')

data = f.read()

print(data)

def format_data(account):
    '''Format the account data into printable format.'''
    indice_symbol = account['symplols'],
    indice_name = account['names'],
    indice_price = account['price'],
    price_change = account['price change'],
    percentage_change = account['Percentage change']
    return f'This Indice with symbol {indice_symbol} and name {indice_name},\nhas a price of {indice_price} and daily price change of {price_change}'


# Generate a random account from the game data.

account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:
    account_b = random.choice(data)

print(format_data(account_a))
print(format_data(account_b))
