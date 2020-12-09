"""pip install yahoo_fin - on CMD

use: stock_info.get_live_price() -> to call live stock price of stock required
"""



from yahoo_fin import stock_info 
from tkinter import *
from datetime import date, timedelta
import matplotlib.pyplot as plt

  
  
def stock_price_checker(): 
    stockprice = stock_info.get_live_price(e1.get()) 
    Current_stock.set(stockprice) 

    longResult = stock_info.get_data(e1.get(), date.today() - timedelta(60), date.today())
    Date = []
    Price = [openPrice[0] for openPrice in longResult.values] 
    for i in range(len(Price)):
        Date.append(i)
    
    plt.plot(Date, Price)
    plt.title('Last ' + str(len(Price)) + ' price points for ' + e1.get())
    plt.xlabel('Day')
    plt.ylabel('Price')
    plt.show()
  
  
master = Tk() 
Current_stock = StringVar() 
  
Label(master, text="Company Symbol : ").grid(row=0, sticky=W) 
Label(master, text="Stock Result:").grid(row=3, sticky=W) 
  
result2 = Label(master, text="", textvariable=Current_stock, 
                ).grid(row=3, column=1, sticky=W) 
  
e1 = Entry(master) 
e1.grid(row=0, column=1) 
  
b = Button(master, text="Show", command=stock_price_checker) 
b.grid(row=0, column=2, columnspan=2, rowspan=2, padx=5, pady=5) 
  
mainloop() 