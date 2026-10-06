"""Lezione 1 — Selezione e condizioni."""

print("=== if / else ===")
eta = 20
if eta >= 18:
    print("Maggiorenne")
else:
    print("Minorenne")

print("\n=== if / elif / else: conta l'ordine ===")
voto = 24
if voto < 0 or voto > 30:
    print("Voto non valido")
elif voto < 18:
    print("Esame non superato")
elif voto < 27:
    print("Esame superato")
else:
    print("Ottimo risultato")

print("\n=== Operatori logici e appartenenza ===")
ha_prenotazione = True
documento_valido = True
if ha_prenotazione and documento_valido:
    print("Accesso consentito")
if not ha_prenotazione:
    print("Occorre prenotare")

giorno = "lunedì"
if giorno in ["sabato", "domenica"]:
    print("Fine settimana")
else:
    print("Giorno feriale")

# Esercizio: prova anche 0 e un numero negativo. Quale ramo cambia?
numero = 7
if numero < 0:
    categoria = "negativo"
elif numero == 0:
    categoria = "zero"
else:
    categoria = "positivo"
print(f"\nEsercizio — {numero} è {categoria}")
