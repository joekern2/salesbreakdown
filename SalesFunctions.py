# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 11:23:11 2022

@author: jkern
"""

import numpy as np
import pandas as pd
import os

### read excel functions
def getFiles():
    filename = '~/Documents/BrentProj/MasterPL.xlsx'
    xl_filetot = pd.ExcelFile(filename)
    
    dtot = {sheet_name: xl_filetot.parse(sheet_name) 
              for sheet_name in xl_filetot.sheet_names}
    
    
    filename = '~/Documents/BrentProj/EricPL.xlsx'
    xl_fileEric = pd.ExcelFile(filename)
    
    dEric = {sheet_name: xl_fileEric.parse(sheet_name) 
              for sheet_name in xl_fileEric.sheet_names}
    
    
    filename = '~/Documents/BrentProj/RyanPL.xlsx'
    xl_fileRyan = pd.ExcelFile(filename)
    
    dRyan = {sheet_name: xl_fileRyan.parse(sheet_name) 
              for sheet_name in xl_fileRyan.sheet_names}
    
    filename = '~/Documents/BrentProj/CharlesPL.xlsx'
    xl_fileCharles = pd.ExcelFile(filename)
    
    dCharles = {sheet_name: xl_fileCharles.parse(sheet_name) 
              for sheet_name in xl_fileCharles.sheet_names}
    
    
    filename = '~/Documents/BrentProj/ShanePL.xlsx'
    xl_fileShane = pd.ExcelFile(filename)
    
    dShane = {sheet_name: xl_fileShane.parse(sheet_name) 
              for sheet_name in xl_fileShane.sheet_names}
    
    return dtot, dEric, dRyan, dCharles, dShane


def getTotals(master, c1, c2, c3, c4):
    master['Salesman P&L']['Unnamed: 2'][9] = 0
    master['Salesman P&L']['Unnamed: 3'][9] = 0
    master['Salesman P&L']['Unnamed: 4'][9] = 0
    master['Salesman P&L']['Unnamed: 5'][9] = 0
    master['Salesman P&L']['Unnamed: 6'][9] = 0
    master['Salesman P&L']['Unnamed: 7'][9] = 0
    #commission
    master['Salesman P&L']['Unnamed: 8'][2] = 0
    for i in range(12):
        month = master['Salesman P&L']['SALESMAN P&L'][13:25].iloc[i]
        x, y = sumNewTrucks(c1, c2, c3, c4, month)
        master['Salesman P&L']['Unnamed: 2'][13 + i] = x
        master['Salesman P&L']['Unnamed: 2'][9] += x
        master['Salesman P&L']['Unnamed: 3'][13 + i] = y
        master['Salesman P&L']['Unnamed: 3'][9] += y
        
        a, b = sumOldTrucks(c1, c2, c3, c4, month)
        master['Salesman P&L']['Unnamed: 4'][13 + i] = a
        master['Salesman P&L']['Unnamed: 4'][9] += a
        master['Salesman P&L']['Unnamed: 5'][13 + i] = b
        master['Salesman P&L']['Unnamed: 5'][9] += b
        
        master['Salesman P&L']['Unnamed: 6'][13 + i] = x + a
        master['Salesman P&L']['Unnamed: 6'][9] += x + a
        master['Salesman P&L']['Unnamed: 7'][13 + i] = y + b
        master['Salesman P&L']['Unnamed: 7'][9] += y + b
        
        z = sumCommission(c1, c2, c3, c4, month)
        master['Salesman P&L']['Unnamed: 8'][2] += z
    
    master['Salesman P&L']['Unnamed: 2'][10] = master['Salesman P&L']['Unnamed: 2'][9]
    master['Salesman P&L']['Unnamed: 3'][10] = master['Salesman P&L']['Unnamed: 3'][9]
    master['Salesman P&L']['Unnamed: 4'][10] = master['Salesman P&L']['Unnamed: 4'][9]
    master['Salesman P&L']['Unnamed: 5'][10] = master['Salesman P&L']['Unnamed: 5'][9]
    master['Salesman P&L']['Unnamed: 6'][10] = master['Salesman P&L']['Unnamed: 6'][9]
    master['Salesman P&L']['Unnamed: 7'][10] = master['Salesman P&L']['Unnamed: 7'][9]
    
    return master


def sumNewTrucks(c1, c2, c3, c4, month):
    x = c1[month]['Unnamed: 4'][25]
    x += c2[month]['Unnamed: 4'][25]
    x += c3[month]['Unnamed: 4'][25]
    x += c4[month]['Unnamed: 4'][25]
    
    y = c1[month]['Unnamed: 5'][25]
    y += c2[month]['Unnamed: 5'][25]
    y += c3[month]['Unnamed: 5'][25]
    y += c4[month]['Unnamed: 5'][25]
    
    return x, y
    
    
def sumOldTrucks(c1, c2, c3, c4, month):
    x = c1[month]['Unnamed: 8'][25]
    x += c2[month]['Unnamed: 8'][25]
    x += c3[month]['Unnamed: 8'][25]
    x += c4[month]['Unnamed: 8'][25]
    
    y = c1[month]['Unnamed: 9'][25]
    y += c2[month]['Unnamed: 9'][25]
    y += c3[month]['Unnamed: 9'][25]
    y += c4[month]['Unnamed: 9'][25]
    
    return x, y


def sumCommission(c1, c2, c3, c4, month):
    x = c1[month]['Unnamed: 14'][25]
    x += c2[month]['Unnamed: 14'][25]
    x += c3[month]['Unnamed: 14'][25]
    x += c4[month]['Unnamed: 14'][25]

    
    return x



