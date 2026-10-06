"""Lezione 5 — Interrompere o saltare un'iterazione; else del ciclo."""

print("=== break: interrompere una ricerca ===")
numeri = [3, 7, 10, 12]
cercato = 10
for numero in numeri:
    print(f"Esamino {numero}")
    if numero == cercato:
        print("Trovato: interrompo la ricerca")
        break
else:
    print("Numero non trovato")  # Eseguito soltanto se non c'è stato break.

print("\n=== continue: ignorare i valori negativi ===")
misure = [12, -1, 18, -5, 20]
totale = 0
for misura in misure:
    if misura < 0:
        continue
    totale += misura
    print(f"Misura accettata: {misura}")
print(f"Totale delle misure valide: {totale}")

print("\n=== continue in un while: aggiornare prima del salto ===")
numero = 0
while numero < 5:
    numero += 1
    if numero % 2 == 0:
        continue
    print(f"Dispari: {numero}")

# Esercizio: cerca anche "Sara" e ripeti con una lista vuota.
print("\nEsercizio — ricerca di un nome")
studenti = ["Anna", "Luca", "Sara"]
cercato = "Marco"
for nome in studenti:
    if nome == cercato:
        print(f"{cercato} è presente")
        break
else:
    print(f"{cercato} non trovato")
