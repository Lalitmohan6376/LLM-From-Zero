# 🔄 Complete LLM Data Flow

An LLM data flow describes how information moves through a Large Language Model, from raw input text to numerical representations, through neural network computations, and finally to predicted tokens and readable output.

Understanding this flow connects the individual concepts of tokenization, embeddings, attention, Transformer blocks, logits, and text generation into one complete picture.

This document focuses on **how data changes at each stage of a GPT-style, decoder-only LLM**, both during inference and during training.

---

## 1. What Is Data Flow in an LLM?

Data flow explains three things:

- **Input:** What information enters a component?
- **Transformation:** What does that component do to the information?
- **Output:** What information does the component produce for the next stage?

For example, the embedding layer receives token IDs and produces vectors. The Transformer processes those vectors and produces contextual representations. The language modeling head converts the final representations into vocabulary logits.

Each stage has a different responsibility.

---

## 2. Complete LLM Data Flow at a Glance

```text id="a8m4vx"
                  INPUT TEXT
                      |
                      v
                  TOKENIZER
                      |
                      v
                   TOKEN IDs
                      |
                      v
              TOKEN EMBEDDING LAYER
                      |
                      v
             POSITIONAL INFORMATION
                      |
                      v
             INITIAL REPRESENTATIONS
                      |
                      v
             +---------------------+
             |  TRANSFORMER BLOCKS |
             |                     |
             |  Causal Attention   |
             |          |          |
             |  Feed-Forward Net   |
             |          |          |
             |  Residual + Norm    |
             +---------------------+
                      |
                      v
             FINAL HIDDEN STATES
                      |
                      v
             LANGUAGE MODELING HEAD
                      |
                      v
                    LOGITS
                      |
                      v
            DECODING / TOKEN SELECTION
                      |
                      v
                SELECTED TOKEN
                      |
                      v
             UPDATE THE SEQUENCE
                      |
                      +---- Repeat
                      |
                      v
             TOKENIZER DECODING
                      |
                      v
                  OUTPUT TEXT
```

The tokenizer and decoding logic are part of the overall pipeline, but they are not ordinarily layers inside the neural network itself.

---

## 3. Stage 1 — Raw Text

The process begins with a text input.

For example:

```text id="g2q7wm"
"The cat is sleeping."
```

At this stage, the input is a string of characters.

The computer can store and manipulate this string, but the neural network does not directly use the ordinary text string as its standard numerical input.

The text must first be converted into a representation the model can process.

---

## 4. Stage 2 — Tokenization

The tokenizer divides the text into tokens according to its vocabulary and tokenization rules.

For example:

```text id="v5j9kc"
Input:
"The cat is sleeping."

           |
           v

Tokens:
["The", " cat", " is", " sleeping", "."]

           |
           v

Token IDs:
[45, 182, 27, 903, 14]
```

These token IDs are illustrative. Actual token boundaries and IDs depend on the tokenizer.

### What changes at this stage?

| Before | After |
|---|---|
| Text string | Ordered token IDs |
| Human-readable characters | Integer identifiers |
| Text-specific representation | Tokenizer-specific numerical representation |

A token ID identifies a vocabulary entry. It does not itself contain the token's semantic meaning.

---

## 5. Stage 3 — Token IDs Become Embeddings

The embedding layer uses each token ID to retrieve a learned vector from the embedding matrix.

For example:

```text id="m7x2pf"
Token IDs:
[45, 182, 27, 903, 14]

           |
           v

Embedding Layer

45  -> [0.21, -0.14, 0.73, ...]
182 -> [0.62,  0.08, 0.19, ...]
27  -> [0.11,  0.57, 0.32, ...]
903 -> [0.44, -0.21, 0.68, ...]
14  -> [0.08,  0.33, 0.21, ...]
```

The vectors shown are illustrative.

If the sequence contains \(N\) tokens and the model's hidden dimension is \(d_{\text{model}}\), the embedding tensor commonly has the shape:

\[
[N,d_{\text{model}}]
\]

For batched inputs, the shape is commonly:

