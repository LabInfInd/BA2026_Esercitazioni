"""Soluzione alternativa con SciPy e grafico del dendrogramma.

Esempi dalla cartella principale:
    python3 04_clustering_gerarchico/dendrogram_scipy.py
    python3 04_clustering_gerarchico/dendrogram_scipy.py --metodo centroid

Dipendenze: scipy e matplotlib, elencate in requirements.txt.
"""

import argparse
from pathlib import Path

import matplotlib
from scipy.cluster.hierarchy import dendrogram, linkage

# Importiamo gli stessi dati della soluzione manuale per poter confrontare
# i risultati. Il suo blocco __main__ non viene eseguito durante l'import.
from dendrogram import LABELS, POINTS


def main():
    # argparse legge opzioni da riga di comando: choices ammette soltanto
    # i quattro metodi descritti nella traccia; il default è single linkage.
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--metodo",
        choices=["single", "complete", "average", "centroid"],
        default="single",
        help="Criterio di fusione dei cluster (predefinito: single)",
    )
    parser.add_argument(
        "--no-show",
        action="store_true",
        help="Salva il grafico senza aprire una finestra",
    )
    args = parser.parse_args()

    # Il backend Agg disegna direttamente su file, anche senza interfaccia
    # grafica. Va scelto prima di importare pyplot.
    if args.no_show:
        matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    # linkage sostituisce la ricerca e la fusione scritte a mano.
    # POINTS contiene le coordinate, non la matrice dei quadrati delle
    # distanze presente nella traccia. La metrica è quindi euclidean.
    # single: minimo; complete: massimo; average: media delle distanze;
    # centroid: distanza tra i baricentri dei cluster (esercizio finale).
    Z = linkage(POINTS, method=args.metodo, metric="euclidean")

    # Z ha n-1 righe, una per fusione, e quattro colonne:
    # [ID figlio sinistro, ID figlio destro, distanza, numero di punti].
    # Le foglie hanno ID 0..n-1; il genitore della riga i ha ID n+i.
    # I valori di Z sono numeri in virgola mobile: gli ID e le dimensioni
    # vengono convertiti in int quando li usiamo come indici o li stampiamo.
    print(f"Metodo: {args.metodo}; punti: {len(POINTS)}")
    print("\nMatrice delle fusioni Z:")
    print(Z)

    # Questo dizionario serve solo a spiegare l'output con le lettere.
    # All'inizio ogni ID identifica un punto; dopo ogni fusione aggiungiamo
    # i membri del nuovo cluster, così le righe successive possono usarlo.
    membri = {i: [LABELS[i]] for i in range(len(POINTS))}
    print("\nFusioni con le etichette dei punti:")
    for passo, riga in enumerate(Z, start=1):
        sinistro, destro, distanza, dimensione = riga
        sinistro = int(sinistro)
        destro = int(destro)
        nuovo_id = len(POINTS) + passo - 1
        membri[nuovo_id] = sorted(membri[sinistro] + membri[destro])
        print(
            f"Passo {passo}: {membri[sinistro]} + {membri[destro]} "
            f"-> {membri[nuovo_id]} ({int(dimensione)} punti); "
            f"d = {distanza:.2f}; d^2 = {distanza ** 2:.2f}"
        )

    # dendrogram interpreta Z e disegna i collegamenti fra figli e genitori.
    # L'altezza di ogni collegamento è la distanza della relativa fusione.
    # L'ordine sinistra/destra delle foglie può differire dal disegno della
    # traccia, pur rappresentando gli stessi gruppi e le stesse fusioni.
    figura, asse = plt.subplots(figsize=(9, 5))
    dendrogram(Z, labels=LABELS, ax=asse)
    asse.set_title(f"Clustering gerarchico - {args.metodo} linkage")
    asse.set_xlabel("Punti")
    asse.set_ylabel("Distanza euclidea")
    figura.tight_layout()

    # Il percorso è relativo allo script, quindi non dipende dalla directory
    # da cui viene avviato. Il PNG può essere inserito nelle slide o stampato.
    cartella = Path(__file__).resolve().parent / "grafici_generati"
    cartella.mkdir(parents=True, exist_ok=True)
    percorso = cartella / f"dendrogramma_{args.metodo}.png"
    figura.savefig(percorso, dpi=180)
    print(f"\nGrafico salvato in: {percorso}")

    if not args.no_show:
        plt.show()
    plt.close(figura)


if __name__ == "__main__":
    main()
