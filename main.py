import pandas as pd
from connection import DataReadCondition
from data_processing import  DictToDataFrame



urls = {
        'total_circulating_bitcoin' : 'total-bitcoins',
        'market_price_usd' : 'market-price',
        'market_capitalization' : 'market-cap',
        'exchange_trade_volume' : 'trade-volume',
        'blockchain_size' : 'blocks-size',
        'average_block_size' : 'avg-block-size',
        'average_transactions_per_block' : 'n-transactions-per-block',
        'total_number_of_transactions' : 'n-transactions-total',
        'median_confirmation_time' : 'median-confirmation-time',
        'average_confirmation_time' : 'avg-confirmation-time',
        'total_hash_rate' : 'hash-rate',
        'network_difficulty' : 'difficulty',
        'miners_revenue' : 'miners-revenue',
        'total_transactions_fees_btc' : 'transaction-fees',
        'total_transactions_fees_usd' : 'transaction-fees-usd',
        'cost_%_of_transaction_volume' : 'cost-per-transaction-percent',
        'cost_per_transaction' : 'cost-per-transaction',
        'unique_addresses_used' : 'n-unique-addresses',
        'confirmed_transactions_per_day' : 'n-transactions',
        'transaction_rate_per_second' : 'transactions-per-second',
        'output_value_per_day' : 'output-volume',
        'mempool_transaction_count' : 'mempool-count',
        'mempool_size_growth' : 'mempool-growth',
        'mempool_size_bytes' : 'mempool-size',
        'unspent_transaction_outputs' : 'utxo-count',
        'transactions_excluding_popular_addresses' : 'n-transactions-excluding-popular',
        'estimated_transaction_value_btc' : 'estimated-transaction-volume',
        'estimated_transaction_value_usd' : 'estimated-transaction-volume-usd'
        }



def main():
    
    for url in urls:
        reader = DataReadCondition.create_reader('https://api.blockchain.info/charts/{}?timespan=4years&rollingAverage=12hours&format=json'.format(urls[url]))
        df = DictToDataFrame(reader.read()['values']).dict_to()
        df = df.set_index('x')
        print(df)



if __name__ == '__main__':
    main()