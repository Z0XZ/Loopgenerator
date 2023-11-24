# Matematikk Oppgavegenerator

## Beskrivelse
Dette prosjektet inneholder en Python-applikasjon utviklet av Jon Bjarne Bø, som genererer matematiske oppgaver og løsninger. Programmet støtter flere oppgavetyper, inkludert lineære likninger, andregradslikninger og regnerekkefølger, og kan lage PDF-dokumenter med disse oppgavene.

## Installasjon
Krever Python 3.x og noen eksterne biblioteker.
1. Klon repositoriet: `git clone [repo-link]`.
2. Installer nødvendige biblioteker: `pip install fpdf tkinter`.

## Bruk
Kjør `python oppgavegenerator.py` og følg brukergrensesnittets instruksjoner for å generere og tilpasse oppgaver.

## Kode Detaljer

### Klassen `lageOppgaver`
Denne klassen er ansvarlig for å generere ulike typer matematiske oppgaver. Den inneholder flere metoder, hvor hver metode representerer en type oppgave (f.eks. lineære likninger, andregradslikninger).

#### Metoder
- `lineæreLikninger()`: Genererer oppgaver med lineære likninger.
- `andregradslikninger()`: Genererer oppgaver med andregradslikninger.
- `regnerekkefølge()`: Genererer oppgaver som involverer regnerekkefølge.

### PDF-oppbygging og Layout
Koden inneholder funksjoner for å opprette og formatere PDF-dokumenter med oppgavene.

#### Funksjoner
- `tegnIndreSirkelMedPil()`: Tegner en sirkel med piler for navigasjon mellom oppgaver.
- `tegnSirklerMedTall()`: Oppretter sider i PDF-en med nummererte sirkler for oppgaver.
- `tegnSirklerUtenTall()`: Oppretter svarark-sider i PDF-en.
- `oppgavegenerator()`: Samler alle oppgaver og genererer den endelige PDF-en.

### Tkinter GUI
Interfacet bruker Tkinter for å samle input fra brukeren, som antall oppgaver og type oppgaver som skal genereres.

#### GUI-elementer
- `Entry`-felt for input av antall oppgaver.
- `Button`-elementer for å velge oppgavetype.

## Bidrag
Ditt bidrag er velkomment! For større endringer, vennligst åpne en issue først for å diskutere hva du ønsker å endre.

## Lisens
Distribuert under MIT-lisensen. Se `LICENSE` for mer informasjon.

## Kontakt
Jon Bjarne Bø - [Din e-post]
