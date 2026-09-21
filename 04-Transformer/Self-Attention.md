# 👀 Self-Attention

**Self-Attention** is a mechanism that allows each token in a sequence to interact with other tokens in the **same sequence**.

It helps a Transformer build contextual representations by determining which other tokens are relevant when processing each token.

For example:

```text
The cat sat on the mat.
```

When processing the token `"cat"`, self-attention allows the model to consider information from other tokens in the same sequence.

A simplified view is:

```text id="7m3qpa"
📝 Input Sequence
      ↓
🔤 Tokens
      ↓
🧩 Token Representations
      ↓
👀 Self-Attention
      ↓
📊 Contextual Representations
```

---

# 1. 🧠 What Is Self-Attention?

Self-attention is an attention mechanism where the **Query, Key, and Value representations come from the same input sequence**.

The basic idea is:

```text id="x8v2kn"
Input Sequence
      ↓
Each token looks at
other allowed tokens
      ↓
Calculate relevance
      ↓
Combine information
      ↓
Updated token representations
```

For example:

```text id="4n7cqs"
The   cat   sat   on   the   mat
 ↓     ↓     ↓     ↓    ↓     ↓
 └─────┴─────┴─────┴────┴─────┘
              ↓
        👀 Self-Attention
              ↓
     Contextual Representations
```

The model does not simply treat every token independently.

It allows information between token positions to interact.

---

# 2. 🔍 Why Do We Need Self-Attention?

A token can have different meanings depending on its context.

Consider:

```text id="k4m9zx"
I went to the bank.
```

and:

```text id="p7v2mc"
I sat near the river bank.
```

The token `"bank"` appears in both sentences.

Its surrounding context is different.

Self-attention provides a mechanism for the representation of `"bank"` to use information from other tokens in the sequence.

Conceptually:

```text id="z6q3wp"
"bank"
   ↓
👀 Look at surrounding context
   ↓
🔗 Find relevant relationships
   ↓
📊 Update representation
```

---

# 3. 📝 Example of Self-Attention

Consider:

```text id="m2x7vk"
The cat sat on the mat.
```

Suppose the model is processing:

```text
"cat"
```

Self-attention allows the model to consider other tokens:

```text id="r8p4ns"
The    → information
cat    → current token
sat    → information
on     → information
the    → information
mat    → information
```

The model calculates attention weights to determine how much information from different tokens contributes to the updated representation of `"cat"`.

The exact weights are learned through the model's parameters and depend on the input.

---

# 4. 🔄 Self-Attention Works on Representations

Self-attention does not operate directly on raw words.

The text first becomes token representations.

```text id="c9v5qm"
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
👀 Self-Attention
```

So, self-attention receives numerical vectors rather than strings such as `"cat"` or `"dog"`.

---

# 5. 🔑 Query, Key, and Value

Self-attention uses three important representations:

```text id="n6q2xr"
🔎 Query
🔑 Key
📦 Value
```

They are created from the input representations using learned transformations.

Suppose the input representation is:

```text
X
```

The model creates:

```text
Q = XWQ
K = XWK
V = XWV
```

where:

* `Q` = Query
* `K` = Key
* `V` = Value
* `WQ` = learned Query projection
* `WK` = learned Key projection
* `WV` = learned Value projection

These matrices contain learned parameters.

---

# 6. 🔎 What Is a Query?

A **Query** represents what information a token is looking for.

A simple conceptual interpretation is:

```text id="h8m3vz"
Query
  ↓
"What information might be relevant to me?"
```

For example, when processing a token, its Query is used to compare against the Keys of other tokens.

This comparison helps determine which tokens should receive more attention.

The word "looking" here is only a conceptual analogy. The model performs numerical operations rather than literally asking a question.

---

# 7. 🔑 What Is a Key?

A **Key** represents information that can be used to determine whether a token is relevant to another token.

Conceptually:

```text id="w5x9kp"
Key
 ↓
"What kind of information do I represent?"
```

Queries are compared with Keys.

A stronger match produces a larger attention score.

```text id="b7q2nm"
Query
  ↓
Compare
  ↓
Key
  ↓
Attention Score
```

---

# 8. 📦 What Is a Value?

A **Value** contains the information that can be passed to the output of attention.

Conceptually:

```text id="p3v8xq"
Value
  ↓
"What information can I provide?"
```

After calculating attention weights, the model uses those weights to combine the Value vectors.

```text id="t6m4zr"
Attention Weights
       ↓
   Weighted Values
       ↓
Combined Information
```

---

# 9. 🧩 How Q, K, and V Work Together

The overall idea is:

