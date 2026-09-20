# 🏗️ Transformer Architecture

A **Transformer** is a neural network architecture built to process sequences using **attention** and a collection of repeated components called **Transformer Blocks**.

The Transformer architecture was introduced in the paper **"Attention Is All You Need"** in 2017.

It became the foundation for many modern AI systems, especially large language models.

A simplified Transformer architecture looks like this:

```text id="7m4k2p"
📝 Input
   ↓
🔤 Tokenization
   ↓
🔢 Token IDs
   ↓
🧩 Embeddings
   ↓
📍 Positional Information
   ↓
🔄 Transformer Blocks
   ↓
📊 Final Representation
   ↓
🎯 Output Layer
   ↓
📈 Prediction
```

---

# 1. 🧠 What Is Transformer Architecture?

**Transformer architecture** is the overall design that defines how a Transformer processes input and transforms it into an output.

It contains several important components:

```text id="x8v3qk"
🏗️ Transformer
     │
     ├── 🧩 Input Representation
     │
     ├── 📍 Positional Information
     │
     ├── 👀 Attention
     │
     ├── 🧠 Feed-Forward Network
     │
     ├── ➕ Residual Connections
     │
     ├── 📏 Layer Normalization
     │
     └── 🎯 Output
```

These components work together to transform the input sequence.

---

# 2. 📜 The Original Transformer

The original Transformer architecture was introduced in 2017 in:

> **Attention Is All You Need**

The original architecture contained two major parts:

```text id="n5c8za"
             Transformer
                 │
        ┌────────┴────────┐
        ↓                 ↓
   🧠 Encoder          🎯 Decoder
```

The **encoder** processes the input sequence.

The **decoder** generates the output sequence.

This is called an **encoder-decoder Transformer**.

---

# 3. 🧩 Main Components of a Transformer

A Transformer contains several major components.

| Component                 | Main Purpose                           |
| ------------------------- | -------------------------------------- |
| 🔤 Tokenization           | Converts text into tokens              |
| 🔢 Token IDs              | Represents tokens numerically          |
| 🧩 Embeddings             | Converts IDs into vectors              |
| 📍 Positional Information | Represents token positions             |
| 👀 Attention              | Connects information between positions |
| 🧠 Feed-Forward Network   | Transforms token representations       |
| ➕ Residual Connection     | Helps information flow through layers  |
| 📏 Layer Normalization    | Helps stabilize computations           |
| 🔄 Transformer Blocks     | Repeated processing units              |
| 🎯 Output Layer           | Produces final predictions             |

Not every Transformer implementation uses exactly the same structure or ordering.

---

# 4. 📝 Input to the Transformer

A Transformer does not directly receive raw human text.

For example:

```text id="4j7q3s"
The cat is sleeping.
```

The text first goes through tokenization:

```text id="2x8m6p"
["The", "cat", "is", "sleeping", "."]
```

Then tokens are converted into Token IDs:

```text id="8q1v5n"
[125, 842, 91, 731, 18]
```

Then Token IDs are mapped to embeddings.

```text id="h6t3pz"
Token IDs
    ↓
🧩 Token Embeddings
    ↓
📍 Positional Information
    ↓
Transformer
```

---

# 5. 🧩 Token Embeddings

Each Token ID is mapped to a learned vector.

For example:

```text id="3s7m2k"
"cat"
  ↓
Token ID: 842
  ↓
Embedding:
[0.21, -0.14, 0.72, ...]
```

The actual embedding contains many numerical values.

The embedding represents the token in a numerical form that the neural network can process.

A simplified embedding matrix is:

```text id="5q9v2x"
Vocabulary
    ↓
┌───────────────────────────┐
│ Token 1 → Vector          │
│ Token 2 → Vector          │
│ Token 3 → Vector          │
│ Token 4 → Vector          │
│ ...                       │
└───────────────────────────┘
```

---

# 6. 📍 Positional Information

Transformers need information about the position of tokens.

Consider:

```text id="f8m3qz"
Dog bites man.
```

and:

```text id="k2v7xp"
Man bites dog.
```

The same tokens appear, but the order is different.

Therefore, the model needs positional information.

Conceptually:

```text id="p4x8sn"
Token Embedding
       +
Position Information
       ↓
Transformer Input
```

Different Transformer architectures can use different positional methods.

Examples include:

* Learned positional embeddings
* Sinusoidal positional encoding
* Rotary Position Embeddings (RoPE)

