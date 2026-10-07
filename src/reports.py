import logging
import pandas as pd

logger = logging.getLogger(__name__)


def create_sales_report(df):

    df["quantity"] = pd.to_numeric(
        df["quantity"], errors="coerce"
    ).fillna(1)

    df["unit_price"] = pd.to_numeric(
        df["unit_price"], errors="coerce"
    )

    df["discount"] = pd.to_numeric(
        df["discount"], errors="coerce"
    ).fillna(0)

    df["order_value"] = (
        df["quantity"] *
        df["unit_price"]
    )

    df["discounted_value"] = (
        df["order_value"] *
        (1 - df["discount"])
    )

    total_sales = round(
    df["discounted_value"].sum(),
        2,
    )

    logger.info(
        f"Total försäljning: {total_sales}"
    )

    return total_sales

from pathlib import Path


def create_overview_report(df, output_dir):

    total_sales = round(
        df["discounted_value"].sum(),
        2,
    )

    number_of_orders = df["order_id"].nunique()

    number_of_returns = (
        df["returned"]
        .astype(str)
        .str.lower()
        .eq("true")
        .sum()
        )
    
    overview = pd.DataFrame(
        {
            "metric": [
                "total_sales",
                "order_count",
                "return_count",
            ],
            "value": [
                total_sales,
                number_of_orders,
                number_of_returns,
            ],
        }
    )
    
    overview.to_csv(
        Path(output_dir) / "overview.csv",
        index=False,
    )

    logger.info("overview.csv skapad")