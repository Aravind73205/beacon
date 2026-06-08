from xgboost import XGBClassifier
from pathlib import Path
import joblib

from ml.feature_engineering import FeatureEngineeringPipeline

from sklearn.metrics import (
    accuracy_score, 
    precision_score, 
    recall_score, 
    f1_score, 
    confusion_matrix, 
    classification_report
)


class ChurnModelTrainer:
    """
    train churn prediction model using XGBoost
    """

    def load_training_data(self, dataset_path: str):
        """
        load and prepare training data
        """

        pipeline = FeatureEngineeringPipeline()

        X_train, X_test, y_train, y_test = (
            pipeline.prepare_training_data(dataset_path)
        )

        return X_train, X_test, y_train, y_test


    def train_model(self, X_train, y_train) -> XGBClassifier:
        """
        train the XGBoost model
        """

        model = XGBClassifier(
            n_estimators=100,
            max_depth=6,
            learning_rate=0.1,
            random_state=42
        )

        model.fit(X_train, y_train)

        return model


    def generate_predictions(self, model, X_test):
        """
        generate churn prediction
        """

        predictions = model.predict(X_test)
        return predictions
    
    
    def evaluate_model(self, y_test, predictions):
        """
        evaluate model predictions
        """

        metrics = {
            "accuracy": accuracy_score(y_test, predictions),

            "precision": precision_score(y_test, predictions),

            "recall": recall_score(y_test, predictions),

            "f1_score": f1_score(y_test, predictions),

            "confusion_matrix": confusion_matrix(y_test, predictions),

            "classification_report": classification_report(y_test, predictions) 

        }

        return metrics
    
    
    def save_model(self,model,model_path: str) -> None:
        """
        save trained model to disk
        """

        path = Path(model_path)

        path.parent.mkdir(parents=True, exist_ok=True)

        joblib.dump(model,path)


    def load_model( self, model_path: str):
        """
        load trained model from disk
        """

        path = Path(model_path)

        if not path.exists():
            raise FileNotFoundError(f"Model file not found at {model_path}")

        model = joblib.load(model_path)

        return model
