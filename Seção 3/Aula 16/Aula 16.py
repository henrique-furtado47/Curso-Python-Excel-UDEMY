# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 10:37:00 2025

@author: User
"""
import pandas as pd


menu = pd.DataFrame({"Item":['Pizza',"Pasta","Salad","Burrito","Taco","Burger"],
                     "Price":[14.99, 12.99, 7.99, 10.99, 6.99, 5.99],
                     "Popularity":["High","Medium","Low","High","Medium","High"]})


nutrition = pd.DataFrame({"Item":["Pizza","Pastry","Burrito","Salad","Pasta"],
                         "Avg_Calorie":[3200,800, 940, 240, 740],
                        "Protein":["12%","4%","16%","6%","10%"]})


# Concatenate

pd.concat([menu, nutrition], axis=1, ignore_index=False)

# Merge

menu.merge(nutrition, how="inner")
menu.merge(nutrition, how="outer")
menu.merge(nutrition, how="left")
menu.merge(nutrition, how="right")


# Join

menu.set_index("Item", inplace=True)
menu.reset_index(inplace=True)

menu.set_index("Item").join(nutrition.set_index("Item"))
