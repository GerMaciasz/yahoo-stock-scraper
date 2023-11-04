import requests
from bs4 import BeautifulSoup


def data(ticker):
    ticker.upper()
    URL = f'https://finance.yahoo.com/quote/{ticker}?p={ticker}'
    URLSTATISTICS = f'https://finance.yahoo.com/quote/{ticker}/key-statistics?p={ticker}'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/116.0.0.0 Safari/537.36",
        "Accept-Language": "es-419,es;q=0.9,en;q=0.8",
    }
    response = requests.get(URL, headers=headers)
    response2 = requests.get(URLSTATISTICS, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    soup2 = BeautifulSoup(response2.text, 'html.parser')
    stock = {
        'Company Name': soup.find('h1', {'class': 'D(ib) Fz(18px)'}).text.split(' ')[0],
        'Today price' : soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('fin-streamer')[0].text,
        'Current Price Change': soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('span')[0].text,
        'Percentage change': soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('span')[1].text.replace('(', '').replace(')', ''),
        'P/E': soup.find('table', {'class': 'W(100%) M(0) Bdcl(c)'}).find_all('td')[5].text,
        'EPS': soup.find('table', {'class': 'W(100%) M(0) Bdcl(c)'}).find_all('td')[7].text,
        '1 Year Target': soup.find('table', {'class': 'W(100%) M(0) Bdcl(c)'}).find_all('td')[15].text,
        '52 Week High': soup2.find_all('table', {'class': 'W(100%) Bdcl(c)'})[1].find_all('td')[7].text,
        '52 Week Low': soup2.find_all('table', {'class': 'W(100%) Bdcl(c)'})[1].find_all('td')[9].text,
    }
    return stock




