import os
import requests
from datetime import datetime

class Discord:
    
    def __init__(self, token, bot_id):
        self.webhook_url = f"https://discord.com/api/webhooks/{bot_id}/{token}"
        if not token or not bot_id:
            print("Discord token or bot id not found in environment variables")
    
    def send_alert(self, message: str, error, metadata):
        formated_msg = f"{message}: {str(error)}, {metadata}"
        date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        payload = {
            "embeds": [
                {
                    "title": "Token Inválido",
                    "description": formated_msg,
                    "fields": [
                        {"name": "Scraper", "value": str(metadata.get('scraper_name', 'N/A')), "inline": True},
                        {"name": "Date", "value": date_time, "inline": True},
                        {"name": "Token", "value": str(metadata.get('token', 'N/A')), "inline": True},
                        {"name": "Message", "value": formated_msg, "inline": False}
                    ],
                    "color": 15158332 
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