class TradeEngine:
    def __init__(self, kraken_client, notifier):
        self.kraken = kraken_client
        self.notifier = notifier
        self.symbol = 'BTC/USDT'
        self.position_open = False
        self.trade_amount = 0.001  # BTC amount

    async def execute_trade(self, signal):
        if signal == 'buy' and not self.position_open:
            order = await self.kraken.create_order(self.symbol, 'buy', self.trade_amount)
            if order:
                self.position_open = True
                await self.notifier.send(f"Bought {self.trade_amount} BTC - Order ID: {order['id']}")

        elif signal == 'sell' and self.position_open:
            order = await self.kraken.create_order(self.symbol, 'sell', self.trade_amount)
            if order:
                self.position_open = False
                await self.notifier.send(f"Sold {self.trade_amount} BTC - Order ID: {order['id']}")