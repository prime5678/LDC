"""
Analyzing the relationship between CSCITLTL and KC2 COMDY weekly prices over the span of 10 years
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np    
from sklearn.metrics import r2_score

sheet = pd.read_excel('CERT.xlsx') #import relevant data

#drop all rows with NaN values
sheet = sheet.dropna()
#convert all values to numeric
#KC2 COMDTY already all float values, convert CSCITLTL to integer
new_cscitltl = []
for i in sheet['CSCITLTL']:
    if i[-1] == 'k':
        new_cscitltl.append(float(i[:-1]) * 1000)
    elif i[-1] == 'M':
        new_cscitltl.append(float(i[:-1]) * 1000000)
sheet['CSCITLTL'] = pd.Series(new_cscitltl, index=sheet.index)
#save the sheet to a new excel file
sheet.to_excel('CERT_cleaned.xlsx', index=False)
#create scatter plot of KC2 COMDTY vs CSCITLTL
plt.scatter(sheet['KC2 COMDTY'], sheet['CSCITLTL'], alpha=0.5)
plt.title('KC2 COMDTY vs CSCITLTL')
plt.xlabel('KC2 COMDTY')
plt.ylabel('CSCITLTL')
#plot a regression line
m, b = np.polyfit(sheet['KC2 COMDTY'], sheet['CSCITLTL'], 1)
plt.plot(sheet['KC2 COMDTY'], m*sheet['KC2 COMDTY'] + b, color='red', label='Regression Line')
plt.legend()
plt.show()
#print regression line R^2 value
r2 = r2_score(sheet['CSCITLTL'], m*sheet['KC2 COMDTY'] + b)
print(f'Linear Regression R^2 value: {r2:.4f}')

#Optimize regression line by using trig function
#Previous linear regression line will be downward trend line, use trig function to fith the data better
#need an increasing function for periodicity (k = 2 * pi / period) as well as amplitude (A)
#basic formula: y = A * sin(k * (x - x0)) + b
#where x0 is the phase shift