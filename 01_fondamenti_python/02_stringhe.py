"""Lezione 2 — Stringhe: testo, metodi e slicing."""

print("=== Stringhe ===")
frase = "Ciao, mondo, quanto sei bello!"
print(f"Frase: {frase}")
print(f"Lunghezza: {len(frase)} caratteri")

print("\n=== Metodi utili ===")
print(f"Maiuscolo: {frase.upper()}")
print(f"Minuscolo: {frase.lower()}")
print(f"Parole: {frase.split()}")
print(f"Virgole sostituite: {frase.replace(',', ';')}")

print("\n=== Slicing ===")
print(f"Primi 4 caratteri: {frase[:4]}")
print(f"Ultimi 6 caratteri: {frase[-6:]}")
print(f"Un carattere ogni 2: {frase[::2]}")

print("\n=== Stringhe immutabili ===")
saluto = "ciao"
nuovo_saluto = "m" + saluto[1:]
print(f"Originale: {saluto}; nuova stringa: {nuovo_saluto}")

# Esercizio: ripulisci il nome e stampalo in maiuscolo.
nome = "     Ant  onio     "
nome_pulito = nome.strip().upper()
print(f"\nEsercizio — nome pulito: {nome_pulito}")
