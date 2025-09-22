print("✅ bot.py is starting up")

import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Tokens from environment
bot_token = os.getenv("SLACK_BOT_TOKEN")
app_token = os.getenv("SLACK_APP_TOKEN")

# Initialize bot
app = App(token=bot_token)

# Simple test: reply to any message
@app.event("message")
def handle_message_events(body, say):
    say("👋 Здрасти, видях ти съобщението")

if __name__ == "__main__":
    print("🚀 Starting bot...")
    SocketModeHandler(app, app_token).start()
