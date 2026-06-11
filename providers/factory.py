from providers.implementations.mock_analytics_provider import MockAnalyticsProvider
from providers.implementations.mock_conversation_provider import MockConversationProvider
from providers.implementations.mock_marketing_provider import MockMarketingProvider


class ProviderFactory:
    """
    Factory for creating provider instances
    """

    @staticmethod
    def create_analytics_provider(source: str = "mock"):
        """
        Create analytics provider
        """
        if source == "mock":
            return MockAnalyticsProvider()
        else:
            raise ValueError(f"Unsupported analytics provider source: {source}")


    @staticmethod
    def create_conversation_provider(source: str = "mock"):
        """
        Create conversation provider
        """

        if source == "mock":
            return MockConversationProvider()
        else:
            raise ValueError(f"Unsupported conversation provider source: {source}")


    @staticmethod
    def create_marketing_provider(source: str = "mock"):
        """
        Create marketing provider
        """


        if source == "mock":
            return MockMarketingProvider()
        else:
            raise ValueError(f"Unsupported marketing provider source: {source}")