\[
[B,N,d_{\text{model}}]
\]

Where:

- \(B\) = batch size
- \(N\) = number of token positions
- \(d_{\text{model}}\) = hidden dimension

### What changes at this stage?

The input changes from integer identifiers into learned numerical vectors.

These vectors are the initial token representations. They are not yet the final contextual representations produced by the Transformer.

---

## 6. Stage 4 — Positional Information

The architecture must represent token order because the same tokens can have different meanings when arranged differently.

For example:

```text id="n4k8wy"
"The dog chased the cat."

"The cat chased the dog."
```

The vocabulary may contain the same words, but their positions change the sentence meaning.

The model incorporates positional information using the method supported by its architecture.

Common methods include:

- Learned positional embeddings
- Sinusoidal positional encodings
- Rotary Position Embedding (RoPE)

In a model using learned positional embeddings, token and positional vectors may be combined as follows:

\[
X=E_{\text{token}}+E_{\text{position}}
\]

In a RoPE-based architecture, positional information is incorporated differently, within the attention computation.

### What changes at this stage?

The model's input representations become position-aware through its chosen positional mechanism.

The exact operation depends on the architecture; not every LLM adds positional vectors directly to token embeddings.

---

## 7. Stage 5 — Data Enters the Transformer Blocks

The Transformer blocks perform the main neural network computations.

The input is a sequence of numerical vectors. The output is another sequence of vectors with the same sequence positions and, in a typical standard block, the same hidden dimension.

```text id="r3w6jn"
Initial Representations
          |
          v
    Transformer Block 1
          |
          v
    Transformer Block 2
          |
          v
    Transformer Block 3
          |
          v
           ...
          |
          v
    Transformer Block N
          |
          v
    Final Hidden States
```

The model may contain many Transformer blocks. Each block transforms the representations produced by the previous block.

Two major computational components inside these blocks are causal self-attention and the feed-forward network.

---

## 8. Stage 6 — Causal Self-Attention Data Flow

Self-attention lets a token's representation incorporate information from other permitted positions in the context.

The attention mechanism computes three projections from the input representations:

- Query (Q)
- Key (K)
- Value (V)

The simplified scaled dot-product attention formula is:

\[
\operatorname{Attention}(Q,K,V)
=
\operatorname{softmax}
\left(
\frac{QK^\top}{\sqrt{d_k}}+M
\right)V
\]

Here:

- \(QK^\top\) calculates attention scores.
- \(d_k\) is the key dimension.
- \(M\) represents the causal mask, which blocks disallowed future positions before softmax.
- Softmax converts the allowed scores into attention weights.
- The weights determine how values contribute to the output.

A simplified data flow is:

```text id="x6p2mb"
Input Representations
          |
          v
    Query / Key / Value
          |
          v
     Attention Scores
          |
          v
      Causal Mask
          |
          v
         Softmax
          |
          v
     Weighted Values
          |
          v
    Attention Output
```

### Example

Consider:

```text id="u8m4qz"
"The cat is sleeping."
```

When predicting the token after `The cat is`, a causal decoder can use the available preceding tokens. It cannot use a future target token that has not yet been generated.

During training, a causal mask allows all sequence positions to be processed in parallel without allowing earlier predictions to use future-token information.

### What changes at this stage?

Each token receives an updated representation that incorporates information from other permitted tokens.

Multi-head attention performs this process using multiple learned attention heads, whose outputs are combined.

---

## 9. Stage 7 — Feed-Forward Network Data Flow

After attention, the representations pass through a feed-forward network.

A simplified feed-forward network applies a learned projection, an activation function, and another projection.

\[
\operatorname{FFN}(x)
=
W_2\,\sigma(W_1x+b_1)+b_2
\]

Where:

- \(W_1\) and \(W_2\) are learned weight matrices.
- \(b_1\) and \(b_2\) are biases.
- \(\sigma\) is an activation function.

For example:

```text id="c5n9jw"
Input Representation
       |
       v
First Linear Projection
       |
       v
Intermediate Representation
       |
       v
Activation Function
       |
       v
Second Linear Projection
       |
       v
Output Representation
```

