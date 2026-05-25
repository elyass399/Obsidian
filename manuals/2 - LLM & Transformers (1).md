|     |     |     |     |
| --- | --- | --- | --- |
|     |     |     |     |
|     |     |     |     |

| Gen AI                                         |
| ---------------------------------------------- |
| Chapter 2 - LLM and transformers Roxana Danger |

| Roadmap                                                                                                                                                                           |     |     |     |     |     |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- | --- | --- | --- | --- |
|                                                                                                                                                                                   |     |     |     |     |     |
|                                                                                                                                                                                   |     |     |     |     |     |
| - Part I: The transformer Architecture Overview - Part II: Training and using Transformers - Part III: Inside the transformer Architecture - Part IV: LLMs: Scaling and Inference |     |     |     |     |     |

| Part I - The transformer Architecture                                  |     |     |     |     |     |
| ---------------------------------------------------------------------- | --- | --- | --- | --- | --- |
|                                                                        |     |     |     |     |     |
|                                                                        |     |     |     |     |     |
| - How did we replace RNNs/LSTMs with a parallel processing powerhouse? |     |     |     |     |     |

| The Need to Replace RNNs/LSTMs                                                                                                                                                                                                                                                                                                                                                    |     |     |     |     |     |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- | --- | --- | --- | --- |
|                                                                                                                                                                                                                                                                                                                                                                                   |     |     |     |     |     |
|                                                                                                                                                                                                                                                                                                                                                                                   |     |     |     |     |     |
| - Speed: - Extremely slow, as processing token n cannot begin until token n-1 is complete. No parallelism possible. - Context: - Contextual information from the start of a long sentence is often "forgotten" - Transformer solution = Parallel Processing - Handles the entire input sequence simultaneously using the Attention mechanism. - "Attention Is All You Need", 2017 |     |     |     |     |     |

| A brief history of LLMs |     |     |     |     |     |
| ----------------------- | --- | --- | --- | --- | --- |
|                         |     |     |     |     |     |
|                         |     |     |     |     |     |

| Transformer Original Architecture |     |     |     |     |     |
| --------------------------------- | --- | --- | --- | --- | --- |
|                                   |     |     |     |     |     |
|                                   |     |     |     |     |     |

Input Sequence
Embedding
Encoding Decoding
Output Probabilities
Output sequence /
Sequenza secondaria
Embedding
“LLMs are fabolous” “LLMs sono favolosi”

|     | 6   |
| --- | --- |

| Transformer Original Architecture |     |     |     |     |     |
| --------------------------------- | --- | --- | --- | --- | --- |
|                                   |     |     |     |     |     |
|                                   |     |     |     |     |     |

Input Sequence
Embedding
Encoder multi-head
attention
Feedforward
Decoder Multi-head
attention layers
Multi-head attention
Feedforward

|     | 7   |
| --- | --- |

Output Sequence

| Transformer Architectures |     |     |     |     |     |
| ------------------------- | --- | --- | --- | --- | --- |
|                           |     |     |     |     |     |
|                           |     |     |     |     |     |

Encoder/decoder Encoder Decoder
- Two sequences
- Bidirectional and

unidirectional
knowledge
- T5
- Bidirectional

knowledge
- Bert
- Unidirectional

knowledge (Mask
attentions)
- GPT, Llama

Input Sequence
Embedding
Encoder
multi-head
attention
Feedforward
Decoder
Multi-head
attention layers
Multi-head
attention
Feedforward
Output
Sequence
Linear &
softmax
Input Sequence
Embedding
Encoder
multi-head
attention
Feedforward
Output
Sequence
Linear &
softmax
Input Sequence
Embedding
Decoder
Multi-head
attention layers
Feedforward
Output
Sequence
Linear &
softmax

| Transformer Architectures |     |     |     |     |     |
| ------------------------- | --- | --- | --- | --- | --- |
|                           |     |     |     |     |     |
|                           |     |     |     |     |     |

Encoder/decoder Encoder Decoder

|          | Greta |     |
| -------- | ----- | --- |
| Thunberg |       |     |

