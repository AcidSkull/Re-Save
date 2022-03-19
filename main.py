from flask import Flask, render_template, request, session, url_for, redirect
from datetime import datetime
from uuid import uuid4
import os, praw

# Creating flask variable and assigning secret_key to use session
app = Flask(__name__)
app.secret_key = str(uuid4)

# Variables for praw.Reddit istance
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

# Function to parse reddit API response to valid types in some cases
def parse_reddit_api_response(saved_posts):
    parsed_response = []

    for post in saved_posts.values():
        parsed_response.append({
            'score' : post.score,
            'subreddit' : post.subreddit_name_prefixed,
            'author' : str(post.author),
            'date' : datetime.fromtimestamp(post.created_utc),
            'permalink' : 'https://reddit.com' + str(post.permalink), # Direct link to post page
            'title' : post.title,
            'selftext' : post.selftext_html, # Content of post
            'url' : post.url, # Url to image
            'is_video' : post.is_video,
            'nsfw' : post.over_18,
        })
        # If post is video, get thumbnail or no preview image instead
        if parsed_response[-1]['is_video']:
            if hasattr(post, 'preview'):
                parsed_response[-1]['thumbnail'] = post.preview['images'][0]['source']['url']
            else:
                parsed_response[-1]['thumbnail'] = url_for('static', filename='images/no_preview.png')

    return parsed_response

@app.route('/')
def index():
    url = ''

    # If code response from reddit is present, get verification token and user name and avatar
    if request.args.get('code'):
        session['code'] = request.args.get('code')

        if not session.get('Token'):
            session['Token'] = reddit.auth.authorize(session['code'])
            session['name'] = str(reddit.user.me())
            session['image'] = reddit.user.me().icon_img

        response = {x.id:x for x in reddit.redditor(name=session['name']).saved(limit=None)}
        saved_posts = parse_reddit_api_response(response)

        return render_template('index.html', saved_posts=saved_posts)

    # If no code in get args, create an authentication url and pass to the main page
    else:
        random_string = str(uuid4)
        url = reddit.auth.url(SCOPE, random_string, 'permanent')

    return render_template('welcome_page.html', auth_url=url)
    
# Logout view to destroy session variables and redirect to main view
@app.route('/logout')
def logout():
    if session.get('Token'):
        session.pop('Token')
        session.pop('name')
        session.pop('image')
    return redirect(url_for('index'))

# Getting env variable PORT and running flask app
if __name__ == '__main__':
    port = os.environ.get('PORT', 5000)
    app.run(debug=True, host='0.0.0.0', port=port)