import os
import tweepy
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Access your API keys
api_key = os.environ.get('api_key')
api_key_secret = os.environ.get('api_key_secret')
access_token = os.environ.get('access_token')
access_token_secret = os.environ.get('access_token_secret')

# Debug information (remove sensitive parts before sharing)
print(f"API Key: {api_key[:4]}...{api_key[-4:] if api_key else 'None'}")
print(f"API Secret: {api_key_secret[:4]}...{api_key_secret[-4:] if api_key_secret else 'None'}")
print(f"Access Token: {access_token[:4]}...{access_token[-4:] if access_token else 'None'}")
print(f"Access Secret: {access_token_secret[:4]}...{access_token_secret[-4:] if access_token_secret else 'None'}")

# Read the tweet content from tweet.txt
try:
    with open("tweet.txt", "r", encoding="utf-8") as file:
        tweet_text = file.read().strip()
except Exception as e:
    print("Failed to read tweet.txt:", e)
    tweet_text = None

if tweet_text:
    try:
        # Authenticate with Tweepy
        client = tweepy.Client(
            consumer_key=api_key, 
            consumer_secret=api_key_secret,
            access_token=access_token, 
            access_token_secret=access_token_secret
        )
        
        # Post the tweet using the content from tweet.txt
        response = client.create_tweet(text=tweet_text)
        print(f"Tweet posted successfully! ID: {response.data['id']}")
    except Exception as e:
        print(f"Error type: {type(e).__name__}")
        print(f"Error details: {str(e)}")
else:
    print("No tweet content available to post.")
