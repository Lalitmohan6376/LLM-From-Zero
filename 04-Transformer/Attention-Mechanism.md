# 👀 Attention Mechanism

The **Attention Mechanism** is one of the most important ideas behind the Transformer architecture.

It allows a model to determine **which other tokens are relevant when processing a particular token**.

Instead of treating every token independently, attention allows token representations to interact with each other.

A simplified idea is:

```text
📝 Input Sequence
      ↓
👀 Attention
      ↓
🔗 Token Relationships
      ↓
📊 Updated Representations
```

In Transformer-based LLMs, attention is used to build **context-aware representations** of tokens.

---

# 1. 🧠 What Is Attention?

Attention is a mechanism that allows each token to **look at other relevant token positions** and use information from them.

For example:

```text
The cat sat on the mat.
```

When processing one token, information from other tokens may be useful.

The attention mechanism helps determine:

```text
Which tokens are relevant?
        ↓
How much should each token contribute?
        ↓
What information should be combined?
```

The result is an updated representation for each token.

---

# 2. 🤔 Why Do We Need Attention?

A token by itself may not contain enough information to understand its role in a sentence.

Consider:

```text
The animal didn't cross the road because it was tired.
```

The word:

```text
"it"
```

can be related to another part of the sentence.

Attention allows the model to create relationships between different positions.

Conceptually:

```text
The animal didn't cross the road because it was tired.
      ↑                                      ↑
      └──────────── relationship ────────────┘
```

The exact relationships learned by a model depend on its training, architecture, layer, attention head, and input.

---

# 3. 🔗 Tokens Can Interact With Other Tokens

Without attention, a token representation would have limited access to information from other positions.

With attention:

```text
Token 1 ───────→ Token 2
   │                │
   ├──────────────→ Token 3
   │                │
   └──────────────→ Token 4
```

Each token can use information from other allowed positions.

For example:

```text
The cat sat on the mat.
```

can be represented conceptually as:

```text
The  ↔ cat
The  ↔ sat
cat  ↔ sat
cat  ↔ mat
sat  ↔ mat
...
```

These relationships are represented numerically through attention scores and weights.

---

# 4. 🎯 Attention Does Not Treat Every Token Equally

Attention does not simply give every token the same amount of importance.

Instead, it calculates different weights.

For example:

```text
Token        Attention Weight
-----------------------------
The              0.05
cat              0.15
sat              0.50
on               0.10
the              0.05
mat              0.15
```

These numbers are only illustrative.

Actual attention weights depend on the model and input.

The important idea is:

```text
Different tokens
       ↓
Different attention weights
       ↓
Different contributions
```

---

# 5. 🧩 Attention Works on Representations

Attention does not directly operate on raw words such as:

```text
"cat"
"dog"
"running"
```

The text first goes through earlier stages.

```text
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
👀 Attention
```

Therefore, attention operates on **numerical representations**.

---

# 6. 🔑 Query, Key, and Value

Attention commonly uses three representations:

```text
🔎 Query
🔑 Key
📦 Value
```

They are created from the input representation using learned transformations.

```text
X
│
├──→ WQ → Q
│
├──→ WK → K
│
└──→ WV → V
```

The simplified equations are:

```text
Q = XWQ

K = XWK

V = XWV
```

Their conceptual roles are:

| Component | Role                                           |
| --------- | ---------------------------------------------- |
| 🔎 Query  | Used to determine what information is relevant |
| 🔑 Key    | Used for matching against Queries              |
| 📦 Value  | Contains information that can be combined      |

The detailed Q/K/V process is covered separately in `Query-Key-Value.md`.

---

# 7. 📊 Attention Scores

The first major step is comparing Queries with Keys.

The standard calculation is:

```text
QKᵀ
```

This produces attention scores.

A simplified flow is:

```text
Query
  ↓
Compare with Keys
  ↓
Attention Scores
```

For every Query, the model calculates scores against the relevant Keys.

Higher scores indicate stronger numerical matches before normalization.

---

# 8. 📏 Scaling the Scores

