# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 11:23:11 2022

@author: jkern
"""

import numpy as np
import pandas as pd
import streamlit as st
import os

### read excel functions
def getFiles():
    dtot = 0
    dCharles = 0
    dEric = 0
    dRyan = 0
    dShane = 0
    check = 0
    
    filename = 'MasterPL.xlsx'
    xl_filetot = pd.ExcelFile(filename)
    
    dtot = {sheet_name: xl_filetot.parse(sheet_name) 
              for sheet_name in xl_filetot.sheet_names}
    

    uploaded_filec = st.file_uploader("Upload sheet for Charles")
    if uploaded_filec is not None:
        #read xls or xlsx
        filec=pd.ExcelFile(uploaded_filec)
        dCharles = {sheet_name: filec.parse(sheet_name) 
                    for sheet_name in filec.sheet_names} 
    else:
        st.warning("you need to upload a csv or excel file.")
        
        
    uploaded_filee = st.file_uploader("Upload sheet for Eric")
    if uploaded_filee is not None:
        #read xls or xlsx
        filee=pd.ExcelFile(uploaded_filee)
        dEric = {sheet_name: filee.parse(sheet_name) 
                    for sheet_name in filee.sheet_names} 
    else:
        st.warning("you need to upload a csv or excel file.")
        
        
    uploaded_filer = st.file_uploader("Upload sheet for Ryan")
    if uploaded_filer is not None:
        #read xls or xlsx
        filer=pd.ExcelFile(uploaded_filer)
        dRyan = {sheet_name: filer.parse(sheet_name) 
                    for sheet_name in filer.sheet_names} 
    else:
        st.warning("you need to upload a csv or excel file.")
        
        
    uploaded_files = st.file_uploader("Upload sheet for Shane")
    if uploaded_files is not None:
        #read xls or xlsx
        files=pd.ExcelFile(uploaded_files)
        dShane = {sheet_name: files.parse(sheet_name) 
                    for sheet_name in files.sheet_names} 
    else:
        st.warning("you need to upload a csv or excel file.")
        
    
    selection = st.radio(
    "Who\'s P&L would you like to see?",
    ('All', 'Charles', 'Eric', 'Ryan', 'Shane'))
    
    check = 100
    
    if selection == 'All':
        check = 0
    elif selection == 'Charles':
        check = 1
    elif selection == 'Eric':
        check = 2
    elif selection == 'Ryan':
        check = 3
    elif selection == 'Shane':
        check = 4
# =============================================================================
#     filename = '~/Documents/BrentProj/EricPL.xlsx'
#     xl_fileEric = pd.ExcelFile(filename)
#     
#     dEric = {sheet_name: xl_fileEric.parse(sheet_name) 
#               for sheet_name in xl_fileEric.sheet_names}
#     
#     
#     filename = '~/Documents/BrentProj/RyanPL.xlsx'
#     xl_fileRyan = pd.ExcelFile(filename)
#     
#     dRyan = {sheet_name: xl_fileRyan.parse(sheet_name) 
#               for sheet_name in xl_fileRyan.sheet_names}
#     
#     filename = '~/Documents/BrentProj/CharlesPL.xlsx'
#     xl_fileCharles = pd.ExcelFile(filename)
#     
#     dCharles = {sheet_name: xl_fileCharles.parse(sheet_name) 
#               for sheet_name in xl_fileCharles.sheet_names}
#     
#     
#     filename = '~/Documents/BrentProj/ShanePL.xlsx'
#     xl_fileShane = pd.ExcelFile(filename)
#     
#     dShane = {sheet_name: xl_fileShane.parse(sheet_name) 
#               for sheet_name in xl_fileShane.sheet_names}
# =============================================================================
    
    return dtot, dCharles, dEric, dRyan, dShane, check


def getTotals(master, c1, c2, c3, c4, c):
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
        x, y = sumNewTrucks(c1, c2, c3, c4, month, c)
        master['Salesman P&L']['Unnamed: 2'][13 + i] = x
        master['Salesman P&L']['Unnamed: 2'][9] += x
        master['Salesman P&L']['Unnamed: 3'][13 + i] = y
        master['Salesman P&L']['Unnamed: 3'][9] += y
        
        a, b = sumOldTrucks(c1, c2, c3, c4, month, c)
        master['Salesman P&L']['Unnamed: 4'][13 + i] = a
        master['Salesman P&L']['Unnamed: 4'][9] += a
        master['Salesman P&L']['Unnamed: 5'][13 + i] = b
        master['Salesman P&L']['Unnamed: 5'][9] += b
        
        master['Salesman P&L']['Unnamed: 6'][13 + i] = x + a
        master['Salesman P&L']['Unnamed: 6'][9] += x + a
        master['Salesman P&L']['Unnamed: 7'][13 + i] = y + b
        master['Salesman P&L']['Unnamed: 7'][9] += y + b
        
        z = sumCommission(c1, c2, c3, c4, month, c)
        master['Salesman P&L']['Unnamed: 8'][2] += z
    
    master['Salesman P&L']['Unnamed: 2'][10] = master['Salesman P&L']['Unnamed: 2'][9]
    master['Salesman P&L']['Unnamed: 3'][10] = master['Salesman P&L']['Unnamed: 3'][9]
    master['Salesman P&L']['Unnamed: 4'][10] = master['Salesman P&L']['Unnamed: 4'][9]
    master['Salesman P&L']['Unnamed: 5'][10] = master['Salesman P&L']['Unnamed: 5'][9]
    master['Salesman P&L']['Unnamed: 6'][10] = master['Salesman P&L']['Unnamed: 6'][9]
    master['Salesman P&L']['Unnamed: 7'][10] = master['Salesman P&L']['Unnamed: 7'][9]
    
    return master


def sumNewTrucks(c1, c2, c3, c4, month, c):
    x = 0
    y = 0
    
    if c == 0 or c == 1:
        x = c1[month]['Unnamed: 4'][25]
        y = c1[month]['Unnamed: 5'][25]
    if c == 0 or c == 2:
        x += c2[month]['Unnamed: 4'][25]
        y += c2[month]['Unnamed: 5'][25]
    if c == 0 or c == 3:
        x += c3[month]['Unnamed: 4'][25]
        y += c3[month]['Unnamed: 5'][25]
    if c == 0 or c == 4:
        x += c4[month]['Unnamed: 4'][25]
        y += c4[month]['Unnamed: 5'][25]
    
    return x, y
    
    
def sumOldTrucks(c1, c2, c3, c4, month, c):
    x = 0
    y = 0
    
    if c == 0 or c == 1:
        x = c1[month]['Unnamed: 8'][25]
        y = c1[month]['Unnamed: 9'][25]
    if c == 0 or c == 2:
        x += c2[month]['Unnamed: 8'][25]
        y += c2[month]['Unnamed: 9'][25]
    if c == 0 or c == 3:
        x += c3[month]['Unnamed: 8'][25]
        y += c3[month]['Unnamed: 9'][25]
    if c == 0 or c == 4:
        x += c4[month]['Unnamed: 8'][25]
        y += c4[month]['Unnamed: 9'][25]
        
    return x, y


def sumCommission(c1, c2, c3, c4, month, c):
    x = 0
    if c == 0 or c == 1:
        x = c1[month]['Unnamed: 14'][25]
    if c == 0 or c == 2:
        x += c2[month]['Unnamed: 14'][25]
    if c == 0 or c == 3:
        x += c3[month]['Unnamed: 14'][25]
    if c == 0 or c == 4:
        x += c4[month]['Unnamed: 14'][25]

    
    return x


# =============================================================================
# @st.cache
# def convert_df(df):
#     # IMPORTANT: Cache the conversion to prevent computation on every rerun
#     return df.to_csv().encode('utf-8')
# 
# =============================================================================
