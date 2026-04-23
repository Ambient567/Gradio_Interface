from bs4 import BeautifulSoup
import requests

#Standard headers to fecth the webpage
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.3'
}

def fetch_website_contents(url):
    """
    Return the title and contents of the website at the given URL; Truncate to 2000 characters as a sensible limit.
    """

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    title = soup.title.string if soup.title else "No Title Found"
    if soup.body:
        for irrelevant in soup(["script", "style", "img", "input"]):
            irrelevant.decompose()
        text = soup.body.get_text(separator="\n", strip=True)

    else:
        text = ""
    return (title + "\n\n" + text)[:2000]