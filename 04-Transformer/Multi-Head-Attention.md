# 🧠 Multi-Head Attention

**Multi-Head Attention** is an attention mechanism that allows a Transformer to perform multiple attention operations in parallel.

Instead of having one attention process look at the relationships between tokens, Multi-Head Attention uses multiple **attention heads**.

Each head can learn to focus on different types of relationships or patterns in the input.

---

## 1. What Is Multi-Head Attention?

In simple attention, we calculate relationships between tokens using:

```text
Query (Q)
Key (K)
Value (V)
```

Multi-Head Attention performs this process multiple times in parallel.

Simplified idea:

```text
                Input
                  ↓
        ┌─────────┴─────────┐
        ↓         ↓         ↓
     Head 1     Head 2     Head 3     ... Head N
        ↓         ↓         ↓
        └─────────┬─────────┘
                  ↓
              Concatenate
                  ↓
          Output Projection
                  ↓
               Output
```

The goal is to allow different heads to learn different attention patterns.

---

# 2. Why Do We Need Multiple Heads?

A single attention operation has to represent many different relationships between tokens.

For example:

```text
The cat sat on the mat because it was tired.
```

Different relationships may exist between the tokens.

One attention head might learn a pattern related to:

```text
"it" → "cat"
```

Another might focus on:

```text
"sat" → "on"
```

Another might focus on:

```text
"tired" → "was"
```

These are only illustrative examples.

The actual patterns learned by attention heads depend on the model, training data, layer, and input.

Multi-Head Attention gives the model multiple parallel attention mechanisms instead of forcing everything through one attention calculation.

---

# 3. Single-Head Attention vs Multi-Head Attention

### Single-Head Attention

```text
Input
  ↓
Q, K, V
  ↓
Attention
  ↓
Output
```

### Multi-Head Attention

```text
Input
  ↓
Q, K, V
  ↓
┌───────┬───────┬───────┐
↓       ↓       ↓
Head 1  Head 2  Head 3  ... Head N
↓       ↓       ↓
└───────┴───────┴───────┘
          ↓
     Concatenate
          ↓
   Output Projection
          ↓
        Output
```

The main difference is that Multi-Head Attention performs attention in multiple smaller representation spaces.

---

# 4. What Is an Attention Head?

An **attention head** is one individual attention operation inside Multi-Head Attention.

Each head has its own Query, Key, and Value projections.

Conceptually:

```text
Input X
  ↓
┌─────────────────────────────┐
│                             │
├──→ Q₁, K₁, V₁ → Head 1      │
│                             │
├──→ Q₂, K₂, V₂ → Head 2      │
│                             │
├──→ Q₃, K₃, V₃ → Head 3      │
│                             │
└──→ Qₙ, Kₙ, Vₙ → Head N      │
```

Each head can therefore learn different transformations and attention patterns.

---

# 5. Where Does Multi-Head Attention Come From?

Multi-Head Attention starts with the input representation.

Suppose:

```text id="f3bqj2"
Input
   ↓
X
```

The model creates Query, Key, and Value representations.

For a particular head:

```text id="y8q1l8"
Q = XWQ
K = XWK
V = XWV
```

The projection matrices are learned during training.

For multiple heads, each head has its own projection parameters conceptually:

```text id="p7k6qx"
Head 1 → WQ₁, WK₁, WV₁
Head 2 → WQ₂, WK₂, WV₂
Head 3 → WQ₃, WK₃, WV₃
...
Head N → WQₙ, WKₙ, WVₙ
```

Actual implementations may combine these projections into larger matrices for efficiency.

---

# 6. One Head Performs Normal Attention

Each head performs scaled dot-product attention.

The standard formula is:

```text id="b6l0g4"
Attention(Q, K, V)
=
softmax(QKᵀ / √dₖ)V
```

For a particular head:

```text id="v2e8xw"
Q₁, K₁, V₁
      ↓
Attention
      ↓
Head Output 1
```