The intermediate dimension is often larger than the hidden dimension, although exact designs vary. Some LLMs use gated feed-forward networks.

### What changes at this stage?

The model applies learned nonlinear transformations to each token position's representation.

Attention combines information across token positions, while the feed-forward network transforms the representation at each position.

---

## 10. Stage 8 — Residual Connections and Normalization

Transformer blocks also use residual connections and normalization.

A residual connection allows the input to a sublayer to contribute directly to its output.

A simplified expression is:

\[
y=x+F(x)
\]

Here, \(F(x)\) represents the sublayer transformation.

Normalization helps manage activation scales and supports stable computation.

The exact ordering varies across architectures. For example, many modern LLMs normalize representations before attention and feed-forward sublayers, while other designs normalize after residual additions.

### What changes at this stage?

The block combines transformed information with residual information and applies its normalization operations according to the architecture.

The block outputs a new sequence of hidden representations for the next block.

---

## 11. Stage 9 — Final Hidden States

After passing through the Transformer stack, the model produces final hidden representations.

```text id="p8v3ka"
Transformer Block 1
        |
        v
Transformer Block 2
        |
        v
       ...
        |
        v
Transformer Block N
        |
        v
Final Normalization (if used)
        |
        v
Final Hidden States
```

These representations have been transformed using the context available to the model.

They may encode information about relationships between tokens, grammatical patterns, semantic associations, and other learned features.

They are still numerical vectors rather than readable text.

### Important distinction

An initial embedding represents a token before the full Transformer computation. A final hidden representation reflects the transformations and contextual information incorporated through the network.

---

## 12. Stage 10 — Hidden States Become Logits

The language modeling head converts hidden representations into vocabulary-sized scores.

A simplified expression is:

\[
z=hW_{\text{out}}+b
\]

Where:

- \(h\) = hidden representation
- \(W_{\text{out}}\) = output projection weights
- \(b\) = optional bias
- \(z\) = logits

Suppose the model's vocabulary contains 50,000 tokens. The logits for one prediction position contain 50,000 scores.

For next-token generation, the model generally uses the logits from the last available position.

For training, logits are commonly computed for many positions in the sequence.

### Example

```text id="k7w2np"
Final Hidden State
        |
        v
Language Modeling Head
        |
        v
Vocabulary Logits

" cat"      -> 2.8
" dog"      -> 1.9
" bird"     -> 0.7
...         -> ...
```

These scores are illustrative.

### What changes at this stage?

The model changes from a hidden representation with dimension \(d_{\text{model}}\) to a vector containing one score per vocabulary token.

Logits are raw scores, not probabilities.

---

## 13. Stage 11 — Logits Become a Probability Distribution

A softmax function can convert logits into probabilities:

\[
P_i=\frac{e^{z_i}}{\sum_{j=1}^{V}e^{z_j}}
\]

Where:

- \(z_i\) = logit for token \(i\)
- \(V\) = vocabulary size
- \(P_i\) = probability assigned to token \(i\)

For example:

| Candidate token | Illustrative probability |
|---|---:|
| ` cat` | 50% |
| ` dog` | 30% |
| ` bird` | 15% |
| Other candidates combined | 5% |
| **Total** | **100%** |

These values are examples, not actual model predictions.

### What changes at this stage?

The raw vocabulary scores are transformed into a probability distribution. Each probability represents the model's relative prediction for a candidate token under that distribution.

The distribution does not, by itself, guarantee factual correctness or calibrated confidence.

---

## 14. Stage 12 — Decoding Selects a Token

The decoding process decides which token to generate from the available scores or probability distribution.

Common approaches include:

| Strategy | Data-flow behavior |
|---|---|
| Greedy decoding | Selects the highest-scoring token. |
| Temperature sampling | Adjusts the logits before sampling. |
| Top-K sampling | Restricts candidates to the K highest-scoring tokens. |
| Top-P sampling | Restricts candidates based on cumulative probability. |

Some systems apply more than one generation setting. The exact order of transformations and filtering can vary by implementation.

