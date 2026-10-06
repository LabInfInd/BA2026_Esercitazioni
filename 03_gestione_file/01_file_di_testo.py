"""Lezione 1 — Percorsi e scrittura/lettura di testo con UTF-8."""

from pathlib import Path

cartella = Path(__file__).resolve().parent / "dati_generati"
cartella.mkdir(parents=True, exist_ok=True)
percorso = cartella / "saluto.txt"
print(f"File di esempio: {percorso}")

print("\n=== Scrivere testo: w crea o sovrascrive ===")
with percorso.open("w", encoding="utf-8") as file:
    file.write("Ciao, università!\n")
    file.write("Questa è la seconda riga.\n")
print(f"Il file è chiuso fuori dal with: {file.closed}")

print("\n=== Leggere tutto il contenuto ===")
with percorso.open("r", encoding="utf-8") as file:
    contenuto = file.read()
    fine_file = file.read()
print(contenuto, end="")
print(f"Una seconda lettura a fine file restituisce: {fine_file!r}")

print("\n=== Caratteri e byte sono misure diverse ===")
testo = "città"
print(f"{testo!r}: {len(testo)} caratteri, {len(testo.encode('utf-8'))} byte UTF-8")

# Esercizio: aggiungi una terza riga prima della chiusura del primo with.
print(f"\nEsercizio — righe scritte: {len(contenuto.splitlines())}")
