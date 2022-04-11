#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 20:39:30 2020

@author: rvw
"""

import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator)
import matplotlib.cm as cm
import seaborn as sns
import datetime
import numpy as np



txt_df = pd.read_csv('/Users/robertvanderweele/git/surfs_up/resources/51004h2021.csv')

#remove 1st row contains erronous characters
txt_df = txt_df.iloc[1:]


#Rename Year column
txt_df = txt_df.rename(columns={'#YY': 'year', 'MM': 'month', 'DD': 'day', 'hh': 'hour', 'mm': 'minute'})


txt_df['Date'] = pd.to_datetime(txt_df[['year','month','day', 'hour', 'minute']])
txt_df = txt_df.drop(["year", "month", "day", "hour", "minute"], axis=1)
txt_df['DateC'] = txt_df['Date']
#txt_df['DateC'] = pd.to_timedelta(txt_df.DateC).dt.total_seconds().astype(int)
txt_df.set_index("Date", inplace = True) 
#df1 = pd.concat([txt_df, txt_df['WVHT'].mul([3.280839], axis=0).add_prefix('new_WVHT')], axis=1)
               
print(txt_df)  
txt_df.dtypes
#txt_df.to_csv("wave.csv")  

txt_df[["WVHT", "DPD", "APD", "MWD"]] = txt_df[["WVHT", "DPD", "APD", "MWD"]].apply(pd.to_numeric, errors='coerce')
txt_df['WVHT'] = txt_df.loc[:,'WVHT'] * 3.28
txt_df = txt_df[txt_df.DPD != 99]


textstr1 = "  ".join(map(str, ('Maximum Swell Height =', (round(txt_df["WVHT"].max(),1)),"feet")))
textstr2 = "  ".join(map(str, ('Average Swell Height =', (round(txt_df["WVHT"].mean(),1)),"feet")))
textstr3 = "  ".join(map(str, ('Maximum Swell Period =', txt_df["DPD"].max(),"sec")))
textstr4 = "  ".join(map(str, ('Average Swell Period =', (round(txt_df["DPD"].mean(),1)),"sec")))
textstr5 = "  ".join(map(str, ('Northern Most Swell Direction =', txt_df["MWD"].max(),"Deg")))
textstr6 = "  ".join(map(str, ('Southern Most Swell Direction =', txt_df["MWD"].min(),"Deg")))
textstr7 = "  ".join(map(str, ('Average Swell Direction =',(round(txt_df["MWD"].mean(),0)),"Deg")))
#d = txt_df["Date"].max()
# plotting

fig,ax = plt.subplots(3,sharex=True, figsize=(22, 16))
txt_df.WVHT.plot(ax=ax[0])
ax[0].set_title('Buoy Station 51004 Southeast Hawaii - Swell Data', fontsize=24)
ax[0].set_ylabel('Height (feet)',fontsize=16)
ax[0].tick_params(axis='y', which='major', labelsize=10)
ax[0].annotate(textstr1, xy=(0, 0), xycoords='axes fraction', xytext= (0.15, 0.95), textcoords='axes fraction')
ax[0].annotate(textstr2, xy=(0, 0), xycoords='axes fraction', xytext= (0.15, 0.90), textcoords='axes fraction')

  
txt_df.DPD.plot(ax=ax[1])
ax[1].set_ylabel('Period (sec)',fontsize=16)
ax[1].tick_params(axis='y', which='major', labelsize=10)
ax[1].annotate(textstr3, xy=(0, 0), xycoords='axes fraction', xytext= (0.15, 0.95), textcoords='axes fraction')
ax[1].annotate(textstr4, xy=(0, 0), xycoords='axes fraction', xytext= (0.15, 0.90), textcoords='axes fraction')

txt_df.MWD.plot(ax=ax[2])
ax[2].set_ylabel('Direction (Deg)',fontsize=16)
ax[2].set_xlabel('Date',fontsize=16)
ax[2].xaxis.set_major_locator(MultipleLocator(8))
ax[2].tick_params(axis='both', which='major', labelsize=10)
ax[2].annotate(textstr5, xy=(0, 0), xycoords='axes fraction', xytext= (0.51, 0.95), textcoords='axes fraction')
ax[2].annotate(textstr6, xy=(0, 0), xycoords='axes fraction', xytext= (0.51, 0.90), textcoords='axes fraction')
ax[2].annotate(textstr7, xy=(0, 0), xycoords='axes fraction', xytext= (0.51, 0.85), textcoords='axes fraction')


sns.despine()

#plt.show()
plt.savefig("/Users/robertvanderweele/git/surfs_up/Images/DataBouy_plot(2021).png")

      