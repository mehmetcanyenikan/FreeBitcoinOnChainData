from abc import ABC, abstractmethod
import pandas as pd
from connection import DataReadCondition



class ConvertData(ABC):

    def __init__(self, dictionary):
        self.dictionary = dictionary
    
    @abstractmethod
    def dict_to(self):
        pass



class DictToDataFrame(ConvertData):

    def dict_to(self) -> pd.DataFrame:
        return pd.DataFrame(self.dictionary)



class DataFetcher:
    def __init__(self, urls):
        self.urls = urls

    def fetch_data(self):
        df_list = []
        for url_key, url_value in self.urls.items():
            reader = DataReadCondition.create_reader(f'https://api.blockchain.info/charts/{url_value}?timespan=6years&rollingAverage=24hours&format=json')
            df = DictToDataFrame(reader.read()['values']).dict_to()
            df = df.set_index('x')
            df.index = pd.to_datetime(df.index, unit='s').date

            df.columns = [f"{url_key}_{col}" for col in df.columns]
            df_list.append(df)
        return df_list



class DataCombiner:
    def __init__(self, data_frames):
        self.data_frames = data_frames

    def combine_data(self):
        return pd.concat(self.data_frames, axis=1)
