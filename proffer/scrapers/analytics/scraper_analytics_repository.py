from datetime import datetime

from proffer.observability.analytics import AnalyticsRepository


class ScraperAnalyticsRepository(AnalyticsRepository):

  def __init__(self, db_connection):
    super().__init__(db_connection)

  
  def format_data(self, data):
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
        }