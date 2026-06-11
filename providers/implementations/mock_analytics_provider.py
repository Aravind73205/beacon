from providers.interfaces.analytics_provider import AnalyticsProvider


class MockAnalyticsProvider(AnalyticsProvider):

    def get_engagement_data(self, customer_id: str) -> dict:

        return {
            "customer_id": customer_id,
            "email_open_rate": 0.72,
            "session_frequency": 15
        }

    def get_behavioral_trends(self,customer_id: str) -> dict:

        return {
            "customer_id": customer_id,
            "trend": "stable"
        }