import logging

logger = logging.getLogger(__name__)

def create_sales_report(df):
    total_sales = df["order_value"].sum()

    logger.info(
        f"Total försäljning: {total_sales}"
    )

    return total_sales