The selected token is then appended to the current sequence.

```text id="z2m7vw"
Logits
  |
  v
Optional Logit Processing
  |
  v
Probability Distribution
  |
  v
Decoding Strategy
  |
  v
Selected Token
```

### What changes at this stage?

The model's candidate scores become a concrete token choice for the next position.

---

## 15. Stage 13 — The Sequence Is Updated

The selected token becomes part of the context used for the next prediction.

For example:

```text id="m9x4ka"
Initial context:
"The cat"

        |
        v

Selected token:
" is"

        |
        v

Updated context:
"The cat is"

        |
        v

Next selected token:
" sleeping"

        |
        v

Updated context:
"The cat is sleeping"
```

The example illustrates the process; the actual tokens depend on the model and decoding settings.

This repeated process is called **autoregressive generation**.

The new token affects the context available for subsequent predictions, so each next-token prediction is conditioned on the sequence generated so far.

---

## 16. Stage 14 — KV Cache and Repeated Computation

During autoregressive inference, many implementations use a key-value (KV) cache to reuse previously computed attention information.

The cache stores key and value representations from earlier token positions.

```text id="q6w3rn"
Process Initial Prompt
          |
          v
Compute Attention Keys and Values
          |
          v
Store in KV Cache
          |
          v
Generate New Token
          |
          v
Compute New Token's Keys and Values
          |
          v
Reuse Previous Cache
          |
          v
Predict the Following Token
```

This reduces repeated computation during decoding.

The cache is temporary inference state. It is not the model's permanent knowledge and does not update the learned model parameters.

---

## 17. Stage 15 — Stop and Decode the Output

Generation continues until a configured stopping condition is reached.

Possible conditions include:

- An end-of-sequence token
- A configured stop sequence
- The maximum number of new tokens
- Another applicable generation limit

Once generation ends, the tokenizer converts the generated token IDs into readable text.

```text id="w4n8cz"
Generated Token IDs
         |
         v
Stopping Condition Reached
         |
         v
Tokenizer Decoding
         |
         v
Readable Output Text
```

The final displayed text may depend on how special tokens, whitespace, and formatting are handled.

---

## 18. Complete Data Flow During Inference

The full inference flow combines all the previous stages.

```text id="f3j8mx"
INPUT TEXT
    |
    v
TOKENIZER
    |
    v
TOKEN IDs
    |
    v
EMBEDDING LOOKUP
    |
    v
POSITIONAL INFORMATION
    |
    v
INITIAL REPRESENTATIONS
    |
    v
TRANSFORMER BLOCKS
    |
    +--> CAUSAL SELF-ATTENTION
    |
    +--> FEED-FORWARD NETWORK
    |
    +--> RESIDUAL CONNECTIONS
    |
    +--> NORMALIZATION
    |
    v
FINAL HIDDEN REPRESENTATION
    |
    v
LANGUAGE MODELING HEAD
    |
    v
LOGITS
    |
    v
DECODING / TOKEN SELECTION
    |
    v
SELECTED TOKEN
    |
    v
UPDATE CONTEXT
    |
    +---- Repeat prediction and selection
    |
    v
STOP GENERATION
    |
    v
TOKENIZER DECODING
    |
    v
OUTPUT TEXT
```

During the initial prompt-processing stage, the model can process multiple positions together. During subsequent autoregressive decoding, it typically uses the latest position to predict the next token and may reuse cached attention information.

---

## 19. Complete Data Flow During Training

The input-to-logits path is also used during training, but the output participates in a learning process.

The training pipeline adds target tokens, loss calculation, gradient computation, and parameter updates.

```text id="y7v2ka"
TRAINING TEXT
      |
      v
TOKENIZATION
      |
      v
TOKEN IDS
      |
      v
TRAINING SEQUENCES
      |
      v
INPUTS AND SHIFTED TARGETS
      |
      v
EMBEDDINGS + POSITIONAL INFORMATION
      |
      v
TRANSFORMER BLOCKS
      |
      v
LOGITS
      |
      v
LOSS AGAINST TARGET TOKENS
      |
      v
BACKPROPAGATION
      |
      v
GRADIENTS
      |
      v
OPTIMIZER UPDATES PARAMETERS
      |
      v
REPEAT WITH MORE BATCHES
```

