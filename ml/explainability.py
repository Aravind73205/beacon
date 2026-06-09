import shap

class ChurnExplainer:
    """
    Generate SHAP explainations for churn prediction
    """

    def create_explainer(self, model):
        """
        create shap explainer for trained model
        """ 

        explainer = shap.TreeExplainer(model)
        return explainer


    def explain_prediction(self, explainer, X_test):
        """
        generate shap values for predictions
        """

        shap_values = explainer.shap_values(X_test)
        return shap_values
    
    def explain_customer(self, shap_values, customer_index, feature_names, top_n=5):
        """
        get top contributing features for a customer
        """

        customer_shap = shap_values[customer_index]

        explanation = {
            feature: value
            for feature, value in zip(feature_names, customer_shap)
        }

        sorted_explanation = dict(
            sorted(
                explanation.items(),
                key=lambda item: abs(item[1]),  
                reverse=True
            )
        )

        return dict(list(sorted_explanation.items())[:top_n])


    def get_feature_importance(self, shap_values, feature_names):
        """
        calculate global feature importance
        """

        importance_scores = abs(shap_values).mean(axis=0)
        feature_importance = {
            feature: score
              for feature, score in zip(feature_names, importance_scores)
        }

        return dict(
            sorted(
                feature_importance.items(),
                key=lambda item: item[1],         # # Sort by feature importance score
                reverse=True
            )
        )