```text id="s9x3qm"
Input Representations
        ↓
   ┌────┼────┐
   ↓    ↓    ↓
   Q    K    V
   │    │    │
   └────┼────┘
        ↓
Compare Q with K
        ↓
Attention Scores
        ↓
Softmax
        ↓
Attention Weights
        ↓
Weighted Vectors
        ↓
Self-Attention Output
```

This is the core process of self-attention.

---

# 10. 📊 Attention Scores

The model calculates how strongly a Query relates to each Key.

The standard scaled dot-product attention formula is:

```text id="q4n8vy"
Attention(Q, K, V)
=
softmax(QKᵀ / √dₖ)V
```

The first important part is:

```text id="v8m2xp"
QKᵀ
```

This calculates similarity scores between Queries and Keys.

Conceptually:

```text id="j5r7kc"
Query
  ↓
Compare with Keys
  ↓
Attention Scores
```

---

# 11. 📏 Why Divide by √dₖ?

The formula includes:

```text id="c3x9qm"
/ √dₖ
```

where `dₖ` is the dimension of the Key vectors.

This scaling helps keep the attention scores at a suitable numerical scale before applying softmax.

Without appropriate scaling, the dot products can become large as the vector dimension increases, which can make the softmax distribution excessively concentrated.

For beginner understanding, the main idea is:

> **The scaling factor helps make the attention calculation numerically more stable.**

---

# 12. 🎲 Softmax and Attention Weights

After calculating the scaled attention scores, softmax converts them into weights.

For example:

```text id="k7p2zn"
Token       Score
-------------------
The          1.2
cat          3.5
sat          0.8
mat          2.1
```

After softmax, these become values that form a distribution:

```text id="m4x8qc"
Token       Weight
-------------------
The          0.08
cat          0.45
sat          0.05
mat          0.20
...
```

The numbers above are only illustrative.

The weights indicate how strongly the corresponding Value vectors contribute to the output for that Query.

---

# 13. 📦 Weighted Combination of Values

Once the attention weights are calculated, they are used to combine the Value vectors.

Conceptually:

```text id="z8q3vm"
Value 1 ──┐
Value 2 ──┤
Value 3 ──┤──→ Weighted Combination
Value 4 ──┤
Value 5 ──┘
                 ↓
        Self-Attention Output
```

A token's updated representation therefore contains information gathered from other tokens it attends to.

---

# 14. 🧠 Simple Example

Consider:

```text id="v2m7qx"
The cat sat on the mat.
```

Suppose we are calculating the output for `"cat"`.

Conceptually:

```text id="n5k8zr"
             Query for "cat"
                    │
       ┌────────────┼────────────┐
       ↓            ↓            ↓
     "The"         "sat"        "mat"
       │            │            │
       ↓            ↓            ↓
      Key          Key          Key
       │            │            │
       └────────────┼────────────┘
                    ↓
             Attention Scores
                    ↓
             Attention Weights
                    ↓
             Weighted Values
                    ↓
          Updated "cat" Representation
```

The model performs this numerical process for every relevant position.

---

# 15. 🔄 Self-Attention Happens for Every Token

Self-attention is not performed only for one token.

It is calculated for all positions in the sequence.

For:

```text id="x7q4pm"
The cat sat on the mat.
```

the model produces an updated representation for:

```text
The
cat
sat
on
the
mat
```

Conceptually:

```text id="j3v9kc"
Input Representations
        ↓
   👀 Self-Attention
        ↓
┌───────┬───────┬───────┬───────┐
↓       ↓       ↓       ↓       ↓
Rep 1   Rep 2   Rep 3   Rep 4   ...
```

Each output representation can contain information gathered from other allowed positions.

---

# 16. 🧠 Self-Attention Creates Contextual Representations

Before self-attention, a token has an initial representation based primarily on its token embedding and positional information.

After self-attention, its representation incorporates information from other positions.

```text id="f8m3qx"
Token Embedding
      ↓
Self-Attention
      ↓
Contextual Representation
```

For example:

```text id="a5v7nz"
"bank"
   ↓
Context from surrounding tokens
   ↓
Updated representation
```

This is one reason Transformer models can use context effectively.

---

# 17. 🌐 Self-Attention vs Attention

The terms **attention** and **self-attention** are closely related, but they are not always identical.

### Attention

A general mechanism for weighting information based on relevance.

### Self-Attention

A form of attention where the Queries, Keys, and Values are derived from the same sequence.

```text id="q6x2mv"
Self-Attention:

Same sequence
   ├── Query
   ├── Key
   └── Value
```

In the original encoder-decoder Transformer, the decoder also uses **cross-attention**, where the Query comes from the decoder while the Keys and Values come from encoder representations.

---

# 18. 🔗 Self-Attention vs Cross-Attention

### Self-Attention

Q, K, and V come from the same sequence representation.

