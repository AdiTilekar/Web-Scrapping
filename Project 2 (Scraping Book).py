import requests 
from bs4 import BeautifulSoup
from tqdm import tqdm 
link = 'https://books.toscrape.com/'
response = requests.get(link)
soup = BeautifulSoup(response.text,'html.parser')
data=[]
for sp in soup.find_all('li',class_='col-xs-6 col-sm-4 col-md-3 col-lg-3'):

    Book_tittle = sp.find_all('a')[-1].get('title')
    Book_link   = 'https://books.toscrape.com/'+sp.find_all('a')[-1].get('href')
    Image_link  = 'https://books.toscrape.com/'+sp.find_all('img')[0].get('src')
    Rating      = sp.find('p').get('class')[-1]
    price       = sp.find('p',class_='price_color').text[1:]
    availability = sp.find('p',class_='instock availability').text.strip()
    data.append([Book_tittle,Rating,price,availability,Book_link,Image_link])
    #print(Book_tittle,'|',Rating,'|',price,'|',availability,'|',link+Book_link,'|',link+Image_link)
print(data)
