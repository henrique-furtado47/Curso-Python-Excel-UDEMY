# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 09:42:08 2025

@author: User
"""

import numpy as np
import pandas as pd

np_array = np.array([2,6,3,1])

pd_series = pd.Series(np_array, index=["a",'b','c','d'])

pd_series2 = pd.Series({'a':2, 'b':6, 'c': 1, 'd':3})

pd_series['b']
pd_series[['b','d']]

pd_series2[2:] 
pd_series2[1:3]