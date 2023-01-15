import pandas as pd
import requests
from bs4 import BeautifulSoup
import lxml
import hashlib

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html"
data  = requests.get(url).text
soup = BeautifulSoup(data, 'html5lib') # parsear el texto

# Convertir la tabla html en un dataframe panda
netflix_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Volume"])

for row in soup.find("tbody").find_all('tr'):
    col = row.find_all("td")
    date = col[0].text
    Open = col[1].text
    high = col[2].text
    low = col[3].text
    close = col[4].text
    adj_close = col[5].text
    volume = col[6].text

    # Finally we append the data of each row to the table
    netflix_data = netflix_data.append({"Date":date, "Open":Open, "High":high, "Low":low, "Close":close, "Adj Close":adj_close, "Volume":volume}, ignore_index=True)

# imprimimos el dataFrame
netflix_data.head()

read_html_pandas_data = pd.read_html(url) # We can also use the pandas read_html function using the url
read_html_pandas_data = pd.read_html(str(soup)) # Or we can convert the BeautifulSoup object to a string

netflix_dataframe = read_html_pandas_data[0]
netflix_dataframe.head()







url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/amazon_data_webpage.html"
html_data  = requests.get(url).text

soup = BeautifulSoup(html_data, 'html5lib')
print(soup.find("title"))

amazon_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Volume"])

for row in soup.find("tbody").find_all("tr"):
    col = row.find_all("td")
    date = row[0].text
    Open = row[1].text
    high = row[2].text
    low = row[3].text
    close = row[4].text
    adj_close = row[5].text
    volume = row[6].text
    
    amazon_data = amazon_data.append({"Date":date, "Open":Open, "High":high, "Low":low, "Close":close, "Adj Close":adj_close, "Volume":volume}, ignore_index=True)

