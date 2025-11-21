from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model.base import Base
from model.temperature import Temperature
import logging
import sys
sys.path.append("..")
import config.global_config as gc


class DbOperator:
    __database_url = gc.SQLALCHEMY_DATABASE_URI
    __engine = create_engine(__database_url)


    def create_db(self):
        try:
            Base.metadata.create_all(bind=self.__engine)
        except Exception as er:
            logging.info(f">> Ошибка при попытке создания базы данных. {er}")


    def create_commit(self, city_name, local_time, temperature):
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.__engine)
        session_local = SessionLocal()
        new_record = Temperature(
            city=city_name,
            l_time=local_time,
            temp=temperature
        )
        session_local.add(new_record)
        session_local.commit()