Another head:

```text id="7w1lru"
Q₂, K₂, V₂
      ↓
Attention
      ↓
Head Output 2
```

And so on.

---

# 7. Each Head Uses a Smaller Dimension

Suppose the model's hidden dimension is:

```text
d_model = 768
```

and there are:

```text
12 attention heads
```

A common conceptual arrangement is:

```text
768 ÷ 12 = 64
```

So each head works with:

```text
64 dimensions
```

Conceptually:

```text id="lqzq8u"
                 768
                  ↓
        ┌─────────┼─────────┐
        ↓         ↓         ↓
       64        64        64 ... 64
     Head 1    Head 2    Head 3 ... Head 12
```

This is an illustrative common configuration.

The exact dimensions and number of heads vary by model.

---

# 8. Why Split the Representation?

Instead of one attention operation working with the entire representation, the model divides the representation into multiple smaller spaces.

This allows different heads to learn different relationships.

Conceptually:

```text id="t9zq7x"
                    Input
                      ↓
              768-dimensional
                representation
                      ↓
       ┌──────┬──────┬──────┬──────┐
       ↓      ↓      ↓      ↓      ↓
      64     64     64     64     64 ...
      H1     H2     H3     H4     H5
```

Each head performs its own attention calculation.

---

# 9. Query, Key, and Value for Each Head

Each head produces its own Q, K, and V.

For example:

```text id="z0p7x5"
Head 1:

X → Q₁
X → K₁
X → V₁
```

```text id="d9q1kw"
Head 2:

X → Q₂
X → K₂
X → V₂
```

And:

```text id="e2x1pl"
Head N:

X → Qₙ
X → Kₙ
X → Vₙ
```

These projections are learned.

Therefore, different heads can transform the same input into different Q/K/V representations.

---

# 10. Attention Happens Independently in Each Head

Suppose there are three heads.

Each head performs:

```text id="r5k8hs"
Head 1:
Q₁, K₁, V₁
     ↓
Attention
     ↓
H₁
```

```text id="f8g4v2"
Head 2:
Q₂, K₂, V₂
     ↓
Attention
     ↓
H₂
```

```text id="x2k7pa"
Head 3:
Q₃, K₃, V₃
     ↓
Attention
     ↓
H₃
```

The calculations happen in parallel conceptually.

---

# 11. Attention Scores in Each Head

Every head calculates its own attention scores.

For Head 1:

```text id="k3p4sy"
Q₁K₁ᵀ
```

For Head 2:

```text id="z5h8vc"
Q₂K₂ᵀ
```

For Head 3:

```text id="u7k2pd"
Q₃K₃ᵀ
```

Therefore, different heads can produce different attention patterns.

Conceptually:

```text id="x8k5sa"
Head 1              Head 2              Head 3

[.8 .1 .1]          [.2 .7 .1]          [.1 .2 .7]
[.3 .6 .1]          [.1 .2 .7]          [.6 .2 .2]
[.2 .2 .6]          [.5 .3 .2]          [.2 .7 .1]
```

These numbers are only illustrative.

---

# 12. Attention Masking in Multi-Head Attention

In decoder-only LLMs, each attention head also follows the causal restriction.

Conceptually:

```text id="f8j3kc"
Input
  ↓
Q, K, V
  ↓
Attention Scores
  ↓
🎭 Causal Mask
  ↓
Softmax
  ↓
Attention Output
```

For every head:

```text id="3i7t9s"
Head 1 → causal attention
Head 2 → causal attention
Head 3 → causal attention
...
Head N → causal attention
```

Future positions are blocked when causal self-attention is used.

---

# 13. Attention Weights in Each Head

After calculating attention scores, softmax converts them into attention weights.

For example:

```text id="q9g4l3"
Head 1:

Scores
  ↓
Softmax
  ↓
Weights
```

The same happens independently for other heads.

