# freqtrade-stuff

DISCLAIMER : NEVER USE IT LIVE. IT'S BORKEN. YOU WILL LOOSE YOUR MONEY. I HAVE NO RESPONSABILITY INTO THIS !!!


###TrailingBuyStrat.py
TrailingBuyStrat is tirail's original one, using process_new_candle = False
TrailingBuyStrat2 is my modification of tirail's one, using process_new_candle = True
TrailingBuyStrat2a is a recent modified one, using uzirox's old dynamic offset (you can change it to their latest offset if you want) and I'm adding a sell_trend check to abort trailing if sell signal is triggered (this new feature is off by default. Turn it on if you want to use it)