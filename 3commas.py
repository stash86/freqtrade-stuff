# https://github.com/bogdanteodoru/py3cw

def confirm_trade_entry(self, pair: str, order_type: str, amount: float, rate: float,
                            time_in_force: str, current_time: datetime, **kwargs) -> bool:
        
        bot_id = 0 #replace this with your actual bot_id

        coin, currency = pair.split('/')

        p3cw = Py3CW(
            key='3commas_key_goes_here',
            secret='3commas_secret_goes_here',
        )

        logger.info(f"3Commas: Sending buy signal for {pair} to 3commas bot_id={bot_id}")

        error, data = p3cw.request(
            entity='bots',
            action='start_new_deal',
            action_id=f'{bot_id}',
            payload={
                "bot_id": bot_id,
                "pair": f"{currency}_{coin}",
            },
        )

        if error:
            logger.error(f"3Commas: {error['msg']}")
        else:
            logger.info(f"3Commas: {data['bot_events'][0]['message']}")
        
        PairLocks.lock_pair(
            pair=pair,
            until=datetime.now(timezone.utc) + timedelta(minutes=1),
            reason="Send 3c buy order"
        )

        return False  # we don't want to keep the trade in freqtrade db
