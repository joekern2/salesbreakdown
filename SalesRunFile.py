# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 11:23:14 2022

@author: jkern
"""

from SalesFunctions import *

## sales run file

def run():

    master, charles, eric, ryan, shane, c, mc, c1c, c2c, c3c, c4c = getFiles()
    
    if mc == 1:
        master = getTotals(master, charles, eric, ryan, shane, c, c1c, c2c, c3c, c4c)
    
# =============================================================================
#     with pd.ExcelWriter('MasterPL.xlsx',
#                         mode='a', if_sheet_exists='replace') as writer:  
#         master['Salesman P&L'].to_excel(writer, sheet_name='Data')
# =============================================================================
    
    temp = master['Salesman P&L'][['SALESMAN P&L', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4',
                                   'Unnamed: 5', 'Unnamed: 6', 'Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9',
                                   'Unnamed: 10', 'Unnamed: 11', 'Unnamed: 12', 'Unnamed: 13']]
    temp = temp[14:26]
    st.dataframe(temp)

    if mc == 1:
        CSV = convert_df(master['Salesman P&L'])

    if c == 0:
        string = 'Master'
    elif c == 1:
        string = 'Charles'
    elif c == 2:
        string = 'Eric'
    elif c == 3:
        string = 'Ryan'
    elif c == 4:
        string = 'Shane'
        
    string += ' P&L.csv'
    
    if mc == 1:
        st.download_button(label='Download Current Result',
                                    data=CSV,
                                    file_name= string)





if __name__ == '__main__':
    run()