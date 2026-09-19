# 👀 Attention

**Attention** is one of the most important ideas behind the Transformer architecture.

It allows the model to determine **which parts of the input sequence are important when processing each token**.

Instead of treating every token independently, attention allows token representations to interact with other relevant tokens.

A simple idea is:

```text
📝 Input Sequence
      ↓
👀 Attention
      ↓
🔗 Token Relationships
      ↓
📊 Updated Representations
```

---

# 📌 1. What Is Attention?

Attention is a mechanism that helps a neural network **focus on relevant information from the input** when processing a particular token.

For example:

```text
The cat sat on the mat because it was tired.
```

When processing:

```text
it
```

the model may need information from earlier tokens to understand what `it` refers to.

Attention allows the representation of one token to use information from other tokens.

Conceptually:

```text
The ───────┐
cat ───────┤
sat ───────┤
on ────────┤──→ Attention
the ───────┤
mat ───────┤
it ────────┘
```

The model learns which relationships are useful.

---

# 🧩 2. Why Is Attention Needed?

Language is highly dependent on context.

Consider:

```text
The bank is near the river.
```

and:

```text
The bank approved the loan.
```

The word:

```text
bank
```

appears in both sentences, but its context is different.

Attention allows the model to consider surrounding tokens when creating the representation of a token.

```text
📌 Token
   +
🌐 Context
   ↓
📊 Contextual Representation
```

---

# 🔗 3. Tokens Can Interact With Other Tokens

Suppose we have:

```text
The dog chased the ball.
```

The representation of:

```text
dog
```

can interact with information from:

```text
The
chased
the
ball
```

Similarly, the representation of:

```text
ball
```

can interact with other tokens.

Conceptually:

```text
The     ─────┐
dog     ─────┤
chased  ─────┤
the     ─────┤──→ Attention
ball    ─────┘
```

Attention creates relationships between token representations.

---

# 🎯 4. Attention Does Not Mean Every Token Is Equally Important

A token can pay different amounts of attention to different tokens.

For example:

```text
The cat sat on the mat.
```

When processing:

```text
cat
```

the model might assign different attention strengths to different tokens.

Illustratively:

```text
The      → 0.10
cat      → 0.20
sat      → 0.30
on       → 0.05
the      → 0.10
mat      → 0.25
```

These numbers are only for understanding the concept.

They do **not** represent actual attention values from a real model.

The important idea is:

> **Different tokens can contribute different amounts of information.**

---

# 📊 5. Attention Scores

To determine how strongly tokens should interact, the attention mechanism calculates **attention scores**.

A simplified flow is:

```text
🧩 Token Representations
          ↓
📊 Attention Scores
          ↓
📈 Attention Weights
          ↓
🔗 Combine Information
          ↓
📊 Updated Representations
```

Higher attention weight means that a token contributes more strongly to the resulting representation.

---

# 🧠 6. Attention Uses Token Representations

Attention does not directly operate on raw text.

The input has already gone through earlier stages:

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
👀 Attention
```

Therefore, attention works with **numerical representations**.

---

# 🔑 7. Query, Key, and Value

A core part of modern Transformer attention is the use of three representations:

```text
🔎 Query
🔑 Key
📦 Value
```

They are commonly called:

**Q, K, and V**

The basic idea is:

* 🔎 **Query** → What information am I looking for?
* 🔑 **Key** → What information does this token represent for matching?
* 📦 **Value** → What information should be passed forward?

Simplified:

```text
Input Representation
        ↓
   ┌────┼────┐
   ↓    ↓    ↓
   Q    K    V
   ↓    ↓    ↓
   └────┼────┘
        ↓
Attention
        ↓
Updated Representation
```

The detailed Query-Key-Value mechanism is covered separately.

---

# 🔍 8. How Attention Finds Relevant Information

The basic conceptual process is:

```text
1️⃣ Create Queries, Keys, and Values
              ↓
