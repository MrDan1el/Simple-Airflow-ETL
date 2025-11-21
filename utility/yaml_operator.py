import yaml
import logging


class YamlOperator:

    @staticmethod
    def write_yaml(file_path, data):
        try:
            with open(file_path, 'w') as f:
                yaml.dump(data, f)
        except Exception as er:
            logging.info(f">> Ошибка при попытке записать yaml файл. {er}")


    @staticmethod
    def get_data_from_yaml(file_path):
        try:
            with open(file_path) as f:
                data = yaml.safe_load(f)
            return data
        except FileNotFoundError:
            logging.info(">> Ошибка: файл yaml не найден.")
        except Exception as er:
            logging.info(f">> Ошибка при попытке получения данных из yaml файла. {er}")