import os
import requests

class Discord:
    
    def __init__(self):
        discord_token = os.getenv("DISCORD_TOKEN")
        discord_bot_id = os.getenv("DISCORD_BOT_ID")
        self.webhook_url = f"https://discord.com/api/webhooks/{discord_bot_id}/{discord_token}"
        if not discord_token or not discord_bot_id:
            print("Discord token or bot id not found in environment variables")
    
    def send_alert(self, message: str, error, metadata):
        formated_msg = f"{message}: {str(error)}, {metadata}"
        payload = {
            "content": formated_msg
        }
        try:
            response = requests.post(self.webhook_url, json=payload)
            if not response.ok:
                print(f"Failed to send alert to Discord: {response.status_code} {response.reason}")
        except requests.RequestException as e:
            print(f"Failed to send alert to Discord: {str(e)}")
            

def discord_bot():
    return Discord()