"""
Project 1: Time Series Analysis of Arabica Coffee

Abstract: One of the biggest priorities for LDC's trading operations is their ability to trade with increased volume - this is one of the rules for success that the firm has
maintained for years and contributes heavilty to the firm's success. Particulary with commodities, timing is very important because the cyclic production nature of crops also
affects the liquidity of the market annually, i.e. it can be fruitful to have a bigger market presence during periods of high expected participation than maintaining a presence
throughout the year. The power of timing enables the firm to casually deploy greater capital into enterprises, which might not be possible given that the firm is actively
trading uniformly throughout the year, where the number of available trades might be limited. The goal is to attempt to use time series data (of upwards 5 years at least) to
model the activity of Arabica coffee future contracts.
"""
#~~~~~~~~~~~To Do~~~~~~~~~~~
#1. Define function for importing data
#2. Define function for calculating spreads
#3. Define function for plotting data

#Coffee 'C' is the cert of Arabica coffee futures
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import blpapi
from xbbg import blp
from datetime import datetime

d = {3:'H', 5:'K', 7:'N', 9:'U', 12:'Z'} #information on ticker 

#Function accepting month + year and fetching relevant information
def get_past_prices(month, year):
    #first check to make sure month represents either March, May, July, September, or December
    valid_months = [3, 5, 7, 9, 12]
    if month not in valid_months:
        raise ValueError("Inputted month does not represent a valid future contract month for KC contracts")
    #then, check to make sure that the inputted month + date falls before the current date (otherwise different formatting required to get historical data)
    #assuming day is 28 to check for strictly less than 
    test_date = datetime(year, month, 30)
    current_date = datetime.now()
    if not (test_date < current_date):
        raise ValueError("Inputted date must fall before current month and year for past data retrieval")
    #total future timeline: from three years ago and one month ahead ---> current point in time 
    #therefore for December, would only want to decrement the year by 2 instead
    start_month, start_year, start_day = -1, -1, 1
    if (month != 12):
        start_month = month + 1
        start_year = year - 3
    else:
        start_month = 1
        start_year = year - 2
    end_day = 30
    #Now must generate a valid string to lookup
    
    ticker = 'KC'+ str(d[month]) + str(year % 1000) + " Comdty"
    end_date, start_date = "", ""
    if start_month > 9:
        start_date = str(start_year) + "-" + str(start_month) + "-0" + str(start_day)
        end_date = str(year) + "-0" + str(month) + "-" + str(end_day)
    elif month > 9:
        start_date = str(start_year) + "-0" + str(start_month) + "-0" + str(start_day)
        end_date = str(year) + "-" + str(month) + "-" + str(end_day)
    else:
        start_date = str(start_year) + "-0" + str(start_month) + "-0" + str(start_day)
        end_date = str(start_year) + "-0" + str(month) + "-0" + str(end_day)
    #I wonder why open, high, low, volume fields are not daily...
    fields = ['Last_Price']
    return blp.bdh(tickers = ticker, flds = fields, start_date = start_date, end_date = end_date)#now data is a multi-index



def graph_previous_data(month, year):
    df = get_past_prices(month, year)
    string = 'KC' + str(d[month]) + str(year % 1000)
    last_price_values = df[string + ' Comdty', 'Last_Price'].tolist() #extracts the price
    plt.plot([i for i in range(len(last_price_values))], last_price_values)
    plt.xlabel('Day')
    plt.ylabel('Price ($)')
    plt.title(string + 'Prices Since Inception')
    plt.show()

graph_previous_data(12, 2023)


