import requests

def fetch_top_post():
    # Construct the URL and parameters.
    # Adding .json returns the data in JSON format.
    base_url = "https://www.reddit.com/r/CryptoCurrency/top/.json"
    params = {
        "t": "day",  # Top posts for the day
        "f": 'flair_name:"GENERAL-NEWS"'  # Filter by the "GENERAL-NEWS" flair
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; TopCryptoTweet/1.0)"
    }

    try:
        response = requests.get(base_url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()

        posts = data.get("data", {}).get("children", [])
        if not posts:
            print("No posts found for the specified criteria.")
            return None

        # Get the top post data.
        top_post = posts[0]["data"]
        return top_post

    except requests.RequestException as e:
        print("Error fetching data from Reddit:", e)
        return None

def format_tweet(post):
    # Prepare tweet text: combine title and Reddit post URL.
    title = post.get("title", "No title")
    # Create the post URL from the permalink.
    post_url = "https://reddit.com" + post.get("permalink", "")
    tweet_text = f"{title}\n{post_url}"
    
    # Ensure tweet is within Twitter's 280-character limit.
    if len(tweet_text) > 280:
        # Truncate and add ellipsis if necessary.
        tweet_text = tweet_text[:277] + "..."
    
    return tweet_text

def save_tweet(tweet_text, filename="tweet.txt"):
    # Save the tweet text into a file.
    with open(filename, "w", encoding="utf-8") as f:
        f.write(tweet_text)
    print(f"Tweet saved to {filename}")

def main():
    post = fetch_top_post()
    if post:
        tweet_text = format_tweet(post)
        print("Formatted Tweet:")
        print(tweet_text)
        save_tweet(tweet_text)

if __name__ == "__main__":
    main()
