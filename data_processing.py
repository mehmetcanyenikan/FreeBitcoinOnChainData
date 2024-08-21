from abc import ABC, abstractmethod
import pandas as pd



class ConvertData(ABC):

    def __init__(self, dictionary):
        self.dictionary = dictionary
    
    @abstractmethod
    def dict_to(self):
        pass



class DictToDataFrame(ConvertData):

    def dict_to(self) -> pd.DataFrame:
        return pd.DataFrame(self.dictionary)

