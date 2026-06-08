from flask import Flask
import threading
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'TechVJ - Bot is Running Successfully!'

def run_web_server():
    # Hugging Face default port 7860 read karta hai
    port = int(os.environ.get("PORT", 7860))
    app.run(host='0.0.0.0', port=port)

# Background mein web server chalu karne ke liye thread
threading.Thread(target=run_web_server, daemon=True).start()
