from app.rag.qdrant_service import (
    QdrantService
)

from app.providers.embeddings.sentence_transformer_provider import (
    SentenceTransformerProvider
)


def main():

    embedding_provider = (
        SentenceTransformerProvider(
            "BAAI/bge-small-en-v1.5"
        )
    )

    qdrant_service = (
        QdrantService(
            collection_name=
                "zenfuture_knowledge"
        )
    )

    query = (
        "How many global clients do they serve?"
    )

    query_embedding = (
        embedding_provider.embed_text(
            query
        )
    )

    results = (
        qdrant_service.search(
            query_embedding,
            limit=5
        )
    )

    print("\n")
    print("=" * 80)
    print("QUERY")
    print("=" * 80)

    print(query)

    print("\n")
    print("=" * 80)
    print("RESULTS")
    print("=" * 80)

    for idx, result in enumerate(
        results,
        start=1
    ):

        print("\n")
        print(f"Result {idx}")
        print("-" * 40)

        print(
            result.payload["text"]
        )

        print("\nScore:", result.score)


if __name__ == "__main__":
    main()