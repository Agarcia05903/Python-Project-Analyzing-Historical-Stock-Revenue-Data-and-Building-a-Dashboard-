
import yfinance as yf
tesla_data = yf.download('TSLA', start='2023-01-01', end='2023-10-01')
tesla_data.reset_index(inplace=True)
print(tesla_data.head())
import pandas as pd



import yfinance as yf
gme_data = yf.download('GME', start='2023-01-01', end='2023-10-01')
gme_data.reset_index(inplace=True)
print(gme_data.head())
gme_data.to_csv('gme_stock_data.csv')








import matplotlib.pyplot as plt

def make_graph(data, title):
    
    plt.plot(data['Date'], data['Close'], label='Tesla Stock Price')
    

    plt.xlabel('Date')
    plt.ylabel('Closing Price')
    plt.title('Tesla Stock Graph')  
    plt.legend()


    
   
    plt.show()


make_graph(tesla_data, 'Tesla Stock Price')


import matplotlib.pyplot as plt


def make_graph(data, title):
   
    plt.plot(data['Date'], data['Close'], label='GameStop Stock Price')
    
    
    plt.xlabel('Date')
    plt.ylabel('Closing Price')
    plt.title('Game Stop Stocks')  
    plt.legend()
    
    
    plt.show()


make_graph(gme_data, 'GameStop Stock Price')




