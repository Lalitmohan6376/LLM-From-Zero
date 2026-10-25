# 🧠 Complete LLM Architecture

A Large Language Model (LLM) is built from multiple connected components that transform input text into numerical representations, process those representations through neural network layers, and generate output text.

This document explains the complete architecture of a typical **GPT-style, decoder-only LLM**, from input tokens to generated text.

---

## 1. What Is LLM Architecture?

LLM architecture describes how the internal components of a language model are organized and how information flows between them.

A typical GPT-style LLM contains these major components:

1. **Tokenizer** — converts text into token IDs.
2. **Token Embedding Layer** — converts token IDs into vectors.
3. **Positional Information** — provides information about token positions.
4. **Transformer Blocks** — process tokens and build contextual representations.
5. **Final Normalization** — prepares the final hidden representations when used by the architecture.
6. **Language Modeling Head** — converts hidden representations into vocabulary-sized logits.
7. **Decoding Process** — selects the next token from the model's predictions.

The tokenizer and decoding process are generally outside the neural network itself, but they are essential parts of the complete text-generation pipeline.

---

## 2. Complete Architecture at a Glance

```text
                 INPUT TEXT
                     |
                     v
             "The cat is sleeping"
                     |
                     v
                 TOKENIZER
                     |
                     v
              TOKEN IDs
             [45, 182, 27, 903]
                     |
                     v
             TOKEN EMBEDDINGS
                     |
                     v
            POSITIONAL INFORMATION
                     |
                     v
             INITIAL REPRESENTATIONS
                     |
                     v
          +--------------------------+
          |    TRANSFORMER BLOCK 1   |
          |                          |
          |  Causal Self-Attention   |
          |             |            |
          |  Feed-Forward Network    |
          +--------------------------+
                     |
                     v
          +--------------------------+
          |    TRANSFORMER BLOCK 2   |
          |                          |
          |  Causal Self-Attention   |
          |             |            |
          |  Feed-Forward Network    |
          +--------------------------+
                     |
                     v
                    ...
                     |
                     v
          +--------------------------+
          |    TRANSFORMER BLOCK N   |
          +--------------------------+
                     |
                     v
             FINAL NORMALIZATION
                     |
                     v
              FINAL HIDDEN STATE
                     |
                     v
           LANGUAGE MODELING HEAD
                     |
                     v
                    LOGITS
                     |
                     v
            PROBABILITY DISTRIBUTION
                     |
                     v
              NEXT TOKEN SELECTION
                     |
                     v
               GENERATED TOKEN
                     |
                     v
           TOKENIZER DECODES TOKENS
                     |
                     v
                OUTPUT TEXT
```

**Important:** The Transformer blocks and language modeling head are part of the neural network. Tokenization, token selection, and text decoding are surrounding pipeline operations.

---

## 3. Step 1 — Tokenizer

The model does not directly process ordinary text as words that humans read. A tokenizer divides the text into tokens and maps each token to an integer ID.

For example:

```text
Input text:
"The cat is sleeping"

             |
             v

Tokens:
["The", " cat", " is", " sleeping"]

             |
             v

Token IDs:
[45, 182, 27, 903]
```

These token IDs are illustrative. Actual IDs depend on the tokenizer.

### Why is tokenization necessary?

- Neural networks operate on numerical data.
- Token IDs provide the numerical representation used to retrieve embeddings.
- Tokenization determines how text is divided into manageable units.
- The model's vocabulary defines the available token IDs.

Token IDs themselves do not contain the semantic meaning of words. That information is represented through learned parameters and the computations performed by the model.

---

## 4. Step 2 — Token Embedding Layer

The embedding layer converts each token ID into a learned vector.

For example:

```text
Token IDs:
[45, 182, 27, 903]

             |
             v

Embedding Layer

45  -> [0.21, -0.14, 0.73, ...]
182 -> [0.62,  0.08, 0.19, ...]
27  -> [0.11,  0.57, 0.32, ...]
903 -> [0.44, -0.21, 0.68, ...]
```

Each token ID identifies a row in the model's embedding matrix.

If the model uses an embedding dimension of \(d_{\text{model}}\), every token is represented by a vector with that many values.

For a sequence of \(N\) tokens, the embedding output has the shape:

\[
X \in \mathbb{R}^{N \times d_{\text{model}}}
\]

For a batch of inputs, the shape is commonly:

