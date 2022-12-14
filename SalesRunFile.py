# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 11:23:14 2022

@author: jkern
"""

from SalesFunctions import *

## sales run file

def run():

    master, charles, eric, ryan, shane, c = getFiles()
    
    master = getTotals(master, charles, eric, ryan, shane, c)
    
# =============================================================================
#     with pd.ExcelWriter('MasterPL.xlsx',
#                         mode='a', if_sheet_exists='replace') as writer:  
#         master['Salesman P&L'].to_excel(writer, sheet_name='Data')
# =============================================================================

    CSV = convert_df(master['Salesman P&L'])

    st.download_button(label='Download Current Result',
                                data=CSV,
                                file_name= 'Master P&L.xlsx')





if __name__ == '__main__':
    run()