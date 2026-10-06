# Clustering gerarchico e dendrogramma

Questa esercitazione collega le strutture Python delle lezioni precedenti
all'algoritmo di clustering gerarchico agglomerativo: si parte da un cluster
per punto e si fondono ripetutamente i due cluster più vicini, fino a ottenere
un'unica radice.

## Materiale

- [Guida stampabile al clustering](../output/pdf/guida_clustering_gerarchico.pdf):
  15 pagine A4 con il codice dei due script, spiegazioni, risultati e grafici
  di confronto tra single linkage e metodo del baricentro.
- [`Traccia.pdf`](Traccia.pdf): copia della traccia fornita, con i nove punti,
  le matrici, le fusioni e il dendrogramma dell'esempio single linkage.
- [`dendrogram.py`](dendrogram.py): soluzione fornita, arricchita con commenti
  didattici e stampa delle etichette dei cluster. L'algoritmo di fusione è invariato.
- [`dendrogram_scipy.py`](dendrogram_scipy.py): soluzione alternativa commentata
  con SciPy, stampa delle fusioni e grafico con Matplotlib.
- [`requirements.txt`](requirements.txt): dipendenze dell'alternativa.

Per eseguire dalla cartella principale del progetto:

```bash
python3 04_clustering_gerarchico/dendrogram.py
```

Per la soluzione manuale è sufficiente Python 3: non sono richieste librerie
esterne o input da tastiera.

Le stampe mostrano i membri con le etichette A–I, per esempio:

```text
  -> Uniti cluster {A} e {C} (distanza: 5.66)
Cluster finale: {A, B, C, D, E, F, G, H, I}
```

La funzione `hierarchical_clustering` accetta `labels=LABELS`; omettendo il
parametro si mostrano gli indici numerici. I nomi servono soltanto per la
stampa: gli insiemi `members` conservano gli indici utilizzati nei calcoli.

## Soluzione alternativa con SciPy

Installare le dipendenze nell'ambiente Python utilizzato per la lezione:

```bash
python3 -m pip install -r 04_clustering_gerarchico/requirements.txt
```

Per chi usa l'ambiente virtuale già presente nel progetto, attivarlo prima
con `source .venv/bin/activate` su macOS/Linux, oppure con
`.venv\Scripts\Activate.ps1` in PowerShell su Windows.

```bash
# Stesso criterio della soluzione manuale e dell'esempio svolto nella traccia.
python3 04_clustering_gerarchico/dendrogram_scipy.py

# Metodo del baricentro richiesto nell'esercizio finale.
python3 04_clustering_gerarchico/dendrogram_scipy.py --metodo centroid

# Altri criteri descritti nella traccia.
python3 04_clustering_gerarchico/dendrogram_scipy.py --metodo average
python3 04_clustering_gerarchico/dendrogram_scipy.py --metodo complete

# Salvataggio senza aprire una finestra, anche senza interfaccia grafica.
python3 04_clustering_gerarchico/dendrogram_scipy.py --no-show
```

Lo script importa `POINTS` e `LABELS` da `dendrogram.py`, calcola le fusioni
con `linkage` e le disegna con `dendrogram`. Stampa la matrice `Z` e poi
ricostruisce i membri di ciascun cluster usando le lettere, con distanza
euclidea e suo quadrato per facilitare il confronto con la traccia.
Il PNG è salvato in `grafici_generati/dendrogramma_<metodo>.png`, escluso da
Git e sovrascritto quando si esegue nuovamente lo stesso metodo. Confrontare
fusioni e altezze: la disposizione sinistra/destra delle foglie può variare.

Ogni riga di `Z` contiene quattro valori:

| Colonna | Significato |
| --- | --- |
| `Z[i, 0]` | ID del primo cluster figlio |
| `Z[i, 1]` | ID del secondo cluster figlio |
| `Z[i, 2]` | Distanza della fusione |
| `Z[i, 3]` | Numero di punti del nuovo cluster |

Con nove punti, le foglie hanno ID da 0 a 8 e i genitori da 9 a 16.
`average` media le distanze fra coppie di punti; `centroid` calcola la
distanza fra baricentri. Passare le coordinate a `linkage` con metrica
euclidea è essenziale per usare correttamente il metodo `centroid`.

Riferimenti: [linkage](https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.linkage.html)
e [dendrogram](https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.dendrogram.html).

## Come leggere il codice durante la lezione

1. **Dati e indici.** `POINTS` è una lista di tuple di coordinate; `LABELS`
   associa le lettere ai punti. Gli indici del codice vanno da 0 a 8,
   mentre la traccia numera i punti da 1 a 9: `{0, 2}` significa A e C,
   cioè i punti 1 e 3. `format_cluster` traduce gli indici in etichette e li
   ordina per rendere la stampa stabile: il cluster viene mostrato come `{A, C}`.
