# Order Report Project
 
## Beskrivning
 
Detta projekt är utvecklat som en del av kursen Pythonprogrammering.
 
Programmet läser in orderdata från en CSV-fil, validerar datakvaliteten och genererar flera rapporter baserade på försäljning och returer. Resultaten sparas automatiskt som CSV-filer i output-mappen.
 
## Funktioner
 
Programmet kan:
 
- Läsa in orderdata från CSV-fil
- Validera att nödvändiga kolumner finns
- Hantera fel med hjälp av try/except
- Logga programmets körning
- Beräkna total försäljning
- Beräkna antal ordrar
- Beräkna antal returer
- Skapa rapporter per produktkategori
- Skapa rapporter per region
- Beräkna returgrad
- Exportera rapporter till CSV-filer
 
## Projektstruktur
 
```text
order_report_project/
│
├── README.md
├── data/
│ └── orders.csv
│
├── output/
│ ├── overview.csv
│ ├── sales_by_category.csv
│ ├── sales_by_region.csv
│ └── returns_by_category.csv
│
├── src/
│ ├── main.py
│ ├── config.py
│ ├── validator.py
│ └── reports.py
│
└── tests/