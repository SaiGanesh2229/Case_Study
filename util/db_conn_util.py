import pyodbc
from util.util_properties import PropertyUtil


class DBConnection:
    connection = None

    @staticmethod
    def getConnectionOBJ():
        if DBConnection.connection is None:
            connection_string = PropertyUtil.getPropertyString()
            if not isinstance(connection_string, str) or not connection_string.strip():
                raise ValueError(
                    "The connection string is invalid. Please check the property configuration."
                )
            try:
                DBConnection.connection = pyodbc.connect(connection_string)
            except pyodbc.Error as e:
                print(f"Error while connecting to SQL database: {e}")
        return DBConnection.connection
