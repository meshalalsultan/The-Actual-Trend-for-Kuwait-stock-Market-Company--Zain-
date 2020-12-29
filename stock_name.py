#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 17:38:52 2020

@author: meshal
"""
import investpy 
import pandas as pd
import matplotlib as plt
import seaborn as sn
import numpy as np
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima_model import ARIMA
from pmdarima.arima import auto_arima
from sklearn.metrics import mean_squared_error, mean_absolute_error


df = investpy.get_stock_recent_data(stock='zain',
                                    country='KUWAIT')
print(df.head())



eur = investpy.get_currency_cross_recent_data(currency_cross='EUR/USD')
print(df.head())

#Stock Company Profile Retrieval

zain_profile = investpy.get_stock_company_profile(stock='zain',
                                                     country='KUWAIT')
print(zain_profile)

#rolling mean this period if time 

last_month_zain = investpy.get_stock_recent_data(stock='zain', country='kuwait', as_json=False,
order='ascending')

df['Close'].plot(figsize=(20,10), linewidth=5, fontsize=20)


close = df[['Close']]
close.rolling(12).mean().plot(figsize=(20,10), linewidth=5, fontsize=20)


open_price = df[['Open']]
open_price.rolling(12).mean().plot(figsize=(20,10), linewidth=5, fontsize=20)

df_rm = pd.concat([close.rolling(12).mean(), open_price.rolling(12).mean()], axis=1)
df_rm.plot(figsize=(20,10), linewidth=5, fontsize=20)

close.diff().plot(figsize=(20,10), linewidth=5, fontsize=20 , xlabel=('Date'))


#Take The Trend from data
import statsmodels.api as sm
df['Close'].plot()
zain_open , zain_close  = sm.tsa.filters.hpfilter(df['Close'])

df['trend'] = zain_close
df[['Close' , 'trend']].plot()





