The scores are scaled using the Key dimension:

```text
QKᵀ / √dₖ
```

where:

```text
dₖ = Key dimension
```

The scaling helps prevent the dot-product values from becoming too large as the dimensionality increases.

The flow becomes:

```text
QKᵀ
 ↓
Divide by √dₖ
 ↓
Scaled Attention Scores
```

---

# 9. 🎲 Softmax and Attention Weights

The scaled scores are passed through softmax.

```text
Scaled Scores
      ↓
    Softmax
      ↓
Attention Weights
```

Softmax converts the scores into a distribution.

For example:

```text
Score:
[1.0, 2.5, 0.5]

       ↓

Softmax:

[0.18, 0.67, 0.15]
```

The numbers above are illustrative.

The weights indicate how strongly the corresponding Value vectors contribute to the output.

---

# 10. 📦 Combining the Values

After calculating attention weights, the model uses them to combine the Value vectors.

Conceptually:

```text
Attention Weight 1 × Value 1
+
Attention Weight 2 × Value 2
+
Attention Weight 3 × Value 3
        ↓
Attention Output
```

The complete operation is:

```text
Attention(Q, K, V)
=
softmax(QKᵀ / √dₖ)V
```

This is called **scaled dot-product attention**.

---

# 11. 🔄 Complete Attention Calculation

The complete basic process is:

```text
🧩 Input Representations
          ↓
     Linear Projections
          ↓
      ┌───┼───┐
      ↓   ↓   ↓
      Q   K   V
      │   │   │
      └───┼───┘
          ↓
        QKᵀ
          ↓
     Scale by √dₖ
          ↓
    Apply Mask if Needed
          ↓
       Softmax
          ↓
  Attention Weights
          ↓
      × Values
          ↓
   Attention Output
```

This output becomes the updated representation passed further through the Transformer.

---

# 12. 👀 Attention as Information Mixing

One useful way to understand attention is:

> **Attention mixes information from different token positions.**

Suppose a sequence contains:

```text
Token A
Token B
Token C
Token D
```

The representation of Token C can receive information from other allowed positions:

```text
Token A ──┐
Token B ──┤
Token C ──┼──→ Updated Token C
Token D ──┘
```

The amount contributed by each token depends on its attention weight.

---

# 13. 🧠 Contextual Representations

One of the important results of attention is the creation of **contextual representations**.

Consider the word:

```text
bank
```

It can appear in different contexts:

```text
I went to the bank to deposit money.

The boat reached the river bank.
```

The surrounding context is different.

Attention allows information from surrounding tokens to influence the representation.

```text
Token
  +
Context
  ↓
Contextual Representation
```

This is one reason Transformers can represent the same token differently depending on its context.

---

# 14. 🔄 Attention for Every Token

Attention is not calculated for only one token.

For a sequence:

```text
The cat sat on the mat.
```

the model calculates an attention output for every relevant position.

Conceptually:

```text
"The" → Attention → Updated representation

"cat" → Attention → Updated representation

"sat" → Attention → Updated representation

"on"  → Attention → Updated representation

"the" → Attention → Updated representation

"mat" → Attention → Updated representation
```

These updated representations continue through the Transformer Block.

---

# 15. 📐 Attention Matrix

When multiple Queries are compared with multiple Keys, the result can be represented as an **attention score matrix**.

For example:

```text
             Key
          1    2    3    4
       ┌────────────────────
Q  1   │ 0.2  0.5  0.2  0.1
u  2   │ 0.1  0.6  0.2  0.1
e  3   │ 0.3  0.2  0.4  0.1
r  4   │ 0.2  0.1  0.3  0.4
```

Each row corresponds to a Query.

Each column corresponds to a Key.

The values represent attention weights after normalization in this simplified example.

---

# 16. 🔒 Attention Masking

Sometimes the model should not be allowed to attend to certain positions.

A **mask** prevents those positions from contributing to attention.

For decoder-only LLMs, a **causal mask** is used.

Example:

