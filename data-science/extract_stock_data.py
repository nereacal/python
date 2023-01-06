import yfinance as yf
import pandas as pd

### STOCK INFO
# Crear un objeto Ticker para acceder a los metodos y extraer data. El símbolo para Apple es 'AAPL'
apple = yf.Ticker("AAPL")

# 'info' para extraer información sobre el stock
apple_info = apple.info

# obtener el 'country'
apple_info['country']

# 'history()' para obtener el precio de una participación en un periodo (con 'period')
# The options for period are 1 day (1d), 5d, 1 month (1mo) , 3mo, 6mo, 1 year (1y), 2y, 5y, 10y, ytd, and max.
# El formato de respuesta es Pandas DataFrame. Con 'Date' como índice y Open, High, Low, Close, Volume y Stock Splits para la fecha dada
apple_share_price_data = apple.history(period="max")
apple_share_price_data.head()

# Reseteamos el indice con 'reset_index' y 'inplace' = True para que se efectúe el cambio
apple_share_price_data.reset_index(inplace=True)



### EXTRAER DIVIDENDOS
# Con 'dividens' obtenemos el dataframe de los datos del periodo establecido en 'history'
apple.dividends
apple.dividends.plot()

amd = yf.Ticker("AMD")
amd_info = amd.info
amd_share_price_data = amd.history(period="max")
print(amd_share_price_data.head())


