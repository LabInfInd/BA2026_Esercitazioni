"""Lezione 4 — Tuple e insiemi."""

print("=== Tuple ===")
coordinate = (41.1171, 16.8719)
latitudine, longitudine = coordinate
print(f"Coordinate: {coordinate}")
print(f"Latitudine: {latitudine}, longitudine: {longitudine}")
print("Le tuple sono ordinate ma non possono essere modificate.")

print("\n=== Insiemi ===")
partecipanti_a = {"Anna", "Luca", "Marta", "Luca"}
partecipanti_b = {"Marta", "Paolo", "Sara"}
print(f"Gruppo A: {partecipanti_a}")
print(f"Gruppo B: {partecipanti_b}")
print(f"Tutti: {partecipanti_a | partecipanti_b}")
print(f"In entrambi: {partecipanti_a & partecipanti_b}")
print(f"Solo nel gruppo A: {partecipanti_a - partecipanti_b}")

print("\n=== Insieme immutabile ===")
giorni_festivi = frozenset(["sabato", "domenica"])
print(f"frozenset: {giorni_festivi}")
print("Un frozenset non espone il metodo add(), perché è immutabile.")

# Esercizio: trova gli elementi comuni tra i due insiemi.
numeri_pari = {2, 4, 6, 8}
numeri_primi = {2, 3, 5, 7}
print(f"\nEsercizio — pari e primi: {numeri_pari & numeri_primi}")
