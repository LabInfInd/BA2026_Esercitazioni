"""
Clustering Gerarchico Agglomerativo
====================================
Implementazione di un algoritmo di clustering gerarchico con supporto per:
- Single linkage (distanza minima tra cluster)
- Average linkage (distanza media tra cluster)

Versione didattica commentata della soluzione fornita.

Collegamento con Traccia.pdf:
- A, B, ..., I corrispondono ai punti 1, 2, ..., 9 della traccia.
- Il codice usa indici Python da 0 a 8 per accedere alla lista POINTS.
- La traccia riporta d^2; il codice restituisce d, cioè la radice di d^2.
  Per esempio, A e C hanno d^2 = 32 e vengono uniti a circa 5.66.
- Average linkage e metodo del baricentro sono due criteri diversi.
  Il baricentro richiesto nell'esercizio finale non è implementato qui.
- Il programma costruisce l'albero in memoria e stampa le fusioni;
  non produce un disegno del dendrogramma.

Precondizioni della soluzione originale: dataset non vuoto, punti con
lo stesso numero di coordinate, metodo "single" oppure "average".
L'algoritmo originale è invariato; le stampe usano le etichette dei punti
quando vengono fornite al parametro labels.
"""

# Import già presente nella soluzione: la radice viene calcolata con ** 0.5.
import math

# =============================================================================
# CONFIGURAZIONE DATI
# =============================================================================

# Dataset: coordinate (x, y) dei punti da clusterizzare.
# POINTS è una lista di tuple: POINTS[0] è A, POINTS[1] è B, ecc.
# Un cluster memorizzerà gli indici dei punti, non le coordinate stesse.
POINTS = [
    (12, 23),  # A
    (25, 20),  # B
    (16, 27),  # C
    (81, 26),  # D
    (55, 21),  # E
    (70, 35),  # F
    (18, 52),  # G
    (48, 64),  # H
    (51, 69)  # I
]

# Etichette associate ai punti.
# Le stampe traducono gli indici in etichette: {0, 2} diventa {A, C},
# cioè i punti 1 e 3 della traccia. I calcoli continuano a usare gli indici.
LABELS = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]


# =============================================================================
# FUNZIONI DI DISTANZA
# =============================================================================

def distanza_euclidea(p, q):
    """
    Calcola la distanza euclidea tra due punti.

    Args:
        p (tuple): Primo punto (coordinate)
        q (tuple): Secondo punto (coordinate)

    Returns:
        float: Distanza euclidea tra p e q

    Esempio:
        >>> distanza_euclidea((0, 0), (3, 4))
        5.0
    """
    # Accumulatore: parte da zero e raccoglie (p[i] - q[i])^2.
    # La funzione vale anche in più di due dimensioni, purché p e q
    # abbiano lo stesso numero di componenti.
    somma_quadrati = 0.0

    # len(p) conta le coordinate; range produce gli indici da 0 a len(p)-1.
    for i in range(len(p)):
        # Calcola la differenza tra la i-esima componente di p e q
        differenza = p[i] - q[i]
        # += aggiorna la somma; moltiplicare la differenza per se stessa
        # rende non negativo ogni contributo.
        somma_quadrati += differenza * differenza

    # Il quadrato della distanza è quello riportato nelle matrici della
    # traccia. La radice restituisce la distanza euclidea effettiva.
    return somma_quadrati ** 0.5  # Radice quadrata


def cluster_distance(c1, c2, points, linkage):
    """
    Calcola la distanza tra due cluster secondo il metodo specificato.

    Args:
        c1 (dict): Primo cluster
        c2 (dict): Secondo cluster
        points (list): Lista di tutti i punti
        linkage (str): Metodo di linkage ("single" o "average")

    Returns:
        float: Distanza tra i due cluster
        None: Se il metodo di linkage non è riconosciuto
    """
    # c1 e c2 sono dizionari. La chiave "members" contiene un insieme
    # di indici: points[i] permette di recuperare il punto corrispondente.
    # Ogni coppia incrociata contiene un punto di c1 e un punto di c2.
    if linkage == "single":
        # SINGLE LINKAGE: distanza minima tra due punti dei cluster
        # +infinito è maggiore di ogni distanza finita: la prima coppia
        # esaminata potrà quindi aggiornare il minimo.
        distanza_minima = float("inf")

        # Cicli annidati: per ciascun membro del primo cluster si
        # confrontano tutti i membri del secondo cluster.
        for i in c1["members"]:
            punto1 = points[i]
            for j in c2["members"]:
                punto2 = points[j]
                distanza = distanza_euclidea(punto1, punto2)

                # Il minimo viene aggiornato solo quando si trova
                # una coppia di punti più vicina di quelle già esaminate.
                if distanza < distanza_minima:
                    distanza_minima = distanza

        return distanza_minima

    elif linkage == "average":
        # AVERAGE LINKAGE: media delle distanze di tutte le coppie
        # incrociate, una con un punto di c1 e uno di c2.
        # Non è la distanza tra baricentri. Si mediano le distanze
        # euclidee, non i loro quadrati.
        somma_distanze = 0.0
        numero_coppie = 0

        # Cicli annidati: per ciascun membro del primo cluster si
        # confrontano tutti i membri del secondo cluster.
        for i in c1["members"]:
            punto1 = points[i]
            for j in c2["members"]:
                punto2 = points[j]
                distanza = distanza_euclidea(punto1, punto2)

                numero_coppie += 1
                somma_distanze += distanza

        # Se i cluster hanno m e n membri, le coppie sono m*n.
        # I cluster creati dall'algoritmo sono sempre non vuoti,
        # quindi il denominatore è diverso da zero.
        return somma_distanze / numero_coppie

    # Metodo non riconosciuto: il comportamento originale restituisce
    # None. Il chiamante confronta il risultato con un numero, quindi
    # occorre passare "single" o "average" per evitare TypeError.
    return None


