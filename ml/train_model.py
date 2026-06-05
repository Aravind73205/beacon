from xgboost import XGBClassifier

from ml.feature_engineering import FeatureEngineeringPipeline
from sklearn.metrics import accuracy_score


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

        accuracy = accuracy_score(y_test, predictions)
        return accuracy
    