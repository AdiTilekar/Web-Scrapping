import requests 
import pandas as pd
from bs4 import BeautifulSoup
from tqdm import tqdm 
data=[]
for page in tqdm(range(1,51)):
    link = 'https://books.toscrape.com/catalogue/page-'+str(page)+'.html'
    response = requests.get(link)
    soup = BeautifulSoup(response.text,'html.parser')
    for sp in soup.find_all('li',class_='col-xs-6 col-sm-4 col-md-3 col-lg-3'):
        Book_tittle = sp.find_all('a')[-1].get('title')
        Book_link   = 'https://books.toscrape.com/'+sp.find_all('a')[-1].get('href')
        Image_link  = 'https://books.toscrape.com/'+sp.find_all('img')[0].get('src')
        Rating      = sp.find('p').get('class')[-1]
        Price       = sp.find('p',class_='price_color').text[1:]
        Availability = sp.find('p',class_='instock availability').text.strip()
        data.append([Book_tittle,Rating,price,availability,Book_link,Image_link])
    
df=pd.DataFrame(data , columns = ['Book_tittle','Rating','Price','Availability','Book_link','Image_link'])
df.to_csv('Books_data.csv', index = False)  
