# 🎭 Attention Masking

Attention masking is a technique used in attention mechanisms to control **which token positions are allowed to interact with which other positions**.

It is especially important in Transformer-based LLMs because the model may need to prevent certain tokens from being visible during attention.

For example, in a decoder-only LLM, when predicting the next token, the model must not look at future tokens.

---

## 1. What Is Attention Masking?

Attention masking means placing restrictions on attention between token positions.

A mask tells the attention mechanism:

> **"These positions can be attended to, and these positions cannot."**

Simplified flow:

```text
🧩 Input Representations
          ↓
      Query (Q)
          ↓
      Key (K)
          ↓
    📊 Attention Scores
          ↓
      🎭 Mask
          ↓
    📊 Modified Scores
          ↓
       Softmax
          ↓
   🎯 Attention Weights
          ↓
   📊 Attention Output
```

The mask affects the attention scores **before softmax**.

---

# 2. Why Do We Need Attention Masking?

Without masking, every token could potentially attend to every other token.

Sometimes that is exactly what we want.

But sometimes we need to restrict attention.

For example:

```text
The cat is sleeping
```

When predicting:

```text
The cat is
```

the model should not be allowed to see:

```text
sleeping
```

because `sleeping` is the future token.

If the model could see the answer during training, next-token prediction would become invalid.

---

# 3. Attention Without Masking

Suppose we have four tokens:

```text
The   cat   is   sleeping
```

Without a mask, the attention matrix could look conceptually like:

```text
          The   cat   is   sleeping
The       ✓     ✓     ✓       ✓
cat       ✓     ✓     ✓       ✓
is        ✓     ✓     ✓       ✓
sleeping  ✓     ✓     ✓       ✓
```

Every token can potentially attend to every token.

This is called **full attention** or **unmasked attention**.

It is useful in architectures where tokens are allowed to see the complete sequence.

---

# 4. Causal Attention Masking

Decoder-only LLMs use **causal masking** to prevent a token from attending to future tokens.

For example:

```text
The   cat   is   sleeping
```

The allowed attention pattern is:

```text
          The   cat   is   sleeping
The       ✓     ✗     ✗       ✗
cat       ✓     ✓     ✗       ✗
is        ✓     ✓     ✓       ✗
sleeping  ✓     ✓     ✓       ✓
```

The important rule is:

> A token can attend to itself and previous tokens, but not future tokens.

This preserves the autoregressive nature of next-token prediction.

---

# 5. Why Is It Called "Causal"?

It is called **causal** because the model follows the direction of the sequence.

For example:

```text
Token 1 → Token 2 → Token 3 → Token 4
```

Token 3 can use:

```text
Token 1
Token 2
Token 3
```

but not:

```text
Token 4
```

The model therefore only uses information that would have been available at that point in the sequence.

---

# 6. Attention Scores Before Masking

Recall the attention calculation:

```text
QKᵀ
```

This produces attention scores.

For a sequence of four tokens, the score matrix has a conceptual shape:

```text
4 × 4
```

For example:

```text
          T1    T2    T3    T4
T1       2.1   1.2   0.8   1.5
T2       0.7   2.4   1.6   1.1
T3       1.0   1.8   2.2   1.4
T4       0.9   1.3   1.7   2.6
```

At this stage, future positions have not yet been restricted.

---

# 7. Applying the Causal Mask

The future positions are masked.

Conceptually, the matrix becomes:

```text
          T1    T2    T3    T4
T1       2.1    -∞    -∞    -∞
T2       0.7    2.4    -∞    -∞
T3       1.0    1.8    2.2    -∞
T4       0.9    1.3    1.7    2.6
```

The `-∞` values mean:

```text
🚫 Do not allow attention to these positions
```

In actual implementations, a sufficiently large negative value may be used instead of literal mathematical infinity.

---

# 8. Why Is the Mask Applied Before Softmax?

This is very important.

The standard attention calculation is:

```text
Attention(Q, K, V)
=
softmax(QKᵀ / √dₖ)V
```