\[
X \in \mathbb{R}^{B \times N \times d_{\text{model}}}
\]

Where:

- \(B\) = batch size
- \(N\) = sequence length
- \(d_{\text{model}}\) = hidden representation dimension

The actual dimensions depend on the model.

### What does an embedding represent?

An embedding is a learned numerical representation of a token. It is not the token's final contextual meaning.

That distinction becomes important when the token enters the Transformer blocks.

---

## 5. Step 3 — Positional Information

Self-attention processes relationships between tokens, so the architecture needs a way to represent their positions or order.

Consider:

- `The dog chased the cat.`
- `The cat chased the dog.`

The same words appear in different arrangements, but the meanings differ.

Positional information helps the model distinguish these arrangements.

Common approaches include:

| Method | Basic idea |
|---|---|
| Learned positional embeddings | Learn a vector associated with each position. |
| Sinusoidal positional encoding | Use fixed mathematical patterns to represent positions. |
| Rotary Position Embedding (RoPE) | Incorporate position information by rotating query and key representations. |

These approaches are not identical, and a model does not necessarily use all of them.

For example, a model using learned positional embeddings may combine token embeddings with positional vectors:

\[
X = E_{\text{token}} + E_{\text{position}}
\]

In a RoPE-based model, positional information is incorporated differently, within the attention computation.

**Key point:** The architecture must represent positional relationships, but the exact method depends on the model.

---

## 6. Step 4 — Transformer Blocks

Transformer blocks are the main computational components of a GPT-style LLM.

A model typically stacks many Transformer blocks. Each block transforms the representations produced by the previous block.

A simplified block looks like this:

```text
       INPUT REPRESENTATIONS
                 |
                 v
        CAUSAL SELF-ATTENTION
                 |
                 v
         RESIDUAL CONNECTION
                 |
                 v
        NORMALIZATION (if used
        at this point in design)
                 |
                 v
       FEED-FORWARD NETWORK
                 |
                 v
         RESIDUAL CONNECTION
                 |
                 v
        NORMALIZATION (if used
        at this point in design)
                 |
                 v
        OUTPUT REPRESENTATIONS
```

This diagram illustrates the main components, not a universal execution order. Many modern LLMs use pre-normalization, where normalization occurs before attention and the feed-forward network.

A typical Transformer block contains:

- Causal self-attention
- A feed-forward network
- Residual connections
- Normalization layers

Let's examine the two main computational components.

### 6.1 Causal Self-Attention

Self-attention allows each token to incorporate information from other tokens in its context.

For example:

```text
"The animal did not eat because it was full."
```

When processing the token `it`, attention can help the model use information from earlier tokens to interpret the surrounding context.

In a decoder-only LLM, causal masking prevents a token from attending to future token positions.

For example:

```text
Position:       1    2    3    4
Tokens:        The  cat  is   ...

Token "The":   can attend to position 1
Token "cat":   can attend to positions 1-2
Token "is":    can attend to positions 1-3
```

During training, the full sequence can be processed in parallel, while the causal mask prevents future-token information from being used to predict earlier positions.

During autoregressive generation, the model predicts from the available context.

### Query, Key, and Value

Attention uses three learned projections:

- **Query (Q):** Represents what a token is looking for.
- **Key (K):** Represents information used to calculate how relevant a token is to another token.
- **Value (V):** Carries information that contributes to the attention output.

The standard scaled dot-product attention formula is:

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
- \(M\) represents the causal mask, with disallowed positions masked before softmax.
- Softmax converts the allowed scores into attention weights.
- The weights determine how values contribute to the output.

The result is a new representation for each token, incorporating information from the allowed context.

### Multi-Head Attention

Many Transformer blocks use multiple attention heads.

Each head performs attention using its own learned projections. The resulting representations are combined to produce the block's attention output.

Conceptually:

```text
Input Representations
          |
          v
  +-------+-------+
  |       |       |
  v       v       v
 Head 1  Head 2  Head 3  ... Other Heads
  |       |       |
  v       v       v
  +-------+-------+
          |
          v
   Combine Head Outputs
          |
          v
    Attention Output
```

Different heads can learn different patterns of relationships. However, it is not guaranteed that each head corresponds to one clean, human-interpretable function.

### 6.2 Feed-Forward Network

After attention, each token's representation passes through a feed-forward network.

A simplified version is:

\[
\operatorname{FFN}(x)
=
W_2\,\sigma(W_1x+b_1)+b_2
\]

