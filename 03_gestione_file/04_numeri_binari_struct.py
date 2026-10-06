"""Lezione 4 — Un formato binario esplicito per tre interi."""

from pathlib import Path
import struct

cartella = Path(__file__).resolve().parent / "dati_generati"
cartella.mkdir(parents=True, exist_ok=True)
percorso = cartella / "temperature.bin"
print(f"File di esempio: {percorso}")

print("\n=== pack: dai numeri ai byte ===")
temperature = [-5, 0, 23]
formato = "<3i"  # Little-endian, 3 interi con segno da 4 byte ciascuno.
# *temperature passa i tre elementi come tre argomenti a pack.
dati = struct.pack(formato, *temperature)
print(f"Temperature originali: {temperature}")
print(f"Dimensione prevista: {struct.calcsize(formato)} byte")
print(f"Byte prodotti: {dati.hex(' ')}")
with percorso.open("wb") as file:
    file.write(dati)

print("\n=== unpack: dai byte ai numeri ===")
with percorso.open("rb") as file:
    riletti = file.read()

# unpack richiede esattamente il numero di byte previsto dal formato.
if len(riletti) == struct.calcsize(formato):
    recuperate = struct.unpack(formato, riletti)
    print(f"Temperature recuperate (tupla): {recuperate}")
    print(f"Valori conservati: {list(recuperate) == temperature}")
else:
    print("Dimensione non valida per il formato concordato")

# Esercizio: cambia i tre interi. La dimensione del file cambia?
print(f"\nEsercizio — dimensione effettiva: {percorso.stat().st_size} byte")
