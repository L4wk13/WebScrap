import requests
from bs4 import BeautifulSoup
import unicodedata
import pandas

country = input("Enter a Country: ")
url = 'https://www.timeanddate.com/weather/' + country
page = requests.get(url)

print(page.status_code)

soup = BeautifulSoup(page.content, 'html.parser')
result = soup.find_all('table')
result2 = result[0].find_all('td')
data = [unicodedata.normalize('NFKD', item.get_text()) for item in result2 if item.get_text() != '']

town = []
time = []
temp = []
count = 0

for i in range(int(len(data)/3)):
    town.append(data[count])
    time.append(data[count+1])
    temp.append(data[count+2])
    count += 3

weather = pandas.DataFrame({
    'town': town,
    'time': time,
    'temp': temp
})

print(weather)