---

# 7. 👀 Attention

Attention is one of the most important parts of the Transformer.

It allows token representations to interact with other positions.

For example:

```text id="v6n2qb"
The cat sat on the mat.
```

When processing one token, attention can determine which other token representations are relevant.

Conceptually:

```text id="y9k4ms"
The  ─────┐
cat ──────┤
sat ──────┤
on ───────┤──→ 👀 Attention
the ──────┤
mat ──────┘
```

Attention produces updated representations containing information gathered from other positions.

---

# 8. 🔍 Self-Attention

When attention is calculated between tokens within the same sequence, it is called **self-attention**.

For example:

```text id="q7m3xa"
The cat sat on the mat.
```

The tokens can interact with each other through self-attention.

A simplified view:

```text id="s4p8nd"
Token Representations
        ↓
   Self-Attention
        ↓
Contextual Representations
```

Self-attention is a fundamental part of Transformer Blocks.

---

# 9. 🔑 Query, Key, and Value

Self-attention uses three representations:

```text id="d8q2mz"
🔎 Query
🔑 Key
📦 Value
```

A simplified interpretation is:

```text id="h4x9cp"
Query
  ↓
"What information am I looking for?"

Key
  ↓
"What information do I contain?"

Value
  ↓
"What information should I provide?"
```

Attention compares queries and keys to calculate attention scores.

The values are then combined according to those scores.

The standard scaled dot-product attention operation is:

```text id="z5n8vr"
Attention(Q, K, V)
=
softmax(QKᵀ / √dₖ)V
```

For causal attention, the future positions are masked before the softmax operation.

---

# 10. 🧠 Multi-Head Attention

A Transformer does not necessarily use only one attention operation.

It can use **multiple attention heads**.

Conceptually:

```text id="w3f7kx"
                 Input
                   ↓
        ┌──────────┼──────────┐
        ↓          ↓          ↓
     👀 Head 1  👀 Head 2  👀 Head 3
        ↓          ↓          ↓
        └──────────┼──────────┘
                   ↓
               🔗 Combine
                   ↓
                Output
```

Each head can learn different patterns of relationships.

For example, different heads may learn patterns involving:

* Nearby tokens
* Long-distance relationships
* Syntactic relationships
* Other contextual patterns

These examples are conceptual. The exact behavior of attention heads is learned during training.

---

# 11. 🧠 Feed-Forward Network

After attention, Transformer Blocks contain a **Feed-Forward Network (FFN)**.

Its role is different from attention.

```text id="m7x2qa"
👀 Attention
     ↓
Mixes information between token positions

🧠 Feed-Forward Network
     ↓
Transforms information at each position
```

A simplified FFN is:

```text id="v5p9ks"
Input
  ↓
Linear Transformation
  ↓
Activation Function
  ↓
Linear Transformation
  ↓
Output
```

Modern architectures may use activation functions and gated variants such as GELU or SwiGLU-like structures.

---

# 12. ➕ Residual Connections

Transformer Blocks use residual connections to help information flow through the network.

A simplified representation is:

```text id="n8r4yc"
Input ───────────────────┐
  ↓                      │
Attention                │
  ↓                      │
Transformed Information  │
  ↓                      │
       ➕ ←───────────────┘
  ↓
Output
```

The input can be combined with the transformed output.

Residual connections are especially useful when many Transformer Blocks are stacked.

---

# 13. 📏 Layer Normalization

Transformer architectures also commonly use **Layer Normalization**.

It helps stabilize the values flowing through the network.

Conceptually:

```text id="c6m2vx"
Representation
      ↓
📏 Layer Normalization
      ↓
Normalized Representation
```

The exact placement of Layer Normalization can differ between architectures.

---

# 14. 🔄 Transformer Block

The Transformer Block is the main repeated unit inside a Transformer.

A simplified block is:

```text id="a3q7mn"
📊 Input
   ↓
👀 Self-Attention
   ↓
➕ Residual Connection
   ↓
📏 Layer Normalization
   ↓
🧠 Feed-Forward Network
   ↓
➕ Residual Connection
   ↓
📏 Layer Normalization
   ↓
📊 Output
```

Some architectures use a different ordering, such as normalization before the attention and FFN sublayers.

The exact implementation varies.

---

# 15. 📚 Stacking Transformer Blocks

One Transformer Block is usually not enough for a large model.

Multiple blocks are stacked together.

