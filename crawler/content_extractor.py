import requests

from bs4 import BeautifulSoup


class ContentExtractor:

    def __init__(self, timeout: int = 10):
        self.timeout = timeout

    def extract(
        self,
        url: str
    ) -> dict:

        response = requests.get(
            url,
            timeout=self.timeout
        )

        response.raise_for_status()

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        for tag in soup([
            "script",
            "style",
            "noscript"
        ]):
            tag.decompose()

        title = ""

        if soup.title:
            title = soup.title.get_text(
                strip=True
            )

        content = soup.get_text(
            separator=" ",
            strip=True
        )

        content = " ".join(
            content.split()
        )

        return {
            "url": url,
            "title": title,
            "content": content
        }