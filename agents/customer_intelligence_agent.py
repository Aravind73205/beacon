from services.prediction_service import PredictionService
from services.explainability_service import ExplainabilityService
from services.memory_service import MemoryService


class CustomerIntelligenceAgent:
    """
    builds customer intelligence report
    """

    def __init__(self):
        self.prediction_service = PredictionService()

        self.prediction_service.load_model("models/churn_model.pkl")
        self.model = self.prediction_service.model

        self.explainability_service = ExplainabilityService()
        self.explainer = self.explainability_service.create_explainer(self.model)

        self.memory_service = MemoryService()


    def analyze_customer(self, customer_id, customer_features):
        """
        Generate customer intelligence report
        """
        probability = self.prediction_service.predict_probability(customer_features)[0]

        if probability >= 0.7:
            risk_level = "High"

        elif probability >= 0.3:
            risk_level = "Medium"

        else:
            risk_level = "Low"

        history = self.memory_service.get_customer_history(customer_id)

        shap_values = self.explainability_service.explain_prediction(self.explainer, customer_features)

        customer_explanation = self.explainability_service.explain_customer(shap_values, 0, customer_features.columns, top_n=3)
        
        top_customer_factors = list(customer_explanation.keys())

        report = {
            "customer_id": customer_id,
            "risk_level": risk_level,
            "churn_probability": round(float(probability), 4),
            "previous_analyses": len(history),
            "top_customer_factors": top_customer_factors
        }

        self.memory_service.save_customer_analysis(report)

        return report
    
if __name__ == "__main__":

    from ml.feature_engineering import (
        FeatureEngineeringPipeline
    )

    agent = (
        CustomerIntelligenceAgent()
    )

    pipeline = (
        FeatureEngineeringPipeline()
    )

    X_train, X_test, y_train, y_test = (
        pipeline.prepare_training_data(
            "data/raw/synthetic_customers.csv"
        )
    )

    sample_customer = (
        X_test.head(1)
    )

    report = (
        agent.analyze_customer(
            customer_id="CUST_001",
            customer_features=sample_customer
        )
    )

    print(
        "\nCustomer Intelligence Report\n"
    )

    print(report)