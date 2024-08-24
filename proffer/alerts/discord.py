import os
import requests
from datetime import datetime

class Discord:
    
    def __init__(self, token, bot_id):
        self.webhook_url = f"https://discord.com/api/webhooks/{bot_id}/{token}"
        if not token or not bot_id:
            print("Discord token or bot id not found in environment variables")
    
    def send_alert(self, message: str, error, metadata):
        date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        description = (
            f"Scraper: {metadata.get('scraper_name', 'N/A')}\n"
            f"Date: {date_time}\n"
            f"Token: {metadata.get('token', 'N/A')}\n"
            f"Erro: {str(error)}"
        )
        
        payload = {
            "embeds": [
                {
                    "title": message,
                    "description": description,
                    "color": 15158332,
                    "thumbnail": {
                        "url": ""  # Adicionar a thumbnail da Proffer
                    }
                }
            ]
        }
        
        try:
            response = requests.post(self.webhook_url, json=payload)
            if not response.ok:
                print(f"Failed to send alert to Discord: {response.status_code} {response.reason}")
        except requests.RequestException as e:
            print(f"Failed to send alert to Discord: {str(e)}")
            

def get_discord_bot():
    token = os.getenv("DISCORD_TOKEN")
    bot_id = os.getenv("DISCORD_BOT_ID")
    return Discord(token, bot_id)