from abc import ABC
from abc import abstractmethod


class EmbeddingProvider(ABC):

    @abstractmethod
    def embed_text(self, text: str) -> list[float]:
        pass

    @abstractmethod
    def embed_batch(self, texts: list[str]) -> list[list[float]]:
        pass