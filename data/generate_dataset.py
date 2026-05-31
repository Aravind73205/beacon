import numpy as np
import pandas as pd


NUM_CUSTOMERS = 10000


def generate_customer_data() -> pd.DataFrame:
    """
    Generate synthetic customer dataset for churn prediction.
    """

    np.random.seed(42)

    df = pd.DataFrame({
        "customer_id": [f"CUST_{i:05d}" for i in range(NUM_CUSTOMERS)],

        "recency_days": np.random.randint(1, 365, NUM_CUSTOMERS),

        "purchase_frequency": np.random.randint(1, 50, NUM_CUSTOMERS),

        "avg_order_value": np.round(
            np.random.uniform(10, 500, NUM_CUSTOMERS),
            2
        ),

        "email_open_rate": np.round(
            np.random.uniform(0, 1, NUM_CUSTOMERS),
            2
        ),

        "session_frequency": np.random.randint(
            1,
            100,
            NUM_CUSTOMERS
        ),

        "support_tickets": np.random.randint(
            0,
            10,
            NUM_CUSTOMERS
        ),

        "customer_tier": np.random.choice(
            ["Bronze", "Silver", "Gold"],
            size=NUM_CUSTOMERS,
            p=[0.7, 0.2, 0.1]
        ),

        "vip_flag": np.random.choice(
            [0, 1],
            size=NUM_CUSTOMERS,
            p=[0.85, 0.15]
        )
    })

    # Lifetime value estimate
    df["ltv"] = (
        df["purchase_frequency"]
        * df["avg_order_value"]
    ).round(2)

    return df


def generate_churn_labels(df: pd.DataFrame) -> pd.DataFrame:
    """
    Generate realistic churn labels.
    """

    churn_score = (
        0.35 * (df["recency_days"] / 365)
        + 0.25 * (1 - df["email_open_rate"])
        + 0.20 * (1 - (df["purchase_frequency"] / 50))
        + 0.10 * (df["support_tickets"] / 10)
        - 0.15 * df["vip_flag"]
    )

    df["churn_label"] = (
        churn_score > 0.55
    ).astype(int)

    return df


def main():
    df = generate_customer_data()

    df = generate_churn_labels(df)

    output_path = "data/raw/synthetic_customers.csv"

    df.to_csv(
        output_path,
        index=False
    )

    print(f"Dataset saved to: {output_path}")

    print(df.head())

    print("\nShape:", df.shape)

    print(
        "\nChurn Distribution:\n",
        df["churn_label"].value_counts(normalize=True)
    )


if __name__ == "__main__":
    main()