Where:

- \(W_1\) and \(W_2\) are learned weight matrices.
- \(b_1\) and \(b_2\) are bias terms.
- \(\sigma\) is an activation function.

The first projection often expands the hidden dimension, and the second projects it back to the model's hidden dimension.

For example:

```text
Hidden Dimension
      768
       |
       v
First Linear Layer
       |
       v
Intermediate Dimension
      3072
       |
       v
Activation Function
       |
       v
Second Linear Layer
       |
       v
Hidden Dimension
      768
```

These dimensions are illustrative.

Attention primarily mixes information across token positions, while the feed-forward network transforms each position's representation using learned nonlinear computations.

Modern LLMs may use gated feed-forward networks rather than this simplified form.

### 6.3 Residual Connections

Residual connections provide a path for the original representation to contribute directly to a block's output.

A simplified expression is:

\[
y=x+F(x)
\]

Here, \(F(x)\) represents a transformation such as an attention or feed-forward sublayer, including any relevant operations in that sublayer.

Residual connections help information and gradients flow through deep networks.

### 6.4 Normalization

Normalization helps control the scale and distribution of intermediate activations.

Transformer architectures commonly use Layer Normalization or RMSNorm.

The placement of normalization differs between designs. For example:

- **Pre-norm:** Normalize the input before a sublayer.
- **Post-norm:** Normalize after a residual addition.

Therefore, the exact block ordering must be determined from the architecture being studied.

---

## 7. Step 5 — Stacking Transformer Blocks

A typical LLM contains multiple Transformer blocks arranged sequentially.

```text
Initial Token Representations
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
      Final Hidden Representations
```

Every block receives the previous block's output and produces a new set of representations.

As information passes through the network, representations can incorporate increasingly complex contextual patterns.

For example, a token's representation may become more informative about:

- Its surrounding words
- Grammatical relationships
- Relevant information elsewhere in the context
- Semantic relationships
- Patterns learned during training

These are examples of information the model can represent, not a guarantee that every layer performs one specific human-interpretable task.

The number of blocks, hidden dimension, attention configuration, and other architectural details depend on the model.

---

## 8. Step 6 — Final Normalization

Some architectures apply a final normalization layer after the last Transformer block.

```text
Last Transformer Block
          |
          v
  Final Normalization
          |
          v
  Final Hidden States
```

This operation prepares the representations for the output layer.

Not every architecture uses exactly the same normalization method or placement.

---

## 9. Step 7 — Language Modeling Head

The language modeling head converts the final hidden representations into scores for the model's vocabulary.

Suppose the vocabulary contains 50,000 possible token IDs. The output layer produces one score for each vocabulary token at every position where predictions are computed.

A simplified linear projection is:

\[
z=hW_{\text{out}}+b
\]

Where:

- \(h\) = hidden representation
- \(W_{\text{out}}\) = output projection weights
- \(b\) = optional bias
- \(z\) = logits

For a vocabulary of size \(V\), the logits for one position have \(V\) values.

During training, logits are commonly calculated for many positions in a sequence. During generation, the next-token decision generally uses the logits for the last available position.

### Example

```text
Final Hidden State
       |
       v
Language Modeling Head
       |
       v
Vocabulary Logits

"The"       -> 1.2
"cat"       -> 3.8
" sleeps"   -> 2.1
" runs"     -> 0.9
...         -> ...
```

These scores are illustrative and do not represent a real model's output.

**Logits are raw scores, not probabilities.** A larger logit indicates a higher score relative to other candidates, but the scores do not have to lie between zero and one.

---

## 10. Step 8 — Probability Distribution

The model can convert logits into a probability distribution using softmax.

\[
P_i=\frac{e^{z_i}}{\sum_{j=1}^{V}e^{z_j}}
\]

Where:

- \(z_i\) is the logit for token \(i\).
- \(V\) is the vocabulary size.
- \(P_i\) is the resulting probability for token \(i\).

The probabilities are non-negative and sum to one, subject to normal numerical behavior.

For example, a model might produce the following illustrative probabilities:

| Candidate token | Probability |
|---|---:|
| ` sleeps` | 55% |
| ` runs` | 25% |
| ` plays` | 15% |
| Other candidates combined | 5% |
| **Total** | **100%** |

These values are examples, not actual predictions from a particular model.

The distribution describes the model's relative predictions for the next token given the current context.

