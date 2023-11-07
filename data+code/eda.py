
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#import statsmodels.api as sm

df = pd.read_csv('Sales-Superstore.csv')
#df.info()

df['Category'].value_counts().plot(kind = 'bar', label = 'Category', color = 'green')
plt.legend()

dff = df.loc[df['Category'] == 'Technology']
#print(dff['Sub-Category'].unique())
#print(dff.columns.to_list())

#Drop irrelevant columns
cols = ['Row ID', 'Ship Date', 'Ship Mode', 'Country','Category', 'Customer Name']
df0 = dff.drop(cols, axis = 1)
#df0.head(5)

df1 = df0.loc[df0['Segment'] == 'Consumer']
df0['Segment'].value_counts().plot(kind = 'bar', label = 'Segment', color = 'purple')
df1['Sub-Category'].value_counts().plot(kind = 'bar', label = 'Sub-Category', color = 'green')
plt.legend()

df2 = df1.loc[df1['Sub-Category'] == 'Phones']
cols1 = ['Segment', 'Sub-Category']
df3 = df2.drop(cols1, axis = 1)
#print(df3)

#plt.figure(figsize = (9, 6))
#df2['State'].value_counts().plot(kind = 'bar', label = 'State', color = 'violet')
#plt.legend()

cols2 = ['Product ID', 'Postal Code', 'City', 'Customer ID']
df4 = df3.drop(cols2, axis = 1)
df4['PPU']= df4['Sales']/df4['Quantity']
#df4.head(5)

dfE = df4.groupby('State').sum()
#dfE.head()
dfE.plot.bar(y = ['PPU','Quantity', 'Profit', 'Discount'], subplots = True, figsize = (10,8)) #x is dfE.index by default

df_Cal = df4.loc[df4['State'] == 'California']
df_Cal['Order Date'] = pd.to_datetime(df_Cal['Order Date'])
df11 = df_Cal.set_index('Order Date')
df_NY = df4.loc[df4['State'] == 'New York']
df_NY['Order Date'] = pd.to_datetime(df_NY['Order Date'])
df22 = df_NY.set_index('Order Date')
#print(df_Cal.shape, df_NY.shape)
#df11.info()
#df22.info()

plt.figure(figsize = (10, 6))
df11['Sales'].plot()
df11['Profit'].plot()
plt.title('California')
plt.legend()
plt.show()

plt.figure(figsize = (10, 6))
df11['Quantity'].plot()
plt.title('California')
plt.legend()
plt.show()

plt.figure(figsize = (10, 6))
df11['PPU'].plot()
plt.title('California')
plt.legend()
plt.show()

plt.figure(figsize = (10, 6))
df22['Sales'].plot()
df22['Profit'].plot()
plt.title('New York')
plt.legend()
plt.show()

plt.figure(figsize = (10, 6))
df22['Quantity'].plot()
plt.title('New York')
plt.legend()
plt.show()

plt.figure(figsize = (10, 6))
df22['PPU'].plot()
plt.title('New York')
plt.legend()
plt.show()

plt.scatter(df22['Quantity'], df22['PPU'])
sns.regplot(x = "Quantity", y = "PPU", data = df22)
plt.xlabel('Quantity')
plt.ylabel('PPU')
plt.title('New York')
plt.show()

vol_log = np.log(df22['Quantity'])
price_log = np.log(df22['PPU'])
sns.regplot(x = vol_log, y = price_log, data = df22)
plt.scatter(vol_log, price_log)
plt.xlabel('Log(Quantity)')
plt.ylabel('Log(PPU)')
plt.title('New York')
plt.show()

plt.scatter(df11['Quantity'], df11['PPU'])
sns.regplot(x = "Quantity", y = "PPU", data = df11)
plt.xlabel('Quantity')
plt.ylabel('PPU')
plt.title('California')
plt.show()

vol_log = np.log(df11['Quantity'])
price_log = np.log(df11['PPU'])
sns.regplot(x = vol_log, y = price_log, data = df11)
plt.title('Log Transforms')
plt.scatter(vol_log, price_log)
plt.xlabel('Log(Quantity)')
plt.ylabel('Log(PPU)')
plt.title('California')
plt.show()

#Simple Moving Average for forecasting
#Rolling statistics of monthly sales over 6 months
##moving_avg = df11.rolling(6).mean()
#moving_std = df11.rolling(6).std()
##plt.figure(figsize = (9, 6))
##orig = plt.plot(monthly_sales, color = 'blue',label = 'Actual sales')
##mean = plt.plot(moving_avg, color = 'red', label = 'Rolling Mean', linestyle = 'dotted')
#std = plt.plot(moving_std, color = 'black', label = 'Rolling Std')
##plt.legend(loc = 'best')
##plt.xlabel('Order Date')
##plt.title('Rolling Average of Sales')
##plt.show(block = False)

#Exponentially-weighted Moving Average for forecasting
#expwighted_avg = ts_log.ewm(halflife = 6).mean()

#plt.figure(figsize = (9, 6))
#orig = plt.plot(ts_log, color = 'blue', label = 'Actual sales')
#expmean = plt.plot(expwighted_avg, color = 'red', label = 'Exponentially-weighted mean')
#plt.legend(loc = 'best')
#plt.xlabel('Order Date')
#plt.ylabel('Log of Monthly Sales')
#plt.title('Exponentially-weighted Average of Sales (log transform)')
#plt.show(block = False)

#expwighted_avg = monthly_sales['Sales'].ewm(halflife = 6).mean() #The parameter ‘halflife’ defines the amount of exponential decay in the weights
#plt.figure(figsize = (9, 6))
#orig = plt.plot(monthly_sales['Sales'], color = 'blue', label = 'Actual sales')
#expmean = plt.plot(expwighted_avg, color = 'red', label = 'Exponentially-weighted mean')
#plt.legend(loc = 'best')
#plt.xlabel('Order Date')
#plt.ylabel('Monthly Sales')
#plt.title('Exponentially-weighted Average of Sales')
#plt.show(block = False)


