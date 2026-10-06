# Didattica 2026

Materiale didattico per le esercitazioni e le lezioni di programmazione.

## Guida per la lezione

La [guida unica in PDF](output/pdf/guida_python_controllo_e_file.pdf)
raccoglie in 16 pagine A4 il codice completo degli esempi delle cartelle
`02_strutture_di_controllo` e `03_gestione_file`, con spiegazioni,
risultati attesi, domande per l'aula ed esercizi. È pronta per la stampa.

La [guida al clustering gerarchico](output/pdf/guida_clustering_gerarchico.pdf)
dedica 15 pagine A4 all'esercitazione della cartella `04_clustering_gerarchico`:
codice manuale e alternativa SciPy, etichette dei cluster, spiegazioni,
confronto con la traccia e dendrogrammi single e centroid.

## Struttura

- [`01_fondamenti_python/`](01_fondamenti_python/): cinque lezioni eseguibili
  sui concetti iniziali di Python: tipi di dato, stringhe, liste, tuple e
  insiemi, dizionari.
- [`02_strutture_di_controllo/`](02_strutture_di_controllo/): condizioni
  `if`/`elif`/`else`, cicli `for` e `while`, simulazione del `do-while`,
  `break`, `continue` e cicli annidati.
- [`03_gestione_file/`](03_gestione_file/): percorsi, lettura e scrittura
  di file di testo, aggiunta in coda, file binari ed errori di accesso.
- [`04_clustering_gerarchico/`](04_clustering_gerarchico/): traccia e soluzione
  commentata del clustering gerarchico, con spiegazione delle fusioni e
  della struttura del dendrogramma; alternativa con SciPy e grafico Matplotlib.

Ogni file può essere eseguito singolarmente dalla cartella del progetto, ad
esempio:

```bash
python 01_fondamenti_python/01_tipi_di_dato.py
```

I materiali richiedono Python 3. Le prime tre cartelle e la soluzione manuale
del clustering usano soltanto la libreria standard; l'alternativa con SciPy
richiede le dipendenze elencate in `04_clustering_gerarchico/requirements.txt`.
I README delle singole cartelle contengono spiegazioni, una traccia per
la lezione ed esercizi. Gli esempi non richiedono input da tastiera.

```bash
python3 02_strutture_di_controllo/01_if_elif_else.py
python3 03_gestione_file/01_file_di_testo.py
```

Gli esempi sui file creano i propri dati nella sottocartella
`03_gestione_file/dati_generati/`, esclusa da Git. Ogni script è autonomo
e può essere eseguito anche da una directory di lavoro diversa.
