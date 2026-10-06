"""Lezione 2 — Scrivere righe, aggiungere in coda e leggere a righe."""

from pathlib import Path

cartella = Path(__file__).resolve().parent / "dati_generati"
cartella.mkdir(parents=True, exist_ok=True)
percorso = cartella / "studenti.txt"
print(f"File di esempio: {percorso}")

print("\n=== Preparare un contenuto iniziale ===")
# Il reset con w rende il risultato identico a ogni esecuzione.
with percorso.open("w", encoding="utf-8") as file:
    file.writelines(["Anna\n", "Luca\n"])  # Gli a capo sono espliciti.

print("\n=== Append: conservare il testo e aggiungere in fondo ===")
with percorso.open("a", encoding="utf-8") as file:
    file.write("Sara\n")

print("\n=== Iterare sulle righe ===")
conteggio = 0
with percorso.open("r", encoding="utf-8") as file:
    for posizione, riga in enumerate(file, start=1):
        nome = riga.rstrip("\n")
        print(f"{posizione}. {nome}")
        conteggio += 1

print("\n=== readline: ogni lettura avanza il cursore ===")
with percorso.open("r", encoding="utf-8") as file:
    print(f"Prima riga: {file.readline()!r}")
    print(f"Seconda riga: {file.readline()!r}")

# Esercizio: aggiungi un altro nome nel blocco in modalità a.
print(f"\nEsercizio — numero di righe: {conteggio}")
