from flask import Flask, render_template, request
from flask_caching import Cache
from uuid import uuid4
import os, random, requests

app = Flask(__name__)

CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
CLIENT_ID = os.environ.get("CLIENT_ID")
URI = 'https://savescraperforreddit.herokuapp.com'


def get_access_token():
    auth = requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
    
    code = request.args.get('code') 
    data = {'grant_type' : 'authorization_code',
            'code' : code,
            'redirect_uri' : URI}

    headers = {'User-agent' : 'SaveScraper 0.1 by u/AciidSkull'}

    access_token = requests.post('https://ssl.reddit.com/api/v1/access_token', auth=auth, data=data, headers=headers)
    token = access_token.json()

    return token['access_token']

@app.route('/')
def index():
    random_string = str(uuid4())
    url = f"https://www.reddit.com/api/v1/authorize?client_id={CLIENT_ID}&response_type=code&state={random_string}&redirect_uri={URI}&duration=temporary&scope=history"
    Obj = None
    if (request.args.get('code')):
        Token = get_access_token()
        response = requests.get("https://oauth.reddit.com/api/v1/me", headers={"Authorization" : "bearer " + Token}).json()
        Obj = response['name']

    return render_template('index.html', auth_url=url, Obj=Obj)

if __name__ == '__main__':
    port = os.environ.get('PORT', 5000)
    app.run(debug=True, host='0.0.0.0', port=port)