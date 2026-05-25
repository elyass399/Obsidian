ML

Convertito da: ML.pdf

ARTIFICIAL INTELLIGENCE
AND DATA SPECIALIST
2022 - 2024

Eris Chinellato
MACHINE LEARNING

Machine learning – approcci principali
o
Supervised learning (Apprendimento supervisionato)
Il sistema è fornito di un insieme di dati di input e delle corrispondenti etichette o output
desiderati. Impara quindi a fare previsioni o classificazioni basandosi su questi esempi
etichettati.
o
Unsupervised learning (Apprendimento non supervisionato)
Il sistema riceve solo dati di input senza etichette o informazioni sull'output desiderato. Deve
quindi scoprire modelli o strutture all'interno dei dati senza avere una guida esterna.
o
Reinforcement learning (Apprendimento per rinforzo)
Un agente impara a prendere decisioni attraverso l'interazione con l’ambiente. L'agente è
ricompensato o penalizzato per le azioni che esegue, ma non gli viene detto esplicitamente
cosa dovrebbe fare.

Machine learning – problems / tasks
o
Classificazione
Assegnare dei dati ad una categoria tra le diverse disponibili
o
Regressione
Predire l'output numerico corretto per un dato input numerico
o
Clustering
Organizzare i dati in gruppi significativi senza avere informazioni esplicite sui gruppi
o
Riduzione della dimensionalità
Ridurre le dimensioni dei dati con la minima perdita di informazioni
o
Selezione dell'azione
Decidere cosa fare in una situazione complessa, in base ai dati sensoriali e all'esperienza
S
U
P
E
R
V
I
S
E
D
U
N
S
U
P
E
R
V
I
S
E
D
R
L

Supervised learning
Learn from input/output examples
Training (learn)
Input / output pairs
Testing (predict)
New input Predicted output
Trained Model
Untrained
Model

Supervised learning - classification
Categorical output (labels/classes/categories)
3, 6, 8, 1, 7, 9, 6, 6, 9, 1
6, 7, 5, 7, 8, 6, 3, 4, 8, 5
2, 1, 7, 9, 7, 1, 2, 8, 4, 5
4, 8, 1, 9, 0, 1, 8, 8, 9, 4
Untrained Model
Trained Model
O
u
t
p
u
t
I
n
p
u
t

Multidimensional inputs
28 rows * 28 columns:
784 pixels
784 features
values between 0 (black) and 1 (white)
1 output, integer value between 0 and 9

Supervised learning - regression
Continuous numerical output

| Age   | Weight | Height  | Neck  | Chest |
| ----- | ------ | ------- | ----- | ----- |
| Thigh | Hip    | Abdomen | Knee  | Ankle |
|       | Biceps | Forearm | Wrist |       |

Percentage body fat

| 23  | 70.0 | 172  | 36.2 | 93.1 |
| --- | ---- | ---- | ---- | ---- |
| 59  | 94.5 | 85.2 | 37.3 | 21.9 |
|     | 32.0 | 27.4 | 17.1 |      |

Untrained Model
O
u
t
p
u
t

| 9
Unsupervised
and
reinforcement
learning

Unsupervised learning
Extract meaningful information from data
Input New information
What is extracted?
Associations, patterns, dependencies, redundancies, …
Data
processing

Unsupervised learning example - Clustering

Principal component Analysis - PCA
Riduzione delle dimensioni : analisi dei componenti principali
Qual è il modo più “naturale” o “logico” di allineare gli assi del Sistema di riferimento?

Reinforcement learning
Action selection technique, used when the best solution is unknown, but it’s possible to tell if
an action consequence is good or bad.
The Agent interact with the Environment, performs Actions and receives Rewards
(positive or negative), thus reinforcing good choices.

| 14
Algoritmi di
classificazione

Classification - nomenclature
o
Feature: one of the characteristics describing the data
o
Feature space: the set of characteristics used [size: f]
o
Class, label: on of the possible data categories
o
Class set: all known categories [size: c]
o
Instance, data point: values describing one element in the data [f] and its class [1]
o
Data set: set of all [n] data, including their features [n x f] and classes [n x 1]
o
Training set: set of data with known classes ([n
x f] + [n
x 1]) used for training the
classifier
o
Test set: set of data with known classes ([n
x f] + [n
x 1]) used to assess the
classifier accuracy

K nearest neighbours
o
Compute the distance (in the multidimensional feature space) of a test point x from all
labelled points
o
Select the k points closest to x, and count their classes
o
Assign to x the most frequent class of the k nearest neighbours

Decision trees
o
Choose the feature which best separates the data classes
o
Set a threshold (quantitative variable) or a split criterion (qualitative)
o
Repeat the above for each feature one at a time (reintroduce features after one step)
o
For a new data point follow the three checking each feature against its cut-off value

Boundary methods
o
Compute linear or non linear surfaces in the feature space which gives the best
separation of the labelled data
o
Discriminant analysis makes some assumptions on data distribution shapes; LR provides
individual class probabilities
o
For a new data point, check on what side of the borders it falls

Naïve Bayes
o
Compute the probabilities of observing certain feature values for points belonging to a
given class
o
Use Bayes rules on a new data point to estimate the probability of those feature values to
belong to each class
o
Can perform non linear separations in some conditions