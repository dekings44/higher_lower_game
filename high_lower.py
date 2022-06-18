import random


#Read the dictionary from world_indices.txt file
f = open('world_indice.txt', 'r')

data = f.read()

print(data[2])



# def format_data():
#     '''Format the account data into printable format.'''
#     indice_symbol = data['symplols'],
#     indice_name = data['names'],
#     indice_price = data['price'],
#     price_change = data['price change'],
#     percentage_change = data['Percentage change']
#     return f'This Indice with symbol {indice_symbol} and name {indice_name},\nhas a price of {indice_price} and daily price change of {price_change}'


# Generate a random account from the game data.

# account_a = random.choice(data)
# account_b = random.choice(data)
# if account_a == account_b:
#     account_b = random.choice(data)

# print(format_data(account_a))
# print(format_data(account_b))