“LLM sono favolosi”
<nac>Swedish</nac>
activist
Input
Sequence
Embedding
Encoder
multi-head
attention
Feedforward
Decoder
Multi-head
attention layers
Multi-head
attention
Feedforward
Output
Sequence
Linear &
softmax
Input
Sequence
Embedding
Encoder
multi-head
attention
Feedforward
Output
Sequence
Linear &
softmax
Input Sequence
Embedding
Decoder
Multi-head
attention layers
Feedforward
Output
Sequence
Linear &
softmax

| The Encoder (e.g. Bert) (encoder): BertEncoder( (layer): ModuleList( |                                              |     |     |     |     |     |
| -------------------------------------------------------------------- | -------------------------------------------- | --- | --- | --- | --- | --- |
|                                                                      | (encoder): BertEncoder( (layer): ModuleList( |     |     |     |     |     |
|                                                                      |                                              |     |     |     |     |     |

(0-11): 12 x BertLayer(
(attention): BertAttention(
(self): BertSdpaSelfAttention(

|     |                                                                                                                                                                                                                                                                                                                                                                                                 |     | (query): Linear(in_features=768,                 |                                          |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- | ------------------------------------------------ | ---------------------------------------- |
|     |                                                                                                                                                                                                                                                                                                                                                                                                 |     | out_features=768, bias=True)                     |                                          |
|     |                                                                                                                                                                                                                                                                                                                                                                                                 |     | (key): Linear(in_features=768, out_features=768, |                                          |
|     |                                                                                                                                                                                                                                                                                                                                                                                                 |     |                                                  |                                          |
|     |                                                                                                                                                                                                                                                                                                                                                                                                 |     | bias=True)                                       |                                          |
|     | BertModel( (embeddings): BertEmbeddings( (word_embeddings): Embedding(30522, 768,...) (position_embeddings): Embedding(512, 768) (token_type_embeddings): Embedding(2, 768) (LayerNorm): LayerNorm((768,), …) (dropout): Dropout(p=0.1, inplace=False) ) (encoder): BertEncoder( … ) (pooler): BertPooler( (dense): Linear(in_features=768, out_features=768, bias=True) (activation): Tanh() ) | b   |                                                  | (value): Linear(in_features=768,         |
|     |                                                                                                                                                                                                                                                                                                                                                                                                 |     |                                                  | out_features=768, bias=True)             |
|     |                                                                                                                                                                                                                                                                                                                                                                                                 |     |                                                  | (dropout): Dropout(p=0.1, inplace=False) |
|     |                                                                                                                                                                                                                                                                                                                                                                                                 |     |                                                  | )                                        |
|     |                                                                                                                                                                                                                                                                                                                                                                                                 |     | b                                                |                                          |

|     |     | (word_embeddings): Embedding(30522,        |
| --- | --- | ------------------------------------------ |
| 76  | 8,  | ...)                                       |
|     |     | (position_embeddings): Embedding(512, 768) |

|     | out_features=768, bias=True)      |
| --- | --------------------------------- |
|     | (LayerNorm): LayerNorm((768,), …) |

|     | out_features=3072, bias=True)           |
| --- | --------------------------------------- |
|     | (intermediate_act_fn): GELUActivation() |

(LayerNorm): LayerNorm((768,),...)
(dropout): Dropout(p=0.1, inplace=False)
)
)
)
)
)

| 10  |
| --- |
|     |

| The Decoder (GPT-X) |     |     |     |     |     |
| ------------------- | --- | --- | --- | --- | --- |
|                     |     |     |     |     |     |
|                     |     |     |     |     |     |

