from datetime import datetime
import requests
import logging
import sys
sys.path.append('..')
import config.global_config as gc


class RequestOperator:
    __api_key = gc.API_KEY_WEATHER
    __URL = gc.URL


    def __get_data(self, city):
        url = f'{str(self.__URL)}?q={str(city)}&key={str(self.__api_key)}'
        try:
            r = requests.get(url=url)
            result = r.json()
            return result
        except Exception as er:
            logging.info(f">> Ошибка при попытке получения данных по API реквесту. {er}")


    @staticmethod
    def __get_temp_dict(data, city):
        try:
            temp_dict = {
                'city': city,
                'date': str(datetime.now().date()),
                'l_time': data.get('location').get('localtime')[-5:],
                'temp c': data.get('current').get('temp_c')
            }
            return temp_dict
        except Exception as er:
            logging.info(f">> Ошибка при попытке получить словарь с данными для {city}. {er}")


    def get_temp_list(self, cities):
        temp_list = list()
        try:
            for city in cities:
                data = self.__get_data(city)
                temp_dict = RequestOperator.__get_temp_dict(data, city)
                temp_list.append(temp_dict)
            return temp_list
        except Exception as er:
            logging.info(f">> Ошибка при попытке получить список температур. {er}")