So:

```text id="w8m2nq"
Head 1 → Attention Weights 1
Head 2 → Attention Weights 2
Head 3 → Attention Weights 3
...
Head N → Attention Weights N
```

Each head can therefore distribute attention differently.

---

# 14. Each Head Produces an Output

After the attention weights are applied to the Values:

```text id="9qv7xn"
Attention Weights × V
        ↓
   Head Output
```

For multiple heads:

```text id="c2x8qm"
Head 1 → H₁
Head 2 → H₂
Head 3 → H₃
...
Head N → Hₙ
```

These outputs are then combined.

---

# 15. Concatenating the Heads

The outputs of all heads are concatenated.

For example:

```text id="6q1n4b"
H₁ | H₂ | H₃ | ... | Hₙ
              ↓
         Concatenate
              ↓
       Combined Output
```

If:

```text
12 heads × 64 dimensions
```

then:

```text
12 × 64 = 768
```

So the concatenated representation returns to the model dimension:

```text
768
```

Again, this is an illustrative configuration.

---

# 16. Output Projection

After concatenating the heads, the combined representation is passed through an output projection.

Conceptually:

```text id="v4k1hz"
Head 1 ─┐
Head 2 ─┤
Head 3 ─┤
   ...   ├──→ Concatenate
Head N ─┘
              ↓
       Output Projection
              ↓
           Attention
            Output
```

The output projection is another learned transformation.

It allows the model to combine information from the different heads.

---

# 17. Complete Multi-Head Attention Flow

The complete process is:

```text id="h8r3mx"
🧩 Input Representation
          ↓
    ┌─────┴─────┐
    ↓           ↓
  Head 1      Head 2 ... Head N
    ↓           ↓
 Q₁,K₁,V₁    Q₂,K₂,V₂ ... Qₙ,Kₙ,Vₙ
    ↓           ↓
 Attention    Attention
    ↓           ↓
   H₁           H₂    ... Hₙ
    └─────┬─────┘
          ↓
      Concatenate
          ↓
   Output Projection
          ↓
   Multi-Head Output
```

---

# 18. Multi-Head Attention Formula

For each head:

```text id="6p3d8y"
headᵢ =
Attention(Qᵢ, Kᵢ, Vᵢ)
```

where:

```text id="p0y8ka"
Qᵢ = XWQᵢ
Kᵢ = XWKᵢ
Vᵢ = XWVᵢ
```

Then:

```text id="z2h4ms"
MultiHead(Q, K, V)
=
Concat(head₁, head₂, ..., headₕ)WO
```

where:

```text
headᵢ = Attention(Qᵢ, Kᵢ, Vᵢ)
```

The formulas describe the conceptual structure. Actual implementations may combine projections for efficiency.

---

# 19. What Does Each Head Learn?

It is tempting to say:

```text
Head 1 = grammar
Head 2 = nouns
Head 3 = verbs
```

But this would be too strict.

Attention heads do not necessarily have one fixed human-interpretable role.

A head may learn patterns involving:

* nearby tokens
* long-range relationships
* syntax
* repeated patterns
* positional relationships
* punctuation
* semantic relationships
* other statistical structures

The patterns can differ across:

```text
Layer
Head
Input
Model
```

Therefore, the roles of attention heads should be treated as learned patterns rather than fixed labels.

---

# 20. Multi-Head Attention and Context

One of the important purposes of attention is to allow token representations to incorporate information from other positions.

Multi-Head Attention provides multiple ways to perform this information mixing.

Conceptually:

```text id="f3q9sm"
Token Representation
        ↓
┌───────────────────────────┐
│                           │
│  Head 1 → Relationship A  │
│  Head 2 → Relationship B  │
│  Head 3 → Relationship C  │
│  Head 4 → Relationship D  │
│          ...              │
│                           │
└───────────────────────────┘
        ↓
Combined Representation
```

