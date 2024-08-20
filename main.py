import requests
import pandas as pd
from abc import ABC, abstractmethod

# Blockchain.com API URLs
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


#### for Data Read ####
class DataReadAPI(ABC):
    def __init__(self, api_url : str):
        self.api_url = api_url
    
    @abstractmethod
    def read_json(self) -> dict:
        pass
        


class BlockchainCom(DataReadAPI):
    
    def read_json(self) -> dict:
        try:
            return requests.get(self.api_url).json()
        except: 
            return print("An error")


#### for convert data ####

class ConvertData(ABC):
    def __init__(self, dictionary : dict):
        self.dictionary = dictionary
    
    @abstractmethod
    def dict_to(self):
        pass

class DictToDataFrame(ConvertData):
    def dict_to(self):
        return pd.DataFrame(self.dictionary)


class index_set:
    def __init__(self, df : pd.DataFrame):
        self.df = df
    
    def setting(self):
        return self.df.set_index('x')

def main():
    
    for url in urls:
        blockchain_com = BlockchainCom(api_url= 'https://api.blockchain.info/charts/{}?timespan=3years&format=json'.format(urls[url]))
        df = DictToDataFrame(blockchain_com.read_json()['values']).dict_to()
        
        indexing = index_set(df = df)
        df_time_index = indexing.setting()
        print(type(df_time_index))
        
if __name__ == '__main__':
    main()