GPT2Model(

| (wte): Embedding(50257, 768) |
| ---------------------------- |
| (wpe): Embedding(1024, 768)  |

(drop): Dropout(p=0.1, inplace=False)
(h): ModuleList(
(0-11): 12 x GPT2Block(
(ln_1): LayerNorm((768,), eps=1e-05, elementwise_affine=True)
(attn): GPT2Attention(

| (c_attn): Conv1D(nf=2304, nx=768)              |
| ---------------------------------------------- |
| (c_proj): Conv1D(nf=768, nx=768)               |
| (attn_dropout): Dropout(p=0.1, inplace=False)  |
| (resid_dropout): Dropout(p=0.1, inplace=False) |
| )                                              |

| (ln_2): LayerNorm((768,), eps=1e-05, elementwise_affine=True) |
| ------------------------------------------------------------- |
| (mlp): GPT2MLP(                                               |

| (c_fc): Conv1D(nf=3072, nx=768)          |
| ---------------------------------------- |
| (c_proj): Conv1D(nf=768, nx=3072)        |
| (act): NewGELUActivation()               |
| (dropout): Dropout(p=0.1, inplace=False) |
| )                                        |

)
)
(ln_f): LayerNorm((768,), eps=1e-05, elementwise_affine=True)
)

|     |     |     |     |
| --- | --- | --- | --- |
|     |     |     |     |
|     |     |     |     |

Practical Session
Review model architectures
Use pipelines for generation

| Part II: Training and using Transformers                                                                                         |     |     |     |     |     |
| -------------------------------------------------------------------------------------------------------------------------------- | --- | --- | --- | --- | --- |
|                                                                                                                                  |     |     |     |     |     |
|                                                                                                                                  |     |     |     |     |     |
| - How are Transformers trained? - How does inference occurs? - How can I use the knowledge in based models? - Use cases examples |     |     |     |     |     |

