
#data will be in following format

#  ticker = str()

#     data = {
#         'EPS': [],
#         'Revenue': [],
#         'ROCE': [],
#         'Gross Profit': []
#     }

import matplotlib.pyplot as plt 

def plot_comparison(st1,st2,theme):
    
    if theme==1:
        col='black'
        marker_col='white'
    else:
        col='white'
        marker_col='black'
        

    
    fig=plt.figure(figsize=(10,6))
    fig.suptitle(f"{st1.ticker} vs {st2.ticker}")
    fig.set_facecolor('yellow')
    plt.subplots_adjust(hspace=.5,wspace=.5)
    
    
    ax=plt.subplot(2,2,1)
    ax.set_facecolor(col)
    plt.plot(st1.index,st1.data['EPS'],label=st1.ticker,marker='o',markerfacecolor=marker_col)
    plt.plot(st2.index,st2.data['EPS'],label=st2.ticker,marker='o',markerfacecolor=marker_col)
    plt.title('EPS')
    plt.xlabel('Years')
    plt.ylabel('EPS')
    plt.legend()
        
    ax=plt.subplot(2,2,2)
    ax.set_facecolor(col)
    plt.plot(st1.index,st1.data['Revenue'],label=st1.ticker,marker='o',markerfacecolor=marker_col)
    plt.plot(st2.index,st2.data['Revenue'],label=st2.ticker,marker='o',markerfacecolor=marker_col)
    plt.title('Revenue')
    plt.xlabel('Years')
    plt.ylabel('Revenue')
    plt.legend()
    
    ax=plt.subplot(2,2,3)
    ax.set_facecolor(col)
    plt.plot(st1.index,st1.data['ROCE'],label=st1.ticker,marker='o',markerfacecolor=marker_col)
    plt.plot(st2.index,st2.data['ROCE'],label=st2.ticker,marker='o',markerfacecolor=marker_col)
    plt.title('ROCE')
    plt.xlabel('Years')
    plt.ylabel('ROCE')
    plt.legend()
    
    ax=plt.subplot(2,2,4)
    ax.set_facecolor(col)
    plt.plot(st1.index,st1.data['Gross Profit'],label=st1.ticker,marker='o',markerfacecolor=marker_col)
    plt.plot(st2.index,st2.data['Gross Profit'],label=st2.ticker,marker='o',markerfacecolor=marker_col)
    plt.title('Gross Profit')
    plt.xlabel('Years')
    plt.ylabel('Gross Profit')
    plt.legend()
    
    
    plt.show()
    