2️⃣ Compare Queries with Keys
              ↓
3️⃣ Calculate Attention Scores
              ↓
4️⃣ Convert Scores into Weights
              ↓
5️⃣ Combine Values using those Weights
              ↓
6️⃣ Produce Updated Representations
```

This allows the model to determine which information should contribute to each token's new representation.

---

# 📐 9. Attention Scores

A common attention mechanism calculates a score using the Query and Key.

Conceptually:

```text
Query × Key
     ↓
Attention Score
```

A standard scaled dot-product attention formula is:

```text
Attention(Q, K, V)
=
softmax(QKᵀ / √dₖ)V
```

For now, the important parts are:

```text
Q × K
  ↓
Scores
  ↓
Softmax
  ↓
Weights
  ↓
Values
  ↓
Output
```

The detailed mathematical meaning of this formula can be studied separately.

---

# 📈 10. Attention Weights

The attention scores are converted into weights.

Softmax is commonly used for this conversion.

For example:

```text
Attention Scores
       ↓
    Softmax
       ↓
Attention Weights
```

Illustrative weights:

```text
Token A → 0.10
Token B → 0.20
Token C → 0.60
Token D → 0.10
```

The weights indicate how strongly each corresponding value contributes to the output.

Typically, the weights form a distribution whose values sum to approximately 1 for each query.

---

# 📦 11. Combining the Values

After obtaining attention weights, the model uses them to combine the Value representations.

Conceptually:

```text
Value A × 0.10
        +
Value B × 0.20
        +
Value C × 0.60
        +
Value D × 0.10
        ↓
Attention Output
```

Therefore, the output representation contains information gathered from multiple tokens.

---

# 🔄 12. Attention as Information Mixing

A useful mental model is:

```text
Token Representations
        ↓
🔍 Decide what is relevant
        ↓
⚖️ Assign weights
        ↓
📦 Collect information
        ↓
📊 Create updated representations
```

So attention can be thought of as a mechanism for **context-dependent information mixing**.

---

# 📝 13. Simple Example

Consider:

```text
The cat drank the milk because it was thirsty.
```

Suppose the model is processing:

```text
it
```

The representation of `it` can use information from other tokens.

Conceptually:

```text
The
 ↓
cat ───────────────┐
 ↓                 │
drank              │
 ↓                 │
the                ├──→ Attention
 ↓                 │
milk ──────────────┤
 ↓                 │
because            │
 ↓                 │
it ────────────────┘
 ↓
was
 ↓
thirsty
```

The actual attention pattern depends on the model, layer, head, input, and position.

This example is only meant to show why contextual relationships are useful.

---

# 🚫 14. Attention Does Not Simply "Understand" the Sentence

It is common to say:

> "The model looks at the important words."

This is a useful beginner-friendly explanation, but internally the model performs numerical operations on learned representations.

The actual process involves:

```text
🧩 Numerical Representations
        ↓
🔎 Queries
🔑 Keys
📦 Values
        ↓
📊 Scores
        ↓
⚖️ Weights
        ↓
📦 Weighted Values
        ↓
📊 New Representations
```

So attention should not be imagined as a human literally looking at words.

---

# 🔄 15. Attention Inside a Transformer Block

Attention is one major part of a Transformer Block.

A simplified Transformer Block is:

```text
📊 Input Representation
          ↓
👀 Attention
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
📊 Block Output
```

The exact ordering can vary between architectures.

---

# 🧠 16. Attention and Contextual Representations

Before attention:

```text
🧩 Token Representation
```

After attention:

```text
📊 Context-Aware Representation
```

This does not mean the token embedding itself is permanently changed.

Rather, the Transformer produces a new representation based on the current context.

Conceptually:

```text
Token Embeddings
       ↓
Attention
       ↓
