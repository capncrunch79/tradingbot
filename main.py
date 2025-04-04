import asyncio
from strategies.strategy_manager import StrategyManager
from kraken_connector import KrakenClient
from trade_engine import TradeEngine
from notifier import Notifier
from dashboard.app import start_dashboard
import os
from dotenv import load_dotenv

load_dotenv()

kraken = KrakenClient()
notifier = Notifier()
strategy_manager = StrategyManager()
trade_engine = TradeEngine(kraken, notifier)

async def main_loop():
    while True:
        market_data = await kraken.fetch_market_data('BTC/USDT')
        signal = strategy_manager.evaluate_all(market_data)

        if signal:
            await trade_engine.execute_trade(signal)

        await asyncio.sleep(60)

if __name__ == '__main__':
    start_dashboard()  # Flask runs in a separate thread
    asyncio.run(main_loop())