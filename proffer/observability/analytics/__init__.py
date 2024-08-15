# import os
# from typing import Any, Dict

# from proffer.services.database import DatabaseConnection
# from proffer.observability.analytics.analytics_repository import AnalyticsRepository


# def send_to_analytics(table: str, data: Dict[str, Any]) -> None:
#     db_connection = DatabaseConnection(
#         host=os.getenv('DB_HOST', 'localhost'),
#         dbname=os.getenv('DB_NAME', 'poc_elk'),
#         user=os.getenv('DB_USER', 'postgres'),
#         password=os.getenv('DB_PASSWORD', 'postgres'),
#         port=int(os.getenv('DB_PORT', 5432))
#     )
    
#     analytics_repo = AnalyticsRepository(db_connection)
    
#     analytics_repo.insert_data(table, data)    