```text id="n8m4xp"
Sequence
  ├── Q
  ├── K
  └── V
       ↓
Self-Attention
```

### Cross-Attention

The Query comes from one representation while the Keys and Values come from another.

```text id="w3q7kc"
Decoder → Q
Encoder → K, V
       ↓
Cross-Attention
```

This distinction is important in encoder-decoder Transformers.

---

# 19. 🔒 Causal Self-Attention

Decoder-only LLMs use **causal self-attention**.

It prevents a token from attending to future tokens during autoregressive language modeling.

Suppose the sequence is:

```text id="m5v8qz"
The cat is sleeping
```

When predicting the token after:

```text
The cat is
```

the model should not use:

```text
sleeping
```

as information for that prediction.

Therefore, a causal mask is applied.

---

# 20. 🛡️ Causal Mask

A simplified attention mask can look like:

```text id="x2k9pv"
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
✓ = allowed to attend
✗ = masked
```

So:

```text id="z7m4qx"
Position 1 → sees 1
Position 2 → sees 1, 2
Position 3 → sees 1, 2, 3
Position 4 → sees 1, 2, 3, 4
```

This creates the causal structure required for autoregressive next-token prediction.

---

# 21. 🎯 Why Is Causal Masking Important?

Suppose the training sequence is:

```text id="r3v8km"
The sky is blue
```

For next-token prediction:

```text id="q5n2xz"
Input:  The
Target: sky
```

Then:

```text
Input:  The sky
Target: is
```

Then:

```text
Input:  The sky is
Target: blue
```

When predicting `"blue"`, the model must not see `"blue"` as an input.

Causal masking ensures that future information is hidden.

```text id="p8m3vz"
Previous Tokens
      ↓
👀 Causal Self-Attention
      ↓
🎯 Predict Next Token
```

---

# 22. 🧠 Self-Attention Inside a Transformer Block

Self-attention is one major part of a Transformer Block.

A simplified block is:

```text id="c7x2mn"
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

The exact ordering can vary by architecture.

Self-attention itself is not the entire Transformer Block.

---

# 23. 📐 Self-Attention Matrix

For a sequence containing multiple tokens, attention scores can be represented as a matrix.

For example:

```text id="v6q9pk"
             Keys
          T1  T2  T3  T4
        ┌─────────────────
Query T1│ .   .   .   .
      T2│ .   .   .   .
      T3│ .   .   .   .
      T4│ .   .   .   .
        └─────────────────
```

Each cell represents the relationship between a Query position and a Key position.

After softmax, the matrix contains attention weights.

For causal self-attention, future positions are masked.

---

# 24. 📊 Shape of Self-Attention

Suppose:

```text
Sequence Length = 5
```

Then a single attention head can produce a:

```text
5 × 5
```

attention score/weight matrix.

Conceptually:

```text id="k3x8qm"
5 Query Positions
        ×
5 Key Positions
        =
5 × 5 Attention Matrix
```

For a batch of sequences and multiple attention heads, additional dimensions are present.

A common conceptual shape is:

```text id="z4m7xp"
Batch Size
    ×
Number of Heads
    ×
Sequence Length
    ×
Sequence Length
```

The exact tensor layout depends on the implementation.

---

# 25. 🔢 Self-Attention in Mathematical Form

The standard scaled dot-product self-attention formula is:

```text id="q9v2mk"
Attention(Q, K, V)
=
softmax(QKᵀ / √dₖ)V
```

The process can be divided into four steps:

```text id="s5x8qn"
1. Calculate QKᵀ
        ↓
2. Scale by √dₖ
        ↓
3. Apply softmax
        ↓
4. Multiply by V
```

For causal attention:

```text id="m8q4vz"
QKᵀ
  ↓
Apply Causal Mask
  ↓
Scale
  ↓
Softmax
  ↓
Multiply by V
```

In practice, masking and scaling are implemented together in optimized operations.

---

# 26. 🧩 Where Do Q, K, and V Come From?

Suppose the input representation is:

```text
X
```

The model applies learned linear projections:

```text id="r7x3kp"
X
│
├── × WQ → Q
│
├── × WK → K
│
└── × WV → V
```

These projection matrices are learned during training.

Therefore, the model learns how to transform the input representations into useful Queries, Keys, and Values.

---

# 27. 🔄 Self-Attention and Multi-Head Attention

A Transformer can use multiple self-attention heads.

```text id="x4m8qz"
Input
  ↓
┌───────────────┐
│ Head 1        │ → Attention Output
├───────────────┤
│ Head 2        │ → Attention Output
├───────────────┤
│ Head 3        │ → Attention Output
├───────────────┤
│ ...           │
└───────────────┘
  ↓
Concatenate / Combine
  ↓
