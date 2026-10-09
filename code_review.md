### Code Review av originalkoden

### Fynd 1: All funktionalitet ligger i samma fil
Observation
Originalkoden hanterar filinläsning, validering, datarensning, beräkningar, rapportgenerering och export till CSV i samma programfil.

Konsekvens
Det gör koden svårare att förstå, underhålla och testa.

Förslag
Dela upp lösningen i separata moduler.

----------------------------------------

### Fynd 2: Använder print() för statusmeddelanden

Observation
Programmet använder print() för att visa information om programmets körning.

Konsekvens
Det blir svårt att styra loggning och felsöka problem.

Förslag
Använd logging istället för print().

----------------------------------------

### Fynd 3: Duplicerad kod vid rapportgenerering

Observation
Flera rapporter skapas med liknande groupby-, sorterings- och exportlogik.

Konsekvens
Koden blir längre och svårare att underhålla.

Förslag
Flytta gemensam logik till återanvändbara funktioner.

----------------------------------------

### Fynd 4: Generell felhantering

Observation
Programmet fångar alla fel med ett generellt Exception.

Konsekvens
Det blir svårare att förstå vad som orsakat felet.

Förslag
Fånga specifika fel som FileNotFoundError och ValueError.

----------------------------------------

### Fynd 5: Hårdkodade sökvägar

Observation
Filvägar för indata och utdata är definierade direkt i koden.

Konsekvens
Programmet blir mindre flexibelt.

Förslag
Samla konfiguration i en separat modul eller dataclass.

----------------------------------------

### Fynd 6: Begränsad testbarhet

Observation
Många beräkningar sker direkt i huvudflödet.

Konsekvens
Det blir svårare att skriva automatiska tester.

Förslag
Flytta logik till separata funktioner som kan testas isolerat.