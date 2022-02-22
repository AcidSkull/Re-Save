from flask import Flask, render_template
import os, random

app = Flask(__name__)

REDDIT_TOKEN = os.environ.get("REDDIT_TOKEN")
CLIENT_ID = os.environ.get("CLIENT_ID")
RANDOM_STRING = random.randint(16)
URI = 'https://savescraperforreddit.herokuapp.com'

url = f"https://www.reddit.com/api/v1/authorize?client_id={CLIENT_ID}&response_type=code&state={RANDOM_STRING}&redirect_uri={URI}&duration=temporary&scope=history"

@app.route('/')
def index():
    return render_template('index.html', auth=url)

if __name__ == '__main__':
    port = os.environ.get('PORT', 5000)
    app.run(debug=True, host='0.0.0.0', port=port)