# =============================================================================
# FUNZIONI PER LA CREAZIONE DI CLUSTER
# =============================================================================

def make_leaf(idx):
    """
    Crea un cluster foglia (nodo iniziale contenente un singolo punto).

    Args:
        idx (int): Indice del punto nel dataset

    Returns:
        dict: Cluster foglia con struttura:
            - id: identificatore del cluster
            - members: insieme degli indici dei punti contenuti
            - height: altezza nel dendrogramma (0 per le foglie)
            - size: numero di punti nel cluster
    """
    # Una foglia è un dizionario che rappresenta un solo punto.
    # {idx} è un insieme con un elemento, non un dizionario.
    # L'altezza è zero perché non è ancora avvenuta alcuna fusione.
    return {
        "id": idx,
        "members": {idx},
        "height": 0.0,
        "size": 1
    }


def make_parent(new_idx, left, right, height):
    """
    Crea un cluster genitore fondendo due cluster esistenti.

    Args:
        new_idx (int): Nuovo identificatore del cluster
        left (dict): Cluster figlio sinistro
        right (dict): Cluster figlio destro
        height (float): Altezza (distanza) a cui avviene la fusione

    Returns:
        dict: Cluster genitore con struttura che include:
            - left/right: riferimenti ai cluster figli
            - members: unione dei membri dei due cluster
    """
    # Il genitore è un nuovo nodo dell'albero. "left" e "right"
    # conservano i figli, così le fusioni precedenti non vanno perdute.
    # Il valore height è la distanza TRA I CLUSTER al momento della
    # fusione: non è la somma delle altezze dei due figli.
    # | unisce due insiemi, conservando ciascun indice una sola volta.
    # I cluster attivi sono disgiunti, quindi le loro size si sommano.
    return {
        "id": new_idx,
        "left": left,
        "right": right,
        "members": left["members"] | right["members"],  # Unione insiemi
        "height": height,
        "size": left["size"] + right["size"]
    }


# =============================================================================
# ALGORITMO DI CLUSTERING GERARCHICO
# =============================================================================

def format_cluster(cluster, labels=None):
    """Restituisce i membri come {A, C}, oppure {0, 2} senza etichette."""
    # Un insieme non garantisce un ordine di visualizzazione: sorted
    # ordina gli indici secondo la posizione dei punti nel dataset.
    indici = sorted(cluster["members"])
    if labels is None:
        nomi = [str(i) for i in indici]
    else:
        nomi = [str(labels[i]) for i in indici]

    # join separa i nomi con una virgola; le graffe richiamano l'insieme
    # dei membri. Questa funzione modifica solo la rappresentazione testuale.
    return "{" + ", ".join(nomi) + "}"


