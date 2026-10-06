"""Lezione 5 — Distinguere errori di accesso ed errori nei dati."""

from pathlib import Path
from tempfile import TemporaryDirectory

cartella = Path(__file__).resolve().parent / "dati_generati"
cartella.mkdir(parents=True, exist_ok=True)

# Una directory temporanea garantisce che il file assente non esista
# e isola i casi di errore; viene rimossa all'uscita dal with esterno.
with TemporaryDirectory(prefix="errori_", dir=cartella) as nome_cartella:
    cartella_temporanea = Path(nome_cartella)
    print(f"Directory temporanea di esempio: {cartella_temporanea}")

    print("\n=== File assente ===")
    assente = cartella_temporanea / "assente.txt"
    try:
        with assente.open("r", encoding="utf-8") as file:
            print(file.read())
    except FileNotFoundError:
        print("Il file richiesto non esiste")
    except PermissionError:
        print("Mancano i permessi per leggere il file")

    print("\n=== File presente, contenuto non valido ===")
    percorso = cartella_temporanea / "numero.txt"
    with percorso.open("w", encoding="utf-8") as file:
        file.write("dodici\n")
    with percorso.open("r", encoding="utf-8") as file:
        testo = file.read().strip()
    try:
        numero = int(testo)
        print(f"Numero letto: {numero}")
    except ValueError:
        print(f"{testo!r} non rappresenta un numero intero")

    print("\n=== x impedisce di sovrascrivere un file esistente ===")
    try:
        with percorso.open("x", encoding="utf-8") as file:
            file.write("42\n")
    except FileExistsError:
        print("Il file esiste già: creazione rifiutata")
    with percorso.open("r", encoding="utf-8") as file:
        print(f"Contenuto conservato: {file.read().strip()!r}")

# Esercizio: sostituisci "dodici" con "12" e prevedi l'output.
print("\nLa directory temporanea è stata rimossa automaticamente")
