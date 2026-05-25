ANN

Convertito da: ANN.pdf

ARTIFICIAL INTELLIGENCE
AND DATA SPECIALIST
2022 - 2024

Eris Chinellato
RETI NEURALI

What are Neural Networks?
o
Machine learning technique inspired by the brain and nervous system
o
Very simple principles, very complex behaviours
o
Simulate the parallel processes of real neural systems
o
Somehow unpredictable, hard to look inside
o
Require careful, often ad-hoc settings
o
Many different types and architectures
o
Balance of effective problem solving and biological plausibility

Real neural networks
o
The human brain has about 100 billion
- neurons

o
Neuron size is between 4 and 100
microns (10-6m)
o
Typically many (up to 105) inputs
- and one output (axon)

o
Axons can be 1m long, connecting any
brain areas
o
Action potentials can travel at 100 m/s

Artificial Neural Network
output
input

Neurons & synapses vs. nodes & weights
Neurons (nodes)
do the computations
Synapses (weights)
store memories

Structure of a node (Perceptron)
1. Weighted sum of inputs to node j:

𝐺𝐺
𝑗𝑗
=
∑𝑖𝑖=1
𝑁𝑁
𝑥𝑥
𝑖𝑖
𝑤𝑤
𝑖𝑖𝑗𝑗
2. Limiting, non linear transfer function:

𝑦𝑦
𝑗𝑗
=
1+𝑒𝑒
−𝐺𝐺𝐺𝐺
3. Output y

j
of node j can be input to another neuron

Feed-forward neural networks
“Multilayer perceptrons”
Information flow is unidirectional
Data is presented to Input layer
Passed on to Hidden Layer
Passed on to Output layer
Information is distributed
Information processing is parallel

| Example application: |     |     | p   |     | i   |
| -------------------- | --- | --- | --- | --- | --- |
|                      |     |     |     |     |     |
|                      |     |     |     |     |     |
|                      |     |     |     |     |     |
|                      |     |     |     |     |     |
|                      |     |     |     |     |     |
|                      |     |     |     |     |     |

|     |     |     |     |
| --- | --- | --- | --- |
|     |     |     |     |
|     |     |     |     |
|     |     |     |     |
|     |     |     |     |
|     |     |     |     |
|     |     |     |     |
|     |     |     |     |
|     |     |     |     |
|     |     |     |     |
|     |     |     |     |
|     |     |     |     |
|     |     |     |     |
|     |     |     |     |
|     |     |     |     |
|     |     |     |     |
|     |     |     |     |
|     |     |     |     |

Calculating the output for a given input
(1 × 0.25) + (0.5 × (-1.5)) = 0.25 + (-0.75) = - 0.5
0.3775
5 . 0
=
+ e
�
𝑖𝑖=1
𝑁𝑁
𝑥𝑥
𝑖𝑖
𝑤𝑤
𝑖𝑖𝑗𝑗
𝑦𝑦
𝑗𝑗
=
1 + 𝑒𝑒
−𝐺𝐺𝐺𝐺

Training the Network - Learning
o
Learning = (clever) weight adjustment
o
Requires training set (input / output pairs - supervised learning)
o
Starts with random weights
o
Adjust weights to reduce cost function calculated from output error
o
Backpropagation: change weight backwards, from output to input
Feed-forward backpropagation networks

Perceptron learning – Delta Rule
Errors require changing the weights that generated them.
Weight change is proportional to input value and output error:
∆w
ij
= αx
i
(d
j
-y
j
), w
ij
= w
ij
+ ∆w
ij
α =
learning rate
; d
j
=
desired output of neuron
j
y
j
x
i
w
ij

w
w
E
Gradient Descent






∂
∂
∂
∂
∂
∂
= ∇
n
w
E
w
E
w
E
w E ,..., , ) (
1 0

= Gradient of error E w.r.t. the weight vector
The cost function depends on the classification or regression error.
We compute the derivative, and estimate the direction in which it decreases faster.

Learning procedure
Repeat process multiple times for all training pairs
o
Present data
o
Calculate error
o
Adjust weights
o
Check stop conditions
error trend

Deep learning
o
No agreed definitions, but usually denotes an ANN with "many" layers
o
There are usually a variety of layers performing different jobs (e.g. CNN)
o
It requires a large amount of "good" data for training, and plenty of resources
o
Saves on time on feature engineering, but requires more design settings
o
Perform exceptionally well in some applications