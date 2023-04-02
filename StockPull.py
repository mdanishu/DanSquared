import sys
import yfinance as yf
import pandas as pd
import matplotlib as plt
from datetime import datetime
import requests
from config import alphavantage_key 

#plt.style.use('seaborn')

tickers = 'GOOGL'

# tickers = input("ticker please:")

# def analysisout (tickers, period='5y', interval='1d'):
#     stock = yf.Ticker(tickers)
#     stockinfo = stock.info
#     twohundred = stock.info['twoHundredDayAverage']
#     volume = stock.info['volume']
#     recs = stock.recommendations
#     lastClose = stock.info['previousClose']
#     percentBelow200 = (lastClose - twohundred) / twohundred * 100

#     hist = stock.history(period, interval)

#     hist.reset_index(inplace=True)
#     hist = hist.rename(columns={'index': 'Date', 'Close':'Price'})
#     hist = hist[['Date', 'Price', 'Volume']]

#     return (hist)
# print(analysisout(tickers))

def AlphaAnalysis (tickers):
    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={tickers}&apikey={alphavantage_key}'
    r = requests.get(url)
    data = r.json()
    del data["Meta Data"]
    df = pd.DataFrame.from_dict(data)
    return(df)
    
print(AlphaAnalysis(tickers))

    # return({'Short Name':stock.info.get('shortName'),
    #         "Two Hundred Day Price:": twohundred,
    #         "Previous Close Price:": stock.info.get('previousClose'),
    #         "Percent Difference:": percentBelow200,
    #         "Volume:": volume})
    # print(stockinfo.keys())
    # return()
# pd.set_option('display.max_columns',None)

# PDAnalasis = pd.DataFrame(analysisout(tickers))
# print(type(PDAnalasis))
#for key,value in stockinfo.items():
    #print(key,":",value)



