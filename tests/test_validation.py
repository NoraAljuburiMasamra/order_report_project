import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pandas as pd
import pytest

from src.validator import validate_columns


def test_validate_columns_valid_data():
    df = pd.DataFrame({
        "order_id": [1],
        "order_date": ["2026-01-01"],
        "customer_id": ["C001"],
        "region": ["North"],
        "product_category": ["Books"],
        "quantity": [2],
        "unit_price": [100],
        "discount": [0],
        "returned": [False]
    })

    validate_columns(df)


def test_validate_columns_missing_region():
    df = pd.DataFrame({
        "order_id": [1],
        "order_date": ["2026-01-01"],
        "customer_id": ["C001"],
        "product_category": ["Books"],
        "quantity": [2],
        "unit_price": [100],
        "discount": [0],
        "returned": [False]
    })

    with pytest.raises(ValueError):
        validate_columns(df)


def test_validate_columns_missing_order_id():
    df = pd.DataFrame({
        "order_date": ["2026-01-01"],
        "customer_id": ["C001"],
        "region": ["North"],
        "product_category": ["Books"],
        "quantity": [2],
        "unit_price": [100],
        "discount": [0],
        "returned": [False]
    })

    with pytest.raises(ValueError):
        validate_columns(df)


def test_validate_columns_empty_dataframe():
    df = pd.DataFrame()

    with pytest.raises(ValueError):
        validate_columns(df)