Contextual Representations
```

As the representation passes through more Transformer Blocks, it can be transformed further.

---

# 🔢 17. Attention for Every Token

Attention is not performed for only one token.

For a sequence:

```text
The cat sat on the mat
```

the mechanism produces an attention-based output for each token position.

Conceptually:

```text
The → 📊 Updated Representation
cat → 📊 Updated Representation
sat → 📊 Updated Representation
on  → 📊 Updated Representation
the → 📊 Updated Representation
mat → 📊 Updated Representation
```

Each position has its own Query and therefore its own pattern of attention over the available Keys and Values.

---

# 📊 18. Attention Matrix

For a sequence of tokens, attention can be represented as a matrix.

For example:

```text
          The   cat   sat   mat
The       0.4   0.3   0.2   0.1
cat       0.1   0.5   0.3   0.1
sat       0.1   0.2   0.5   0.2
mat       0.1   0.2   0.2   0.5
```

These numbers are purely illustrative.

Each row represents the attention distribution for one query position.

For example:

```text
cat → [0.1, 0.5, 0.3, 0.1]
```

means that, for this illustrative example, the representation at `cat` gives different weights to the available tokens.

---

# 🚫 19. Causal Attention in Decoder-Only LLMs

Decoder-only LLMs such as GPT-style models use **causal self-attention** during autoregressive language modeling.

This means a token cannot use information from future positions when predicting the next token.

For example:

```text
The cat is
```

When predicting the next token, the model can use:

```text
The
cat
is
```

but it cannot use the future answer.

Conceptually:

```text
The  → can see The
cat  → can see The, cat
is   → can see The, cat, is
```

The attention pattern is therefore restricted by a causal mask.

---

# 🔐 20. Causal Mask

A simplified causal attention matrix looks like:

```text
        The  cat  is  sleeping
The     ✓
cat     ✓    ✓
is      ✓    ✓    ✓
sleeping✓    ✓    ✓     ✓
```

A token can attend to itself and earlier positions, but not future positions.

For example:

```text
cat → The ✓
cat → cat ✓
cat → is  ✗
cat → sleeping ✗
```

This prevents the model from seeing future tokens during next-token prediction.

---

# 🔀 21. Self-Attention

When the Query, Key, and Value representations all come from the same input sequence, the mechanism is called **Self-Attention**.

```text
Input Sequence
      ↓
 ┌────┼────┐
 ↓    ↓    ↓
 Q    K    V
 └────┼────┘
      ↓
Self-Attention
      ↓
Output
```

The term "self" means that the sequence attends to itself.

Self-attention is a central component of the Transformer architecture.

---

# 🧩 22. Attention vs Self-Attention

These terms are closely related but not always identical.

### Attention

A general mechanism for weighting and combining information.

### Self-Attention

Attention where the Queries, Keys, and Values are derived from the same sequence.

```text
Attention
    ↓
General Mechanism

Self-Attention
    ↓
Attention within the same sequence
```

Transformer architectures heavily use self-attention.

---

# 👥 23. Multi-Head Attention

Transformers commonly use **Multi-Head Attention**.

Instead of performing only one attention operation, the model uses multiple attention heads.

Simplified:

```text
                 Input
                   ↓
        ┌──────────┼──────────┐
        ↓          ↓          ↓
     👀 Head 1  👀 Head 2  👀 Head 3
        ↓          ↓          ↓
        └──────────┼──────────┘
                   ↓
               Combine
                   ↓
                 Output
```

Different heads can learn different types of relationships.

The detailed mechanism is covered separately in:

```text
Multi-Head-Attention.md
```

---

# 🏗️ 24. Attention Through the LLM

The complete simplified flow is:

```text
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
👀 Self-Attention
      ↓
🧠 Feed-Forward Network
      ↓
🔄 More Transformer Blocks
      ↓
📊 Final Representation
      ↓
🎯 Language Modeling Head
      ↓
📈 Token Probabilities
      ↓
