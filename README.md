# Order Report Project
Overview

This project analyzes order data from a CSV file and generates summary reports.

The application:

- Validates input data

- Calculates sales metrics

- Creates sales reports by region

- Creates sales reports by product category

- Generates return statistics

- Exports results to CSV files

  Project Structure
  
order_report_project/
│

├── data/

│   └── orders.csv
│

├── output/

│   ├── overview.csv

│   ├── sales_by_region.csv

│   ├── sales_by_category.csv

│   └── returns_by_category.csv

│
├── src/

│   ├── main.py

│   ├── validator.py

│   ├── reports.py

│   └── config.py

│
├── tests/

│   └── test_validation.py

│
├── README.md

├── requirements.txt

└── .gitignore

Features

Data validation

Report generation

CSV data processing

Automated testing with Pytest

Technologies

Python

Pandas

Pytest

Installation

Clone the repository:


git clone https://github.com/NoraAljuburiMasamra/order_report_project.git

Navigate to the project folder:


cd order_report_project

Install dependencies:


pip install -r requirements.txt

Run the Project

python src/main.py

Run Tests

python -m pytest

Test Results

Current test suite contains:


Column validation test

Sales calculation test

Empty dataframe test

Missing column test

Negative quantity test

All tests are passing.


Author

Nora Aljuburi Masamra
