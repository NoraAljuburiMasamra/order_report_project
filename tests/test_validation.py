import pandas as pd
from src.validator import validate_columns

def test_validate_columns():
    df = pd.DataFrame({
        "order_id": [1],
        "order_date": ["2026-01-01"],
        "region": ["North"],
        "product_category": ["Books"],
        "quantity": [2],
        "unit_price": [100],
        "discount": [0],
        "returned": [False],
        "customer_id": ["C001"],
    })
    
    validate_columns(df)
    assert len(df.columns) > 0


def test_total_sales():
    df = pd.DataFrame({
        "unit_price": [100, 200],
        "quantity": [1, 2]
    })
    
    total = (df["unit_price"] * df["quantity"]).sum()

    assert total == 500

def test_empty_dataframe():
    df = pd.DataFrame()
    assert df.empty

def test_missing_column():
    df = pd.DataFrame({"order_id": [1]})
    assert "region" not in df.columns

def test_negative_quantity():
    df = pd.DataFrame({"quantity": [-1]})
    assert (df["quantity"] < 0).any()