🔤 Next Token
```

Attention is therefore one part of a much larger LLM pipeline.

---

# 🎓 25. Attention During Training

During training, attention is used as part of the forward pass.

Simplified:

```text
📚 Training Sequence
        ↓
🔢 Token IDs
        ↓
🧩 Embeddings
        ↓
👀 Attention
        ↓
🧠 Feed-Forward Network
        ↓
📊 Transformer Output
        ↓
🎯 Prediction
        ↓
📉 Loss
        ↓
🔄 Backpropagation
        ↓
⚙️ Parameter Updates
```

The parameters used by the attention mechanism are learned during training.

---

# 🚀 26. Attention During Inference

During inference, the trained attention mechanism processes new input.

```text
📝 Prompt
   ↓
🔢 Tokens
   ↓
🧩 Representations
   ↓
👀 Attention
   ↓
📊 Transformer Output
   ↓
🎯 Next-Token Prediction
```

The model then generates another token and continues the process.

---

# ⚠️ 27. Important Clarification

Attention is **not the entire Transformer**.

A Transformer contains several components.

For example:

```text
Transformer
│
├── 👀 Attention
├── ➕ Residual Connections
├── 📏 Layer Normalization
├── 🧠 Feed-Forward Networks
└── 🔄 Multiple Transformer Blocks
```

Attention is one of the most important components, but it works together with the other components.

---

# 📋 28. Attention vs Token Embeddings

These are different concepts.

| Concept                      | Purpose                                                               |
| ---------------------------- | --------------------------------------------------------------------- |
| 🧩 Token Embedding           | Converts a token ID into a learned vector                             |
| 📍 Positional Information    | Provides information about token position                             |
| 👀 Attention                 | Allows representations to interact based on learned attention weights |
| 📊 Contextual Representation | Resulting representation after Transformer processing                 |

Simplified:

```text
Token ID
   ↓
🧩 Embedding
   ↓
📍 Position
   ↓
👀 Attention
   ↓
📊 Contextual Representation
```

---

# 🧠 29. Simple Mental Model

Think of attention as a mechanism that helps every token answer:

> **"Which other information in the sequence should contribute to my representation?"**

Simplified:

```text
🧩 Token
   ↓
🔎 What am I looking for?
   ↓
🔑 Which tokens match?
   ↓
⚖️ How important are they?
   ↓
📦 Collect their information
   ↓
📊 Create an updated representation
```

This is the central intuition behind attention.

---

# 🔗 30. Complete Attention Flow

```text
🧩 Input Representations
          ↓
     🔎 Queries
     🔑 Keys
     📦 Values
          ↓
   🔍 Compare Q and K
          ↓
    📊 Attention Scores
          ↓
       Softmax
          ↓
    ⚖️ Attention Weights
          ↓
   📦 Weighted Values
          ↓
    📊 Attention Output
          ↓
   ➕ Residual Connection
          ↓
      📏 Normalize
```

For decoder-only LLMs, causal masking is applied so future tokens cannot be used.

---

# 🎯 Key Takeaways

* 👀 **Attention** allows token representations to interact with other relevant information.
* 🔗 It helps the model use context when processing a token.
* 🔎 Modern Transformer attention uses **Queries, Keys, and Values (Q, K, V)**.
* 📊 Queries and Keys are used to calculate attention scores.
* ⚖️ Scores are converted into attention weights.
* 📦 The weights are used to combine Value representations.
* 🔄 **Self-Attention** means the Queries, Keys, and Values come from the same sequence.
* 🔐 Decoder-only LLMs use **causal self-attention** for autoregressive next-token prediction.
* 👥 Transformers commonly use **Multi-Head Attention**.
* 🧠 Attention is one component of a Transformer Block, not the entire Transformer.
* 📊 Attention produces updated representations that can carry contextual information.
* 🔄 Multiple Transformer Blocks repeatedly transform these representations.
* 🎯 The final representations are eventually used to predict the next token.