---

## 11. Step 9 — Decoding and Next-Token Selection

Once the model produces logits, a decoding strategy determines how the next token is selected.

Common approaches include:

| Strategy | Basic behavior |
|---|---|
| Greedy decoding | Select the token with the highest probability. |
| Temperature sampling | Adjust the sharpness of the distribution before sampling. |
| Top-K sampling | Restrict candidates to the K highest-scoring tokens. |
| Top-P sampling | Restrict candidates using cumulative probability. |

Depending on the generation configuration, the system may modify logits before calculating the final sampling distribution.

For example, greedy decoding selects the highest-scoring token directly, while sampling-based strategies can select a different token from the candidate distribution.

The chosen token is appended to the sequence, and generation continues.

---

## 12. Step 10 — Autoregressive Generation

GPT-style LLMs generally generate text autoregressively: they produce one new token at a time, using the available sequence as context for the next prediction.

Suppose the prompt is:

```text
"The cat"
```

A simplified generation process might look like this:

```text
Prompt:
"The cat"
    |
    v
Predict next token:
" is"
    |
    v
Updated sequence:
"The cat is"
    |
    v
Predict next token:
" sleeping"
    |
    v
Updated sequence:
"The cat is sleeping"
    |
    v
Predict another token or stop
```

The tokens shown are illustrative.

The core loop is:

1. Process the available context through the model.
2. Obtain logits for the next token.
3. Apply the decoding strategy.
4. Select the next token.
5. Append the token to the sequence.
6. Repeat until a stopping condition is reached.

### KV Cache

During generation, many implementations use a **key-value (KV) cache**.

The cache stores previously computed attention keys and values so the model can reuse them during subsequent decoding steps.

Without caching, the model could repeatedly recompute attention information for earlier tokens. With caching, it can avoid much of this repeated work.

The KV cache is temporary inference state; it is not the same as the model's learned parameters.

---

## 13. Step 11 — Stopping Generation

Generation ends when an applicable stopping condition is reached.

Common conditions include:

- The model generates an end-of-sequence (EOS) token.
- A configured stop sequence is detected.
- The maximum number of new tokens is reached.
- Another system-defined generation limit is triggered.

The **context window** and the **maximum number of new tokens** are different concepts.

The context window limits how much tokenized context the model can handle under its configured limits. The maximum-new-token setting limits how many tokens the generation process may produce in a particular request.

---

## 14. Step 12 — Convert Tokens Back to Text

After generation stops, the tokenizer's decoding process converts the generated token IDs into readable text.

```text
Generated Token IDs
          |
          v
       TOKENIZER
          |
          v
    Decoded Text
          |
          v
"The cat is sleeping."
```

The displayed text may also depend on how the application handles special tokens, whitespace, and other formatting details.

The tokenizer does not generate the answer itself. It converts between text and the token representation used by the model.

---

## 15. How the Architecture Works During Training

The architecture is used during both training and inference, but the overall processes have different purposes.

During training, the model learns by adjusting its parameters to reduce prediction errors on training examples.

A simplified causal language-model training pipeline is:

```text
Training Text
      |
      v
Tokenization
      |
      v
Input Token IDs + Target Token IDs
      |
      v
Embeddings + Positional Information
      |
      v
Transformer Blocks
      |
      v
Language Modeling Head
      |
      v
Logits
      |
      v
Loss Calculation
      |
      v
Backpropagation
      |
      v
Optimizer Updates Parameters
      |
      v
Updated Model
```

For next-token prediction, input and target sequences are generally shifted relative to each other. The model predicts the next token at each eligible position, and the loss measures the difference between predictions and the correct targets.

The causal mask prevents future tokens from leaking into earlier predictions.

Backpropagation calculates gradients, and the optimizer uses those gradients to update trainable parameters.

This process is repeated across training batches and iterations.

---

## 16. How the Architecture Works During Inference

During inference, the model uses its trained parameters to produce predictions for a given prompt.

A simplified inference pipeline is:

```text
User Prompt
     |
     v
Tokenization
     |
     v
Token IDs
     |
     v
Embeddings + Positional Information
     |
     v
Transformer Blocks
     |
     v
Language Modeling Head
     |
     v
Logits for Next Token
     |
     v
Decoding Strategy
     |
     v
Selected Token
     |
     v
Update Context and Repeat
     |
     v
Generated Text
```

During ordinary inference, the model's learned parameters are not updated.