```text id="r9v4ks"
Input
  ↓
🔄 Transformer Block 1
  ↓
🔄 Transformer Block 2
  ↓
🔄 Transformer Block 3
  ↓
🔄 Transformer Block 4
  ↓
      ...
  ↓
🔄 Transformer Block N
  ↓
Final Representation
```

Every block receives the representation from the previous block.

---

# 16. 🧠 Contextual Representations

The representation of a token changes as it passes through Transformer Blocks.

For example:

```text id="x4p8nz"
Token Embedding
      ↓
Transformer Block 1
      ↓
Contextual Representation
      ↓
Transformer Block 2
      ↓
More Contextual Representation
      ↓
Transformer Block 3
      ↓
Further Transformed Representation
```

This allows the network to build increasingly complex representations.

The model does not simply store one fixed meaning for every token.

The representation depends on context and the processing performed by the network.

---

# 17. 🏗️ Original Encoder-Decoder Architecture

The original Transformer contains an encoder and a decoder.

```text id="m8q2vy"
             Input
               ↓
        🧠 Encoder Stack
               ↓
       Encoder Representations
               ↓
        🎯 Decoder Stack
               ↓
             Output
```

The encoder processes the input sequence.

The decoder generates the output sequence.

The decoder can use information from the encoder through attention.

---

# 18. 🧠 Encoder

The encoder contains multiple encoder blocks.

A simplified structure is:

```text id="q6v3mx"
Input Embeddings
      ↓
Encoder Block 1
      ↓
Encoder Block 2
      ↓
Encoder Block 3
      ↓
...
      ↓
Encoder Block N
      ↓
Encoder Output
```

The encoder is designed to build representations of the input sequence.

---

# 19. 🎯 Decoder

The original Transformer decoder also contains multiple blocks.

A simplified decoder block includes:

```text id="s2k8vf"
Masked Self-Attention
        ↓
Cross-Attention
        ↓
Feed-Forward Network
        ↓
Output
```

The decoder's self-attention is masked so that a position cannot use future target tokens during autoregressive generation.

The decoder can also attend to encoder representations through **cross-attention**.

---

# 20. 🔗 Cross-Attention

Cross-attention allows the decoder to use information produced by the encoder.

A simplified view is:

```text id="n4x7pz"
Encoder Output
      │
      │
      ↓
   🔗 Cross-Attention
      ↑
      │
Decoder Representation
```

This is an important part of the original encoder-decoder Transformer.

It is different from self-attention, where queries, keys, and values come from the same sequence representation.

---

# 21. 🤖 Decoder-Only Transformer

Many modern LLMs use a **decoder-only Transformer**.

Examples include GPT-style architectures.

A simplified architecture is:

```text id="w7m3qx"
📝 Input Text
      ↓
🔤 Tokenization
      ↓
🔢 Token IDs
      ↓
🧩 Token Embeddings
      ↓
📍 Positional Information
      ↓
🔄 Decoder Block 1
      ↓
🔄 Decoder Block 2
      ↓
🔄 Decoder Block 3
      ↓
       ...
      ↓
🔄 Decoder Block N
      ↓
📊 Final Representation
      ↓
🎯 Language Modeling Head
      ↓
📈 Logits
      ↓
🔤 Next Token
```

These models use **causal self-attention**.

---

# 22. 🔒 Causal Self-Attention

In a decoder-only language model, each position can attend only to the current and previous positions.

For example:

```text id="k5n8rx"
Token 1 → Token 1

Token 2 → Token 1, Token 2

Token 3 → Token 1, Token 2, Token 3

Token 4 → Token 1, Token 2, Token 3, Token 4
```

Future tokens are masked.

This allows the model to learn next-token prediction without seeing the future answer.

---

# 23. 🎯 Output Layer

After the Transformer Blocks, the final representation is passed to an output layer.

For a language model:

```text id="b6x9mq"
Final Representation
        ↓
🎯 Language Modeling Head
        ↓
📈 Logits
        ↓
🎲 Probability Distribution
        ↓
🔤 Next Token
```

The output dimension corresponds to the vocabulary size.

For example, if a vocabulary contains:

```text
50,000 tokens
```

the model can produce a score for each of those tokens.

---

# 24. 📈 Logits

The output layer produces **logits**.

Logits are raw scores for possible output tokens.

For example:

```text id="q8m3vz"
Token       Logit
------------------
"cat"       2.1
"dog"       1.8
"car"       0.4
"tree"     -0.7
```

