import requests as rq
from bs4 import BeautifulSoup as bs

url = rq.get('https://uk.finance.yahoo.com/world-indices/')

print(url.status_code)

response = url.text

print(len(response))

page_data = bs(response, 'html.parser')

tickers = page_data.find_all('a', 'Fw(600) C($linkColor)')

print(tickers[:5])