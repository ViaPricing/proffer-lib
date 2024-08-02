import psycopg2

class DatabaseConnection:
    def __init__(self, host: str, dbname: str, user: str, password: str, port: int = 5432):
        self.host = host
        self.dbname = dbname
        self.user = user
        self.password = password
        self.port = port
        self.connection = None

    def connect(self):
        self.connection = psycopg2.connect(
            host=self.host,
            dbname=self.dbname,
            user=self.user,
            password=self.password,
            port=self.port
        )

    def close(self):
        if self.connection:
            self.connection.close()