With masking:

```text
Attention(Q, K, V)
=
softmax((QKᵀ / √dₖ) + Mask)V
```

Conceptually:

```text
QKᵀ
 ↓
Scale
 ↓
🎭 Apply Mask
 ↓
Softmax
 ↓
Attention Weights
 ↓
Weighted Values
```

The mask must affect the scores **before softmax** so that masked positions receive essentially zero attention weight.

---

# 9. What Happens During Softmax?

Suppose the scores for one token are:

```text
[2.0, 1.0, -∞, -∞]
```

After softmax, the result is conceptually:

```text
[0.73, 0.27, 0.00, 0.00]
```

The exact values depend on the scores.

The important point is:

```text
-∞
 ↓
Softmax
 ↓
0 probability
```

Therefore, the token cannot receive attention from those masked positions.

---

# 10. Causal Mask as a Lower-Triangular Matrix

The causal mask is often represented conceptually using a lower-triangular pattern:

```text
1  0  0  0
1  1  0  0
1  1  1  0
1  1  1  1
```

Where:

```text
1 = allowed
0 = masked
```

The exact implementation can use different conventions, but the idea remains the same.

---

# 11. Example: Next-Token Prediction

Consider:

```text
The cat is sleeping
```

During training, the model learns:

```text
Input:
The

Target:
cat
```

Then:

```text
Input:
The cat

Target:
is
```

Then:

```text
Input:
The cat is

Target:
sleeping
```

The model must not use the target token itself as information when making the prediction.

Causal masking enforces this restriction.

---

# 12. Causal Masking During Training

One important feature of Transformers is that many token positions can be processed **in parallel during training**.

For example:

```text
The cat is sleeping
```

The model can process the sequence together:

```text
Position 1 → predict cat
Position 2 → predict is
Position 3 → predict sleeping
Position 4 → predict ...
```

But causal masking prevents each position from looking into the future.

Conceptually:

```text
Position 1 → sees [1]
Position 2 → sees [1, 2]
Position 3 → sees [1, 2, 3]
Position 4 → sees [1, 2, 3, 4]
```

So training can be parallelized while still respecting the autoregressive constraint.

---

# 13. Causal Masking During Inference

During generation, the model generates tokens one by one.

For example:

```text
The cat
     ↓
Predict next token
     ↓
is
     ↓
The cat is
     ↓
Predict next token
     ↓
sleeping
```

At each step, the model only has access to the tokens already generated.

Therefore, there are no future generated tokens available to look at.

Causal masking still defines the decoder-only attention behavior, although inference implementations also use optimizations such as **KV caching**.

---

# 14. Attention Masking vs Causal Masking

These terms are related but not identical.

| Term              | Meaning                                                |
| ----------------- | ------------------------------------------------------ |
| Attention Masking | General technique for restricting attention            |
| Causal Masking    | Specific masking strategy that blocks future positions |
| Padding Mask      | Prevents attention to padding tokens                   |
| Mask              | General representation of allowed/blocked positions    |

So:

```text
Attention Masking
       ↓
Different types
       ↓
├── Causal Masking
├── Padding Masking
└── Other architecture-specific masks
```

---

# 15. Padding Masking

Another common reason for masking is **padding**.

Suppose sequences have different lengths:

```text
Sequence 1:
The cat sleeps

Sequence 2:
The dog
```

To put them into the same batch, padding may be added:

```text
The cat sleeps <PAD>
The dog        <PAD>
```

The `<PAD>` position does not represent real content.

A padding mask can prevent the model from attending to padding positions.

Conceptually:

```text
The cat sleeps <PAD>
 ↑    ↑    ↑     ✗
```

The exact handling of padding depends on the model and implementation.

---

# 16. Causal Masking vs Padding Masking

These two masks solve different problems.