```text
             Key Position
           1   2   3   4
        ┌─────────────────
Query 1 │ ✓   ✗   ✗   ✗
Query 2 │ ✓   ✓   ✗   ✗
Query 3 │ ✓   ✓   ✓   ✗
Query 4 │ ✓   ✓   ✓   ✓
```

Here:

```text
✓ = allowed
✗ = masked
```

This means a token cannot use information from future positions.

---

# 17. 🎯 Why Is Causal Masking Needed?

Decoder-only LLMs are commonly trained to predict the next token.

Consider:

```text
The sky is blue
```

Training targets can be thought of as:

```text
The
 ↓
sky

The sky
 ↓
is

The sky is
 ↓
blue
```

When predicting:

```text
blue
```

the model should not already have access to the target `"blue"`.

Therefore:

```text
Previous Tokens
      ↓
🔒 Causal Mask
      ↓
👀 Attention
      ↓
🎯 Next-Token Prediction
```

The mask is applied to the attention scores before softmax so that future positions do not contribute.

---

# 18. 🔗 Self-Attention

When the Query, Key, and Value representations come from the **same sequence**, the mechanism is called **self-attention**.

```text
Same Input
    │
 ┌──┼──┐
 ↓  ↓  ↓
 Q  K  V
    ↓
Self-Attention
```

For example:

```text
The cat sat on the mat.
```

The tokens attend to other tokens from the same sequence, subject to any mask.

Self-attention is the main attention mechanism used inside Transformer blocks.

---

# 19. 🌐 Cross-Attention

Cross-attention is different.

The Query comes from one representation, while the Key and Value come from another.

```text
Sequence A
    ↓
    Q

Sequence B
    ↓
 ┌──┴──┐
 K    V
```

A classic example is the original encoder-decoder Transformer.

```text
Encoder Output
      ↓
     K, V

Decoder
      ↓
      Q

      ↓
Cross-Attention
```

This allows the decoder to use information from the encoder.

---

# 20. 👀 Attention vs Self-Attention

These terms are related but should not always be treated as identical.

### Attention

A general mechanism for calculating weighted information from representations.

### Self-Attention

A type of attention where Q, K, and V come from the same sequence.

```text
Attention
   │
   ├── Self-Attention
   │
   └── Cross-Attention
```

The exact terminology can depend on the architecture and context.

---

# 21. 🔄 Attention Inside a Transformer Block

Attention is one major component of a Transformer Block.

A simplified block is:

```text
📊 Input Representation
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
📊 Output Representation
```

The exact ordering of normalization and residual operations can vary across Transformer architectures.

---

# 22. 🧠 Attention Is Not the Entire Transformer

A common misunderstanding is:

```text
Transformer = Attention
```

This is not correct.

Attention is one important component of a Transformer.

A simplified Transformer Block contains:

```text
👀 Attention
      +
🧠 Feed-Forward Network
      +
➕ Residual Connections
      +
📏 Layer Normalization
```

Therefore:

```text
Attention ≠ Transformer

Attention → One major component of a Transformer
```

---

# 23. 🔄 Multi-Head Attention

Transformers commonly use **Multi-Head Attention**.

Instead of performing one attention operation, the model performs multiple attention operations in parallel.

Conceptually:

```text
Input
  │
  ├──→ 👀 Attention Head 1
  │
  ├──→ 👀 Attention Head 2
  │
  ├──→ 👀 Attention Head 3
  │
  └──→ 👀 Attention Head 4
              ↓
       Combine Outputs
              ↓
       Output Projection
```

Different heads can learn different patterns of relationships.

For example, different heads may learn useful relationships involving syntax, nearby tokens, or longer-range dependencies, but the exact behavior is learned rather than manually assigned.

---

# 24. 🧩 Attention and Positional Information

Attention needs information about token positions because word order matters.

Consider:

```text
The dog chased the cat.
```

and:

```text
The cat chased the dog.
```

The same words appear, but their order is different.

The Transformer therefore uses some form of positional information.

```text
Token Embeddings
       +
Positional Information
       ↓
Transformer Representations
       ↓
Attention
```

