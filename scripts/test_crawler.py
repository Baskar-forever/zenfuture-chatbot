from crawler.website_crawler import WebsiteCrawler

crawler = WebsiteCrawler()

urls = crawler.crawl(
    "https://zenfuture.in"
)

print(f"Found {len(urls)} URLs\n")

for url in urls:
    print(url)