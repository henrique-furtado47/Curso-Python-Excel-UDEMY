# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 09:51:51 2025

@author: User
"""

import pandas as pd
import numpy as np

df = pd.DataFrame(np.array([[1,2,3,],
                           [4,5,6],
                           [7,8,9]]), columns=['alpha','beta','cappa'])

df.columns = ['a','b','c']
df.index= ['m','n','o']

df_dict = pd.DataFrame({"a":[1,2,3]
                        ,"b":[3,4,5]
                        ,"c":[6,7,8]})


type(df["a"])
df[["a","b"]]

df.loc["m"]

df.loc["n":,"b":]

df.loc[['m','o'],['b','c']]