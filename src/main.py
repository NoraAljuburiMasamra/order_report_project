import logging
from pathlib import Path

import pandas as pd

from config import ReportConfig
from validator import validate_columns
from reports import create_sales_report

# Konfigurera logging centralt
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

def main():
    config = ReportConfig(
        input_file=Path("data/orders.csv"),
        output_dir=Path("output")
    )

    logger.info("Läser in data")

    try:
       data = pd.read_csv(config.input_file)

       logger.info(
            f"{len(data)} rader inlästa"
       )

       validate_columns(data)
       logger.info("Validering klar")

       report = create_sales_report(data)

       logger.info(
           f"Total försäljning: {report}"
       )

    except FileNotFoundError:
        logger.error(
            f"Datafilen hittades inte: {config.input_file}"
        )
        return

    except ValueError as error:
        logger.error(
            f"Valideringsfel: {error}"
        )   
        return

    except Exception as error:
        logger.error(
            f"Ett oväntat fel uppstod: {error}"
        )
        return

    if __name__ == "__main__":
        main()