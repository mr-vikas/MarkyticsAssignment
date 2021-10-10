# Importing libraries
from pandas_datareader import data
import pandas as pd
import datetime

# Fetching Current and 90 days ago Date
current_date = datetime.datetime.now()
ago = datetime.timedelta(days = 90)
past_date = current_date-ago

# Reading Excel File that Contain Symbols
df = pd.read_excel("List of Stocks case study (1).xlsx")

# Defing function That Export Closings of All Symbols Present in File
def exportClosings(symbol):
  symbol = symbol.strip() # Removing extra spaces of symbols
  try:
    # Fetching Last 3 months Stock data from yahoo finance. Here we can also use paid api to fetch stock data.
    closing = data.DataReader(symbol, 'yahoo', past_date, current_date)
    # Exporting Closing data in data folder with the file name of symbol.
    closing['Close'].to_excel('data/'+symbol+'.xlsx')
  except:
    print('DataNotFound Of ',symbol)  # Handling Exception if Data not Found

# Apply Lambda function that itterate symbols.
df['SYMBOL    '].apply(exportClosings)
