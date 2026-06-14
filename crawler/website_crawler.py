from collections import deque
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup


class WebsiteCrawler:
    def __init__(self, timeout: int = 10):
        self.timeout = timeout

    def _is_valid_url(
        self,
        url: str,
        base_domain: str
    ) -> bool:

        if not url:
            return False

        if url.startswith(("mailto:", "tel:", "javascript:")):
            return False

        parsed = urlparse(url)

        if parsed.netloc and parsed.netloc != base_domain:
            return False

        return True

    def crawl(
        self,
        start_url: str
    ) -> list[str]:

        parsed_start = urlparse(start_url)
        base_domain = parsed_start.netloc

        visited = set()
        discovered_urls = []

        queue = deque([start_url])

        while queue:

            current_url = queue.popleft()

            if current_url in visited:
                continue

            try:
                response = requests.get(
                    current_url,
                    timeout=self.timeout
                )

                response.raise_for_status()

                visited.add(current_url)
                discovered_urls.append(current_url)

                soup = BeautifulSoup(
                    response.text,
                    "html.parser"
                )

                for link in soup.find_all("a", href=True):

                    href = link["href"]

                    absolute_url = urljoin(
                        current_url,
                        href
                    )

                    absolute_url = absolute_url.split("#")[0]

                    if not self._is_valid_url(
                        absolute_url,
                        base_domain
                    ):
                        continue

                    if absolute_url not in visited:
                        queue.append(absolute_url)

            except Exception as e:
                print(f"Failed: {current_url} -> {e}")

        return sorted(set(discovered_urls))