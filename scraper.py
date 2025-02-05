import requests
from bs4 import BeautifulSoup
from config import BASE_URL

def extract_magnet_links(post_url):
    """Scrape magnet links from the post page."""
    full_url = BASE_URL + post_url
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        response = requests.get(full_url, headers=headers)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, "html.parser")
        magnets = [a["href"] for a in soup.find_all("a", href=True) if "magnet:?" in a["href"]]
        
        return magnets
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {full_url}: {e}")
        return []
