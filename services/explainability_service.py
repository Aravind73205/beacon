from ml.explainability import ChurnExplainer


class ExplainabilityService:
    """
    service for explainability operations
    """

    def __init__(self):
        self.explainer = ChurnExplainer()


    def create_explainer(self, model):
        """
        create shap explainer
        """

        return self.explainer.create_explainer(model)
    

    def explain_prediction(self, explainer, X_test):
        """
        generate shap values
        """

        return self.explainer.explain_prediction(explainer, X_test)
    

    def explain_customer(self, shap_values, customer_index, feature_names, top_n=5):
        """
        get top contributing features for a customer
        """

        return self.explainer.explain_customer(shap_values, customer_index, feature_names, top_n)
    
    
    def get_feature_importance(self, shap_values, feature_names):
        """
        return global feature importance
        """

        return self.explainer.get_feature_importance(shap_values, feature_names)