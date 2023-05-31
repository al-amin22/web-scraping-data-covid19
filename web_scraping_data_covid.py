from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://www.worldometers.info/coronavirus/'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')

tabel = soup.find('table', id='main_table_countries_today')

headers=[]
for i in tabel.find_all('th'):
    judul = i.text
    headers.append(judul)
    
headers[13] = 'Tests/1M pop'

dataku = pd.DataFrame(columns= headers)

for i in tabel.find_all('tr')[1:]:
    data_baris = i.find_all('td')
    baris = [tr.text for tr in data_baris]
    panjang = len(dataku)
    dataku.loc[panjang] = baris
    
dataku.drop(dataku.index[0:7], inplace=True)
dataku.drop(dataku.index[222:229], inplace=True)

dataku.reset_index(inplace=True, drop=True)

dataku.drop('#', inplace=True, axis=1)

dataku.to_csv('data_covid19.csv', index=False)

buka = pd.read_csv('data_covid19.csv')