This produces richer contextual representations.

---

# 21. Multi-Head Attention Inside a Transformer Block

Multi-Head Attention is one of the major components of a Transformer Block.

A simplified decoder-style block can be shown as:

```text id="c5m8pk"
📊 Input Representation
          ↓
🧠 Multi-Head Self-Attention
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

The exact ordering of normalization and residual operations varies across Transformer architectures.

---

# 22. Multi-Head Attention vs Self-Attention

These terms describe different aspects.

### Self-Attention

Describes **where Q, K, and V come from**.

In self-attention:

```text
Q, K, V
   ↑
Same input sequence
```

### Multi-Head Attention

Describes **how many attention operations are performed in parallel**.

```text
Head 1
Head 2
Head 3
...
Head N
```

Therefore, a model can have:

```text
Multi-Head Self-Attention
```

This is common in Transformer-based LLMs.

---

# 23. Multi-Head Self-Attention

For decoder-only LLMs, the common structure is:

```text id="x3r8qt"
Input
  ↓
Q, K, V projections
  ↓
┌─────────┬─────────┬─────────┐
↓         ↓         ↓
Head 1    Head 2    Head 3 ... Head N
↓         ↓         ↓
Causal    Causal    Causal
Attention Attention Attention
↓         ↓         ↓
└─────────┴─────────┴─────────┘
          ↓
      Concatenate
          ↓
  Output Projection
```

This allows multiple causal self-attention heads to operate in parallel.

---

# 24. Multi-Head Attention vs Cross-Attention

Multi-head attention can be used with different types of attention.

### Multi-Head Self-Attention

```text
Q ← same sequence
K ← same sequence
V ← same sequence
```

### Multi-Head Cross-Attention

```text
Q ← one representation
K ← another representation
V ← another representation
```

For example, in an encoder-decoder Transformer:

```text id="2j9p8v"
Encoder Output
     ↓
   K, V
     ↑
     |
Decoder
  ↓
 Q
```

The multi-head mechanism can still be used.

---

# 25. Multi-Head Attention During Training

During training, the model processes token sequences and learns the projection parameters.

The simplified process is:

```text id="q7v4m3"
📝 Training Text
       ↓
🔤 Tokenization
       ↓
🔢 Token IDs
       ↓
🧩 Representations
       ↓
🧠 Multi-Head Attention
       ↓
📊 Transformer Output
       ↓
🎯 Next-Token Prediction
       ↓
📉 Loss
       ↓
🔄 Backpropagation
       ↓
⚙️ Parameter Updates
```

The model learns parameters associated with the attention projections and other Transformer components.

---

# 26. Multi-Head Attention During Inference

During text generation:

```text id="q8h4n1"
📝 Prompt
   ↓
🔤 Tokens
   ↓
🧩 Representations
   ↓
🧠 Multi-Head Attention
   ↓
📊 Transformer Output
   ↓
🎯 Next Token
   ↓
🔄 Repeat
```

The attention mechanism uses the available context to produce representations for predicting the next token.

Modern implementations can use **KV caching** to avoid recomputing keys and values for previously processed tokens.

---

# 27. Multi-Head Attention and KV Cache

During autoregressive generation, the model repeatedly processes an expanding context.

Without caching, previous Key and Value representations could be recomputed.

With KV caching:

```text id="t7k3qp"
Previous Tokens
      ↓
Stored K and V
      ↓
     Cache
      ↓
New Token
      ↓
New Q, K, V
      ↓
