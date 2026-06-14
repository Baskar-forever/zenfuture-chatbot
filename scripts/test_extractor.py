from crawler.content_extractor import ContentExtractor

extractor = ContentExtractor()

doc = extractor.extract(
    "https://zenfuture.in/about.php"
)

print(doc["title"])
print()
print(doc["content"][:1000])