from app.providers.embeddings.sentence_transformer_provider import (
    SentenceTransformerProvider
)

from app.providers.llm.ollama_provider import (
    OllamaProvider
)

from app.rag.qdrant_service import (
    QdrantService
)

from app.rag.retriever import (
    Retriever
)

from app.repositories.session_repository import (
    SessionRepository
)

from app.repositories.lead_repository import (
    LeadRepository
)

from app.repositories.message_repository import (
    MessageRepository
)

from app.services.rag_service import (
    RAGService
)

from app.services.chat_service import (
    ChatService
)


class ServiceContainer:

    def __init__(self):

        self.embedding_provider = (
            SentenceTransformerProvider(
                model_name="BAAI/bge-small-en-v1.5"
            )
        )

        self.qdrant_service = (
            QdrantService(
                collection_name="zenfuture_knowledge"
            )
        )

        self.retriever = (
            Retriever(
                embedding_provider=
                    self.embedding_provider,
                qdrant_service=
                    self.qdrant_service
            )
        )

        self.llm_provider = (
            OllamaProvider(
                model="llama3.2"
            )
        )

        self.rag_service = (
            RAGService(
                retriever=self.retriever,
                llm_provider=self.llm_provider
            )
        )

        self.chat_service = (
            ChatService(
                rag_service=self.rag_service,
                session_repository=
                    SessionRepository(),
                lead_repository=
                    LeadRepository(),
                message_repository=
                    MessageRepository()
            )
        )


container = ServiceContainer()