These numbers are not probabilities.

A softmax operation can convert them into a probability distribution.

```text id="z4p7kx"
Logits
  ↓
Softmax
  ↓
Probabilities
```

---

# 25. 🔁 Autoregressive Generation

Decoder-only language models generate text one token at a time.

For example:

```text id="j8x2mq"
The sky
   ↓
The sky is
   ↓
The sky is blue
   ↓
The sky is blue today
```

The process is:

```text id="t5n9vc"
📝 Prompt
   ↓
🔤 Tokens
   ↓
🔄 Transformer
   ↓
📈 Logits
   ↓
🎲 Token Selection
   ↓
🔤 New Token
   ↓
➕ Add to Context
   ↓
🔄 Transformer Again
   ↓
Repeat
```

---

# 26. 🏗️ Complete Transformer Architecture

A high-level view of a Transformer-based language model is:

```text id="f3v7qa"
                    📝 Text
                       ↓
                 🔤 Tokenization
                       ↓
                  🔢 Token IDs
                       ↓
                 🧩 Embeddings
                       ↓
              📍 Positional Information
                       ↓
             ┌─────────────────────┐
             │ 🔄 Transformer      │
             │                     │
             │ 👀 Attention        │
             │ ➕ Residual         │
             │ 📏 Normalization    │
             │ 🧠 Feed-Forward     │
             │                     │
             └─────────────────────┘
                       ↓
                 🔄 Repeat Blocks
                       ↓
              📊 Final Representation
                       ↓
                🎯 Output Layer
                       ↓
                   📈 Logits
                       ↓
              🎲 Probability Distribution
                       ↓
                  🔤 Next Token
```

---

# 27. 🆚 Encoder-Decoder vs Decoder-Only

| Feature               | Encoder-Decoder            | Decoder-Only                     |
| --------------------- | -------------------------- | -------------------------------- |
| Encoder               | ✅ Yes                      | ❌ No                             |
| Decoder               | ✅ Yes                      | ✅ Yes                            |
| Cross-attention       | ✅ Yes                      | Usually ❌                        |
| Causal self-attention | Decoder side               | ✅ Yes                            |
| Input processing      | Encoder                    | Decoder stack                    |
| Typical use           | Sequence-to-sequence tasks | Autoregressive language modeling |
| Example family        | Original Transformer       | GPT-style models                 |

This distinction is important because the word **"decoder"** in "decoder-only Transformer" refers to the architecture, not simply to a text-decoding step.

---

# 28. 🧩 Transformer Architecture at Different Levels

The architecture can be understood at different levels.

### Level 1 — Complete Model

```text
Input
 ↓
Transformer
 ↓
Output
```

### Level 2 — Transformer Stack

```text
Input
 ↓
Block 1
 ↓
Block 2
 ↓
...
 ↓
Block N
 ↓
Output
```

### Level 3 — Transformer Block

```text
Attention
 ↓
Residual
 ↓
Normalization
 ↓
FFN
 ↓
Residual
 ↓
Normalization
```

### Level 4 — Attention

```text
Query
 ↓
Compare with Keys
 ↓
Attention Weights
 ↓
Combine Values
 ↓
Output
```

Each level explains a different amount of detail.

---

# 29. 🔄 Complete Data Flow

Let's connect everything together.

```text id="p9v3kx"
📝 Human Text
      ↓
🔤 Tokenization
      ↓
🔢 Token IDs
      ↓
🧩 Token Embeddings
      ↓
📍 Positional Information
      ↓
🔄 Transformer Block
      │
      ├── 👀 Self-Attention
      │
      ├── ➕ Residual Connection
      │
      ├── 📏 Layer Normalization
      │
      ├── 🧠 Feed-Forward Network
      │
      ├── ➕ Residual Connection
      │
      └── 📏 Layer Normalization
      ↓
🔄 More Transformer Blocks
      ↓
📊 Final Representation
      ↓
🎯 Output / Language Modeling Head
      ↓
📈 Logits
      ↓
🎲 Probability Distribution
      ↓
🔤 Output Token
```

---

# 30. 🏋️ Transformer Architecture During Training

During training, the Transformer processes training sequences and learns its parameters.

A simplified flow is:

```text id="y4m8qs"
📚 Training Data
      ↓
🔤 Tokenization
      ↓
🔢 Token IDs
      ↓
🧩 Embeddings
      ↓
📍 Position Information
      ↓
🔄 Transformer Blocks
      ↓
🎯 Prediction
      ↓
📉 Loss
      ↓
🔄 Backpropagation
      ↓
⚙️ Parameter Updates
      ↓
🔁 Repeat
```

