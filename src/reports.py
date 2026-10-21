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

    df["unit_price"] = df["unit_price"].fillna(
        df["unit_price"].median()
    )

    df["discount"] = pd.to_numeric(
        df["discount"], errors="coerce"
    ).fillna(0)

    df["returned"] = (
        df["returned"]
        .fillna("false")
        .astype(str)
        .str.strip()
        .str.lower()
        .isin(["true", "yes", "1", "ja"])
    )

    df["region"] = (
        df["region"]
        .fillna("Unknown")
        .astype(str)
        .str.strip()
        .str.title()
    )

    df["product_category"] = (
        df["product_category"]
        .fillna("Unknown")
        .astype(str)
        .str.strip()
        .str.title()
    )

    df["order_value"] = (
        df["quantity"]
        * df["unit_price"]
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

def create_sales_by_category_report(df, output_dir):

        result = (
         df.groupby(
            "product_category",
            as_index=False,
        )
        .agg(
            order_count=("order_id", "nunique"),
            total_sales=("discounted_value", "sum"),
            returns=("returned", "sum"),
        )
    )

        result["total_sales"] = result["total_sales"].round(2)

        result["return_rate"] = (
            result["returns"]
            / result["order_count"]
        ).round(3)

        result = (
        result
        .sort_values(
            "total_sales",
            ascending=False,
        )
        .reset_index(drop=True)
    )

        result.to_csv(
            Path(output_dir) / "sales_by_category.csv",
            index=False,
    )

        logger.info("sales_by_category.csv skapad")


def create_sales_by_region_report(df, output_dir):

        result = (
        df.groupby(
            "region",
            as_index=False,
        )
        .agg(
            order_count=("order_id", "nunique"),
            total_sales=("discounted_value", "sum"),
            returns=("returned", "sum"),
        )
        )

        result["total_sales"] = result["total_sales"].round(2)

        result["return_rate"] = (
            result["returns"]
            / result["order_count"]
        ).round(3)

        result = (
        result
        .sort_values(
            "total_sales",
            ascending=False,
        )
        .reset_index(drop=True)
    )

        result.to_csv(
            Path(output_dir) / "sales_by_region.csv",
            index=False,
    )

        logger.info("sales_by_region.csv skapad")

def create_returns_by_category_report(df, output_dir):

        result = (
        df.groupby(
            "product_category",
            as_index=False,
        )
        .agg(
            order_count=("order_id", "nunique"),
            returns=("returned", "sum"),
        )
    )

        result["return_rate"] = (
            result["returns"]
            / result["order_count"]
        ).round(3)

        result = (
        result
        .sort_values(
            "return_rate",
            ascending=False,
        )
        .reset_index(drop=True)
    )

        result.to_csv(
        Path(output_dir) / "returns_by_category.csv",
        index=False,
    )

        logger.info("returns_by_category.csv skapad")