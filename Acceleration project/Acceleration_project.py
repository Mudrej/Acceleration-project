# -*- coding: cp1251 -*-

import numpy as np
import pandas as pd

# Data import 
excel_path = input('Enter the path to the excel file and name: ') 
DT = pd.read_excel(excel_path)

# Preliminary processing: removing columns and sorting
DT.drop(columns = ['Код субъекта РФ','Арктическая зона','Федеральный округ','Участок переписи населения','Номер домохозяйства','Пол'], axis = 1, inplace = True)
DT.sort_values(by = 'Код населенного пункта')

# Creating a dictionary of settlements and deleting the original data table
Settl = {}
Start_Cut = 0
for i in range(DT.shape[0]-1):
    if DT.iloc[i,0] != DT.iloc[i + 1,0]:
        Settl.update({DT.iloc[i,0]: DT.iloc[Start_Cut:i]})
        Start_Cut = i + 1
del DT

print(Settl, len(Settl))
