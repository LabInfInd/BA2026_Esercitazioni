"""Lezione 4 — Python non ha do-while: simulazione con while True."""

print("=== while: controllo prima del corpo ===")
numero = 0
while numero > 0:
    print(f"Valore: {numero}")
    numero -= 1
print("Con valore iniziale 0, il corpo non è stato eseguito")

print("\n=== Simulazione do-while: controllo dopo il corpo ===")
numero = 0
while True:
    print(f"Valore: {numero}")
    numero -= 1
    if numero <= 0:  # Esci quando la continuazione (numero > 0) è falsa.
        break
print("Con valore iniziale 0, il corpo è stato eseguito una volta")

print("\n=== Esercizio — ripetere una richiesta fino a un valore valido ===")
# Valori preparati per rendere lo script eseguibile senza input da tastiera.
# Esercizio: aggiungi altri numeri non positivi prima del valore positivo.
tentativi = [-3, 0, 5]
indice = 0
while True:
    numero = tentativi[indice]
    indice += 1
    print(f"Tentativo {indice}: {numero}")
    if numero > 0:
        break
    print("Valore non valido: riprova")
print(f"Numero accettato: {numero}")
# La sequenza deve contenere un numero positivo, altrimenti si esaurisce
# e l'accesso tentativi[indice] produce IndexError.
