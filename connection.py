import requests
import pandas as pd
from abc import ABC, abstractmethod



class DataRead(ABC):

    def __init__(self, source : str):
        self.source = source
    
    @abstractmethod
    def read(self) -> dict:
        pass



class BlockchainComAPI(DataRead):
    
    def read(self) -> dict:
        try:
            return requests.get(self.source).json()
        except: 
            return print("An error")



class CsvFile(DataRead):

    def read(self) -> pd.DataFrame:
        try:
            return pd.read_csv(self.source)
        except:
            return print('Csv file not found.')



class ExcelFile(DataRead):

    def read(self) -> pd.DataFrame:
        try:
            return pd.read_excel(self.source)
        except:
            return print('Excel file not found.')
        


class DataReadCondition:
    @staticmethod
    def create_reader(source: str) -> DataRead:
        if 'csv' in source:
            return CsvFile(source)
        elif 'xlsx' in source:
            return ExcelFile(source)
        elif 'api' in source:
            return BlockchainComAPI(source)
        else:
            raise ValueError('Unsupported data source type.')