# 🧠 Decoder-Only Architecture

## 📌 Introduction

A **Decoder-Only Architecture** is a Transformer architecture that uses only a stack of **decoder-style Transformer blocks** to process text and generate the next token.

Modern generative LLMs such as GPT-style models are commonly built using this architecture.

The basic idea is:

```text
Text
 ↓
Tokenization
 ↓
Token IDs
 ↓
Token Embeddings
 ↓
Positional Information
 ↓
Decoder Block
 ↓
Decoder Block
 ↓
Decoder Block
 ↓
...
 ↓
Final Representation
 ↓
Language Model Head
 ↓
Logits
 ↓
Probabilities
 ↓
Next Token
```

The important point is that a decoder-only LLM does **not** contain a separate Encoder stack.

---

# 1. 🏗️ What Is Decoder-Only Architecture?

A decoder-only architecture is a Transformer-based architecture where the model consists primarily of a stack of Transformer blocks using:

* Causal self-attention
* Feed-forward networks
* Residual connections
* Layer normalization
* Positional information

It is called **decoder-only** because there is no separate Encoder stack.

A simplified structure is:

```text
                Input Text
                    ↓
               Tokenization
                    ↓
                Token IDs
                    ↓
             Token Embeddings
                    ↓
          Positional Information
                    ↓
        ┌───────────────────────┐
        │   Decoder Block 1     │
        ├───────────────────────┤
        │   Decoder Block 2     │
        ├───────────────────────┤
        │   Decoder Block 3     │
        ├───────────────────────┤
        │          ...          │
        ├───────────────────────┤
        │   Decoder Block N     │
        └───────────────────────┘
                    ↓
          Final Hidden States
                    ↓
              Language Model
                  Head
                    ↓
                 Logits
                    ↓
             Next Token
```

---

# 2. 🔄 Original Transformer vs Decoder-Only

The original Transformer architecture introduced in **"Attention Is All You Need"** used two main stacks:

```text
Input
  ↓
Encoder
  ↓
Encoder Representations
  ↓
Decoder
  ↓
Output
```

The Encoder and Decoder had different responsibilities.

A decoder-only LLM removes the separate Encoder:

```text
Input
  ↓
Decoder-Only Transformer
  ↓
Output
```

So:

```text
Original Transformer

Encoder + Decoder
```

while:

```text
GPT-style LLM

Decoder-only
```

---

# 3. 🧩 Why Is It Called a Decoder?

The word **decoder** comes from the original Transformer architecture.

The original Transformer Decoder was designed to generate output tokens while using:

1. Masked self-attention
2. Cross-attention to Encoder outputs
3. Feed-forward network

However, a decoder-only LLM does not use the separate Encoder or the Encoder-Decoder cross-attention pathway.

A simplified decoder-only block is:

```text
Input
  ↓
Causal Self-Attention
  ↓
Residual Connection
  ↓
Layer Normalization
  ↓
Feed-Forward Network
  ↓
Residual Connection
  ↓
Layer Normalization
  ↓
Output
```

The exact ordering can vary between architectures.

---

# 4. 🚫 No Separate Encoder

One of the most important characteristics is:

```text
Decoder-Only LLM

Encoder ❌
Decoder-style Transformer Blocks ✅
```

There is no separate path like:

```text
Input → Encoder → Encoder Output
                         ↓
                      Decoder
                         ↓
                      Output
```

Instead:

```text
Input
  ↓
Decoder Block 1
  ↓
Decoder Block 2
  ↓
Decoder Block 3
  ↓
...
  ↓
Output
```

The same stack processes the input and builds increasingly contextual representations.

---

# 5. 👀 Causal Self-Attention

Decoder-only language models use **causal self-attention**.

Causal attention prevents a token from using information from future positions.

For example:

```text
The cat is sleeping
```

During training, the model should not allow:

```text
The → cat
```

to use information from future tokens such as:

```text
is sleeping
```

The allowed attention pattern is:

```text
          The cat is sleeping
The       ✓   ✗   ✗    ✗
cat       ✓   ✓   ✗    ✗
is        ✓   ✓   ✓    ✗
sleeping  ✓   ✓   ✓    ✓
```

This is controlled by a **causal mask**.

---

# 6. 🎭 Causal Mask

The causal mask follows a lower-triangular pattern:

```text
        1 2 3 4
    1   1 0 0 0
    2   1 1 0 0
    3   1 1 1 0
    4   1 1 1 1
```

Here:

* `1` → attention is allowed
* `0` → attention is blocked

So position `3` can see:

```text
1, 2, 3
```

but cannot see:

```text
4
```

The important rule is:

```text
A token can attend to itself
and all previous tokens,
but not future tokens.
```

---

# 7. 🧠 Why Does Decoder-Only Need Causal Attention?

The main training objective is usually **next-token prediction**.

For example:

```text
Input:

The cat is

Target:

cat is sleeping
```

Conceptually:

```text
The       → cat
The cat   → is
The cat is → sleeping
```

The model must learn to predict the next token using only information available up to that position.

Without causal masking, the model could see the answer during training.

That would create **information leakage**.

---

# 8. 🎯 Next-Token Prediction

The core task can be represented as:

```text
Previous Tokens
      ↓
Decoder-Only Transformer
      ↓
Probability Distribution
      ↓
Next Token
```

Example:

```text
"The cat is"
```

The model might produce probabilities such as:

```text
sleeping    0.45
running     0.15
eating      0.10
sitting     0.08
...
```

The model selects or samples a token according to the generation strategy.

Suppose:

```text
sleeping
```

is selected.

The sequence becomes:

```text
"The cat is sleeping"
```

Then the model predicts another token.

---

# 9. 🔁 Autoregressive Generation

Decoder-only LLMs generate text **autoregressively**.

This means the generated token is added to the sequence and becomes part of the context for the next prediction.

Example:

```text
Prompt:
The weather today is

        ↓

Predict:
beautiful

        ↓

The weather today is beautiful

        ↓

Predict:
and

        ↓

The weather today is beautiful and

        ↓

Predict:
sunny

        ↓

The weather today is beautiful and sunny
```

The process continues until generation stops.

---

# 10. 🧱 Transformer Blocks

A decoder-only LLM contains many Transformer blocks.

For example:

```text
Input
  ↓
┌─────────────────┐
│ Transformer     │
│ Block 1         │
└─────────────────┘
  ↓
┌─────────────────┐
│ Transformer     │
│ Block 2         │
└─────────────────┘
  ↓
┌─────────────────┐
│ Transformer     │
│ Block 3         │
└─────────────────┘
  ↓
        ...
  ↓
┌─────────────────┐
│ Transformer     │
│ Block N         │
└─────────────────┘
  ↓
Final Representation
```

Each block transforms the representations produced by the previous block.

---

# 11. 🔍 What Happens Inside a Decoder Block?

A simplified decoder-only Transformer block contains:

```text
Input
  ↓
Causal Self-Attention
  ↓
Residual Connection
  ↓
Layer Normalization
  ↓
Feed-Forward Network
  ↓
Residual Connection
  ↓
Layer Normalization
  ↓
Output
```

The exact ordering can differ.

Some modern architectures use **Pre-LayerNorm** instead of the simplified ordering shown above.

---

# 12. 👁️ Causal Self-Attention

Causal self-attention allows each token to combine information from earlier tokens.

For example:

```text
"The dog chased the cat"
```

When processing:

```text
cat
```

the model can use information from:

```text
The
dog
chased
the
cat
```

But a token cannot use information from tokens appearing later in the sequence.

For position `i`, the model can attend to positions:

```text
j ≤ i
```

but not:

```text
j > i
```

---

# 13. 🔑 Query, Key and Value

Self-attention uses three representations:

```text
Query (Q)
Key   (K)
Value (V)
```

They are usually created from the input representation:

```text
Q = XWQ
K = XWK
V = XWV
```

Attention is then calculated as:

```text
Attention(Q, K, V)
=
softmax(QKᵀ / √dₖ)V
```

For decoder-only models, the causal mask is applied before the softmax operation.

Conceptually:

```text
QKᵀ
 ↓
Scale
 ↓
Apply Causal Mask
 ↓
Softmax
 ↓
Attention Weights
 ↓
Weighted Values
```

---

# 14. 🧠 Multi-Head Attention

Modern Transformer blocks generally use **multi-head attention**.

Instead of performing one attention operation, multiple attention heads operate in parallel.

```text
                    Input
                      ↓
          ┌───────────┼───────────┐
          ↓           ↓           ↓
        Head 1      Head 2      Head 3
          ↓           ↓           ↓
          └───────────┼───────────┘
                      ↓
                  Concatenate
                      ↓
                Output Projection
```

Different heads can learn different patterns or relationships.

For example, one head might capture a relationship between nearby words while another may capture a longer-range dependency.

These interpretations are conceptual; individual attention heads are not guaranteed to have one simple human-readable role.

---

# 15. ⚡ Feed-Forward Network