Different architectures can implement positional information differently.

Examples include:

* Learned positional embeddings
* Sinusoidal positional encoding
* Rotary Position Embeddings (RoPE)

---

# 25. 🧠 Attention and Context

Attention helps each token representation incorporate information from other allowed positions.

This creates increasingly contextual representations as the data moves through Transformer blocks.

```text
Token Representations
        ↓
     Attention
        ↓
Contextual Representations
        ↓
   Next Transformer Block
        ↓
     Attention Again
        ↓
More Contextual Representations
```

Because Transformer blocks are stacked, this process happens repeatedly.

---

# 26. 🔢 Attention Shapes

Suppose:

```text
Sequence Length = 4
```

Then the attention score matrix can conceptually have shape:

```text
4 × 4
```

For a sequence of length `N`:

```text
Attention Scores
      ↓
N × N
```

Each Query can have a score against each Key position before masking.

For causal attention, some entries are masked.

For example:

```text
N = 4

      K1  K2  K3  K4
Q1    ✓   ✗   ✗   ✗
Q2    ✓   ✓   ✗   ✗
Q3    ✓   ✓   ✓   ✗
Q4    ✓   ✓   ✓   ✓
```

This quadratic relationship is one reason long sequences can require significant computation and memory.

---

# 27. ⚡ Attention During Training

During training, attention processes training sequences.

A simplified flow is:

```text
📚 Training Text
      ↓
🔤 Tokenization
      ↓
🔢 Token IDs
      ↓
🧩 Representations
      ↓
Q, K, V
      ↓
👀 Attention
      ↓
🔄 Transformer Blocks
      ↓
🎯 Prediction
      ↓
📉 Loss
      ↓
🔄 Backpropagation
```

The parameters involved in attention are updated through training.

---

# 28. ⚡ Attention During Inference

During inference, the trained parameters are used to process the input.

```text
📝 Prompt
   ↓
🔤 Tokens
   ↓
🧩 Representations
   ↓
Q, K, V
   ↓
👀 Attention
   ↓
🔄 Transformer Blocks
   ↓
🎯 Next-Token Prediction
```

For autoregressive generation, new tokens are added and the process continues.

---

# 29. ⚡ KV Cache During Generation

During autoregressive generation, the model can reuse previously calculated Keys and Values.

```text
Previous Tokens
      ↓
Previous K + V
      ↓
   KV Cache
      ↑
      │
New Token
      ↓
New Query
      ↓
Attention
      ↓
Next Token
```

This avoids recalculating the same previous Key and Value representations repeatedly.

The KV cache is an inference optimization, not a different attention mechanism.

---

# 30. 🧠 What Does Attention Actually Do?

A useful conceptual description is:

> **Attention determines how information from different token positions should be combined to update token representations.**

It does this through:

```text
Q
 ↓
Compare with K
 ↓
Attention Scores
 ↓
Softmax
 ↓
Attention Weights
 ↓
Weighted V
 ↓
Attention Output
```

It is therefore better to think of attention as **learned information mixing** rather than human-like attention or understanding.

---

# 31. ❌ Common Misunderstandings

### ❌ "Attention means the model understands the sentence."

Not necessarily.

Attention is a numerical mechanism for combining information.

---

### ❌ "The token with the highest attention weight is always the most important token."

Not necessarily.

Attention patterns can be distributed across multiple positions, and interpreting individual attention weights as a complete explanation of model behavior can be misleading.

---

### ❌ "Attention is the entire Transformer."

No.

Attention is one major component of a Transformer Block.

---

### ❌ "Every Transformer uses exactly the same attention design."

No.

Different architectures can use different attention variants and optimizations.

---

### ❌ "Attention always looks at every token."

Not necessarily.

Masks or other architectural constraints can restrict which positions can contribute.

---

# 32. 🧠 Attention vs Token Embeddings

These are different things.

