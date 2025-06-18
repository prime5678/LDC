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
import investpy as ip
import datetime as dt
#since dealing with certs, each ticker always should start with 'KC'
def get_historical_data(ticker: str):
    if ticker[0:2] != 'KC':
        raise ValueError("Ticker must start with 'KC' for Arabica coffee futures.")
    valid_months = {'H': 3, 'K': 5, 'N': 7, 'U': 9, 'Z': 12}
    if ticker[2] not in valid_months.keys():
        raise ValueError(f"Invalid month code in ticker. Valid months are: {list(valid_months.keys())}")
    #need to process the ticker to determine if the date falls before or after 2000 to get historical info
    #only need about 25 years of data, so we can process dates that go maximum back to 2000
    year = int(ticker[3:])
    if year >= 3 and year <= 29:
        #create the start date
        if valid_months[ticker[2]] < 9:
            start_date = "0" + str(valid_months[ticker[2]] + 1) + "/01/" + str(year + 1997)
            end_date = "0" + str(valid_months[ticker[2]]) + "/30/" + str(year + 2000)
        elif valid_months[ticker[2]] == 9:
            start_date = str(valid_months[ticker[2]] + 1) + "/01/" + str(year + 1997)
            end_date = "0" + str(valid_months[ticker[2]]) + "/30/" + str(year + 2000)
        elif valid_months[ticker[2]] == 12:
            start_date = "01/01/" + str(year + 1998)
            end_date = "12/31/" + str(year + 2000)
    else:
        raise ValueError("Year in ticker must be between 3 and 29 inclusive.")