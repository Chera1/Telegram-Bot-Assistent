from binance.client import Client


def main(api_key, api_secret):
    client = Client(api_key, api_secret)
    tickers = client.get_all_tickers()
    all_coins = {}
    results = ''
    for coin in tickers:
        c, price = coin.values()
        all_coins[c] = price

    info = client.get_account()

    for coins in info['balances']:
        coin, free, locked = coins.values()
        if float(free) > 0 or float(locked) > 0:
            if 'LD' in coin:
                coin = coin[2:]
            try:
                summ = float(all_coins[coin + 'USDT']) * float(free)
                # results += coin.ljust(8) + free.ljust(16) + '$' + str(summ).ljust(15) + '~' + '  ' + '₽' + str(
                #     summ * float(all_coins['USDTRUB'])) + '\n'
                rub = (summ * float(all_coins["USDTRUB"]))
                results += f'{coin.ljust(8)} {float(free):.5f} ${summ:.2f} ~ ₽{rub:.2f}\n'
            except KeyError:
                # results += coin.ljust(8) + free.ljust(16) + '\n'
                results += f'{coin.ljust(8)} {float(free):.5f} \n'
    print(results)
    return results


if __name__ == "__main__":
    main(api_key='mchf4hZ1JQikoNpma0SlNtP7it9Rv8qoo5wyv41ypDIXAVjPrtfBMyVIt6EqLXPG',
         api_secret='ZRXG7mMukVpR4YRr6NWyZ5oVGNFFjudjt7eUIoJAPOjlUTFj8U2YeCPBC1Zyy1Re')
