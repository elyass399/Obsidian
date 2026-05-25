Unsupervised Learning

Convertito da: Unsupervised_Learning.pdf

Unsupervised Learning
Eris Chinellato

Machine learning – approcci principali
Apprendimento supervisionato
Supervised learning
Input + Output
Apprendimento per rinforzo Reinforcement learning
Input + Feedback
Apprendimento non supervisionato Unsupervised learning
Input

Unsupervised learning
Estrazione di informazione dai dati
Input Nuova informazione
Che tipo di informazione?
Associazioni, pattern, dipendenze, ridondanze, …
Processamento
Dati

Associazioni e frequenze

K-means
1. Inizializzazione: Scegliere casualmente k centroidi.
2. Assegnazione: Assegnare ogni punto al cluster con il centroide più vicino.
3. Aggiornamento: Calcolare la nuova posizione dei centroidi come media dei punti del cluster.
4. Iterazione: Ripetere i passaggi 2 e 3 fino a quando i centroidi non si spostano più.

Come si sceglie K?
Inertia, silhouette, AIC, BIC, …

DBscan
Raggruppa i punti che sono densamente connessi tra loro, identificando regioni ad alta densità separate
da regioni a bassa densità.
 ε: Raggio di vicinato di un punto.
 MinP: Numero minimo di punti all'interno del raggio ε per considerare un punto come "core point".
 Core point: Punto con almeno MinP vicini entro il suo raggio ε.
 Border point: Punto che ha meno di MinP vicini entro Eps, ma è raggiungibile da un core point.
 Noise point: Punto che non è né un core point né un border point.

Confronto tra algoritmi

| 12
PCA: analisi delle
componenti
principali

Sistema di riferimento "naturale"
C'è un sistema di riferimento più conveniente per rappresentare dei dati?

Dimensionality reduction - PCA
Trovo un nuovo Sistema di riferimento completo, con nuovi origine e direzioni degli assi
Voglio il sistema di riferimento che minimizza la deviazione totale dei dati dagli assi

Principal component Analysis - PCA
o
Gli autovettori sono le direzioni nello spazio che contengono più informazione sui dati
o
Possiamo rappresentare i dati sui nuovi assi moltiplicando per gli autovettori (eigenvectors)
o
Gli autovalori (eigenvalues) rappresentano “l’importanza” di ogni nuova dimensione

Dimensionality reduction - PCA
o
Possiamo decidere di rimuovere delle dimensioni semplificando i dati
o
Quanta informazione si perde rappresentando il Sistema Solare con due sole dimensioni?

o
Dati, variabili, dimensioni
o
Sistemi di riferimento (e.g. Oxy):
 Il sistema di riferimento iniziale non dipende dai dati
 Il sistema di riferimento dopo PCA sì dipende dai dati
o
Autovettori (componenti principali) – assi del nuovo sistema di riferimento
o
Autovalori: "importanza" dei nuovi assi
o
Gli assi sono ordinati per importanza decrescente
o
Trasformazione: moltiplica dati originali per autovettori per ottenere dati sui nuovi assi
o
Riduzione: rimuovo componenti (dalla fine) prima di trasformare i dati
o
La matrice delle componenti ridotta trasforma i dati originali in dati di dimensioni ridotte