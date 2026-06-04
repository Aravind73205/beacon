from pathlib import Path
import pandas as pd

from sklearn.model_selection import train_test_split


class FeatureEngineeringPipeline:
    """
    Feature engineering pipeline for churn prediction
    """

    def load_dataset(self, dataset_path: str) -> pd.DataFrame:
        """
        load raw customer dataset
        """
        
        path = Path(dataset_path)

        if not path.exists():
            raise FileNotFoundError(f"Dataset not found at {dataset_path}")
        
        df = pd.read_csv(path)

        return df     
    

    def validate_dataset(self, df: pd.DataFrame) -> None:
        """
        validate dataset structure and required columns
        """

        if df.empty:
            raise ValueError("Dataset is empty")

        required_columns = [
            "customer_id",
            "recency_days",
            "purchase_frequency",
            "avg_order_value",
            "email_open_rate",
            "session_frequency",
            "support_tickets",
            "customer_tier",
            "vip_flag",
            "ltv",
            "churn_label",
        ]

        missing_columns = [
            column 
            for column in required_columns
            if column not in df.columns
        ]

        if missing_columns:
            raise ValueError(f"Missing required columns: {missing_columns}")
    
    
    def handle_missing_values(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        handle missing values in the dataset
        """

        numeric_columns = [
            "recency_days",
            "purchase_frequency",
            "avg_order_value",
            "email_open_rate",
            "session_frequency",
            "support_tickets",
            "ltv",
        ]

        for column in numeric_columns:
            df[column] = df[column].fillna(df[column].median())

        df["customer_tier"] = df["customer_tier"].fillna(df["customer_tier"].mode()[0])

        return df


    def create_features(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        create derived business features
        """

        df["engagement_score"] = (df["email_open_rate"] * df["session_frequency"])

        df["customer_value_score"] = (df["ltv"] * (1 + df["vip_flag"]))

        purchase_frequency = (df["purchase_frequency"].replace(0, 1))     # avoid division by zero if purchase_frequency is zero

        df["support_ticket_ratio"] = (df["support_tickets"] / purchase_frequency)

        return df


    def encode_features(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        encode categorical features using one-hot encoding
        """

        df = pd.get_dummies(df, columns=["customer_tier"], dtype=int)

        return df


    def split_dataset(self, df: pd.DataFrame):
        """
        split dataset into training and testing sets
        """

        X = df.drop(columns=["customer_id", "churn_label"])
        y = df["churn_label"]

        X_train, X_test, y_train, y_test = (
            train_test_split(
                X,
                y, 
                test_size=0.2, 
                random_state=42, 
                stratify=y
            )
        )

        return (
            X_train, 
            X_test, 
            y_train, 
            y_test
        )


    def prepare_training_data(self, dataset_path: str):
        """
        Execute the complete feature engineering pipeline
        """

        df = self.load_dataset(dataset_path)

        self.validate_dataset(df)
   
        df = self.handle_missing_values(df)

        df = self.create_features(df)

        df = self.encode_features(df)

        X_train, X_test, y_train, y_test = (
            self.split_dataset(df)
        )

        return (
            X_train,
            X_test,
            y_train,
            y_test
        )

    def save_processed_dataset(self, df: pd.DataFrame, output_path: str) -> None:
        """
        save the processed dataset to a new CSV file
        """

        path = Path(output_path)

        path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        df.to_csv(
            path,
            index=False
        )