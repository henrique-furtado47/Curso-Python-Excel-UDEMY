# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 09:20:06 2025

@author: User
"""

import pandas as pd

data = pd.read_excel("data.xlsx", sheet_name= "Orders", header=3, index_col="Row ID")

data.columns

data["Postal Code"] = data["Postal Code"].astype(str)
data["Order Date"] = data["Order Date"].astype(str)

data["Order Date"] = pd.to_datetime(data["Order Date"], errors="raise", format="%Y-%m-%d")
data['Month'] = data["Order Date"].dt.month
data['Year'] = data["Order Date"].dt.year
data['Processing Time'] = data["Order Date"] - data["Ship Date"]

data["String Date"] = data["Order Date"].dt.strftime("%b-%Y")