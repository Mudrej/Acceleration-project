# -*- coding: cp1251 -*-

import pandas as pd

def data_preparation(path):
    MunicipalObjects = {202:"�����������", 204:"�����������", 206:"���������", 
                        208:"�����������", 210:"������������", 212:"������������", 
                        215:"������������", 217:"������������", 220:"����������-�������", 
                        223:"�����������", 225:"��������", 226:"�����������", 
                        227:"����������", 230:"�������", 234:"���������", 
                        237:"������������", 240:"����������", 242:"���������", 
                        244:"����������", 246:"��������", 248:"��������������", 
                        250:"����������", 253:"����������", 256:"������", 
                        258:"���������", 401:"������", 405:"�������", 
                        410:"������", 415:"������"
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
            Settl.update({MunicipalObjects[DT.iloc[i,0]]: [DT.iloc[Start_Cut:i,1],len(DT.iloc[Start_Cut:i,1])]})
            Start_Cut = i + 1
    Settl.update({MunicipalObjects[DT.iloc[DT.shape[0]-1,0]]: [DT.iloc[Start_Cut:DT.shape[0]-1,1],int(len(DT.iloc[Start_Cut:DT.shape[0]-1,1]))]})

    del DT
    
    for i in Settl:
        Settl[i][0] = int(Settl[i][0].mean())

    return(Settl)