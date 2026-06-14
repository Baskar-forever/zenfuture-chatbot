from app.providers.embeddings.sentence_transformer_provider import (
    SentenceTransformerProvider
)

provider = SentenceTransformerProvider(
    "BAAI/bge-small-en-v1.5"
)

vector = provider.embed_text(
    "ZenFuture provides cloud services."
)

print(len(vector))