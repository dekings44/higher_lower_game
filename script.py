import requests as rq
from bs4 import BeautifulSoup as bs

url = rq.get('https://uk.finance.yahoo.com/world-indices/')

print(url.status_code)

response = url.text

print(len(response))

page_data = bs(response, 'html.parser')

tickers = page_data.find_all('a', 'Fw(600) C($linkColor)')

print(tickers[:5])


#Extract text from data and remove ths ang ('^') symbol leading in the text
tickers_name = [stock_name.text.replace('^', '') for stock_name in tickers]

print(tickers_name)

# Get the company's indices names

indice = page_data.find_all('td', {'aria-label': 'Name'})

indices = [ticker_name.text for ticker_name in indice]

print(indices)

# Get the current day price of the indices

price = page_data.find_all('td', {'aria-label': 'Last price'})

#extract prices, replace every instance of comma in the price and convert to float
all_prices = [float(index_price.text.replace(',', '')) for index_price in price]

print(all_prices)


# Get the Change in price from the prvious day

price_change = page_data.find_all('td', {'aria-label': 'Change'})

#extract prices, replace every instance of comma in the price and convert to float
all_price_change = [float(priceChange.text.replace(',', '')) for priceChange in price_change]

print(all_price_change)