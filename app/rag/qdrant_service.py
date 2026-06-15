from uuid import uuid4

from qdrant_client.models import (
Distance,
PointStruct,
VectorParams
)

from app.rag.qdrant_client import client

class QdrantService:


    def __init__(
        self,
        collection_name: str    
    ):
        self.collection_name = (
            collection_name
        )

    def create_collection(
        self,
        vector_size: int
    ):

        collections = (
            client.get_collections()
        )

        existing = [
            c.name
            for c in collections.collections
        ]

        if self.collection_name in existing:
            return

        client.create_collection(
            collection_name=self.collection_name,
            vectors_config=VectorParams(
                size=vector_size,
                distance=Distance.COSINE
            )
        )

    def upsert_chunks(
        self,
        chunks,
        embeddings
    ):

        points = []

        for chunk, embedding in zip(
            chunks,
            embeddings
        ):

            point = PointStruct(
                id=str(uuid4()),
                vector=embedding,
                payload={
                    "chunk_id":
                        chunk.chunk_id,

                    "text":
                        chunk.text,

                    **chunk.metadata
                }
            )

            points.append(point)

        client.upsert(
            collection_name=
                self.collection_name,
            points=points
        )

    def search(
        self,
        query_embedding,
        limit: int = 5
    ):

        result = client.query_points(
            collection_name=
                self.collection_name,

            query=query_embedding,

            limit=limit
        )

        return result.points

