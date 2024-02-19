import pandas as pd
from binance.client import Client
import pytz
from datetime import datetime
import os
from time import sleep

# Test to verify API

api_key = "my API_key"
api_secret = "my API_secret"
client = Client(api_key, api_secret)
def obter_dados_ticker(symbol):
  ticker = client.get_ticker(symbol=symbol)
  return {
        f"{symbol} Preço Atual": float(ticker['lastPrice']),
        f"{symbol} Máximo 24h": float(ticker['highPrice']),
        f"{symbol} Mínimo 24h": float(ticker['lowPrice']),
        f"{symbol} Variação Percentual 24h": float(ticker['priceChangePercent']),
        f"{symbol} Volume 24h": float(ticker['volume']),
        f"{symbol} Número de Negociações": int(ticker['count']),
    }
