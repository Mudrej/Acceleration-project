# -*- coding: cp1251 -*-

import numpy as np
import pandas as pd

excel_path = input('Enter the path to the excel file and name: ')

DT = pd.read_excel(excel_path)

print(DT)