| Causal Mask                      | Padding Mask                              |
| -------------------------------- | ----------------------------------------- |
| Blocks future positions          | Blocks padding positions                  |
| Used for autoregressive behavior | Used when padding exists                  |
| Important in decoder-only LLMs   | Useful for variable-length batches        |
| Preserves next-token prediction  | Prevents meaningless padding interactions |

They can also be combined when an architecture requires both restrictions.

---

# 17. Self-Attention With a Causal Mask

In decoder-only LLMs, attention is generally:

```text
Causal Self-Attention
```

The process is:

```text
🧩 Hidden Representations
          ↓
      Q, K, V
          ↓
    QKᵀ / √dₖ
          ↓
   🎭 Causal Mask
          ↓
       Softmax
          ↓
  Attention Weights
          ↓
      Weighted V
          ↓
 Attention Output
```

This is one of the central mechanisms behind GPT-style architectures.

---

# 18. Attention Masking and Query Positions

Each query position has its own allowed keys.

For four tokens:

```text
          Allowed Keys
Query 1 → 1
Query 2 → 1, 2
Query 3 → 1, 2, 3
Query 4 → 1, 2, 3, 4
```

Therefore:

```text
Query 1 → cannot see future
Query 2 → cannot see future
Query 3 → cannot see future
Query 4 → no future token in this sequence
```

This creates the triangular attention pattern.

---

# 19. Masking Does Not Change the Tokens

A mask does not delete tokens from the sequence.

For example:

```text
The cat is sleeping
```

still contains four tokens.

The mask only controls which token positions can contribute through attention.

So:

```text
Tokens ≠ Mask
```

The tokens remain present, but certain attention connections are disabled.

---

# 20. Masking Does Not Change Token IDs

Similarly, masking does not modify Token IDs.

For example:

```text
Tokens:
["The", "cat", "is", "sleeping"]

IDs:
[101, 205, 37, 812]
```

The IDs remain the same.

The mask operates on the **attention relationships between positions**.

```text
Token IDs
    ↓
Embeddings
    ↓
Q, K, V
    ↓
Attention Scores
    ↓
🎭 Mask
```

---

# 21. Masking and Attention Scores

Attention masking directly affects the score matrix.

Before masking:

```text
          T1   T2   T3   T4
T1        ✓    ✓    ✓    ✓
T2        ✓    ✓    ✓    ✓
T3        ✓    ✓    ✓    ✓
T4        ✓    ✓    ✓    ✓
```

After causal masking:

```text
          T1   T2   T3   T4
T1        ✓    ✗    ✗    ✗
T2        ✓    ✓    ✗    ✗
T3        ✓    ✓    ✓    ✗
T4        ✓    ✓    ✓    ✓
```

Therefore:

```text
Mask
 ↓
Changes available attention connections
 ↓
Changes attention weights
 ↓
Changes attention output
```

---

# 22. Masking and Softmax

The order is important:

```text
1. Calculate QKᵀ
          ↓
2. Scale by √dₖ
          ↓
3. Apply mask
          ↓
4. Softmax
          ↓
5. Calculate weighted values
```

Not:

```text
QKᵀ
 ↓
Softmax
 ↓
Mask
```

The mask needs to be applied before softmax so that blocked positions do not receive meaningful attention weight.

---

# 23. Masking in Encoder and Decoder Architectures

Masking depends on the Transformer architecture.

### Encoder

A standard Transformer encoder generally uses full self-attention:

```text
T1 ↔ T2 ↔ T3 ↔ T4
```

Each token can attend to the other tokens, subject to any padding or architecture-specific masks.

### Decoder

A decoder used for autoregressive generation uses causal self-attention:

```text
T1
 ↓
T1 T2
 ↓
T1 T2 T3
 ↓
T1 T2 T3 T4
```

Future positions are blocked.

---

# 24. Causal Masking and Cross-Attention

Cross-attention is different.

In encoder-decoder Transformers, a decoder can attend to encoder representations.

Conceptually:

```text
Encoder Representation
        ↓
     Keys + Values
        ↑
        |
      Query
        |
     Decoder
```

The decoder's cross-attention is not the same as decoder self-attention.

