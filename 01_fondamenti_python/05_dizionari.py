"""Lezione 5 — Dizionari: associazioni fra chiavi e valori."""

print("=== Dizionari ===")
studente = {"nome": "Ada", "corso": "Python", "voto": 28}
print(f"Scheda: {studente}")
print(f"Nome: {studente['nome']}")
print(f"Aula (se presente): {studente.get('aula', 'non assegnata')}")

print("\n=== Modificare e percorrere ===")
studente["voto"] = 30
studente["lode"] = True
for chiave, valore in studente.items():
    print(f"{chiave}: {valore}")

print("\n=== Comprensione di dizionario ===")
quadrati = {numero: numero ** 2 for numero in range(1, 6)}
print(f"Quadrati: {quadrati}")

# Esercizio: aggiungi una materia al dizionario e calcolane la media.
voti = {"matematica": 27, "informatica": 30, "inglese": 26}
media = sum(voti.values()) / len(voti)
print(f"\nEsercizio — voti: {voti}; media: {media:.1f}")
