# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 10:27:51 2025

@author: User
"""

import pandas as pd

data = pd.read_excel("data.xlsx", sheet_name="Orders", header = 3, index_col ="Row ID")

data.head()
data.tail()
data.dtypes
data.describe()
data.columns
data.drop("Product Name", axis=1, inplace=True)
data.drop(["Product Name", "Ship Date"], axis = 1)

data["Per Unit Sale"] = data["Sales"]/data["Quantity"]
     

data.to_excel("data_2.xlsx", index=False)