def hierarchical_clustering(points, linkage_method="single", verbose=True, labels=None):
    """
    Esegue il clustering gerarchico agglomerativo.

    Args:
        points (list): Lista di punti da clusterizzare
        linkage_method (str): Metodo di linkage ("single" o "average")
        verbose (bool): Se True, stampa i passi dell'algoritmo
        labels (list): Etichette dei punti, nello stesso ordine di points.
            Se omesse, le stampe mostrano gli indici numerici.

    Returns:
        dict: Cluster radice (dendrogramma completo)
    """
    # Ogni punto deve avere la propria etichetta; gli indici restano
    # all'interno dei cluster, così le etichette non influenzano le distanze.
    if labels is not None and len(labels) != len(points):
        raise ValueError("Occorre un'etichetta per ogni punto")

    # Inizializzazione: ogni punto è un cluster separato.
    # La list comprehension richiama make_leaf per ogni indice.
    # "clusters" è la lista dei cluster ATTIVI, ancora candidati alle
    # prossime fusioni; i nodi già fusi restano raggiungibili nei genitori.
    clusters = [make_leaf(i) for i in range(len(points))]
    step = 0

    # verbose controlla soltanto la stampa, non il risultato del calcolo.
    # format_cluster traduce i membri in etichette ordinate e join unisce
    # le rappresentazioni dei cluster con uno spazio. Il for è un generatore.
    if verbose:
        stato = " ".join(format_cluster(c, labels) for c in clusters)
        print(f"Step {step}: {stato}")

    # Iterazione fino a quando rimane un solo cluster.
    # Ogni fusione sostituisce due cluster con uno: il numero di cluster
    # diminuisce di 1. Da n punti si arriva alla radice con n-1 fusioni.
    while len(clusters) > 1:
        # Trova la coppia di cluster con distanza minima.
        # Gli indici best_i e best_j sono POSIZIONI nella lista clusters,
        # non gli identificatori dei nodi né gli indici dei punti.
        # Si azzera la ricerca a ogni iterazione, perché i cluster
        # attivi sono cambiati dopo la fusione precedente.
        best_i = None
        best_j = None
        best_distance = float("inf")

        # Si visitano tutte le coppie di cluster distinti.
        # j parte da i+1: evita il confronto di un cluster con se stesso
        # e non ripete una coppia in ordine inverso. Con k cluster
        # si effettuano k*(k-1)/2 confronti tra cluster.
        for i in range(len(clusters)):
            for j in range(i + 1, len(clusters)):
                distanza = cluster_distance(
                    clusters[i], clusters[j], points, linkage_method
                )

                # Con <, a parità di distanza resta la prima coppia
                # incontrata nell'ordine corrente della lista.
                # La distanza fra cluster è ricalcolata usando i membri,
                # senza memorizzare una matrice delle distanze.
                if distanza < best_distance:
                    best_distance = distanza
                    best_i = i
                    best_j = j

        # Fondi i due cluster più vicini: gli indici selezionati sopra
        # individuano i due dizionari da collegare al nuovo genitore.
        cluster1 = clusters[best_i]
        cluster2 = clusters[best_j]
        # Le foglie hanno ID 0..n-1, i genitori n..2*n-2.
        # L'ID è stabile anche quando cambiano le posizioni nella lista.
        new_id = len(points) + step  # ID univoco per il nuovo cluster
        parent_cluster = make_parent(new_id, cluster1, cluster2, best_distance)

        # Rimuovi i cluster originali e aggiungi quello nuovo
        # (rimuovi prima l'indice maggiore per evitare problemi di shift)
        # Esempio: rimuovendo prima la posizione 1, la vecchia posizione 4
        # diventa 3. Rimuovere prima 4 e poi 1 evita di prendere il nodo errato.
        # pop toglie un elemento dalla lista attiva, non cancella il nodo:
        # il genitore ne conserva il riferimento in "left" o "right".
        for idx in sorted([best_i, best_j], reverse=True):
            clusters.pop(idx)
        clusters.append(parent_cluster)

        # Aggiorna il contatore dopo aver completato la fusione.
        step += 1
        if verbose:
            stato = " ".join(format_cluster(c, labels) for c in clusters)
            print(f"Step {step}: {stato}")
            # La f-string inserisce i valori; :.2f visualizza due decimali.
            # L'arrotondamento riguarda solo la stampa, non il calcolo.
            print(f"  -> Uniti cluster {format_cluster(cluster1, labels)} "
                  f"e {format_cluster(cluster2, labels)} "
                  f"(distanza: {best_distance:.2f})")

    # Rimane la radice, che contiene tutti gli indici e i riferimenti
    # ai figli: seguendoli si può ricostruire l'intero dendrogramma.
    # Con un solo punto si restituisce la sua foglia senza fusioni;
    # con una lista vuota l'originale solleva IndexError.
    return clusters[0]


# =============================================================================
# ESECUZIONE PRINCIPALE
# =============================================================================

# Questo blocco si esegue soltanto avviando il file come script.
# Importando il modulo, dati e funzioni diventano disponibili senza
# eseguire automaticamente il clustering o stampare il risultato.
if __name__ == "__main__":
    print("=" * 70)
    print("CLUSTERING GERARCHICO AGGLOMERATIVO")
    print("=" * 70)
    print(f"\nNumero di punti: {len(POINTS)}")
    print(f"Metodo di linkage: Single Linkage\n")

    # Esegui clustering con la distanza minima, come nell'esempio svolto
    # della traccia. Per esplorare l'altro metodo supportato si può passare
    # linkage_method="average" e aggiornare il testo stampato sopra.
    # Questo confronto non svolge l'esercizio finale sui baricentri.
    root = hierarchical_clustering(
        POINTS, linkage_method="single", verbose=True, labels=LABELS
    )

    print("\n" + "=" * 70)
    print("CLUSTERING COMPLETATO")
    print("=" * 70)
    # root è un dizionario, non un grafico. L'altezza finale è espressa
    # in distanze euclidee: sqrt(1044), arrotondata a 32.31 nella stampa.
    print(f"\nCluster finale: {format_cluster(root, LABELS)}")
    print(f"Altezza totale del dendrogramma: {root['height']:.2f}")
