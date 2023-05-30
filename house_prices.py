# Import packages
import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Retrieve prices with an interval of 1 month for the last 10 years
sp500 = yf.download(tickers='ES=F', period='20y', interval='1mo') # SP500 futures
housing = yf.download(tickers='^HGX', period='20y', interval='1mo') # Housing price index US construction companies
rates = yf.download(tickers='^TNX', period='20y', interval='1mo') # Treasury yield 10 years USD

# Normalize all data around index 100
sp500Norm = sp500['Close'] / sp500['Close'][0] * 100
housingNorm = housing['Close'] / housing['Close'][0] * 100
ratesNorm = rates['Close'] / rates['Close'][-1] * 100

# Average change per year
sp500Diff = (sp500Norm[-1] - sp500Norm[0]) / 20
housingDiff = (housingNorm[-1] - housingNorm[0]) / 20
ratesDiff = (ratesNorm[-1] - ratesNorm[0]) / 20

print('The S&P 500 increased with ' + str(round(sp500Diff, 2)) + ' % on average over the last 20 years.')
print('The house prices increased with ' + str(round(housingDiff, 2)) + ' on average over the last 20 years.')
print('The 10-year treasury interest rates decreased with ' + str(round(ratesDiff, 2)) + ' on average over the last 20 years.')

# Plot result
fig, ax = plt.subplots()

ax.plot(sp500.index, sp500Norm, linewidth=1.0, color='b', label='S&P500')
ax.plot(housing.index, housingNorm, linewidth=1.0, color='r', label='Housing')
ax.plot(rates.index, ratesNorm, linewidth=1.0, color='g', label='Treasury rates')

ax.set_xlabel('Time (Year)')
ax.set_ylabel('Indexed value (-)')
ax.set_title('S&P500, housing prices and 10-year USD treasury rates for the last 20 years')
ax.legend()

plt.savefig('SP500andHousingOverTime.png')
plt.show()