Causal masking is primarily associated with preventing future positions in **autoregressive self-attention**.

Cross-attention can have its own masking rules depending on the architecture and task.

---

# 25. Masking in Multi-Head Attention

Modern Transformers often use multiple attention heads.

Conceptually:

```text
Input
  ↓
┌───────────────┐
│ Attention Head│
│ Attention Head│
│ Attention Head│
│ Attention Head│
└───────────────┘
  ↓
Concatenate
  ↓
Output Projection
```

The appropriate attention mask is applied to the attention scores for the relevant heads.

The exact implementation can vary.

---

# 26. Attention Mask Shape

Suppose:

```text
Sequence Length = 4
```

The attention score matrix has shape:

```text
4 × 4
```

A causal mask therefore needs to represent the allowed relationships between these four positions.

For a batch and multiple heads, the actual tensor shape used by an implementation can contain additional dimensions such as:

```text
Batch × Heads × Sequence Length × Sequence Length
```

The exact broadcasting and storage format depends on the implementation.

---

# 27. Attention Masking and Context

Masking controls what information is available **within the attention operation**.

It does not increase the model's context window.

For example:

```text
Context Window
      ↓
Maximum available tokens
```

while:

```text
Attention Mask
      ↓
Which available positions may interact
```

Therefore:

```text
Context Window ≠ Attention Mask
```

---

# 28. Attention Masking and Token Importance

A mask should not be confused with attention weights.

A mask says:

```text
Allowed / Not allowed
```

Attention weights say:

```text
How much weight each allowed position receives
```

For example:

```text
Mask:

T1 → ✓
T2 → ✓
T3 → ✗
T4 → ✗
```

After softmax, the allowed positions might receive:

```text
T1 → 0.70
T2 → 0.30
T3 → 0.00
T4 → 0.00
```

So:

```text
🎭 Mask
   ↓
Restricts possibilities

🎯 Attention Weights
   ↓
Distribute attention among allowed positions
```

---

# 29. A Simple Numerical Example

Suppose a query produces these scaled attention scores:

```text
[2.0, 1.0, 3.0, 2.5]
```

Suppose the query is at position 2.

Because of causal masking, it can only attend to positions 1 and 2.

So:

```text
Before mask:

[2.0, 1.0, 3.0, 2.5]
```

After mask:

```text
[2.0, 1.0, -∞, -∞]
```

Softmax then produces approximately:

```text
[0.73, 0.27, 0.00, 0.00]
```

Therefore:

```text
Position 1 → contributes
Position 2 → contributes
Position 3 → blocked
Position 4 → blocked
```

The exact probabilities are illustrative.

---

# 30. Why Masking Is Important for LLM Training

Without causal masking, a decoder-only language model could potentially access future tokens during training.

For example:

```text
The cat is sleeping
```

To predict:

```text
sleeping
```

the model should use:

```text
The cat is
```

not:

```text
The cat is sleeping
```

Causal masking ensures that the training setup matches the autoregressive generation process.

This is essential for learning next-token prediction properly.

---

# 31. Attention Masking and Autoregressive Generation

The complete relationship is:

```text
📝 Previous Tokens
       ↓
🔢 Token IDs
       ↓
🧩 Representations
       ↓
👀 Causal Self-Attention
       ↓
🎭 Future Positions Blocked
       ↓
📊 Contextual Representation
       ↓
🎯 Output Layer
       ↓
📈 Logits
       ↓
🎲 Token Selection
       ↓
🔤 Next Token
```

Then the new token is added:

```text
Old Tokens + New Token
        ↓
Causal Self-Attention
        ↓
Next Token
        ↓
🔄 Repeat
```

---

# 32. Attention Masking vs Attention Scores

These concepts should be clearly separated.

| Concept          | Purpose                                |
| ---------------- | -------------------------------------- |
| Attention Score  | Measures Query-Key matching            |
| Attention Mask   | Restricts which positions can interact |
| Attention Weight | Normalized score after softmax         |
| Attention Output | Weighted combination of Values         |

