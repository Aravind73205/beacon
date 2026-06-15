class RetentionStrategyAgent:
    """
    Generates retention strategies
    based on customer intelligence.
    """

    def __init__(self):
        pass


    def generate_strategy(self, customer_report):
        """
        Generate retention strategy based on customer report
        """
        risk_level = customer_report["risk_level"]
        top_factors = customer_report["top_customer_factors"]

        recommended_actions = []

        if risk_level == "High":
           recommended_actions.extend(
               [
                   "send 15% discount",
                   "Trigger win-back campaign",
                   "offer loyalty rewards"
               ]
            )

        elif risk_level == "Medium":
            recommended_actions.extend(
                [ 
                    "send personalized email",
                    "offer limited time promotion"
                ]
            )

        else:
            recommended_actions.extend(
                ["continue engagement campaigns"]
            )


        if "email_open_rate" in top_factors:

            recommended_actions.append(
                "Launch personalized email campaign"
            )

        if "recency_days" in top_factors:

            recommended_actions.append(
                "Send re-engagement offer"
            )

        if "purchase_frequency" in top_factors:

            recommended_actions.append(
                "Provide repeat-purchase incentive"
            )

        requires_human_review = (risk_level == "High")


        strategy_report = {
            "customer_id": customer_report["customer_id"],

            "risk_level": risk_level,

            "recommended_actions": recommended_actions,

            "requires_human_review": requires_human_review
        }

        return strategy_report
    