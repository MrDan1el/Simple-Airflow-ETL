from utility.yaml_operator import YamlOperator
from utility.request_operator import RequestOperator
from utility.csv_operator import CsvOperator
from utility.db_operator import DbOperator
from datetime import datetime
import sys
sys.path.append('..')
import config.global_config as gc


class Main:
    __yaml_file_path = gc.FILE_PATH
    __cities = list()
    __temp_list = list()
    __csv_file_path = ''


    def __get_cities(self):
        self.__cities = YamlOperator.get_data_from_yaml(str(self.__yaml_file_path) + r'/cities.yaml')


    def __send_request(self):
        o_requester = RequestOperator()
        self.__temp_list = o_requester.get_temp_list(self.__cities)


    def __write_data_to_csv(self):
        o_csv = CsvOperator(self.__temp_list)
        self.__csv_file_path = gc.FILE_PATH2 + datetime.now().strftime("\%Y-%m-%d_%H-%M-%S.csv")
        o_csv.write_csv(self.__csv_file_path)


    def __send_data_to_db(self):
        o_db = DbOperator()

        for record in self.__temp_list:
            o_db.create_commit(record.get('city'), record.get('date') + ' ' + record.get('l_time'), record.get('temp c'))


    def run(self):
        self.__get_cities()
        self.__send_request()
        self.__write_data_to_csv()

        # o_db = DbOperator()
        # o_db.create_db()

        self.__send_data_to_db()