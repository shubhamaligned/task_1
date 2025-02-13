import httpx
from bs4 import BeautifulSoup

def fetch_html(url):
    """Fetch HTML content from the given URL using httpx."""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://www.google.com/",
    }

    try:
        with httpx.Client(headers=headers, follow_redirects=True) as client:
            response = client.get(url, timeout=10)
            response.raise_for_status()
            response.encoding = "utf-8"
            return response.text
    except httpx.RequestError as e:
        print(f"Error fetching {url}: {e}")
        return None

def extract_data(html):
    """Extract images, hyperlinks, and buttons from HTML."""
    soup = BeautifulSoup(html, "html.parser")
    
    images = [
        {"src": img.get("src", "N/A"), "alt": img.get("alt", "N/A")}
        for img in soup.find_all("img")
    ]
    
    links = [
        {"href": a.get("href", "N/A"), "text": a.get_text(strip=True)}
        for a in soup.find_all("a") if a.get("href")
    ]
    
    buttons = [
        {"text": btn.get_text(strip=True)}
        for btn in soup.find_all("button")
    ]
    
    return images, links, buttons

def log_results(images, links, buttons):
    """Print extracted elements in a readable format."""
    print("\nImages:")
    for img in images:
        print(f"  - Source: {img['src']}, Alt: {img['alt']}")
    
    print("\nHyperlinks:")
    for link in links:
        print(f"  - URL: {link['href']}, Text: {link['text']}")

    print("\nButtons:")
    for button in buttons:
        print(f"  - Text: {button['text']}")

def main():
    url = "https://www.dell.com/support/home/en-us"
    html = fetch_html(url)
    if html:
        images, links, buttons = extract_data(html)
        log_results(images, links, buttons)

if __name__ == "__main__":
    main()
