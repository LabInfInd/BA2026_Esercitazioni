"""Lezione 3 — Liste: raccolte ordinate e modificabili."""

print("=== Liste ===")
spesa = ["pane", "latte", "uova"]
print(f"Lista iniziale: {spesa}")

print("\n=== Aggiungere e inserire ===")
spesa.append("frutta")
spesa.extend(["pasta", "riso"])
spesa.insert(1, "caffè")
print(f"Dopo le modifiche: {spesa}")

print("\n=== Leggere e rimuovere ===")
print(f"Primo elemento: {spesa[0]}")
print(f"Elementi dal secondo al quarto: {spesa[1:4]}")
elemento_rimosso = spesa.pop()
print(f"Rimosso: {elemento_rimosso}; lista: {spesa}")

print("\n=== Copiare una lista ===")
spesa_copia = spesa[:]
spesa_copia.append("biscotti")
print(f"Originale: {spesa}")
print(f"Copia modificata: {spesa_copia}")

# Esercizio: ordina i numeri in ordine decrescente.
numeri = [7, 3, 10, 4, 5]
numeri_ordinati = sorted(numeri, reverse=True)
print(f"\nEsercizio — {numeri} ordinati: {numeri_ordinati}")
