from flask import Flask, render_template, request, session
from datetime import datetime
from uuid import uuid4
import os, praw, html

app = Flask(__name__)
app.secret_key = str(uuid4)

CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
CLIENT_ID = os.environ.get("CLIENT_ID")
URI = 'https://savescraperforreddit.herokuapp.com'
USER_AGENT = 'SaveScraperForReddit/0.3.5 by u/AciidSkull'
SCOPE = ['identity', 'read', 'history']

reddit = praw.Reddit(
        client_id = CLIENT_ID,
        client_secret = CLIENT_SECRET,
        redirect_uri = URI,
        user_agent = USER_AGENT,
    )
reddit.config.decode_html_entities = True

def parse_reddit_api_response(saved_posts):
    parsed_response = []

    for post in saved_posts.values():
        parsed_response.append([
            str(post.score),
            str(post.subreddit),
            str(post.author),
            datetime.fromtimestamp(post.created_utc),
            'https://reddit.com' + str(post.permalink),
            str(post.title),
            html.unescape(post.selftext_html),
            str(post.url),
        ])

    return parsed_response

@app.route('/')
def index():
    saved_posts = []
    url = ''

    if request.args.get('code'):
        session['code'] = request.args.get('code')

        if not session.get('Token'):
            session['Token'] = reddit.auth.authorize(session['code'])
            session['name'] = str(reddit.user.me())

        response = {x.id:x for x in reddit.redditor(name=session['name']).saved(limit=None)}
        saved_posts = parse_reddit_api_response(response)
    else:
        random_string = str(uuid4)
        url = reddit.auth.url(SCOPE, random_string, 'permanent')
        
    return render_template('index.html', auth_url=url, saved_posts=saved_posts)

if __name__ == '__main__':
    port = os.environ.get('PORT', 5000)
    app.run(debug=True, host='0.0.0.0', port=port)