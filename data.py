from csv import DictReader
import json
import random
from art import logo

#Convert the csv file into dictionary

with open('world_price_indices', 'r') as data:
    #pass the file object to DictReader() to get the DictReader object
    reader = DictReader(data)
    # get a list of dictionaries from the reader
    list_of_data = list(reader)

    with open('world_indice.txt', 'w') as world_index_json:
        world_index_json.write(json.dumps(list_of_data))

    #print(list_of_data)

print(list_of_data[0]['names'])


def format_data(account):
    '''Takes the account data and returns the printable format.'''
    indice_symbol = account['symplols'],
    indice_name = account['names'],
    indice_price = account['price'],
    price_change = account['price change'],
    percentage_change = account['Percentage change']
    return f"This Indice with symbol {''.join(indice_symbol)} and name {''.join(indice_name)},\nhas a percentage change in price of {''.join(percentage_change)} and daily price change of {''.join(price_change)}"



def check_answer(guess, a_price_indices, b_price_indices):
    '''Takes the user guess and indices and returns if they got it right'''
    if a_price_indices > b_price_indices:
        return guess == "a"
    else:
        return guess == "b"


score = 0


game_should_continue = True

account_b = random.choice(list_of_data)

while game_should_continue:
    # Generate a random account from the game data.

    account_a = account_b
    account_b = random.choice(list_of_data)
    
    while account_a == account_b:
        account_b = random.choice(list_of_data)

    print(f'Compare A: {format_data(account_a)}.')
    print(logo)
    print(f'Against B: {format_data(account_b)}')

    guess = input("Which indeices has is more valuable? 'A' or 'B': ").lower()

    a_price_indices = account_a['price']
    b_price_indices = account_b['price']

    is_correct = check_answer(guess, a_price_indices, b_price_indices)


    if is_correct:
        score += 1
        print(f'You are right! Your current score is {score}')
    else:
        game_should_continue = False
        print('Sorry, that is wrong')