# from typing import Any, Dict

# from proffer.services.database import DatabaseConnection
# from psycopg2 import sql


# class AnalyticsRepository:
#     def __init__(self, db_connection: DatabaseConnection):
#         self.db_connection = db_connection

#     def insert_data(self, table: str, data: Dict[str, Any]) -> None:
#         formatted_data = self.format_data(data)
#         try:
#             self.db_connection.connect()
#             columns = formatted_data.keys()
#             values = [formatted_data[column] for column in columns]

#             insert_query = sql.SQL(
#                 "INSERT INTO {table} ({fields}) VALUES ({values})"
#             ).format(
#                 table=sql.Identifier(table),
#                 fields=sql.SQL(',').join(map(sql.Identifier, columns)),
#                 values=sql.SQL(',').join(sql.Placeholder() * len(values))
#             )

#             with self.db_connection.connection.cursor() as cursor:
#                 cursor.execute(insert_query, values)
#                 self.db_connection.connection.commit()
#         except Exception as e:
#             print(f"An error occurred: {e}")
#             if self.db_connection.connection:
#                 self.db_connection.connection.rollback()
#         finally:
#             self.db_connection.close()


#     # create a template method for the repository to format data
#     def format_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
#         pass