# **Web-Scrapping Project 2**

## **Problem Statement**

#### There is a website named as books.toscrape.com you have to scrap the  **Book_tittle, Rating,price, Availability, Book_link, Image_link** which is in the website upto 50 pages and create a CSV file of it.
## **Snapshot of website :-**
![Image](https://github.com/user-attachments/assets/d9bf9090-0781-40ad-b10b-41cbfa5e6c28)

## **Example :-**
    In this example we scrapped the first 4 books with their Book_tittle, Rating,price, Availability, Book_link and Image_link . 

![Image](https://github.com/user-attachments/assets/51adec63-3b15-4cb7-9cb1-f5ed266cb216)

## **Project code :-**
```python
    import requests 
    from bs4 import BeautifulSoup
    import pandas as pd
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
            data.append([Book_tittle,Rating,Price,Availability,Book_link,Image_link])
    df=pd.DataFrame(data , columns = ['Book_tittle','Rating','Price','Availability','Book_link','Image_link'])
    df.to_csv('Books_data.csv', index = False)
```
## **Libraries used in this project :-**

![Image](https://github.com/user-attachments/assets/8ec5108f-a0e3-4976-a253-f6ba8dc11761)

## **Libraries Explanation** :-

#### **requests** :- 
    requests is used to get the website or you can say fetch the website. 

#### **BeautifulSoup** :- 
    Beautiful Soup is a library that makes it easy to scrape information from web pages.

#### **pandas** :-
    pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language.
#### **tqdm** :-
    Tqdm is a Python library that provides fast, extensible progress bars for loops and iterables.

## **Project Code Explanation** :-

    This Python code is a web scraping script designed to extract information about books from the "Books to Scrape" website and save it to a CSV file. Here’s a line-by-line explanation:

---

### **Imports**:
```python
import requests
```
- **Purpose**: Allows you to send HTTP requests to the website and fetch its HTML content.

```python
from bs4 import BeautifulSoup
```
- **Purpose**: A library used to parse HTML and XML documents, making it easier to extract specific content from web pages.

```python
import pandas as pd
```
- **Purpose**: A powerful library for data manipulation and analysis, used here to store and export the scraped data into a CSV file.

```python
from tqdm import tqdm
```
- **Purpose**: A library to show a progress bar for loops, which makes long-running operations more user-friendly.

---

### **Data storage initialization**:
```python
data = []
```
- **Purpose**: An empty list to store the extracted book details as rows, with each row being a list of book attributes.

---

### **Loop through pages**:
```python
for page in tqdm(range(1, 51)):
```
- **Purpose**: Loops through page numbers from 1 to 50. Each page contains a list of books.  
- **`tqdm`**: Provides a progress bar to visualize the scraping process.

---

### **Construct page URL**:
```python
link = 'https://books.toscrape.com/catalogue/page-' + str(page) + '.html'
```
- **Purpose**: Dynamically generates the URL for each page by inserting the current page number into the URL structure.

---

### **Request page content**:
```python
response = requests.get(link)
```
- **Purpose**: Sends a GET request to fetch the HTML content of the page.

```python
soup = BeautifulSoup(response.text, 'html.parser')
```
- **Purpose**: Parses the HTML content of the page into a BeautifulSoup object, allowing easy navigation and extraction of data.

---

### **Extract book details**:
```python
for sp in soup.find_all('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3'):
```
- **Purpose**: Loops through all the `<li>` elements with the specified class, which represent individual books on the page.

```python
Book_tittle = sp.find_all('a')[-1].get('title')
```
- **Purpose**: Extracts the title of the book from the `title` attribute of the last `<a>` tag.

```python
Book_link = 'https://books.toscrape.com/' + sp.find_all('a')[-1].get('href')
```
- **Purpose**: Constructs the full URL of the book's detail page using the `href` attribute of the same `<a>` tag.

```python
Image_link = 'https://books.toscrape.com/' + sp.find_all('img')[0].get('src')
```
- **Purpose**: Constructs the full URL of the book's cover image using the `src` attribute of the `<img>` tag.

```python
Rating = sp.find('p').get('class')[-1]
```
- **Purpose**: Extracts the book's rating, which is stored as a class name (e.g., `One`, `Two`, etc.) in the `<p>` tag.

```python
Price = sp.find('p', class_='price_color').text[1:]
```
- **Purpose**: Extracts the book's price by finding the `<p>` tag with the class `price_color`. The `[1:]` removes the currency symbol (£).

```python
Availability = sp.find('p', class_='instock availability').text.strip()
```
- **Purpose**: Extracts the availability status of the book, trimming unnecessary whitespace using `.strip()`.

```python
data.append([Book_tittle, Rating, Price, Availability, Book_link, Image_link])
```
- **Purpose**: Adds the extracted details of the book as a row to the `data` list.

---

### **Save data to CSV**:
```python
df = pd.DataFrame(data, columns=['Book_tittle', 'Rating', 'Price', 'Availability', 'Book_link', 'Image_link'])
```
- **Purpose**: Converts the `data` list into a Pandas DataFrame with specified column names for easier handling and exporting.

```python
df.to_csv('Books_data.csv', index=False)
```
- **Purpose**: Exports the DataFrame to a CSV file named `Books_data.csv`. The `index=False` argument prevents adding an extra column for row indices.

---

### **Summary**:
    Loops through 50 pages of the website.
    Scrapes details like title, rating, price, availability, and links for each book.
    Stores the data in a list, converts it to a DataFrame, and saves it as a CSV file.