The sequence grows as tokens are generated, and the model uses the updated context to predict subsequent tokens. Temporary state, such as the KV cache, may change during this process.

---

## 17. Training vs. Inference

| Aspect | Training | Inference |
|---|---|---|
| Main purpose | Learn from data | Generate predictions |
| Input | Training sequences | Prompt and generated context |
| Transformer blocks | Process training inputs | Process inference inputs |
| Output logits | Commonly for many positions | Generally used at the last position for next-token generation |
| Loss calculation | Used for optimization | Not required for ordinary text generation |
| Backpropagation | Used to calculate gradients | Not used for ordinary generation |
| Parameter updates | Yes, during optimization | No, during ordinary inference |
| Token generation | Usually not the training objective itself | Repeated next-token selection |
| KV cache | Depends on training implementation; not normally needed for standard full-sequence training | Commonly used for efficient autoregressive decoding |

The same learned model architecture can participate in both processes. The important difference is whether the system is optimizing parameters or using the existing parameters to make predictions.

---

## 18. Important Architectural Concepts

### Model parameters

Parameters are learned numerical values, including weights and biases in embeddings, attention projections, feed-forward networks, and output layers.

Training adjusts these values through optimization.

### Hidden representations

Hidden representations are the vectors produced and transformed inside the network. They contain learned numerical information about tokens and their context.

They are different from token IDs, which are integer identifiers assigned by the tokenizer.

### Contextual representations

A token's representation changes as it passes through Transformer blocks. Its final representation can incorporate information from other permitted tokens in the sequence.

### Vocabulary

The vocabulary is the set of tokens that the tokenizer and model's output layer are designed to represent. It is not a database containing every possible answer.

### Model size

The number of parameters is one measure of model size. Other architectural dimensions, such as the number of Transformer blocks, hidden dimension, and attention configuration, also affect the model's computational requirements and behavior.

A larger parameter count alone does not guarantee better performance.

---

## 19. Common Misconceptions

**Misconception 1: The model directly understands words as humans do.**

The model processes numerical representations and learned patterns. Human-like understanding should not be assumed from its outputs.

**Misconception 2: Token IDs contain meaning.**

Token IDs are identifiers. Learned embeddings and subsequent computations create the representations used by the model.

**Misconception 3: Attention is the entire Transformer block.**

Attention is one component. Transformer blocks also include feed-forward computations, residual connections, and normalization.

**Misconception 4: The model generates a complete response in one forward pass.**

Autoregressive generation generally repeats next-token prediction, updating the available context after each selected token.

**Misconception 5: Inference changes the model's learned parameters.**

Ordinary inference uses the existing parameters without updating them. Temporary context and cache state can still change.

**Misconception 6: The tokenizer is the language model itself.**

The tokenizer converts text to and from token representations. The neural network processes those representations and calculates predictions.

---

## 20. Complete LLM Architecture — Final Summary

A GPT-style LLM connects text processing, neural network computation, and token generation into one pipeline.

```text
TEXT INPUT
    |
    v
TOKENIZER
    |
    v
TOKEN IDS
    |
    v
TOKEN EMBEDDINGS
    |
    v
POSITIONAL INFORMATION
    |
    v
STACKED TRANSFORMER BLOCKS
    |
    +--> Causal Self-Attention
    |
    +--> Feed-Forward Networks
    |
    +--> Residual Connections
    |
    +--> Normalization
    |
    v
FINAL HIDDEN REPRESENTATIONS
    |
    v
LANGUAGE MODELING HEAD
    |
    v
LOGITS
    |
    v
PROBABILITY / DECODING PROCESS
    |
    v
NEXT TOKEN
    |
    v
REPEATED AUTOREGRESSIVE GENERATION
    |
    v
TOKENIZER DECODES OUTPUT
    |
    v
GENERATED TEXT
```

The essential idea is that **the neural network transforms token representations into predictions, and the generation process repeatedly uses those predictions to produce text.**

Remember these distinctions:

- Token IDs identify tokens; embeddings represent them numerically.
- Positional information helps represent token order.
- Transformer blocks build contextual representations.
- The language modeling head produces vocabulary logits.
- Decoding selects the next token.
- Autoregressive generation repeats this process.
- Training updates parameters; ordinary inference uses the trained parameters.

Together, these components explain the complete architecture and basic text-generation workflow of a typical decoder-only LLM.
