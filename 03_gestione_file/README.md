# Gestione dei file: testo e binari

Prerequisiti: stringhe, liste, cicli e condizioni delle prime due cartelle.
Obiettivo: salvare dati su disco, recuperarli e distinguere testo,
codifica e rappresentazione binaria.

## Percorso della lezione

| File | Concetti | Domanda da porre in aula |
| --- | --- | --- |
| `01_file_di_testo.py` | Percorsi, `with`, `write`, `read`, UTF-8 | Che cosa succede riaprendo un file in modalità `w`? |
| `02_righe_e_append.py` | Iterazione sulle righe, `readline`, `writelines`, `a` | `writelines` aggiunge automaticamente gli a capo? |
| `03_file_binari.py` | `bytes`, `wb`, `rb`, lettura a blocchi, `seek` | Qual è la differenza tra `str` e `bytes`? |
| `04_numeri_binari_struct.py` | Serializzare interi con `struct` | Come sa il lettore quanti byte usare per un numero? |
| `05_gestire_errori.py` | `try`/`except`, file assente, formato errato, `x` | Un file leggibile contiene sempre dati validi? |

Esecuzione dalla cartella principale:

```bash
python3 03_gestione_file/01_file_di_testo.py
```

Gli script usano soltanto la libreria standard, non richiedono file
preesistenti e possono essere eseguiti in qualsiasi ordine. Creano i
propri esempi in `dati_generati/`, accanto agli script, e stampano il
percorso dei dati. La cartella è esclusa da Git. Ogni esecuzione ricrea
i file del relativo esempio; anche quello sull'append riparte da un
contenuto iniziale noto. Non usare quei nomi per conservare dati propri.
La lezione sugli errori usa una directory temporanea, rimossa alla fine.

## Percorsi e apertura

`Path` di `pathlib` rappresenta un percorso. L'operatore `/` unisce una
cartella e un nome di file senza dover scrivere separatori specifici del
sistema operativo.

```python
from pathlib import Path

cartella = Path(__file__).resolve().parent / "dati_generati"
cartella.mkdir(parents=True, exist_ok=True)
percorso = cartella / "saluto.txt"
```

`__file__` è il percorso dello script: permette di trovare i dati anche
se lo script viene avviato da una directory diversa. In una console
interattiva o in un notebook `__file__` può non essere disponibile;
in quel caso scegliere esplicitamente la cartella di lavoro, per esempio
`Path.cwd()`. Un semplice percorso relativo come `Path("saluto.txt")`
si riferisce invece alla directory di lavoro corrente.

## Modalità più comuni

| Modalità | Comportamento | Se il file non esiste |
| --- | --- | --- |
| `r` | Legge testo; è la modalità predefinita | Solleva `FileNotFoundError` |
| `w` | Scrive testo, cancellando il contenuto precedente all'apertura | Crea il file |
| `a` | Scrive testo aggiungendo in fondo | Crea il file |
| `x` | Crea un nuovo file; se esiste solleva `FileExistsError` | Crea il file |
| `rb` | Legge byte senza decodificarli | Solleva `FileNotFoundError` |
| `wb` | Scrive byte, cancellando il contenuto precedente all'apertura | Crea il file |
| `ab` | Aggiunge byte in fondo | Crea il file |

Le modalità di scrittura non creano automaticamente le cartelle mancanti.
Il suffisso `+`, per esempio in `r+`, abilita lettura e scrittura insieme;
si può introdurre dopo aver chiarito il comportamento del cursore.

## Perché usare `with`

```python
with percorso.open("w", encoding="utf-8") as file:
    file.write("Ciao, università!\n")
```

Il file resta aperto nel blocco indentato e viene chiuso quando si esce
dal blocco, anche in caso di eccezione. Dopo la chiusura, per leggerlo
bisogna aprirlo di nuovo. La modalità `w` elimina subito il contenuto
precedente, anche se poi non si scrive nulla.

## Testo, righe e codifica

- In modalità testo si leggono e scrivono stringhe (`str`). Specificare
  `encoding="utf-8"` rende esplicita la codifica, anche per lettere accentate.
- `write(testo)` scrive la stringa ricevuta; non aggiunge `\n`.
- `writelines(righe)` scrive più stringhe; non aggiunge separatori.
- `read()` legge tutto il contenuto: comodo per piccoli file, ma occupa
  memoria proporzionale alle dimensioni del file.
- `readline()` legge una riga e restituisce `""` alla fine del file.
  Una riga vuota nel file può invece essere rappresentata da `"\n"`.
- `for riga in file:` legge progressivamente le righe, utile anche per
  file grandi. Gli a capo fanno parte delle stringhe lette; nell'esempio
  si usa `rstrip("\n")` per rimuovere soltanto l'a capo finale.
- Le letture avanzano il cursore: un secondo `read()` a fine file
  restituisce `""`. Riaprire il file o usare `seek(0)` per ripartire.

## Binario e formato dei dati

In modalità binaria si usano oggetti `bytes`, senza `encoding`. Un byte
può contenere un valore da 0 a 255. `read()` restituisce `bytes` e la
fine del file è segnalata da `b""`.

Un file di testo è comunque memorizzato come byte: la codifica stabilisce
come trasformarli in caratteri. Per esempio `"è".encode("utf-8")`
occupa due byte, pur contenendo un solo carattere. `encode` trasforma
testo in byte e `decode` compie la conversione inversa se i byte sono
validi per quella codifica.

La modalità `wb` non trasforma automaticamente interi o liste in un
formato binario: `file.write(42)` non è valido. Nella lezione `04`,
`struct.pack("<3i", ...)` codifica tre interi con segno, ciascuno di
quattro byte, in ordine **little-endian** (`<`, byte meno significativo
per primo). `struct.unpack` legge lo stesso formato e restituisce una
tupla. Il formato è concordato nel codice: il file non contiene una
descrizione automatica del suo significato. In questo esempio sono
ammessi interi tra −2³¹ e 2³¹ − 1.

Nella lezione `03`, `seek(0)` riporta il cursore all'inizio del file
binario e `tell()` restituisce la sua posizione in byte. Per il testo
non assumere che le posizioni del cursore corrispondano agli indici dei
caratteri: intervengono codifica e gestione degli a capo.

## Errori ed esercizi

`try` racchiude un'operazione che può fallire; `except TipoDiErrore`
gestisce una specifica eccezione. Distinguere un file assente, un problema
di accesso e un contenuto non valido. Evitare un `except` generico che
nasconda anche gli errori di programmazione.

1. Scrivere tre nomi, uno per riga, e rileggerli numerandoli.
2. Contare le righe di un file con un ciclo, senza usare `read()`.
3. Aggiungere una nuova riga con `a`, poi verificare che le precedenti
   siano ancora presenti. Confrontare il risultato con `w` su un file di prova.
4. Confrontare `len("città")` con `len("città".encode("utf-8"))`.
5. Copiare un piccolo file binario leggendo blocchi di due byte e
   verificare che originale e copia abbiano gli stessi byte.
6. Cambiare i tre interi della lezione `04` e prevedere se la dimensione
   del file cambia. Verificare la risposta con `struct.calcsize`.
7. Aggiungere un caso per `UnicodeDecodeError` provando a decodificare
   `b"\xff"` come UTF-8: perché non è un file di testo UTF-8 valido?