Output Projection
```

Each head operates on a learned projection of the representation.

Different heads may learn different patterns, although their exact learned behavior is not predetermined.

---

# 28. ⚡ Self-Attention During Training

During Transformer training, self-attention is calculated for the training sequences.

For a decoder-only language model:

```text id="n2v7xm"
📚 Training Sequence
       ↓
🔤 Tokens
       ↓
🧩 Representations
       ↓
👀 Causal Self-Attention
       ↓
🔄 Transformer Blocks
       ↓
🎯 Next-Token Prediction
       ↓
📉 Loss
       ↓
🔄 Backpropagation
```

The parameters used to calculate Q, K, V and the rest of the Transformer are updated during training.

---

# 29. ⚡ Self-Attention During Inference

During inference, the trained parameters are used to process the current context.

For autoregressive generation:

```text id="v9q3mk"
📝 Prompt
   ↓
🔤 Tokens
   ↓
🧩 Representations
   ↓
👀 Causal Self-Attention
   ↓
🔄 Transformer Blocks
   ↓
🎯 Next-Token Prediction
   ↓
🔤 Generated Token
   ↓
🔄 Repeat
```

Modern implementations often use **KV caching** to avoid recomputing certain Key and Value representations for all previous tokens at every generation step.

---

# 30. 🧠 What Does Self-Attention Actually Do?

A useful conceptual description is:

> **Self-attention determines how information from different positions in the same sequence should contribute to each position's updated representation.**

It does not literally:

* Read the sentence like a human
* Understand every relationship perfectly
* Assign one permanent meaning to every token
* Guarantee factual correctness

Instead, it performs learned numerical transformations.

---

# 31. 🧩 Self-Attention vs Token Embeddings

These are different concepts.

### Token Embedding

Converts a Token ID into an initial vector.

```text id="x8q2mn"
Token ID
   ↓
Embedding Lookup
   ↓
Token Embedding
```

### Self-Attention

Uses token representations to combine information across positions.

```text id="j4m7vz"
Token Representations
        ↓
Self-Attention
        ↓
Contextual Representations
```

Therefore:

```text id="p6x9kr"
Token Embedding
      ≠
Self-Attention Output
```

---

# 32. 🧠 Self-Attention vs Feed-Forward Network

Both are important parts of a Transformer Block, but they perform different operations.

| Component               | Main Role                                     |
| ----------------------- | --------------------------------------------- |
| 👀 Self-Attention       | Mixes information across token positions      |
| 🧠 Feed-Forward Network | Transforms information at each token position |

Simplified:

```text id="m7x3qp"
Self-Attention
      ↓
"What information from other tokens matters?"

Feed-Forward Network
      ↓
"How should this representation be transformed?"
```

---

# 33. 🌐 Complete Self-Attention Flow

The complete simplified process is:

```text id="q3v8mx"
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
   Attention Scores
          ↓
   Scaling + Masking
          ↓
       Softmax
          ↓
  Attention Weights
          ↓
   Weighted Values
          ↓
👀 Self-Attention Output
```

For non-causal self-attention, the causal mask is not needed.

For decoder-only causal self-attention, the mask prevents access to future positions.

---

# 34. 🧠 Simple Mental Model

Think of self-attention as a **context-mixing mechanism**.

For every token:

```text id="w5q8zn"
Current Token
     ↓
👀 Compare with other allowed tokens
     ↓
📊 Calculate relevance
     ↓
🎲 Create attention weights
     ↓
📦 Combine information from Values
     ↓
📊 Updated Representation
```

The important idea is:

> **Each token's representation can be updated using information from other tokens in the same sequence.**

---

# 35. 🔑 Key Takeaways

* 👀 **Self-attention** allows tokens in the same sequence to interact.
* 🧩 It operates on numerical token representations, not raw text.
* 🔑 Self-attention uses **Query, Key, and Value** representations.
* 🔎 Queries are compared with Keys to calculate attention scores.
* 🎲 Softmax converts scores into attention weights.
* 📦 Attention weights are used to combine Value vectors.
* 🧠 The result is an updated, more contextual representation.
* 🔄 Self-attention is calculated for the relevant positions in the sequence.
* 🔒 Decoder-only LLMs use **causal self-attention** to prevent access to future tokens.
* 🛡️ Causal masking is essential for autoregressive next-token prediction.
* 🔗 Self-attention is different from cross-attention.
* 🧠 Self-attention is one major component of a Transformer Block, not the entire Transformer.
* 🔄 Multiple attention heads can be used in **multi-head attention**.
* 📊 Attention produces relationships between Query and Key positions.
* ⚙️ The Q, K, and V projection parameters are learned during training.
* ⚡ Self-attention can be highly parallelized during training.
* 🧠 The core idea is **mixing information across token positions based on learned relevance**.
