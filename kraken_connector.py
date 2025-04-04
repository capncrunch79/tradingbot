import ccxt.async_support as ccxt
import os

class KrakenClient:
    def __init__(self):
        self.exchange = ccxt.kraken({
            'apiKey': os.getenv('KRAKEN_API_KEY'),
            'secret': os.getenv('KRAKEN_API_SECRET'),
            'enableRateLimit': True,
        })

    async def fetch_market_data(self, symbol: str, timeframe: str = '1m'):
        try:
            ohlcv = await self.exchange.fetch_ohlcv(symbol, timeframe)
            return ohlcv
        except Exception as e:
            print(f"[ERROR] Kraken market data fetch failed: {e}")
            return None

    async def create_order(self, symbol: str, side: str, amount: float):
        try:
            if side == 'buy':
                order = await self.exchange.create_market_buy_order(symbol, amount)
            else:
                order = await self.exchange.create_market_sell_order(symbol, amount)
            return order
        except Exception as e:
            print(f"[ERROR] Order execution failed: {e}")
            return None

    async def close(self):
        await self.exchange.close()