After attention, the representation is processed by a **Feed-Forward Network (FFN)**.

A simplified FFN is:

```text
Input
  ↓
Linear Layer
  ↓
Activation
  ↓
Linear Layer
  ↓
Output
```

A common simplified formula is:

```text
FFN(x) = W₂ σ(W₁x + b₁) + b₂
```

The FFN mainly transforms the representation at each token position.

A useful mental model is:

```text
Attention
   ↓
Mix information between tokens

FFN
   ↓
Transform information at each position
```

Modern LLMs may use gated FFN variants such as **SwiGLU** instead of the simple FFN shown here.

---

# 16. ➕ Residual Connections

Transformer blocks use residual connections.

Conceptually:

```text
Input
  │
  ├───────────────┐
  ↓               │
Attention         │
  ↓               │
Processed         │
Representation    │
  │               │
  └────── + ◄─────┘
          │
        Output
```

The original representation is combined with the transformed representation.

Residual connections help information flow through deep networks.

---

# 17. 📏 Layer Normalization

Layer normalization helps keep the representations in a useful numerical range during processing.

A simplified block may look like:

```text
Input
  ↓
Attention
  ↓
Residual + Normalization
  ↓
FFN
  ↓
Residual + Normalization
  ↓
Output
```

Modern architectures may arrange normalization differently.

Therefore, the exact block structure should not be assumed to be identical for every decoder-only LLM.

---

# 18. 📚 Stacking Many Blocks

One Transformer block is usually not enough for a large language model.

Multiple blocks are stacked:

```text
Input
  ↓
Block 1
  ↓
Block 2
  ↓
Block 3
  ↓
Block 4
  ↓
...
  ↓
Block N
  ↓
Final Representation
```

Each layer receives the output of the previous layer.

As the representation passes through the stack, it can incorporate increasingly complex contextual information.

---

# 19. 🔄 Representation Through the Network

Consider:

```text
The cat is sleeping
```

After tokenization:

```text
The | cat | is | sleeping
```

After token IDs:

```text
[101, 245, 52, 891]
```

The IDs are mapped to vectors:

```text
ID
 ↓
Embedding
 ↓
Vector
```

After positional information is incorporated, the sequence becomes the input to the Transformer stack.

Then:

```text
Input Representation
        ↓
   Transformer
      Block 1
        ↓
   Transformer
      Block 2
        ↓
        ...
        ↓
   Transformer
      Block N
        ↓
Contextual Representations
```

The vectors are transformed at every layer.

---

# 20. 📤 Final Output

After the final Transformer block, the model has hidden representations.

These are passed to a **Language Model Head**.

```text
Final Hidden States
        ↓
Language Model Head
        ↓
Logits
        ↓
Probability Distribution
        ↓
Next Token
```

The language model head maps the hidden representation to scores for the vocabulary.

---

# 21. 📊 Logits

Suppose the vocabulary contains:

```text
50,000 tokens
```

The output layer can produce approximately:

```text
50,000 logits
```

for the relevant prediction position.

Example:

```text
Token        Logit
-------------------
cat          2.1
dog          4.3
running      1.7
sleeping     5.2
...
```

Logits are **raw scores**.

They are not probabilities yet.

---

# 22. 🎲 Probability Distribution

The logits can be converted into probabilities using softmax.

Conceptually:

```text
Logits
  ↓
Softmax
  ↓
Probabilities
```

Example:

```text
cat        → 0.05
dog        → 0.10
sleeping   → 0.70
running    → 0.15
```

The probabilities form a distribution over the vocabulary.

During actual generation, techniques such as temperature, top-k, or top-p can modify the logits or candidate set before selecting the next token.

---

# 23. 🔁 Complete Generation Loop

Suppose the prompt is:

```text
"Artificial intelligence is"
```

The process is:

```text
Prompt
  ↓
Tokenization
  ↓
Token IDs
  ↓
Embeddings + Positional Information
  ↓
Decoder-Only Transformer
  ↓
Logits
  ↓
Probability Distribution
  ↓
Select Next Token
  ↓
Add Token to Sequence
  ↓
Run Again
  ↓
Select Next Token
  ↓
Add Token
  ↓
...
```

For example:

```text
Artificial intelligence is
            ↓
        changing
            ↓
Artificial intelligence is changing
            ↓
        the
            ↓
Artificial intelligence is changing the
            ↓
        world
```

This is the autoregressive generation process.

---

# 24. 🏋️ Decoder-Only Architecture During Training

During training, the model receives token sequences and learns to predict the next token.

Example:

```text
Input:
The cat is

Target:
cat is sleeping
```

More generally:

```text
Input positions:

The | cat | is | sleeping

Targets:

cat | is | sleeping | ...
```

The model processes the sequence using causal masking.

Importantly, training can process many positions in parallel.

```text
The       → predict cat
The cat   → predict is
The cat is → predict sleeping
```

The causal mask prevents each position from accessing future target information.

---

# 25. 🚀 Decoder-Only Architecture During Inference

During inference, the model generates tokens one by one.

Example:

```text
Prompt:
The cat

        ↓

Predict:
is

        ↓

The cat is

        ↓

Predict:
sleeping

        ↓

The cat is sleeping
```

Unlike training, generation is naturally sequential because each newly generated token becomes part of the context for the next prediction.

---

# 26. ⚡ KV Cache

During autoregressive generation, the model repeatedly processes an expanding sequence.

Recomputing all previous attention keys and values every time would be inefficient.

A **KV cache** stores previously computed:

```text
Keys (K)
Values (V)
```

Then, when a new token arrives:

```text
Previous K/V
      +
New K/V
      ↓
Attention for new token
```

The cache stores K and V, not Q.

Conceptually:

```text
Token 1 → K₁, V₁
Token 2 → K₂, V₂
Token 3 → K₃, V₃
...
```

When generating the next token, previously computed K/V values can be reused.

---

# 27. 🆚 Decoder-Only vs Encoder-Only

These architectures have different purposes.

| Feature               | Encoder-Only                       | Decoder-Only                      |
| --------------------- | ---------------------------------- | --------------------------------- |
| Main purpose          | Understanding/representation tasks | Autoregressive generation         |
| Attention             | Usually bidirectional              | Causal                            |
| Future tokens         | Can normally attend to them        | Cannot attend to future positions |
| Next-token generation | Not the usual objective            | Core objective                    |
| Example               | BERT                               | GPT-style models                  |
| Separate decoder      | No                                 | No separate encoder               |
| Generation            | Not the primary design             | Primary capability                |

These are architectural tendencies rather than absolute rules for every model.

---

# 28. 🆚 Decoder-Only vs Encoder-Decoder

The original Transformer uses:

```text
Encoder
   ↓
Encoder Representations
   ↓
Decoder
   ↓
Output
```

A decoder-only LLM uses:

```text
Input
  ↓
Decoder-Only Stack
  ↓
Output
```

The major difference is the separate Encoder and cross-attention pathway.

| Feature                   | Encoder-Decoder      | Decoder-Only         |
| ------------------------- | -------------------- | -------------------- |
| Encoder                   | ✅                    | ❌                    |
| Decoder                   | ✅                    | Decoder-style blocks |
| Cross-attention           | Usually ✅            | ❌                    |
| Causal self-attention     | In decoder           | ✅                    |
| Autoregressive generation | Usually decoder      | ✅                    |
| Example use               | Translation, seq2seq | Text generation      |

---

# 29. 🧩 Original Decoder vs Decoder-Only LLM

This distinction is important.

The **original Transformer Decoder** contains:

```text
Masked Self-Attention
        ↓
Cross-Attention
        ↓
Feed-Forward Network
```

A decoder-only LLM generally contains:

```text
Causal Self-Attention
        ↓
Feed-Forward Network
```

There is no separate Encoder output to attend to.

Therefore:

```text
Decoder-only
≠
Original Decoder copied exactly
```

It is better understood as a Transformer architecture built around decoder-style causal blocks without a separate Encoder/cross-attention pathway.

---

# 30. 🧠 Why Decoder-Only Works Well for LLMs

Language generation naturally follows:

```text
Previous Tokens
      ↓
Next Token
```

Decoder-only architecture matches this objective directly.

For example:

```text
I love machine
```

The model predicts:

```text
learning
```

Then:

```text
I love machine learning
```

The model predicts another token.

This makes the architecture naturally suitable for autoregressive language modeling.

---

# 31. 🧮 Simplified Mathematical Flow

Let the tokenized input be:

```text
X
```

Token embeddings and positional information produce an initial representation:

```text
H₀
```

The Transformer blocks repeatedly transform it:

```text
H₁ = Block₁(H₀)
H₂ = Block₂(H₁)
H₃ = Block₃(H₂)
...
Hₙ = Blockₙ(Hₙ₋₁)
```

The final representation is:

```text
Hₙ
```

The language model head produces logits:

```text
Z = HₙW + b
```

Then:

```text
P = softmax(Z)
```

where:

```text
P
```

