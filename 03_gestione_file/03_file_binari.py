"""Lezione 3 — Scrivere e leggere byte senza una codifica testuale."""

from pathlib import Path

cartella = Path(__file__).resolve().parent / "dati_generati"
cartella.mkdir(parents=True, exist_ok=True)
percorso = cartella / "byte_esempio.bin"
print(f"File di esempio: {percorso}")

print("\n=== bytes: valori da 0 a 255 ===")
dati = bytes([0, 10, 127, 128, 255])
print(f"Rappresentazione: {dati!r}")
print(f"Valori numerici: {list(dati)}")
with percorso.open("wb") as file:
    file.write(dati)  # In binario si scrivono bytes, non str.

print("\n=== Leggere tutti i byte ===")
with percorso.open("rb") as file:
    riletti = file.read()
print(f"Dati riletti: {riletti!r}")
print(f"Uguali all'originale: {riletti == dati}")

print("\n=== Leggere a blocchi e spostare il cursore ===")
with percorso.open("rb") as file:
    while True:
        blocco = file.read(2)  # L'ultimo blocco può contenere meno di 2 byte.
        if blocco == b"":
            break
        print(f"Blocco: {list(blocco)}; posizione: {file.tell()}")
    file.seek(0)
    print(f"Primo byte dopo seek(0): {file.read(1)!r}")

# Esercizio: cambia i valori iniziali mantenendoli nell'intervallo 0..255.
print(f"\nEsercizio — dimensione del file: {percorso.stat().st_size} byte")
