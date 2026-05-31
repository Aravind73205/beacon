from abc import ABC, abstractmethod

class ConversationProvider(ABC):
    """
    Abstract interface for conversation data providers.
    """

    @abstractmethod
    def get_conversation_history(self, customer_id: str) -> dict:
        pass

    @abstractmethod
    def get_support_interactions(self, customer_id: str) -> dict:
        pass    
    