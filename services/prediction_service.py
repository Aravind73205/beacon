from ml.train_model import ChurnModelTrainer


class PredictionService:
    """
    service for churn prediction operations
    """

   
    def __init__(self):
        self.model = None

    def load_model(self, model_path: str):
        """
        Initialize prediction service.
        """

        trainer = ChurnModelTrainer()

        self.model = (
            trainer.load_model(model_path)
        )

    def predict(self, customer_features):
        """
        Generate churn prediction.
        """
        
        if self.model is None:
            raise ValueError("Model not loaded.")
    
        prediction = (self.model.predict(customer_features))
        return prediction