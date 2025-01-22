# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 11:12:39 2025

@author: User
"""
from collections import Counter
import pandas as pd

data = pd.read_csv("VRA_2024_06.csv", delimiter=';')

log_flights = Counter(data["Situação Voo"])
print(f"""Vôos realizados: {log_flights['REALIZADO']}
      Vôos Cancelados: {log_flights['CANCELADO']}
      Não Informado: {log_flights['NÃO INFORMADO']}""")
     
