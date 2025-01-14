# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 10:55:24 2025

@author: User
"""

import numpy as np

np_array = np.array([12, 6 ,34, -2, 7, 28])

np_array.max()
np.max(np_array)
np_array.argmax()

np.sort(np_array) #retorna uma cópia
np_array.sort() #substitui a variavel original

np_2d_array = np.array([[4,4,1,26,71],
                        [78,6,8,2,10],
                        [34,341,242,142,5]])

np.sort(np_2d_array, axis=1) #ordena as linhas
np.sort(np_2d_array, axis=0) #ordena as colunas

