from flask import Flask, render_template, request, session
from datetime import datetime
from uuid import uuid4
import os, requests, praw

app = Flask(__name__)
app.secret_key = str(uuid4)

CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
CLIENT_ID = os.environ.get("CLIENT_ID")
URI = 'https://savescraperforreddit.herokuapp.com'
USER_AGENT = 'SaveScraperForReddit/0.2.1 by u/AciidSkull'
SCOPE = ['identity', 'read', 'history']

def get_access_token(code):
    auth = requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
    
    data = {'grant_type' : 'authorization_code',
            'code' : code,
            'redirect_uri' : URI}

    headers = {'User-agent' : USER_AGENT}

    access_token = requests.post('https://ssl.reddit.com/api/v1/access_token', auth=auth, data=data, headers=headers)
    token = access_token.json()

    if(token.get('access_token')):
        return token['access_token']
    else:
        return None

def get_user_info(Token):
    response = requests.get("https://oauth.reddit.com/api/v1/me", headers={"Authorization" : "bearer " + Token, 'User-agent' : USER_AGENT})
    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_saved_posts(Token):
    response = requests.get(f"https://oauth.reddit.com/user/{session['name']}/saved?limit=None", headers={"Authorization" : "bearer " + Token, 'User-agent' : USER_AGENT})
    if response.status_code == 200:
        return parse_reddit_api_response(response.json())
    else:
        return []

def parse_reddit_api_response(saved_posts):
    parsed_response = []
    for post in saved_posts['data']['children']:
        score = post['data']['score']
        subreddit_name = post['data']['subreddit_name_prefixed']
        author = post['data']['author']
        date = datetime.fromtimestamp(post['data']['created_utc'])
        permalink = 'https://www.reddit.com' + post['data']['permalink']
        title = post['data']['title']
        selftext = post['data']['selftext']
        img_url = post['data']['url']

        parsed_response.append([score, subreddit_name, author, date, permalink, title, selftext, img_url])

    return parsed_response

@app.route('/')
def index():
    reddit = praw.Reddit(
        client_id = CLIENT_ID,
        client_secret = CLIENT_SECRET,
        redirect_uri = URI,
        user_agent = USER_AGENT,
    )

    if not(session.get('user')):
        random_string = str(uuid4())
        url = reddit.auth.url(SCOPE, random_string, 'permanent')

        if (request.args.get('code')):
            session['Token'] = reddit.auth.authorize(request.args.get('code'))

            if session['Token'] != None:
                session['name'] = reddit.user.me()
                saved_posts = reddit.redditor(name=session['name']).saved(limit=None)
            
        
    return render_template('index.html', auth_url=url, saved_posts=saved_posts)

if __name__ == '__main__':
    port = os.environ.get('PORT', 5000)
    app.run(debug=True, host='0.0.0.0', port=port)