2. **Distanza fra punti.** `distanza_euclidea` somma i quadrati delle differenze
   delle coordinate e restituisce la radice quadrata. Il ciclo e
   l'accumulatore riprendono gli esempi sulle strutture di controllo.
3. **Distanza fra cluster.** `cluster_distance` usa due cicli annidati per
   visitare tutte le coppie incrociate di punti. Con `single` conserva il
   minimo; con `average` divide la somma delle distanze per il numero di coppie.
4. **Rappresentazione dell'albero.** `make_leaf` crea un dizionario per un
   punto. `make_parent` unisce gli insiemi dei membri e conserva i riferimenti
   ai figli in `left` e `right`. `height` è la distanza della fusione;
   `size` conta i punti. L'operatore `|` realizza l'unione degli insiemi.
5. **Ricerca e fusione.** `hierarchical_clustering` mantiene una lista di
   cluster attivi. Per ciascuna iterazione del `while`, i due `for` cercano
   la coppia più vicina. Il secondo parte da `i + 1` per evitare duplicati
   e confronti di un cluster con se stesso.
6. **Aggiornamento della lista.** Si rimuovono prima gli indici maggiori,
   così le posizioni ancora da rimuovere non cambiano. Si aggiunge poi il
   genitore: il numero di cluster attivi diminuisce di uno. Con nove punti
   servono otto fusioni.
7. **Risultato.** `root` contiene l'albero completo, costruito come dizionari
   collegati. Il blocco `if __name__ == "__main__"` esegue e stampa l'esempio
   soltanto quando si avvia direttamente il file.

## Confronto con la traccia

Le matrici e gli indici di aggregazione della traccia riportano **i quadrati
delle distanze**, mentre il codice usa **le distanze euclidee**. Per il single
linkage la radice quadrata conserva l'ordine dei minimi: le fusioni coincidono,
ma i valori numerici stampati sono diversi.

| Fusione | Cluster creato | Punti nella traccia | Distanza nel codice circa | Quadrato nella traccia |
| --- | --- | --- | --- | --- |
| 1 | AC | 1, 3 | 5.66 | 32 |
| 2 | HI | 8, 9 | 5.83 | 34 |
| 3 | ABC | 1, 2, 3 | 11.40 | 130 |
| 4 | DF | 4, 6 | 14.21 | 202 |
| 5 | DEF | 4, 5, 6 | 20.52 | 421 |
| 6 | ABCG | 1, 2, 3, 7 | 25.08 | 629 |
| 7 | ABCDEFG | 1, 2, 3, 4, 5, 6, 7 | 30.02 | 901 |
| 8 | ABCDEFGHI | 1, 2, 3, 4, 5, 6, 7, 8, 9 | 32.31 | 1044 |

L'arrotondamento a due decimali riguarda soltanto l'output: il calcolo conserva
la distanza non arrotondata. Non elevare al quadrato il valore già arrotondato
aspettandoti di ricostruire esattamente gli interi della traccia.

## Average linkage e baricentro

La soluzione supporta `single` e `average`. Per provare `average`, cambiare
il parametro nell'ultima chiamata e aggiornare la descrizione stampata:

```python
root = hierarchical_clustering(
    POINTS, linkage_method="average", verbose=True, labels=LABELS
)
```

L'average linkage calcola la media delle distanze di tutte le coppie incrociate.
Il **metodo del baricentro**, richiesto nell'esercizio finale della traccia,
calcola invece la distanza fra i baricentri dei due cluster, ottenuti mediando
le coordinate dei rispettivi punti. Sono criteri distinti: scegliere `average`
non implementa l'esercizio sui baricentri. Inoltre, la media delle distanze
non equivale alla radice della media dei loro quadrati.

La soluzione manuale costruisce la struttura del dendrogramma e stampa le fusioni;
**non disegna il grafico**. Il baricentro e il disegno restano possibili
estensioni della soluzione manuale; sono disponibili nello script alternativo
`dendrogram_scipy.py` tramite `--metodo centroid` e il grafico Matplotlib.

## Domande per verificare la comprensione

- Perché un cluster conserva indici invece di copiare le coordinate?
- Quante coppie di cluster si confrontano quando ne rimangono quattro?
  Risposta: `4 * 3 / 2 = 6`.
- Perché `best_i` è una posizione nella lista e può essere diverso dall'`id`?
- Perché si rimuove prima la posizione maggiore?
- Dove rimangono i nodi figli dopo la loro rimozione dalla lista attiva?
- Che cosa cambierebbe usando il massimo invece del minimo fra le coppie?
  Si otterrebbe il complete linkage descritto nella traccia.

La soluzione assume dati non vuoti, coordinate numeriche della stessa
dimensione e un metodo riconosciuto. Non aggiunge controlli su queste
precondizioni: i commenti indicano anche i limiti del codice originale.
