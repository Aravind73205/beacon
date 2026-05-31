from abc import ABC, abstractmethod

class MarketingProvider(ABC):
    """
    Abstract interface for marketing data providers.
    """

    @abstractmethod
    def get_customer_segment(self, customer_id: str) -> dict:
        pass

    @abstractmethod
    def get_campaign_history(self, customer_id: str) -> dict:
        pass    
    