represents the probability distribution over vocabulary tokens.

The next token is selected according to the chosen decoding strategy.

---

# 32. 🗺️ Complete Decoder-Only Architecture

The complete simplified flow is:

```text
                    Text
                     ↓
                Tokenization
                     ↓
                  Token IDs
                     ↓
              Token Embeddings
                     ↓
          Positional Information
                     ↓
              ┌─────────────┐
              │ Decoder     │
              │ Block 1     │
              │             │
              │ Causal      │
              │ Self-       │
              │ Attention   │
              │      ↓      │
              │     FFN     │
              └─────────────┘
                     ↓
              ┌─────────────┐
              │ Decoder     │
              │ Block 2     │
              └─────────────┘
                     ↓
                     .
                     .
                     .
                     ↓
              ┌─────────────┐
              │ Decoder     │
              │ Block N     │
              └─────────────┘
                     ↓
             Final Hidden States
                     ↓
              Language Model Head
                     ↓
                   Logits
                     ↓
                  Softmax
                     ↓
             Probability Distribution
                     ↓
               Next Token
                     ↓
             Add to Sequence
                     ↓
                  Repeat
```

---

# 33. 🧠 Simple Mental Model

Think of a decoder-only LLM as a **deep stack of token-processing blocks**.

Each block:

```text
Looks at allowed previous context
            ↓
Mixes information using attention
            ↓
Transforms information using FFN
            ↓
Passes the result to the next block
```

After many blocks:

```text
Contextual Representation
          ↓
      Prediction
          ↓
      Next Token
```

Then the new token becomes part of the context.

---

# 34. ⚠️ Common Misunderstandings

### ❌ "Decoder-only means the model has only one Transformer block."

No.

A decoder-only LLM usually contains **many stacked Transformer blocks**.

---

### ❌ "Decoder-only means the model cannot understand the input."

No.

The Transformer blocks build contextual representations of the input.

The architecture is designed primarily around autoregressive language modeling.

---

### ❌ "The decoder can only look at the immediately previous token."

No.

A token can attend to **all allowed previous tokens**, including itself.

For example:

```text
The cat is sleeping
```

The token `sleeping` can attend to:

```text
The
cat
is
sleeping
```

---

### ❌ "Causal masking removes future tokens from the input."

No.

The tokens remain in the sequence.

The mask only prevents certain attention connections.

---

### ❌ "Decoder-only means there is no attention."

The opposite.

Causal self-attention is one of its core components.

---

### ❌ "Every decoder-only model has exactly the same architecture."

No.

Different models can differ in:

* Number of layers
* Hidden dimension
* Number of attention heads
* Attention implementation
* Positional method
* Normalization
* FFN design
* Vocabulary
* Context length
* Other architectural details

The overall decoder-only idea remains similar.

---

# 35. 🔗 Important Components

The main components can be remembered as:

```text
Tokenization
     ↓
Token IDs
     ↓
Embeddings
     ↓
Positional Information
     ↓
Causal Self-Attention
     ↓
Feed-Forward Network
     ↓
Residual Connections
     ↓
Layer Normalization
     ↓
Many Transformer Blocks
     ↓
Language Model Head
     ↓
Logits
     ↓
Next-Token Prediction
```

---

# 36. 🧠 One-Line Definition

> **A decoder-only architecture is a Transformer architecture that uses a stack of causal, decoder-style Transformer blocks to process token sequences and generate text autoregressively.**

---

# 37. 🎯 Key Takeaways

* 🧠 Decoder-only is a major architecture used for generative LLMs.
* 🚫 It does not contain a separate Encoder stack.
* 👀 It uses causal self-attention.
* 🎭 Causal masking prevents access to future positions.
* 🧱 Multiple Transformer blocks are stacked together.
* 🔍 Attention mixes information between token positions.
* ⚙️ FFNs transform representations at each position.
* ➕ Residual connections and normalization help build deep networks.
* 📤 The final representation is passed to a language model head.
* 📊 The output layer produces logits over the vocabulary.
* 🎲 Probabilities are used to select the next token.
* 🔁 Generated tokens are added back to the sequence.
* ⚡ KV caching improves autoregressive inference efficiency.
* 🔄 The core generation loop is:

```text
Context
  ↓
Decoder-Only Transformer
  ↓
Next Token
  ↓
Add Token to Context
  ↓
Repeat
```

The central idea is simple:

```text
Previous Tokens
      ↓
Causal Transformer
      ↓
Predict Next Token
      ↓
Add Token
      ↓
Predict Again
```