The model's parameters are adjusted to reduce the training loss.

---

# 31. ⚡ Transformer Architecture During Inference

During inference, the trained parameters are used to process an input and produce predictions.

```text id="u8q2mz"
📝 Prompt
   ↓
🔤 Tokenization
   ↓
🔢 Token IDs
   ↓
🧩 Embeddings
   ↓
📍 Position Information
   ↓
🔄 Transformer Blocks
   ↓
📊 Final Representation
   ↓
🎯 Output Layer
   ↓
📈 Logits
   ↓
🎲 Token Selection
   ↓
🔤 Generated Token
```

The selected token can then be added to the context and the process repeated.

---

# 32. ⚠️ Transformer Architecture Is Not One Fixed Design

It is important to understand that **"Transformer" does not mean every model has exactly the same architecture**.

Different Transformer-based models can change:

* Number of layers
* Hidden dimension
* Number of attention heads
* Attention implementation
* Positional method
* Normalization method
* FFN structure
* Activation function
* Residual/normalization ordering
* Encoder/decoder configuration
* Output projection

Therefore, the diagrams in this file are **conceptual representations** of the architecture.

---

# 33. 🧠 Transformer vs Transformer Block

These terms are related but different.

### Transformer

The complete architecture:

```text id="q6z3vn"
Input
 ↓
Block 1
 ↓
Block 2
 ↓
Block 3
 ↓
...
 ↓
Block N
 ↓
Output
```

### Transformer Block

One repeated unit:

```text id="k9m4xp"
Attention
   ↓
Residual
   ↓
Normalization
   ↓
FFN
   ↓
Residual
   ↓
Normalization
```

Therefore:

```text id="s8v2qa"
Transformer
   ↓
Contains multiple
Transformer Blocks
```

---

# 34. 🤖 Transformer vs LLM

A Transformer is an **architecture**.

An LLM is a **large language model**.

For example:

```text id="n3x7mz"
🏗️ Transformer
      ↓
Architecture

🧠 LLM
      ↓
Large-scale language model
      ↓
Often built using Transformer architecture
```

A Transformer can be used for many tasks beyond language.

An LLM specifically focuses on language modeling.

---

# 35. 🧠 Simple Mental Model

Think of a Transformer as a pipeline that repeatedly transforms information.

```text id="v4q8zn"
📝 Input
   ↓
🔢 Numerical Representation
   ↓
👀 Find Relationships
   ↓
🧠 Transform Information
   ↓
🔄 Repeat Many Times
   ↓
📊 Final Representation
   ↓
🎯 Produce Output
```

Inside each block:

```text id="x7m2kp"
👀 Attention
      ↓
"What information from other positions matters?"

       +

🧠 Feed-Forward Network
      ↓
"How should this representation be transformed?"

       +

➕ Residual + 📏 Normalization
      ↓
"Keep information flowing through the network."
```

---

# 36. 🔑 Key Takeaways

* 🏗️ A **Transformer** is a neural network architecture.
* 📜 The original Transformer was introduced in **2017** in *Attention Is All You Need*.
* 👀 **Attention** is a central mechanism of the architecture.
* 🔤 Text is converted into tokens before entering a language Transformer.
* 🔢 Tokens become Token IDs.
* 🧩 Token IDs are mapped to embeddings.
* 📍 Positional information represents token order.
* 👀 Self-attention allows token representations to interact.
* 🔑 Query, Key, and Value are fundamental parts of attention.
* 🧠 Feed-Forward Networks transform token representations.
* ➕ Residual connections help information flow through deep networks.
* 📏 Layer Normalization helps stabilize the network.
* 🔄 Transformer Blocks are stacked to create deeper models.
* 🧠 The original Transformer used an **encoder-decoder** architecture.
* 🤖 Many modern LLMs use **decoder-only Transformers**.
* 🔒 Decoder-only LLMs use **causal self-attention** for autoregressive prediction.
* 🎯 The output layer converts final representations into vocabulary logits.
* 🔁 During generation, tokens are predicted and added to the context repeatedly.
* ⚠️ Transformer architectures vary between models; there is no single implementation that fits every Transformer.
* 🧠 **Transformer = architecture, Transformer Block = repeated building unit, Attention = important mechanism inside the block.**
