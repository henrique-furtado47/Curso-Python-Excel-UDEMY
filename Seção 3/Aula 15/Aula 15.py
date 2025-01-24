# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 10:08:02 2025

@author: User
"""

import pandas as pd

data = pd.read_excel("data_2.xlsx")

data.isna().sum()
data[data.isna().sum(axis = 1)>0]

data.dropna(axis=0, how='any', inplace=True)
data.fillna(0)