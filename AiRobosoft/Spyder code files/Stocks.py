import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv('AAPL Historical Data.csv', usecols = [0,1,2,3,4])

POHL_avg=data[['Price','Open','High','Low']].mean(axis=1)

x=np.arange(1,len(data)+1,1)

plt.plot(x,POHL_avg,'r',label='Apple stocks')