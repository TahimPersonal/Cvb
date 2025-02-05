import feedparser
from config import RSS_FEED_URL, BASE_URL

def get_new_post_links():
    """Fetch post links from the RSS feed."""
    feed = feedparser.parse(RSS_FEED_URL)
    post_links = []
    
    for entry in feed.entries:
        if "link" in entry:
            post_links.append(entry.link.replace(BASE_URL, "").split("&")[0])  # Normalize links
    
    return post_links
