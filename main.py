import pandas as pd
from connection import DataReadCondition
from data_processing import  DictToDataFrame, DataCombiner, DataFetcher
import datetime



def main():
    urls = {
#        'total_circulating_bitcoin' : 'total-bitcoins',
        'market_price_usd' : 'market-price',    # The market price is how much you can sell 1 Bitcoin (BTC) for. 
#        'market_capitalization' : 'market-cap',
        'exchange_trade_volume' : 'trade-volume',   # The Bitcoin trading volume indicates how many Bitcoins are being bought and sold on specific exchanges.
        'blockchain_size' : 'blocks-size',  # The total size of the blockchain minus database indexes in megabytes.
        'average_block_size' : 'avg-block-size',    # The average block size over the past 24 hours in megabytes.
        'average_transactions_per_block' : 'n-transactions-per-block',  # The average number of transactions per block over the past 24 hours.
        'total_number_of_transactions' : 'n-transactions-total',    # The total number of transactions on the blockchain.
        'median_confirmation_time' : 'median-confirmation-time',    # The median time for a transaction with miner fees to be included in a mined block and added to the public ledger.
        'average_confirmation_time' : 'avg-confirmation-time',      # The average time for a transaction with miner fees to be included in a mined block and added to the public ledger.
        'total_hash_rate' : 'hash-rate',    # The estimated number of terahashes per second the bitcoin network is performing in the last 24 hours.
        'network_difficulty' : 'difficulty',    # A relative measure of how difficult it is to mine a new block for the blockchain.
        'miners_revenue' : 'miners-revenue',    # Total value in USD of coinbase block rewards and transaction fees paid to miners.
        'total_transactions_fees_btc' : 'transaction-fees', # The total BTC value of all transaction fees paid to miners. This does not include coinbase block rewards.
        'total_transactions_fees_usd' : 'transaction-fees-usd', # The total USD value of all transaction fees paid to miners. This does not include coinbase block rewards.
        'cost_%_of_transaction_volume' : 'cost-per-transaction-percent', # A chart showing miners revenue as percentage of the transaction volume.
        'cost_per_transaction' : 'cost-per-transaction',    # A chart showing miners revenue divided by the number of transactions.
        'unique_addresses_used' : 'n-unique-addresses', # The total number of unique addresses used on the blockchain.
        'confirmed_transactions_per_day' : 'n-transactions',    # The total number of confirmed transactions per day.
#        'transaction_rate_per_second' : 'transactions-per-second',
        'output_value_per_day' : 'output-volume',   # The total value of all transaction outputs per day. This includes coins returned to the sender as change.
#        'mempool_transaction_count' : 'mempool-count',
#        'mempool_size_growth' : 'mempool-growth',
#        'mempool_size_bytes' : 'mempool-size',
#        'unspent_transaction_outputs' : 'utxo-count',
        'transactions_excluding_popular_addresses' : 'n-transactions-excluding-popular',    # The total number of transactions excluding those involving the network's 100 most popular addresses.
        'estimated_transaction_value_btc' : 'estimated-transaction-volume', # The total estimated value in BTC of transactions on the blockchain. This does not include coins returned as change.
        'estimated_transaction_value_usd' : 'estimated-transaction-volume-usd'  # The total estimated value in USD of transactions on the blockchain. This does not include coins returned as change.
        }

    fetcher = DataFetcher(urls)
    df_list = fetcher.fetch_data()

    combiner = DataCombiner(df_list)
    combined_df = combiner.combine_data()

    print(combined_df)

if __name__ == '__main__':
    main()