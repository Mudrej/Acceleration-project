# -*- coding: cp1251 -*-

import pandas as pd

def data_preparation(path):
    MunicipalObjects = {202:"Ермишинский", 204:"Захаровский", 206:"Кадомский", 
                        208:"Касимовский", 210:"Клепиковский", 212:"Кораблинский", 
                        215:"Милославский", 217:"Михайловский", 220:"Александро-Невский", 
                        223:"Пителинский", 225:"Пронский", 226:"Путятинский", 
                        227:"Рыбновский", 230:"Ряжский", 234:"Рязанский", 
                        237:"Сапожковский", 240:"Сараевский", 242:"Сасовский", 
                        244:"Скопинский", 246:"Спасский", 248:"Старожиловский", 
                        250:"Ухоловский", 253:"Чучковский", 256:"Шацкий", 
                        258:"Шиловский", 401:"Рязань", 405:"Касимов", 
                        410:"Сасово", 415:"Скопин"
                        }

    # Data import  
    DT = pd.read_excel(path)
    
    # Preliminary processing: removing columns and sorting
    DT = DT.iloc[:,[1,23]]
    DT = DT.sort_values(DT.columns[0])
    for i in range(DT.shape[0]):
        DT.iloc[i,0] = int((DT.iloc[i,0] // 1000000) % 1000)
    
    # Creating a dictionary of settlements and deleting the original data table
    Settl = {}
    Start_Cut = 0
    for i in range(DT.shape[0] - 1):
        if DT.iloc[i,0] != DT.iloc[i+1,0]:
            Settl.update({MunicipalObjects[DT.iloc[i,0]]: [DT.iloc[Start_Cut:i,1], len(DT.iloc[Start_Cut:i,1])]})
            Start_Cut = i + 1
    Settl.update({MunicipalObjects[DT.iloc[DT.shape[0]-1,0]]: [DT.iloc[Start_Cut:DT.shape[0]-1,1], len(DT.iloc[Start_Cut:DT.shape[0]-1,1])]})
    del DT
    
    for i in Settl:
        Settl[i].append(list(Settl[i][0].round()))
        Settl[i][0] = int(Settl[i][0].mean())
    return(Settl)