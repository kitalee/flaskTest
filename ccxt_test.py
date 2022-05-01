import ccxt
import pprint

# link against the asynchronous version of ccxt
#import ccxt.async_support as ccxt 

# print(ccxt.exchanges)

binance = ccxt.binance()
binance_market = binance.load_markets()

btcusdt = binance.fetch_ticker("BTC/USDT")

pprint.pprint(btcusdt)
# print(type(binance))

# print(binance_market)