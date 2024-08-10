from typing import Any, Dict
from datetime import datetime
from proffer.services.database import DatabaseConnection
from proffer.observability.analytics.analytics_repository import AnalyticsRepository
import requests
import os


def send_to_analytics(table: str, data: Dict[str, Any]) -> None:
    # db_connection = DatabaseConnection(
    #     host=os.getenv('DB_HOST', 'localhost'),
    #     dbname=os.getenv('DB_NAME', 'poc_elk'),
    #     user=os.getenv('DB_USER', 'postgres'),
    #     password=os.getenv('DB_PASSWORD', 'postgres'),
    #     port=int(os.getenv('DB_PORT', 5432))
    # )
    
    # analytics_repo = AnalyticsRepository(db_connection)
    
    # analytics_repo.insert_data(table, data)

    dto = format_data(data)

    url = os.getenv("HASURA_URL")
    headers = {
        "Content-Type": "application/json",
        "x-hasura-admin-secret": os.getenv("HASURA_ADMIN_SECRET"),
    }

    if not url or not headers["x-hasura-admin-secret"]:
       print("Missing HASURA_URL or HASURA_ADMIN_SECRET")
       return
        
    requests.post(url, json={"object": dto}, headers=headers)
    
def format_data(data):
  return {
          'id': data['id'],
          'ean': data['ean'],
          'estado': data.get('codestado', None),
          'curva': data.get('curva', None),
          'grupo': data.get('grupo', None),
          'qtd_itens': data.get('qtd_itens', None),
          'nome': data.get('scraper_name', None),
          'erro': data.get('type_error', None),
          'timestamp': datetime.now().isoformat(),
          'municipio': data.get('municipio', None),
          'descricao': data.get('descricao', None),
          'categoria': data.get('categoria', None),
          'status': data.get('status', None),
      }