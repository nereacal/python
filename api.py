import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.offline import plot
import matplotlib.pyplot as plt
import datetime
from pycoingecko import CoinGeckoAPI
from mplfinance.original_flavor import candlestick2_ohlc

diccionario = {'a':[11,21,31],'b':[12,22,32]}

# objeto panda con constructor de API Lingo Dataframe para crear una instancia.
df = pd.DataFrame(diccionario)
type(df) # pandas.core.frame.DataFrame
df.head() #  a   b
      #  0  11  12
      #  1  21  22
      #  2  31  32

# para hacer una llamada a la pi de coinGeckoApi para crear un gráfico en forma de candel con el valor de bitcoin en 30 con una observación de 24 horas por dia, 1 por hora.
# Sacaremos el valor máximo, el mínimo, el de apertura y el de cierre
cg = CoinGeckoAPI()
bitcoin_data = cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='usd', days=30) # Devuelve un json con toda la información de los precios, market caps, volumnenes totales...
bitcoin_price_data = bitcoin_data['prices']
bitcoin_price_data[0:5]

# Convertir esta información en un Panda Dataframe
data = pd.DataFrame(bitcoin_price_data, columns=['Timestamp', 'Price'])

# Convertir el timestamp en Date y mapear cada timestap para que sea un datetime legible
data['date'] = data['Timestamp'].apply(lambda d: datetime.date.fromtimestamp(d/1000.0))

# Agrupar por fecha y encontrar el maximo y el minimo, la apertura y el cierre para cada candle stick
candlestick_data = data.groupby(data.date, as_index=False).agg({"Price": ['min', 'max', 'first', 'last']})

# Usar Plotly para crear el gráfico candle stick. Se abrirá una ventana en el navegador con el gráfico :DDDD
fig = go.Figure(data=[go.Candlestick(x=candlestick_data['date'],
                open=candlestick_data['Price']['first'], 
                high=candlestick_data['Price']['max'],
                low=candlestick_data['Price']['min'], 
                close=candlestick_data['Price']['last'])
                ])

fig.update_layout(xaxis_rangeslider_visible=False)

fig.show()