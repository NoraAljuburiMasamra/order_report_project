REQUIRED_COLUMNS = {
    "order_id",
    "order_date",
    "customer_id",
    "region",
    "product_category",
    "quantity",
    "unit_price",
    "discount",
    "returned",
}


def validate_columns(df):
    if not REQUIRED_COLUMNS.issubset(df.columns):
        missing = REQUIRED_COLUMNS - set(df.columns)
        raise ValueError(
            f"Saknade kolumner: {missing}"
        )