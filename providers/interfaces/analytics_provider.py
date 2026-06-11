from abc import ABC, abstractmethod

class AnalyticsProvider(ABC):
    """
    Abstract interface for analytics data providers.

    All analytics providers must implement these methods,
    regardless of whether the source is an MCP server,
    CRM platform, analytics system, mock data source,
    or another external integration.
    """

    @abstractmethod
    def get_engagement_data(self, customer_id: str) -> dict:
        pass

    @abstractmethod
    def get_behavioral_trends(self, customer_id: str) -> dict:
        pass    
    