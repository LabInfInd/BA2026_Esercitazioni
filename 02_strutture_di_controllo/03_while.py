"""Lezione 3 — Ripetere finché una condizione è vera."""

print("=== Contatore: inizializzazione, condizione, aggiornamento ===")
contatore = 1
while contatore <= 5:
    print(f"Iterazione {contatore}")
    contatore += 1  # Senza aggiornamento la condizione resterebbe vera.
print(f"Alla fine il contatore vale {contatore}")

print("\n=== Un while può eseguire zero iterazioni ===")
numero = 0
while numero > 0:
    print("Questo messaggio non viene stampato")
    numero -= 1
print("La condizione iniziale era falsa")

print("\n=== Accumulatore: raggiungere una soglia ===")
totale = 0
numero = 1
while totale < 15:
    totale += numero
    print(f"Aggiunto {numero}; totale = {totale}")
    numero += 1

# Esercizio: cambia la partenza e stampa anche il valore finale.
secondi = 3
print("\nEsercizio — conto alla rovescia")
while secondi > 0:
    print(secondi)
    secondi -= 1
print("Via!")
