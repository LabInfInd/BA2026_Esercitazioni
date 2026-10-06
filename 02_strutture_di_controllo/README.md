# Strutture di controllo in Python

Prerequisiti: variabili, numeri, booleani, stringhe e liste della prima
cartella. Obiettivo: scegliere quali istruzioni eseguire e ripetere un
blocco di codice in modo controllato.

## Percorso della lezione

| File | Concetti | Domanda da porre in aula |
| --- | --- | --- |
| `01_if_elif_else.py` | Confronti, operatori logici, selezione | Quale ramo viene eseguito per un voto di 18? |
| `02_for_e_range.py` | Iterazione, `range`, `enumerate` | Perché `range(1, 6)` non include 6? |
| `03_while.py` | Condizione e aggiornamento dello stato | Cosa succede se togliamo l'incremento? |
| `04_simulare_do_while.py` | Controllo prima o dopo il corpo | Il corpo viene eseguito se la condizione iniziale è falsa? |
| `05_break_continue_else.py` | Interruzione, salto, `else` del ciclo | Quando viene eseguito l'`else` di una ricerca? |
| `06_cicli_annidati.py` | Cicli interni ed esterni | Quante volte viene eseguito il corpo interno? |

Esecuzione dalla cartella principale:

```bash
python3 02_strutture_di_controllo/01_if_elif_else.py
```

Ogni script stampa esempi e un esercizio già risolto da modificare.
Prima dell'esecuzione, chiedere agli studenti di prevedere l'output;
dopo, cambiare un valore e discutere cosa cambia.

## Blocchi, condizioni e selezione

Il simbolo `:` introduce un blocco. Python usa l'**indentazione** per
riconoscere le istruzioni che ne fanno parte: usare quattro spazi per
livello, senza mescolare spazi e tabulazioni.

```python
voto = 24
if voto >= 18:
    print("Esame superato")
else:
    print("Esame non superato")
print("Questa istruzione viene eseguita in entrambi i casi")
```

- `if` verifica una condizione; `elif` verifica una condizione successiva
  solo se le precedenti sono false; `else` gestisce i casi restanti.
- In una catena `if`/`elif`/`else` viene eseguito al massimo un ramo.
  Più `if` separati possono invece eseguire più blocchi.
- Confronti: `==`, `!=`, `<`, `<=`, `>`, `>=`. `=` assegna un valore,
  mentre `==` confronta due valori.
- `and` richiede entrambe le condizioni, `or` almeno una, `not` nega
  la condizione. Usare parentesi per rendere chiara un'espressione composta.
- `in` controlla l'appartenenza a una raccolta.

## Ripetizione: `for` e `while`

`for elemento in raccolta:` visita gli elementi di un iterabile, per
esempio una lista o una stringa. Per ripetere un'operazione su una
sequenza di interi si usa `range`:

- `range(5)` produce 0, 1, 2, 3, 4;
- `range(1, 6)` produce 1, 2, 3, 4, 5;
- `range(5, 0, -1)` produce 5, 4, 3, 2, 1.

Il limite finale è sempre escluso e il passo non può essere zero.
`enumerate(raccolta, start=1)` fornisce insieme posizione ed elemento.

`while condizione:` ripete il blocco finché la condizione è vera, con
una verifica **prima** di ogni iterazione. Può eseguire zero iterazioni.
Nel corpo deve esserci un modo per far diventare falsa la condizione
o interrompere il ciclo; altrimenti il ciclo può essere infinito.

## Come rappresentare il `do-while`

Python **non ha un'istruzione `do-while`**. Per eseguire il corpo almeno
una volta e verificare la continuazione alla fine, si usa questo schema:

```python
while True:
    # Operazioni da eseguire almeno una volta.
    if not condizione_di_continuazione:
        break
```

La condizione di uscita è la negazione della condizione che farebbe
continuare un `do-while`. Nel file `04` si confrontano i due comportamenti
e si simula la richiesta di un numero positivo con valori già preparati.
Per una variante interattiva si può sostituire l'assegnazione del valore
con `numero = int(input("Inserisci un numero positivo: "))`; introdurre
prima la gestione di `ValueError` se il testo digitato non è un intero.

## Controllare i cicli

- `break` termina immediatamente il ciclo più interno.
- `continue` salta le istruzioni rimanenti dell'iterazione corrente.
  In un `while`, attenzione a non saltare l'aggiornamento del contatore.
- L'`else` di un ciclo viene eseguito quando il ciclo termina normalmente,
  senza `break`, anche se il corpo ha eseguito zero iterazioni.
  Non indica che la condizione di un `if` è falsa.
- In un ciclo annidato, il ciclo interno riparte per ogni iterazione
  di quello esterno.
- `pass` è un'istruzione che non fa nulla, utile come segnaposto di un
  blocco ancora da scrivere; non salta l'iterazione come `continue`.

## Esercizi da assegnare

1. Classificare un numero come negativo, zero o positivo con `if`/`elif`/`else`.
2. Sommare i numeri pari da 1 a 20 usando `for`, `%` e una variabile accumulatore.
3. Riscrivere il conto alla rovescia con `while` e spiegare quando si ferma.
4. Modificare i valori simulati del `do-while` aggiungendo altri tentativi
   non validi prima di un valore positivo.
5. Cercare un nome in una lista; stampare «non trovato» usando l'`else` del ciclo.
6. Stampare una tabella di moltiplicazione da 1 a 5 con due cicli annidati.

Per verificare la comprensione, provare anche liste vuote, valori sul
confine di una condizione e una ricerca senza risultati.
