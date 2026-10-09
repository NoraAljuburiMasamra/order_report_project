# Order Report Project

**För**ttare:** Nora Aljuburi Masamra

## Beskrivning

Detta projekt analyserar orderdata från en CSV-fil, validerar datakvaliteten och genererar flera rapporter baserade på försäljning och returer.

Projektet är en refaktorerad version av ett befintligt program där fokus har legat på:

- Modulär struktur
- Validering av data
- Logging
- Felhantering
- Dataclass för konfiguration
- Automatiska tester med pytest

Resultaten exporteras automatiskt till CSV-filer i output-mappen.

---

## Funktioner

Programmet kan:

- Läsa in orderdata från CSV-fil
- Validera att nödvändiga kolumner finns
- Hantera fel med hjälp av exceptions
- Logga programmets körning
- Beräkna total försäljning
- Beräkna antal ordrar
- Beräkna antal returer
- Beräkna returgrad
- Skapa rapporter per produktkategori
- Skapa rapporter per region
- Exportera rapporter till CSV-filer

---

## Installation

### 1. Klona eller ladda ner projektet

Placera projektmappen på din dator.

### 2. Skapa en virtuell miljö

```bash
python -m venv .venv
```

### 3. Aktivera den virtuella miljön

Windows:

```bash
.venv\Scripts\activate
```

### 4. Installera beroenden

```bash
pip install -r requirements.txt
```

---

## Köra programmet

```bash
python src/main.py
```

Programmet läser data från:

```text
data/orders.csv
```

och genererar rapporter i:

```text
output/
```

---

## Köra tester

```bash
pytest
```

---

## Genererade rapporter

### overview.csv

Innehåller:

- Total försäljning
- Antal ordrar
- Antal returer

### sales_by_category.csv

Innehåller försäljning per produktkategori.

### sales_by_region.csv

Innehåller försäljning per region.

### returns_by_category.csv

Innehåller returer och returgrad per kategori.

---

## Förväntat resultat

Efter en körning skapas:

```text
output/
├── overview.csv
├── sales_by_category.csv
├── sales_by_region.csv
└── returns_by_category.csv
```

---

## Projektstruktur

```text
order_report_project/
│
├── README.md
├── requirements.txt
│
├── data/
│   └── orders.csv
│
├── output/
│   ├── overview.csv
│   ├── sales_by_category.csv
│   ├── sales_by_region.csv
│   └── returns_by_category.csv
│
├── src/
│   ├── main.py
│   ├── config.py
│   ├── validator.py
│   └── reports.py
│
└── tests/
    └── test_validation.py
```

---

## Reflektion

När jag började arbetet med refaktoriseringen upplevde jag att den största utmaningen var att förstå den befintliga koden och samtidigt säkerställa att programmets funktionalitet inte förändrades. Eftersom all logik från början låg samlad i en fil blev det ibland svårt att få en överblick över hur de olika delarna påverkade varandra.

Under arbetets gång lärde jag mig hur viktigt det är att dela upp kod i mindre moduler med tydliga ansvarsområden. Genom att separera validering, rapportgenerering och konfiguration blev koden betydligt mer lättläst och enklare att underhålla. Jag fick också en bättre förståelse för hur logging kan användas för att följa programmets körning och underlätta felsökning.

En annan viktig lärdom var betydelsen av automatiserade tester. Innan projektet hade jag begränsad erfarenhet av att skriva tester med pytest. Genom att skapa tester för både normalfall och felscenarier fick jag en bättre förståelse för hur tester kan användas för att säkerställa att koden fungerar som förväntat även efter förändringar.

Det som tog mest tid var att få projektstrukturen, importerna och testerna att fungera tillsammans. Samtidigt gav det mig värdefull erfarenhet av hur Python-projekt organiseras och hur olika delar samverkar.

Jag tycker att refaktoriseringen har förbättrat projektet avsevärt. Koden är nu mer strukturerad, lättare att förstå och enklare att vidareutveckla. Om jag skulle fortsätta utveckla projektet skulle jag vilja utöka testtäckningen ytterligare, införa fler valideringskontroller och förbättra rapporterna med fler analyser och visualiseringar.

    