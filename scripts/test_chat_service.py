from app.db.database import SessionLocal

from app.repositories.session_repository import (
    SessionRepository
)

from app.repositories.lead_repository import (
    LeadRepository
)

from app.repositories.message_repository import (
    MessageRepository
)

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

from app.services.rag_service import (
    RAGService
)

from app.services.chat_service import (
    ChatService
)


def build_chat_service():

    embedding_provider = (
        SentenceTransformerProvider(
            model_name="BAAI/bge-small-en-v1.5"
        )
    )

    qdrant_service = (
        QdrantService(
            collection_name="zenfuture_knowledge"
        )
    )

    retriever = (
        Retriever(
            embedding_provider=embedding_provider,
            qdrant_service=qdrant_service
        )
    )

    llm_provider = (
        OllamaProvider(
            model="llama3.2"
        )
    )

    rag_service = (
        RAGService(
            retriever=retriever,
            llm_provider=llm_provider
        )
    )

    chat_service = (
        ChatService(
            rag_service=rag_service,
            session_repository=SessionRepository(),
            lead_repository=LeadRepository(),
            message_repository=MessageRepository()
        )
    )

    return chat_service


def main():

    db = SessionLocal()

    try:

        chat_service = (
            build_chat_service()
        )

        session = (
            chat_service.create_session(
                db
            )
        )

        session_id = (
            session["session_id"]
        )

        print("\nBOT:")
        print(session["reply"])

        while True:

            print("\nUSER:")
            user_input = input("> ")

            if user_input.lower() in [
                "exit",
                "quit"
            ]:
                break

            response = (
                chat_service.process_message(
                    db=db,
                    session_id=session_id,
                    message=user_input
                )
            )

            print("\nBOT:")
            print(
                response["reply"]
            )

            print(
                f"\nSTATE: "
                f"{response['state']}"
            )

    finally:

        db.close()


if __name__ == "__main__":
    main()