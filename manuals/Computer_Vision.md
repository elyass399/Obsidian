Computer Vision

Convertito da: Computer_Vision.pdf

Visione artificiale
Eris Chinellato

What is vision? Object recognition…

What is vision? Size estimation…

What is vision? Colour perception…

|     |     |     |
| --- | --- | --- |
|     |     |     |
|     |     |     |
|     |     |     |
|     |     |     |

What is vision? Movement detection…

The importance of visual attention
https://www.youtube.com/watch?v=vJG698U2Mvo

The social bias
https://www.youtube.com/watch?v=8FIEZXMUM2I

Vision is not photographic,
What we see depends on:
 Attention
 Goals
 Knowledge of the world
 Language associations
 Other senses
 Context
 Mood and drives
 Social environment
 …

Human eye and photoreceptors
| 10

Colour spectrum and human rods

Photoreceptors in different species

Animal vision
http://www.nhm.ac.uk/discover/how-do-other-animals-see-the-world.html
http://designtaxi.com/news/381848/Watch-Fascinating-Look-At-How-Cats-Snakes-Other-Animals-See-Our-World/

Eye evolution: human vs. octopus
Advantages and disadvantages of “inside out” retina
1. Retina
2. Nerve fibres
3. Optic nerve
4. Blind spot

Eye evolution
A human eye could have evolved in just 400000
generations (less than 10 million years)
Every step conveys a clear advantage over the previous
one (no implausible “jumps” )

Compound eyes
Eight photoreceptors arranged in a
regular pattern: automatic “map building”
Poor spatial quality and light sensitivity
but extremely fast, almost omnidirectional,
movement detection
Reactive vision (e.g. drosophila fly)

Visual processing in the human cortex
In simpler animals visual
cells do most of the job:
complex visual sensors
and simple brain.
In vertebrate (e.g.
humans) the brain cortex
does most of the job:
- simple visual

sensor and complex
brain.

V
i
s
u
a
l
a
r
e
a
s
i
n
t
h
e
p
r
i
m
a
t
e
b
r
a
i
n
| 19

Should artificial vision be like natural vision?
 Objectives
 Reliability
 Sensors
 Complexity
 Flexibility
 Speed
 Other sensory modalities
 Attention

Image analysis – understanding an image
1.
Pre-processing and Segmentation
2.
Representation and Description
3.
Recognition and Interpretation

Image processing
(“pixel manipulation”)
1.
Conversion: convert the image to more suitable formats (resolution, channels, colour space, …)
2. Geometric transformations: adjust the image spatial properties (crop, resize, rotate, …)

3.
Smoothing/sharpening: reduce image noise or enhance features and contrasts
4.
Thresholding: convert the image into binary to separate relevant features from background
5. Morphological transformations: clean-up binary image by eliminating outlier pixels

6.
Gradients: find edges, corners and other salient features

Colour spaces
RGB is used to display
colours for human benefit
HSV are meaningful physical
quantities convenient for processing

Thresholding / binarization

Convolution operations
- Convolve means multiplying two matrices point by point
- The first matrix is the image, the second (smaller one) is the kernel
- The kernel is applied to the image and modifies it
- Values in the kernel represent different types of filters
- Simple typical operations:
- smoothing (low pass filter)
- edge detection (high pass filter)

Image smoothing
 Smoothing reduces the contrast between adjacent pixels, thus reducing
image noise
 Smoothing is usually done by applying a low-pass filter on images
 This is obtained, for example, by substituting a pixel with a weighted average
of nearby pixels

Smoothing kernels
Linear kernel Gaussian kernel










1 1 1
1 1 1
1 1 1

Linear smoothing example
     
 
 
 
     
     
 
 
 
     
7 7 7 7 7 7
7 7 7 7 7 7
7 7 7 7 7 7
1 1 1
1 1 1
1 1 1
8 5 8 8 5 8
8 5 8 8 5 8
8 5 8 8 5 8
=










∗

Linear smoothing examples
Original 5x5 kernel 7x7 kernel 9x9 kernel 11x11 kernel

Edge detection
 find edges, borders, separations, patterns
 apply a filter that enhances differences between nearby pixels, thus
detecting regular contrasts
 there are horizontal, vertical, global and corner detectors

Vertical edge kernel Horizontal edge kernel
Edge gradient magnitude Edge gradient direction
Sobel edge detector

Edge detection example
     
 
 
 
     
     
 
 
 
     
0 0 12 12 0 0
0 0 12 12 0 0
0 0 12 12 0 0
1 0 1
2 0 2
1 0 1
8 5 8 8 5 8
8 5 8 8 5 8
8 5 8 8 5 8
−
−
−
=










−
−
−
∗

From edges to contours

Object
identification

Descriptors
From contours we can now describe features of shapes for classification:
o
Number of corners
o
Holes
o
Ratio between major axes
o
Area/perimeter ratio
o
Fraction of straight sections
o
Fraction of concavities
o
Symmetries
o
…
Object identity

Convolutional Neural Network:
It learns the kernels (filters) for convolution

What's inside a CNN?

Image processing revised
1.
Conversion: convert the image to more suitable formats (resolution, channels, colour space, …)
2. Geometric transformations: adjust the image spatial properties (crop, resize, rotate, …)

3.
Smoothing/sharpening: reduce image noise or enhance features and contrasts
4.
Thresholding: convert the image into binary to separate relevant features from background
5. Morphological transformations: clean-up binary image by eliminating outlier pixels

6.
Gradients: find edges, corners and other salient features

Filters and feature maps

Altri tipi di layers
 Pooling: riduce le dimensioni delle feature maps
 Activation: introduce non linearità
 Normalizzazione: necessario per equilibrare le attivazioni
 Dropout: modifiche random che riducono l'overfitting

Different level filters

YOLO: You Only Look Once
 Single-Shot Detection: Processes entire image in one pass.
 Grid System: Divides image into cells.
 Simultaneous Prediction: Each cell predicts BBoxes, Confidence & Class.

How YOLO achieves its performance
 CNN Backbone: Extracts features efficiently.
 Anchor Boxes (Later Versions): Improves localization for diverse shapes.
 Non-Maximum Suppression (NMS): Refines multiple predictions into one.
 Speed & Accuracy: Balances both for real-world applications.

CNN: vantaggi
 Riduzione dei parametri necessari per input equivalenti rispetto ad ANN
 Invarianza traslazionale: filtri imparati in una zona si possono applicare ad altre
 Estrazione gerarchica di caratteristiche
 Mantengono relazioni topografiche dei dati
 Robustezza: reti meno soggette ad overfitting

CNN: svantaggi
 Progettazione complessa e non intuitive (trial and error)
 Interpretabilità: sono ancora più difficili da comprendere delle normali ANN
 Molto esigenti: necessitano di molti esempi, quantità e qualità
 Dati strutturati: adatte principalmente per dati con struttura spazio-temporale