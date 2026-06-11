from providers.interfaces.conversation_provider import ConversationProvider


class MockConversationProvider(ConversationProvider):

    def get_conversation_history(self, customer_id: str) -> dict:

        return {
            "customer_id": customer_id,
            "messages": 12
        }

    def get_support_interactions(self, customer_id: str) -> dict:

        return {
            "customer_id": customer_id,
            "tickets": 3
        }