import pandas as pd
import logging


class CsvOperator:

    def __init__(self, data):
        self.__data = pd.DataFrame(data)


    def write_csv(self, file_path):
        try:
            self.__data.to_csv(file_path, index=False)
        except Exception as er:
            logging.info(f">> Ошибка при попытке записать csv файл. {er}")
          
            
    @staticmethod
    def read_my_csv(file_path):
        try:
            data = pd.read_csv(file_path)
            return data
        except Exception as er:
            logging.info(f">> Ошибка при попытке прочитать csv файл. {er}")