Attention using cached + new K/V
```

The exact implementation varies by architecture.

The important idea is:

> **KV caching is an inference optimization that stores previously computed Keys and Values.**

Queries are not stored in the KV cache in the standard formulation.

---

# 28. Multi-Head Attention and Parameters

Multi-Head Attention contains learned parameters.

Conceptually, these include:

```text id="q2m7sb"
WQ
WK
WV
WO
```

where:

```text
WQ → Query projection
WK → Key projection
WV → Value projection
WO → Output projection
```

During training, these parameters are updated through backpropagation and optimization.

Therefore, the model learns how to transform representations and combine information through attention.

---

# 29. Shape of Multi-Head Attention

Suppose:

```text
Batch Size = B
Sequence Length = N
Model Dimension = D
Number of Heads = H
Head Dimension = Dh
```

Typically:

```text
D = H × Dh
```

The input shape is conceptually:

```text
[B, N, D]
```

After splitting into heads:

```text
[B, H, N, Dh]
```

The attention score shape is conceptually:

```text
[B, H, N, N]
```

The output is combined back into:

```text
[B, N, D]
```

Exact tensor layouts can vary by implementation.

---

# 30. Why Is Multi-Head Attention Useful?

Multi-Head Attention provides several benefits.

### 🔹 Multiple Representation Spaces

Different heads can transform the input differently.

### 🔹 Multiple Attention Patterns

Different heads can learn different relationships.

### 🔹 Parallel Processing

The heads can be computed efficiently using matrix operations.

### 🔹 Richer Contextual Representations

Information from different attention patterns can be combined.

A simplified idea is:

```text id="l5x2pn"
Multiple Attention Views
          ↓
      Combination
          ↓
Richer Representation
```

These are conceptual benefits; actual behavior depends on the architecture and learned parameters.

---

# 31. Multi-Head Attention Does Not Mean Multiple Models

A common misunderstanding is:

> "If there are 12 heads, does that mean there are 12 separate Transformer models?"

No.

The heads are components inside **one Transformer block**.

```text id="j3p7kw"
             Transformer Block
                    ↓
        ┌─────────────────────┐
        │ Multi-Head Attention│
        │                     │
        │ Head 1              │
        │ Head 2              │
        │ Head 3              │
        │ ...                 │
        │ Head N              │
        └─────────────────────┘
                    ↓
             Feed-Forward Network
```

The outputs of the heads are combined and continue through the same Transformer block.

---

# 32. Multi-Head Attention Does Not Mean Every Head Has a Human Meaning

Another common misunderstanding is:

> "Every attention head represents one specific concept."

Not necessarily.

Some attention heads may show interpretable patterns in analysis, but the model does not explicitly assign human-defined labels to heads.

The learned behavior can be complex and distributed.

So it is better to say:

> **Different heads can learn different attention patterns.**

rather than:

> **Each head has one fixed purpose.**

---

# 33. Multi-Head Attention vs Feed-Forward Network

These two components perform different types of operations.

| Multi-Head Attention                     | Feed-Forward Network                       |
| ---------------------------------------- | ------------------------------------------ |
| Mixes information across token positions | Transforms features at each token position |
| Uses Q, K, V                             | Uses learned linear transformations        |
| Calculates attention weights             | Applies nonlinear transformations          |
| Connects token representations           | Processes each position independently      |
| Can model relationships between tokens   | Adds further feature transformation        |

Simplified:

```text id="k6j2vz"
Attention
   ↓
Mix information across tokens

FFN
   ↓
Transform information within each token representation
```

Both are important parts of a Transformer Block.

---

# 34. Multi-Head Attention vs Attention

**Attention** is the general mechanism.

**Multi-Head Attention** performs multiple attention operations and combines their outputs.

```text id="s4q7mk"
Attention
   ↓
One attention operation

Multi-Head Attention
   ↓
Multiple attention operations
   ↓
Combine outputs
```

Therefore:

```text
Multi-Head Attention ⊃ Multiple Attention Heads
```

---

# 35. Complete Example

Suppose the input is:

```text id="a3f7kp"
The cat is sleeping
```

After tokenization:

```text id="e8q4sn"
[The] [cat] [is] [sleeping]
```

The model creates representations.

Then Multi-Head Attention operates:

```text id="z1p5kr"
Input Representations
        ↓
     Q, K, V
        ↓