| Token Embeddings                    | Attention                                  |
| ----------------------------------- | ------------------------------------------ |
| Initial numerical representation    | Mechanism for mixing information           |
| Maps token IDs to vectors           | Uses relationships between representations |
| Learned embedding parameters        | Uses learned projection parameters         |
| Comes before Transformer processing | Operates inside Transformer blocks         |
| Represents token information        | Creates updated contextual representations |

Simplified:

```text
Token ID
   ↓
Embedding
   ↓
Attention
   ↓
Contextual Representation
```

---

# 33. 🧠 Attention vs Feed-Forward Network

Attention and the Feed-Forward Network have different roles.

| Attention                                | Feed-Forward Network                               |
| ---------------------------------------- | -------------------------------------------------- |
| Mixes information across token positions | Transforms features at each position               |
| Uses Q, K, V                             | Uses learned linear transformations and activation |
| Creates relationships between positions  | Processes the resulting representation             |
| Part of attention sublayer               | Part of FFN sublayer                               |

Simplified:

```text
👀 Attention
Information across tokens
        ↓
🧠 Feed-Forward Network
Feature transformation
```

Both work together inside Transformer Blocks.

---

# 34. 🌐 Attention Through the LLM

A simplified decoder-only LLM pipeline is:

```text
📝 Text
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
   ├── 👀 Attention
   │
   ├── ➕ Residual
   │
   ├── 📏 Normalization
   │
   ├── 🧠 Feed-Forward Network
   │
   └── ➕ Residual + Normalization
   ↓
🔄 More Transformer Blocks
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

# 35. 🔄 Complete Attention Flow

The entire attention mechanism can be summarized as:

```text
🧩 Input Representations
          ↓
      Q, K, V
          ↓
   Compare Q with K
          ↓
    Attention Scores
          ↓
     Scale Scores
          ↓
   Apply Mask if Needed
          ↓
        Softmax
          ↓
  Attention Weights
          ↓
   Weighted Values
          ↓
   Attention Output
          ↓
📊 Updated Representations
```

Mathematically:

```text
Attention(Q, K, V)
=
softmax(QKᵀ / √dₖ)V
```

For causal attention:

```text
Attention(Q, K, V)
=
softmax((QKᵀ + Mask) / √dₖ)V
```

where the mask prevents forbidden positions from contributing.

---

# 36. 🧠 Simple Mental Model

Think of attention as a **learned information-sharing mechanism**.

```text
          👀 Attention
               │
      ┌────────┼────────┐
      ↓        ↓        ↓
   Token A  Token B  Token C
      │        │        │
      └────┬───┴───┬────┘
           ↓       ↓
       Relationships
             ↓
     Weighted Information
             ↓
   Updated Representations
```

The core idea is:

```text
🔎 Query
   +
🔑 Key
   ↓
📊 Attention Weight
   +
📦 Value
   ↓
🧠 Updated Representation
```

---

# 37. 🔑 Key Takeaways

* 👀 **Attention** allows token representations to interact with other relevant positions.
* 🔗 It helps the model combine information from different parts of a sequence.
* 🔎 Queries are compared with Keys to calculate attention scores.
* 📊 Scores are scaled and converted into attention weights.
* 📦 Values are combined using those weights.
* 📐 The standard scaled dot-product attention formula is:

```text
Attention(Q, K, V)
=
softmax(QKᵀ / √dₖ)V
```

* 🔒 Causal attention uses a mask to prevent future-token information from being used.
* 🔗 Self-attention uses Q, K, and V from the same sequence.
* 🌐 Cross-attention can use Q from one representation and K/V from another.
* 🔄 Attention is one major component of a Transformer Block, not the entire Transformer.
* 🧠 Attention helps create contextual representations.
* 🔄 Multiple Transformer Blocks repeatedly apply attention and other transformations.
* ⚡ KV caching can make autoregressive inference more efficient.
* 💡 Attention is best understood as **learned information mixing between token representations**.

```text
🧩 Representations
       ↓
     Q, K, V
       ↓
   Q compared with K
       ↓
 Attention Weights
       ↓
   Weighted Values
       ↓
 Attention Output
       ↓
Contextual Representations
```
