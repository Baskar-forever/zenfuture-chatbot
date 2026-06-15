from crawler.content_extractor import (
ContentExtractor
)

from app.services.ingestion_service import (
IngestionService
)

from app.rag.qdrant_service import (
QdrantService
)

from app.providers.embeddings.sentence_transformer_provider import (
SentenceTransformerProvider
)

COLLECTION_NAME = (
"zenfuture_knowledge"
)

def main():

    extractor = ContentExtractor()

    embedding_provider = (
        SentenceTransformerProvider(
            "BAAI/bge-small-en-v1.5"
        )
    )

    qdrant_service = (
        QdrantService(
            collection_name=
                COLLECTION_NAME
        )
    )

    qdrant_service.create_collection(
        vector_size=384
    )

    ingestion_service = (
        IngestionService(
            extractor=extractor,
            embedding_provider=
                embedding_provider,
            qdrant_service=
                qdrant_service
        )
    )

    result = (
        ingestion_service.ingest_url(
            "https://zenfuture.in/about.php"
        )
    )

    print("\n")
    print("=" * 50)
    print("INGESTION COMPLETE")
    print("=" * 50)

    print(result)


if __name__ == "__main__":
    main()