| How are Transformers trained?                                                                                                                                                                                                                                                                                                                         |     |     |     |     |     |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- | --- | --- | --- | --- |
|                                                                                                                                                                                                                                                                                                                                                       |     |     |     |     |     |
|                                                                                                                                                                                                                                                                                                                                                       |     |     |     |     |     |
| 1. Generate the training dataset as a huge clean “text in internet” (https://huggingface.co/spaces/HuggingFaceFW/blogpost-fineweb-v1) 2. Tokenize the training dataset (https://tiktokenizer.vercel.app/) 3. Create random Context Window Chunks 4. Create examples per each chunk 5. Batch the examples for parallel processing 6. Train transformer |     |     |     |     |     |

| 1&2. Generate and tokenize Training corpus |      |            |
| ------------------------------------------ | ---- | ---------- |
|                                            | rpus |            |
|                                            |      | Split into |

| 3. Chunks of Context Windows Size (C ) w |     |
| ---------------------------------------- | --- |
|                                          | w   |
|                                          |     |

|     | Batched for parallel training |
| --- | ----------------------------- |

| 5. Batch of Sequences in a chunk, B |     |
| ----------------------------------- | --- |
|                                     |     |
|                                     |     |

|     |     |     |     |
| --- | --- | --- | --- |
|     |     |     |     |

|                                                                                                                                                                                                                                                                                                                                                                        |     |                       |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- | --------------------- |
| First Citizen: Before we proceed any further, hear me speak. All: Speak, speak. First Citizen: You are all resolved rather to die than to famish? All: Resolved. resolved. First Citizen: First, you know Caius Marcius is chief enemy to the people. All: We know't, we know't. First Citizen: Let us kill him, and we'll have corn at our own price. Is't a verdict? |     | C = 5, batch_size=2 w |

| 1&2. Generate and tokenize Training corpus |      |            |
| ------------------------------------------ | ---- | ---------- |
|                                            | rpus |            |
|                                            |      | Split into |

|                        |        |
| ---------------------- | ------ |
| 10438, 584, 10570, 904 | , 4726 |

| 3. Chunks of Context Windows Size (C ) w |     |
| ---------------------------------------- | --- |
|                                          | w   |
|                                          |     |

| x                      | y     | batch_index |
| ---------------------- | ----- | ----------- |
| 10438                  | 584   | 1           |
| 10438, 584             | 10570 | 1           |
| 10438, 584, 10570      | 904   | 1           |
| 10438, 584, 10570, 904 | 4726  | 1           |

|     | Batched for parallel training |
| --- | ----------------------------- |

| 5. Batch of Sequences in a chunk, B |     |
| ----------------------------------- | --- |
|                                     |     |
|                                     |     |

| Forward and Backward passes |     |     |     |     |     |
| --------------------------- | --- | --- | --- | --- | --- |
|                             |     |     |     |     |     |
|                             |     |     |     |     |     |

Input
Sequence
Embedding
Encoder
multi-head
attention
Feedforward
Decoder
Multi-head
attention layers
Multi-head
attention
Feedforward
Output
Sequence
Linear &
softmax
https://bbycroft.net/llm

| During inference… |     |     |     |     |     |
| ----------------- | --- | --- | --- | --- | --- |
|                   |     |     |     |     |     |
|                   |     |     |     |     |     |

|     |     | LLM |     |
| --- | --- | --- | --- |

“The people in”
“Venice” “The people in Venice”
“is” “The people in Venice is”
…

| How can Transformers be used?                                                                                                                                                                                                                                                                                                                                                                                              |     |     |     |     |     |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- | --- | --- | --- | --- |
|                                                                                                                                                                                                                                                                                                                                                                                                                            |     |     |     |     |     |
|                                                                                                                                                                                                                                                                                                                                                                                                                            |     |     |     |     |     |
| - Generate - Fine-tune (transfer learning) for specific tasks: connect the output of the Transformer output layers to perform specific tasks - Tasks: - Text - Classification, generation, summarisation, translation - Image - Classification, image2text, text2image, object detection - Audio - Classification, speech recognition, text2speech - Multimodal - Image-text2text, video-text2text Transfer learning video |     |     |     |     |     |

|     |     |     |     |
| --- | --- | --- | --- |
|     |     |     |     |
|     |     |     |     |

Practical Session
Fine-tuning transformers

| Part III: Inside the transformer Architecture                                          |     |     |     |     |     |
| -------------------------------------------------------------------------------------- | --- | --- | --- | --- | --- |
|                                                                                        |     |     |     |     |     |
|                                                                                        |     |     |     |     |     |
| - What are the intricacies of Transformers that makes possible language understanding? |     |     |     |     |     |

| The token embeddings |     |
| -------------------- | --- |
|                      |     |

|     |     |     |     |
| --- | --- | --- | --- |
|     |     |     |     |
|     |     |     |     |

|     |
| --- |
|     |

| Embedding cardinality |
| --------------------- |
|                       |

|     |
| --- |
| 21  |

| The tokenizer |     |
| ------------- | --- |
|               |     |

|     |     |     |     |
| --- | --- | --- | --- |
|     |     |     |     |
|     |     |     |     |

|     |
| --- |
|     |

Tokenizer
Strings

| Byte-Pair Encoding (BPE) - GPTs |     |     |     |     |     |
| ------------------------------- | --- | --- | --- | --- | --- |
|                                 |     |     |     |     |     |
|                                 |     |     |     |     |     |

|                                                                                                                                 | x N |
| ------------------------------------------------------------------------------------------------------------------------------- | --- |
| Count frequencies Vocabulary Adjacent symbols Vocabulary Merge the most frequency frequent pair Update Vocabulary Frequent pair |     |

| Characters |     |
| ---------- | --- |

| WordPiece Encoding (BPE) - Bert |     |     |     |     |     |
| ------------------------------- | --- | --- | --- | --- | --- |
|                                 |     |     |     |     |     |
|                                 |     |     |     |     |     |

|                                                                                                                                                  | x N |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | --- |
| Compute pair score Vocabulary freq(x,y)/(freq(x)*freq(y)) Vocabulary Merge the most score likelihood pair Likelihood pair Update Vocabulary (##) |     |

| Characters |     |
| ---------- | --- |

| Sentence piece Encoding - Llama / T5 |     |     |     |     |     |
| ------------------------------------ | --- | --- | --- | --- | --- |
|                                      |     |     |     |     |     |
|                                      |     |     |     |     |     |

|                                                                                                                                 | x N |
| ------------------------------------------------------------------------------------------------------------------------------- | --- |
| Count frequencies Vocabulary Adjacent symbols Vocabulary Merge the most frequency frequent pair Update Vocabulary Frequent pair |     |

| Unicodes |     |
| -------- | --- |

|     |     |     |     |
| --- | --- | --- | --- |
|     |     |     |     |
|     |     |     |     |

Practical Session
Implementing tokenizers

| The positional embedding |     |
| ------------------------ | --- |
|                          |     |

|     |     |     |     |
| --- | --- | --- | --- |
|     |     |     |     |
|     |     |     |     |

|     |
| --- |
|     |

| I    |
| ---- |
| love |
| NLP  |

| 0   |
| --- |
| 1   |
| 2   |

| P 0,0 | P 0,1 | …   | P 0,d |
| ----- | ----- | --- | ----- |
| P 1,0 | P 1,1 | …   | P 1,d |
| P 2,0 | P 2,1 | …   | P 2,d |

|     |     |     |     |
| --- | --- | --- | --- |
|     |     |     |     |
|     |     |     |     |

Practical Session
Implementing positional encoding
Adding to word embedding

| Self-Attention Mechanism - Core |     |     |     |     |     |
| ------------------------------- | --- | --- | --- | --- | --- |
|                                 |     |     |     |     |     |
|                                 |     |     |     |     |     |

Masked Multi-
Head
Attention
Add & Norm
Feed Forward
Matrix
N
x
Linear
Softmax

| How are tokens passed to the model during training? |     |     |     |     |     |
| --------------------------------------------------- | --- | --- | --- | --- | --- |
|                                                     |     |     |     |     |     |
|                                                     |     |     |     |     |     |

| Training corpus |     |
| --------------- | --- |
|                 |     |
|                 |     |

| Chunks of Context Windows Size (C ) w |     |
| ------------------------------------- | --- |
|                                       |     |
|                                       |     |

|     | Batched for parallel training |
| --- | ----------------------------- |

| Batch of Sequences in a chunk, B |     |
| -------------------------------- | --- |
|                                  |     |
|                                  |     |

C
w
-1 Sequences/examples
x = Chunk[0:j], j ∊ 1..C
w
y = Chunk[j]
B x C
w
x C matrix
C = embedding dimensions
Add & Norm
B x Cw x C
Matrix
N
Softmax

| Decoder transformer [B x C x C] w |     |     |     |     |     |
| --------------------------------- | --- | --- | --- | --- | --- |
|                                   |     |     |     |     |     |
|                                   |     |     |     |     |     |

| k- parallel heads |     |
| ----------------- | --- |

Head
Attention
Add & Norm
Feed Forward
B x Cw x C
Matrix
N
x
Linear
Softmax
[B x C
w
x C]
Matrix
Add & Norm
Feed Forward
[B x C
w
x C]
Matrix
Linear
…
Softmax
d2
MMHA
dN
x
[B x C
w
x C]
Matrix
Block
d1
Matrix

| Encoder/decoder transformer |     |     |     |     |     |
| --------------------------- | --- | --- | --- | --- | --- |
|                             |     |     |     |     |     |
|                             |     |     |     |     |     |

|      |     | …   |
| ---- | --- | --- |
| CMHA |     |     |

Linear
Softmax
B x C
w
x C
Matrix
- x*d-matrix

B x C
w
x C
Matrix
(dencode)
d1 d2 dN
x
…
MMHA MMHA MMHA

| Attention Mechanism                                       |     |     |     |     |     |
| --------------------------------------------------------- | --- | --- | --- | --- | --- |
|                                                           |     |     |     |     |     |
|                                                           |     |     |     |     |     |
| - How does a word decide which other words are important? |     |     |     |     |     |

|     |
| --- |
|     |

|     | Who are we? How can we collaborate? |
| --- | ----------------------------------- |

- What topics will I ask

| Self-Attention Mechanism                                         |     |     |     |     |     |
| ---------------------------------------------------------------- | --- | --- | --- | --- | --- |
|                                                                  |     |     |     |     |     |
|                                                                  |     |     |     |     |     |
| - How does the token “bank” understands what does it stands for? |     |     |     |     |     |

| What topics will I ask everyone about?                              | Do they know about money or geography?                                                                                  | Q   |     |
| ------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | --- | --- |
| How will I introduce myself? what areas of expertise will I expose? | - River -> geography - Money -> finance                                                                                 | K   |     |
| What information will I share if my expertise is relevant?          | - River -> content of "a flowing body of water, nature, etc." - Money -> content of “currency, accounts, finance, etc.” | V   |     |
|                                                                     |                                                                                                                         |     |     |

| The Core: Query, Key, Value (Q, K, V) |     |     |     |     |     |
| ------------------------------------- | --- | --- | --- | --- | --- |
|                                       |     |     |     |     |     |
|                                       |     |     |     |     |     |

X = [ B x C
W
x C ]
[ B x C
W
x d
k
] [ B x C
W
x d
k
] [ B x C
W
x d
k
]

| Multi-head attention                                                                                  |     |     |     |     |     |
| ----------------------------------------------------------------------------------------------------- | --- | --- | --- | --- | --- |
|                                                                                                       |     |     |     |     |     |
|                                                                                                       |     |     |     |     |     |
| - Single head learns one relationship - Outputs concatenated and linearly projected. Decoder (masked) |     |     |     |     |     |

| https://poloclub.github.io/transformer-explainer/ |
| ------------------------------------------------- |
|                                                   |

| Part IV - LLMs: Scaling and Inference                                                                                                                                                                                                                                                                                                        |     |     |     |     |     |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- | --- | --- | --- | --- |
|                                                                                                                                                                                                                                                                                                                                              |     |     |     |     |     |
|                                                                                                                                                                                                                                                                                                                                              |     |     |     |     |     |
| How do we get from a "Transformer Block" to a "Large Language Model"? Scaling Laws - Compute - Data Size - Model Parameters When models grow to a certain size (e.g., >100B parameters), they don't just get better—they start exhibiting new abilities they weren't explicitly trained for. BERT, 340M parameters -> GPT-3, 175B parameters |     |     |     |     |     |

| Autoregression |     |     |     |     |     |
| -------------- | --- | --- | --- | --- | --- |
|                |     |     |     |     |     |
|                |     |     |     |     |     |

|     |     | LLM |     |
| --- | --- | --- | --- |

“The robot in”
“Venice” “The robot in Venice”
“is” “The robot in Venice is”
…

| Decoding strategy                                                                                                          |     |     |     |     |     |
| -------------------------------------------------------------------------------------------------------------------------- | --- | --- | --- | --- | --- |
|                                                                                                                            |     |     |     |     |     |
|                                                                                                                            |     |     |     |     |     |
| How do we choose the one token to append? Logits Apply sampling Obtain Token selection parameters probabilities Next token |     |     |     |     |     |

| Decoding strategy                                                                                                                                                                                           |     |        |     |     |     |     |     |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- | ------ | --- | --- | --- | --- | --- |
|                                                                                                                                                                                                             |     |        |     |     |     |     |     |
|                                                                                                                                                                                                             |     |        |     |     |     |     |     |
| How do we choose the one token to append? Needs yes no deterministic output? Use sampling. How diverse? Needs best sequence? yes no Beam Search Greedy Creativity Avoid repetition (Most probably sequence) |     |        |     |     |     |     |     |
| Beam Search (Most probably sequence)                                                                                                                                                                        |     | Greedy |     |     |     |     |     |
|                                                                                                                                                                                                             |     |        |     |     |     |     |     |
|                                                                                                                                                                                                             |     |        |     |     |     |     |     |

| Deterministic Decoding: Greedy vs. Beam |     |     |     |     |     |
| --------------------------------------- | --- | --- | --- | --- | --- |
|                                         |     |     |     |     |     |
|                                         |     |     |     |     |     |

| Strategy | Pros                                                                                              | Cons                                                                    |
| -------- | ------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| Greedy   | Fastest, simple                                                                                   | - Repetition ("I am I am I am...") - Local maxima issue                 |
| Beam     | Finds sequences with a higher overall probability. Much more coherent. Good for constrained tasks | - Slower, still deterministic, and can produce "safe" or "boring" text. |

| Sampling parameters                                                                                                                                                                                                                                                                                                                                                                                                   |     |     |     |     |     |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- | --- | --- | --- | --- |
|                                                                                                                                                                                                                                                                                                                                                                                                                       |     |     |     |     |     |
|                                                                                                                                                                                                                                                                                                                                                                                                                       |     |     |     |     |     |
| Logits Apply sampling Obtain Token Next parameters probabilities selection token - Temperature: Scales logits before converting to probabilities. scaled_logits = logits / temperature - Top-k Sampling: Keeps only k highest-probability tokens, discards rest. - Top-p (Nucleus Sampling): Keeps smallest set of tokens whose cumulative probability ≥ p. Standard practice: Temperature → Top-k (optional) → Top-p |     |     |     |     |     |

-
-
-

| Sampling parameters: Temperature |     |     |     |     |     |
| -------------------------------- | --- | --- | --- | --- | --- |
|                                  |     |     |     |     |     |
|                                  |     |     |     |     |     |

|     |     |
| --- | --- |
|     | 43  |

| Sampling Knobs: Top-P                                                                                                                                                                                                                                                                                                                                                                                         |     |     |     |     |     |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- | --- | --- | --- | --- |
|                                                                                                                                                                                                                                                                                                                                                                                                               |     |     |     |     |     |
|                                                                                                                                                                                                                                                                                                                                                                                                               |     |     |     |     |     |
| Controls the "vocabulary pool" for sampling. Samples only from the smallest set of tokens whose cumulative probability exceeds p. - p=0.9 (High): Sample from the top 90% most likely words. - p=0.1 (Low): Sample from a very small, high-probability set. Example: Sorted: [cat: 0.4, dog: 0.3, bird: 0.2, fish: 0.08, rock: 0.02] Cumsum: [0.4, 0.7, 0.9, 0.98, 1.0] Keep: [cat, dog, bird] ← stops at 0.9 |     |     |     |     |     |

| Part V - Prompt Engineering & Control                                                                                     |     |     |     |     |     |
| ------------------------------------------------------------------------------------------------------------------------- | --- | --- | --- | --- | --- |
|                                                                                                                           |     |     |     |     |     |
|                                                                                                                           |     |     |     |     |     |
| How do we "steer" the LLM to get the exact output we want? - Prompt engineering - Controlling the creativity of the model |     |     |     |     |     |

| A few examples of prompting strategies |     |     |     |     |     |
| -------------------------------------- | --- | --- | --- | --- | --- |
|                                        |     |     |     |     |     |
|                                        |     |     |     |     |     |

| Strategy               | Idea                                                            | Example                                                                                                                                                                                                               |
| ---------------------- | --------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Zero-shot Prompting    | Ask the model to perform a task directly, with zero examples.   | What is 2+2?                                                                                                                                                                                                          |
| Few-shot prompting     | Ask the model to perform a task providing a few examples.       | Q: What is 2+2? A: 4. Q: What is 5+5? A: 10. Q: What is 3+3? A:                                                                                                                                                       |
| Chain-of-Thought (CoT) | Few-shot prompt where the examples include the reasoning steps. | Q: Roger has 5 tennis balls. He buys 2 cans of 3 balls each. How many does he have? A: Roger started with 5 balls. 2 cans of 3 balls is 6 balls. 5 + 6 = 11. The answer is 11. Q: A juggler has 16 balls and gives …. |

| Q   |
| --- |
| Q   |
| Q   |

Video

|     |     |     |     |
| --- | --- | --- | --- |
|     |     |     |     |
|     |     |     |     |

Practical Session
Decoding and creativity control
(https://huggingface.co/playground)

|     |     |     |     |
| --- | --- | --- | --- |
|     |     |     |     |
|     |     |     |     |

| Generative AI                    |
| -------------------------------- |
| Chapter 2 - LLM and transformers |

| Experience is the best teacher. So, keep coding until the next lesson! Roxana Danger |     |
| ------------------------------------------------------------------------------------ | --- |
|                                                                                      |     |
