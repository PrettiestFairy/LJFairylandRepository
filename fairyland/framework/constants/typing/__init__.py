# coding: utf8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 03 03, 2024
"""

from typing import Literal, Union
from pymysql.connections import Connection
from pymysql.cursors import Cursor
from psycopg2.extensions import connection
from psycopg2.extensions import cursor

# log level
TypeLogLevel = Literal["TRACE", "DEBUG", "INFO", "SUCCESS", "WARNING", "ERROR", "CRITICAL"]

# Database connection
TypeSQLConnection = Union[Connection, connection]
# Database cursor
TypeSQLCursor = Union[Cursor, cursor]
