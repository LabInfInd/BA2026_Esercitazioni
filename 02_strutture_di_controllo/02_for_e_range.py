"""Lezione 2 — Iterare su raccolte e intervalli."""

print("=== for su una lista ===")
studenti = ["Anna", "Luca", "Sara"]
for nome in studenti:
    print(f"Ciao, {nome}!")

print("\n=== range: il limite finale è escluso ===")
for numero in range(1, 6):
    print(f"{numero} al quadrato = {numero ** 2}")

print("\n=== Passo negativo ===")
for secondo in range(3, 0, -1):
    print(secondo)
print("Via!")

print("\n=== enumerate: posizione ed elemento ===")
for posizione, nome in enumerate(studenti, start=1):
    print(f"{posizione}. {nome}")

# Esercizio: estendi il limite a 20 e prevedi il nuovo risultato.
somma = 0
for numero in range(1, 11):
    if numero % 2 == 0:
        somma += numero
print(f"\nEsercizio — somma dei pari da 1 a 10: {somma}")
