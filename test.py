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

#Create function to accept ticker and correctly place .csv files in directory
#New directory is C:\Users\GREGOE\DOwnloads\LDC\LDCData\
#Should store .csv files of future pricings from 2000 - 2025
df = blp.bdp(tickers='NVDA US Equity', flds = ['Security_Name', 'GICS_Sector_Name'])
print(df)