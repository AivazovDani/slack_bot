import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Set up Slack and OpenAI
app = App(token=os.getenv("SLACK_BOT_TOKEN"))
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Respond to direct messages
@app.message(".*")
def handle_message(message, say):
    user_input = message['text']

    # Call OpenAI (GPT-4) using the new API
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Отговаряй само на български език."},
            {"role": "user", "content": user_input}
        ]
    )

    reply = response.choices[0].message.content
    say(reply)

# Start the Slack Socket Mode handler
if __name__ == "__main__":
    handler = SocketModeHandler(app, os.getenv("SLACK_APP_TOKEN"))
    handler.start()
