"""Lezione 1 — Tipi di dato fondamentali."""

print("=== Tipi di dato ===")

# Un nome di variabile può riferirsi a valori di tipo diverso.
intero = 10
decimale = 10.3
complesso = 10 + 3j
booleano = True
testo = "Ciao"

for nome, valore in [
    ("intero", intero),
    ("decimale", decimale),
    ("complesso", complesso),
    ("booleano", booleano),
    ("testo", testo),
]:
    print(f"{nome:10}: {valore!r} ({type(valore).__name__})")

print("\n=== Operazioni e conversioni ===")
somma = intero + decimale
print(f"{intero} + {decimale} = {somma}")

eta_testuale = "20"
eta = int(eta_testuale)
print(f"L'età tra un anno sarà {eta + 1}.")

# Esercizio: cambia base e altezza, quindi stampa l'area del rettangolo.
base = 6
altezza = 4
area = base * altezza
print(f"\nEsercizio — area del rettangolo: {area}")