The complete flow is:

```text
Query + Key
     ↓
Attention Scores
     ↓
🎭 Mask
     ↓
Softmax
     ↓
Attention Weights
     ↓
Values
     ↓
Attention Output
```

---

# 33. Common Misunderstandings

### ❌ "Masking removes the future tokens."

Not exactly.

The tokens remain in the sequence, but their contribution through attention is blocked.

---

### ❌ "Masking changes Token IDs."

No.

Token IDs remain unchanged.

---

### ❌ "Masking is the same as attention weights."

No.

A mask controls which positions are allowed.

Attention weights determine how much the allowed positions contribute.

---

### ❌ "Every Transformer uses the same mask."

No.

Different Transformer architectures and tasks can use different masking strategies.

---

### ❌ "Causal masking is only needed during inference."

No.

It is also important during training so that each position cannot use future information.

---

### ❌ "Causal masking means the model processes tokens one at a time during training."

No.

Training can process many positions in parallel while the causal mask prevents future information from being used.

---

# 34. Complete Attention Masking Flow

The complete process can be summarized as:

```text
📝 Input Tokens
      ↓
🧩 Token Representations
      ↓
🔑 Query, Key, Value
      ↓
📊 QKᵀ
      ↓
📏 Scale by √dₖ
      ↓
🎭 Apply Attention Mask
      ↓
🎲 Softmax
      ↓
🎯 Attention Weights
      ↓
🧩 Weighted Values
      ↓
📊 Attention Output
```

For a decoder-only LLM:

```text
          Future Tokens
               ✗
               ✗
               ✗
                \
                 ↓
🧩 Current Token → 👀 Causal Self-Attention
                 ↑
                /
        Previous Tokens
```

---

# 35. Attention Masking in the Complete LLM

Attention masking is one part of the larger LLM architecture:

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
   ↓
   ├── 👀 Self-Attention
   │       ↓
   │   🎭 Attention Mask
   │       ↓
   │   🎯 Attention Output
   │
   └── 🧠 Feed-Forward Network
   ↓
🔄 More Transformer Blocks
   ↓
📊 Final Representation
   ↓
🎯 Language Modeling Head
   ↓
📈 Logits
   ↓
🔤 Next Token
```

Attention masking therefore sits **inside the attention part of the Transformer block**.

---

# 36. Simple Mental Model

Think of attention as a conversation between token positions.

The mask acts like a rule about **who is allowed to listen to whom**.

For causal attention:

```text
Earlier tokens
      ↓
Allowed
      ↓
Current token

Future tokens
      ↓
🚫 Blocked
```

So the simplest mental model is:

> **🎭 Attention masking controls which token positions are allowed to contribute to attention.**

For decoder-only LLMs:

> **Causal masking prevents a token from attending to future tokens.**

---

# 37. Key Takeaways

* 🎭 **Attention masking controls which token positions can interact through attention.**
* 👀 The mask affects the **attention scores**.
* 📊 Masking is applied **before softmax**.
* 🚫 Causal masking blocks future positions.
* 🧠 Decoder-only LLMs use causal self-attention for autoregressive language modeling.
* 🔢 Masking does not change Token IDs.
* 📝 Masking does not delete tokens from the sequence.
* 🎯 Attention weights are calculated after masking and softmax.
* 📦 Padding masks can prevent attention to padding positions.
* 🔄 Training can still process many positions in parallel while causal masking prevents future information from being used.
* 🧩 Different Transformer architectures can use different masking strategies.
* ⚠️ A mask is not the same thing as an attention score or attention weight.

The central idea is:

```text
📊 Attention Scores
        ↓
🎭 Attention Mask
        ↓
🎲 Softmax
        ↓
🎯 Attention Weights
        ↓
🧩 Attention Output
```

And for a decoder-only LLM:

```text
Current Token
     ↓
Can attend to:
✅ Previous Tokens
✅ Current Token
❌ Future Tokens
```
