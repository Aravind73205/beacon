from providers.interfaces.marketing_provider import MarketingProvider


class MockMarketingProvider(MarketingProvider):

    def get_customer_segment(self, customer_id: str) -> dict:

        return {
            "customer_id": customer_id,
            "segment": "Gold"
        }

    def get_campaign_history(self, customer_id: str) -> dict:

        return {
            "customer_id": customer_id,
            "campaigns": 5
        }