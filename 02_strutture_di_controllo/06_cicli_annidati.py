"""Lezione 6 — Un ciclo dentro un altro ciclo."""

print("=== Coordinate di una griglia 2 x 3 ===")
conteggio = 0
for riga in range(1, 3):
    for colonna in range(1, 4):
        print(f"Riga {riga}, colonna {colonna}")
        conteggio += 1
print(f"Celle visitate: {conteggio}")

print("\n=== break termina soltanto il ciclo più interno ===")
for riga in range(1, 3):
    for colonna in range(1, 4):
        if colonna == 2:
            break
        print(f"Riga {riga}, colonna {colonna}")
    print(f"Fine del ciclo interno per la riga {riga}")

# Esercizio: estendi entrambi i range per ottenere una tabella 5 x 5.
print("\nEsercizio — tabella di moltiplicazione 3 x 3")
for primo in range(1, 4):
    for secondo in range(1, 4):
        print(f"{primo * secondo:3}", end=" ")
    print()  # Una nuova riga al termine del ciclo interno.
