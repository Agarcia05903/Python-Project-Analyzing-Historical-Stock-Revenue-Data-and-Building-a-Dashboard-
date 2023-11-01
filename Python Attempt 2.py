import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots


tesla = yf.Ticker('TSLA')


tesla_data = tesla.history(period='max')


tesla_data.reset_index(inplace=True)
tesla_data['Date'] = tesla_data['Date'].dt.strftime('%Y-%m-%d')

# Displays the first five rows of the tesla_data dataframe
print(tesla_data[['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Dividends', 'Stock Splits']].head(5).to_string(index=False))

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm'
request = requests.get(url)
html_data = request.text

bf = BeautifulSoup(html_data, 'lxml')
table = bf.find_all('tbody')[1]

tesla_revenue = pd.DataFrame(columns=['Date', 'Revenue'])
rows = table.find_all('tr')

for row in rows:
    cols = row.find_all('td')
    tesla_revenue = pd.concat([tesla_revenue, pd.DataFrame({'Date': [cols[0].text], 'Revenue': [cols[1].text]})])

tesla_revenue["Revenue"] = tesla_revenue['Revenue'].str.replace(',|\$',"", )
tesla_revenue.dropna(inplace=True)
tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]


print(tesla_revenue.tail())



gamestop = yf.Ticker('GME')


gme_data = gamestop.history(period='max')


gme_data.reset_index(inplace=True)


gme_data['Date'] = gme_data['Date'].dt.strftime('%Y-%m-%d')


print(gme_data[['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Dividends', 'Stock Splits']].head(5).to_string(index=False))


import requests
import pandas as pd
from bs4 import BeautifulSoup


url_gme = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"
req_gme = requests.get(url_gme)
html_data = req_gme.text

soup = BeautifulSoup(html_data, "html.parser")
table = soup.find_all("table")[1]  
data_list = []

for row in table.find_all("tr")[1:]:  
    columns = row.find_all("td")
    date = columns[0].get_text(strip=True)
    revenue = columns[1].get_text(strip=True)
    data_list.append({"Date": date, "Revenue": revenue})
    
gme_revenue = pd.DataFrame(data_list)
gme_revenue["Revenue"] = gme_revenue["Revenue"].str.replace('[\$,]', '', regex=True)
gme_revenue['Date'] = pd.to_datetime(gme_revenue['Date'])
print(gme_revenue.tail())
print(gme_revenue.dtypes)

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Tesla and GameStop data into tesla_data and gme_data dataframes are loaded thus we can plot the graph:

# An interactive graph for Tesla
tesla_fig = go.Figure()

tesla_fig.add_trace(go.Scatter(x=tesla_data['Date'], y=tesla_data['Close'], mode='lines', name='Tesla Close Price'))
tesla_fig.add_trace(go.Scatter(x=tesla_revenue['Date'], y=tesla_revenue['Revenue'], mode='lines', name='Tesla Revenue'))

tesla_fig.update_layout(
    title='Tesla Stock Data and Revenue',
    xaxis_title='Date',
    yaxis_title='US Dollar',
)

# An interactive graph for GameStop
gme_fig = go.Figure()

gme_fig.add_trace(go.Scatter(x=gme_data['Date'], y=gme_data['Close'], mode='lines', name='GameStop Close Price'))
gme_fig.add_trace(go.Scatter(x=gme_revenue['Date'], y=gme_revenue['Revenue'], mode='lines', name='GameStop Revenue'))

gme_fig.update_layout(
    title='GameStop Stock Data and Revenue',
    xaxis_title='Date',
    yaxis_title='US Dollar',
)

# Subplot with a range slider
fig = make_subplots(rows=2, cols=1, shared_xaxes=True,
                    subplot_titles=('Tesla', 'GameStop'))

fig.add_trace(tesla_fig['data'][0], row=1, col=1)
fig.add_trace(gme_fig['data'][0], row=2, col=1)

fig.update_xaxes(rangeslider_visible=True)

fig.show()