### What is different during training?

- Target tokens provide the correct next-token predictions.
- Loss measures how well the model predicts those targets.
- Backpropagation calculates gradients.
- The optimizer updates trainable parameters.

For standard causal language-model training, the causal mask prevents future tokens from leaking into predictions at earlier positions.

During ordinary inference, the model instead uses its current parameters to generate tokens without performing these parameter updates.

---

## 20. How the Data Changes Throughout the Pipeline

| Stage | Input | Output |
|---|---|---|
| Tokenization | Text | Token IDs |
| Embedding | Token IDs | Learned vectors |
| Positional mechanism | Token vectors and position information, as appropriate | Position-aware representations |
| Attention | Hidden representations | Context-mixed representations |
| Feed-forward network | Hidden representations | Nonlinearly transformed representations |
| Transformer stack | Representations from the previous block | Final hidden representations |
| Language modeling head | Hidden representations | Vocabulary logits |
| Softmax, when used | Logits | Probability distribution |
| Decoding | Scores or probabilities | Selected token |
| Sequence update | Existing context and selected token | Updated context |
| Tokenizer decoding | Generated token IDs | Readable text |

The data changes form at each stage, but the stages are connected: each component produces information used by a later component.

---

## 21. Common Misconceptions

**Misconception 1: Token IDs already contain semantic meaning.**

Token IDs are identifiers. The model retrieves learned embeddings and transforms them through its neural network.

**Misconception 2: Embeddings are the final representations.**

Embeddings are initial token representations. Transformer blocks repeatedly transform them into contextual hidden representations.

**Misconception 3: Attention alone generates the answer.**

Attention is one part of a Transformer block. Feed-forward networks, residual connections, normalization, the output layer, and the decoding process also contribute to the complete pipeline.

**Misconception 4: Logits are readable words or probabilities.**

Logits are numerical scores associated with vocabulary tokens. A probability transformation and decoding strategy can be used to select a token.

**Misconception 5: The entire response is predicted in one step.**

In autoregressive generation, the system repeatedly predicts and selects the next token, updating the context after each selection.

**Misconception 6: The KV cache is a permanent memory of everything the model knows.**

The KV cache stores intermediate attention information for a particular inference context. It is distinct from the model's learned parameters.

**Misconception 7: Training and inference are completely different architectures.**

They commonly use the same core neural network architecture. Training adds loss, gradient computation, and parameter updates, while ordinary inference focuses on predictions and generation.

---

## 22. Complete LLM Data Flow — Final Summary

The complete data flow can be understood in three major stages.

### Stage A — Convert text into representations

```text id="b5n8qx"
Text
 |
 v
Token IDs
 |
 v
Embeddings
 |
 v
Positional Information
```

### Stage B — Transform representations into predictions

```text id="p3w6mv"
Transformer Blocks
       |
       v
Final Hidden States
       |
       v
Language Modeling Head
       |
       v
Logits
       |
       v
Probability Distribution
```

### Stage C — Generate the output

```text id="j8k2rw"
Token Selection
      |
      v
Append Selected Token
      |
      v
Update Context
      |
      v
Repeat Until Stopped
      |
      v
Decode Token IDs
      |
      v
Readable Text
```

The most important idea is that **an LLM transforms text into token IDs, converts those IDs into learned representations, processes those representations through Transformer blocks, and uses the resulting predictions to generate text.**

Remember the complete sequence:

**Text → Token IDs → Embeddings → Positional Information → Transformer Blocks → Hidden States → Logits → Token Selection → Updated Context → Generated Text**

During training, target tokens, loss calculation, backpropagation, and optimizer updates teach the model to improve its predictions. During ordinary inference, the trained model uses its existing parameters to generate the next tokens.

Together, these stages explain how information flows through a typical GPT-style LLM.
