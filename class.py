import importlib 
import numpy as np
import pandas as pd
import yfinance as yf
import plot_module as pm

importlib.reload(pm)

class Stock:

    
    index=["2021","2022","2023","2024"]
    

    def __init__(self, ticker):

        self.ticker = ticker
        self.data = {
        'EPS': [],
        'Revenue': [],
        'ROCE': [],
        'Gross Profit': []
        }
        self.stock_access = yf.Ticker(self.ticker)
        self.fin = pd.DataFrame(self.stock_access.financials.T)
        self.fin.reset_index(drop=True,inplace=True)
        self.bal = pd.DataFrame(self.stock_access.balance_sheet.T)
        self.bal.reset_index(drop=True,inplace=True)
        self.eps()
        self.revenue()
        self.roce()
        self.gross_profit()
       
    def eps(self):

        self.data['EPS'] = np.flip(np.array(self.fin.loc[0:3, 'Basic EPS']))

    def revenue(self):

        self.data['Revenue'] = np.flip(np.array(self.fin.loc[0:3, 'Total Revenue']))

    def roce(self):

        total_assets = np.array(self.bal.loc[0:3, 'Total Assets'])
        total_lib = np.array(self.bal.loc[0:3, 'Current Liabilities'])

        capital_emp = np.array(total_assets-total_lib)

        ebit = np.array(self.fin.loc[0:3, 'EBIT'])

        cal_roce = (ebit/capital_emp*100)

        # round_roce = []

        # for i in cal_roce:
        #     round_roce.append(round(i))

        self.data['ROCE'] = np.flip(cal_roce)
    
    
    def gross_profit(self):
        
        self.data['Gross Profit']=np.flip(np.array(self.fin.loc[0:3,'Gross Profit']))
        


st1=input("Enter the name of 1st stock: ")
st2=input("Enter the name of the 2nd stock: ")

stock1=Stock(st1)
stock2=Stock(st2)

print(f"Enter the plot theme:\n")
print(f"Dark:1\n")
print(f"Light:2\n")
theme=int(input("Enter option: "))



pm.plot_comparison(stock1,stock2,theme)



u_decision=str(input("Do you want to import data to excel: (y/n)"))

if u_decision=='y' or u_decision=='Y':
    
    data1=pd.DataFrame(stock1.data)
    data2=pd.DataFrame(stock2.data)
    
    data1.to_excel(f"{stock1.ticker}_data.xlsx",index=stock1.index)
    data2.to_excel(f"{stock2.ticker}_data.xlsx",index=stock2.index)





