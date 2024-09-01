
import streamlit as st
from streamlit.connections import SQLConnection
from pandas import DataFrame
from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker


class DBClient(object):
    def __init__(self, db_conn_str: str) -> None:
        self._conn_str = db_conn_str
        self._engine: Engine = create_engine(self._conn_str)
        self._st_conn = None

    @property
    def engine(self) -> Engine:
        return self._engine

    @property
    def session(self):
        return sessionmaker(bind=self._engine)

    def query(self, sql: str, echo: bool):
        with self.session() as s:
            print(s.query(sql).all())

    @property
    def st_conn(self) -> SQLConnection:
        if not self._st_conn:
            self._st_conn = st.connection(
                "local_db",
                type="sql",
                url=self._conn_str,
            )
        return self._st_conn

    def st_query(self, sql: str, *args, **kwargs) -> DataFrame:
        print(sql)
        return self.st_conn.query(sql, ttl=1, *args, **kwargs)
