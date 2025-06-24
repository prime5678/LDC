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
print(f'Regression line: y = {m:.4f}x + {b:.4f}')
#Try using a polynomial regression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
# Create polynomial features
poly = PolynomialFeatures(degree=5)
X_poly = poly.fit_transform(sheet[['KC2 COMDTY']])
# Fit polynomial regression model
poly_model = LinearRegression()
poly_model.fit(X_poly, sheet['CSCITLTL'])
# Predict using the polynomial model
y_poly_pred = poly_model.predict(X_poly)
# Calculate R^2 score for polynomial regression
r2_poly = r2_score(sheet['CSCITLTL'], y_poly_pred)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(f'Polynomial Regression R^2 value: {r2_poly:.4f}')
# Plot the polynomial regression line
plt.scatter(sheet['KC2 COMDTY'], sheet['CSCITLTL'], alpha=
0.5, label='Data Points')   
plt.plot(sheet['KC2 COMDTY'], y_poly_pred, color='green', label='Polynomial Regression Line')
plt.title('KC2 COMDTY vs CSCITLTL (Polynomial Regression)')
plt.xlabel('KC2 COMDTY')
plt.ylabel('CSCITLTL')
plt.legend()
plt.show()
# Save the polynomial regression model coefficients
coefficients = poly_model.coef_
intercept = poly_model.intercept_
print(f'Polynomial Regression Coefficients: {coefficients}')
print(f'Polynomial Regression Intercept: {intercept:.4f}')
#print closed form solution for polynomial regression
print("Closed form solution for polynomial regression:")
for i, coef in enumerate(coefficients):
    if i == 0:
        print(f'y = {intercept:.4f}', end=' ')
    else:
        print(f'+ {coef:.4f}x^{i}', end=' ')
#try a curve fitting using scipy 
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")