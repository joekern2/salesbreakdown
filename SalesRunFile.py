# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 11:23:14 2022

@author: jkern
"""

from SalesFunctions import *

## sales run file

master, eric, ryan, charles, shane = getFiles()

master = getTotals(master, eric, ryan, charles, shane)

with pd.ExcelWriter('MasterPL.xlsx',
                    mode='a', if_sheet_exists='replace') as writer:  
    master['Salesman P&L'].to_excel(writer, sheet_name='Total Salesman P&L')