┌───────┬───────┬───────┐
↓       ↓       ↓
Head 1  Head 2  Head 3  ... Head N
↓       ↓       ↓
Attention Attention Attention
↓       ↓       ↓
 H₁      H₂      H₃     ... Hₙ
└───────┴───────┴───────┘
        ↓
   Concatenate
        ↓
Output Projection
        ↓
Attention Output
```

In a decoder-only LLM, causal masking prevents each position from using future positions.

---

# 36. Complete Multi-Head Attention Pipeline

```text id="p7w2mc"
📝 Input Sequence
        ↓
🧩 Input Representations
        ↓
   Query / Key / Value
        ↓
┌──────────────────────────────┐
│      Multiple Heads          │
│                              │
│ Head 1 → Q₁ K₁ V₁            │
│ Head 2 → Q₂ K₂ V₂            │
│ Head 3 → Q₃ K₃ V₃            │
│ ...                          │
│ Head N → Qₙ Kₙ Vₙ            │
└──────────────────────────────┘
        ↓
📊 Attention Scores
        ↓
🎭 Attention Mask
        ↓
🎲 Softmax
        ↓
🎯 Attention Weights
        ↓
🧩 Weighted Values
        ↓
📦 Concatenate Heads
        ↓
🔄 Output Projection
        ↓
📊 Multi-Head Attention Output
```

---

# 37. Multi-Head Attention Inside the Complete LLM

```text id="x8r4nv"
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
      ↓
🧠 Multi-Head Self-Attention
      ↓
🎭 Causal Mask
      ↓
📊 Attention Output
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
🔄 More Transformer Blocks
      ↓
📊 Final Representation
      ↓
🎯 Language Modeling Head
      ↓
📈 Logits
      ↓
🎲 Probability Distribution
      ↓
🔤 Next Token
```

---

# 38. Simple Mental Model

Think of Multi-Head Attention as having **multiple ways of looking at the relationships between tokens**.

```text id="g6n2rs"
                 Input
                   ↓
        ┌──────────┼──────────┐
        ↓          ↓          ↓
     👀 Head 1  👀 Head 2  👀 Head 3
        ↓          ↓          ↓
    Pattern A   Pattern B   Pattern C
        └──────────┼──────────┘
                   ↓
              Combine
                   ↓
            Better Context
```

The heads are not separate models.

They are parallel attention mechanisms inside the same Transformer block.

---

# 39. Key Takeaways

* 🧠 **Multi-Head Attention performs multiple attention operations in parallel.**
* 👀 Each attention head can learn different attention patterns.
* 🔑 Each head uses Query, Key, and Value representations.
* 📊 Each head calculates its own attention scores and weights.
* 🎭 In causal self-attention, future positions are masked.
* 📦 Outputs from all heads are concatenated.
* 🔄 An output projection combines the concatenated representation.
* 🧩 Multi-Head Attention is a component inside a Transformer Block.
* 🔗 Self-attention describes where Q, K, and V come from.
* 🧠 Multi-head describes the use of multiple attention operations.
* ⚙️ The projection parameters are learned during training.
* 🚀 Multiple heads allow the model to represent different relationships in parallel.
* ⚠️ The role of each head is not necessarily fixed or human-interpretable.
* 💾 KV caching can make autoregressive inference more efficient.
* 📐 The exact number of heads, dimensions, projection implementation, and architecture vary between models.

The central idea is:

```text id="v5x8qn"
🧩 Input
   ↓
🔑 Q, K, V
   ↓
┌────────┬────────┬────────┐
👀 Head 1 👀 Head 2 👀 Head 3 ... 👀 Head N
└────────┴────────┴────────┘
   ↓
📦 Concatenate
   ↓
🔄 Output Projection
   ↓
📊 Multi-Head Attention Output
```

**Multi-Head Attention = multiple attention views + combined representation.**
