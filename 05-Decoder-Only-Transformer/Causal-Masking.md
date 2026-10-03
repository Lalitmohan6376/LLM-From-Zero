# 🎭 Causal Maskings

**Causal Masking** is a technique used in decoder-only Transformers to prevent a token from attending to **future tokens**.

It ensures that when the model predicts the next token, it can only use information that would already be available.

The core idea is simple:

```text
Past tokens     → Allowed ✅
Current token   → Allowed ✅
Future tokens   → Blocked ❌
```

---

# 1. Why Do We Need Causal Masking?

A language model is commonly trained to predict the next token.

For example:

```text
The cat is sleeping
```

The model should learn:

```text
The              → cat
The cat           → is
The cat is        → sleeping
```

When predicting `sleeping`, the model should not already have access to:

```text
sleeping
```

Otherwise, the model would see the answer during training.

Causal masking prevents this information leakage.

---

# 2. The Problem With Normal Self-Attention

Suppose we have:

```text
A B C D
```

Without masking, self-attention can allow every position to attend to every other position:

```text
A → A B C D
B → A B C D
C → A B C D
D → A B C D
```

This is useful for bidirectional processing.

But for autoregressive language modeling, future information must be blocked.

We want:

```text
A → A
B → A B
C → A B C
D → A B C D
```

Causal masking creates this restriction.

---

# 3. What Is a Mask?

A mask is a mechanism that tells the attention calculation:

> **Which positions are allowed to interact and which positions are not.**

For causal attention:

```text
Allowed    → 1
Blocked    → 0
```

For the sequence:

```text
A B C D
```

the causal mask can be represented as:

```text
        A  B  C  D

A       1  0  0  0
B       1  1  0  0
C       1  1  1  0
D       1  1  1  1
```

The lower-triangular region is allowed.

The upper-triangular region is blocked.

---

# 4. Visualizing the Causal Mask

A simple visualization is:

```text
█
██
███
████
```

The filled area represents allowed attention.

The missing area represents future positions.

For example:

```text
             Key Position

             A  B  C  D
Query A      ✓  ✗  ✗  ✗
Query B      ✓  ✓  ✗  ✗
Query C      ✓  ✓  ✓  ✗
Query D      ✓  ✓  ✓  ✓
```

---

# 5. What Does Each Row Mean?

Each row represents the token that is currently producing a query.

For example:

```text
Query B
```

can attend to:

```text
A
B
```

but not:

```text
C
D
```

Similarly:

```text
Query C
```

can attend to:

```text
A
B
C
```

but not:

```text
D
```

So:

```text
A → A
B → A B
C → A B C
D → A B C D
```

---

# 6. Where Is the Mask Applied?

The causal mask is applied to the **attention scores**.

The simplified attention process is:

```text
Q, K, V
  ↓
QKᵀ
  ↓
Scale by √dₖ
  ↓
Causal Mask
  ↓
Softmax
  ↓
Attention Weights
  ↓
Multiply by V
  ↓
Attention Output
```

The important order is:

```text
Scores
  ↓
Mask
  ↓
Softmax
```

---

# 7. Attention Scores Before Masking

Suppose the scaled attention scores are:

```text
        A     B     C     D

A      2.1   1.2   0.8   1.5
B      1.0   2.4   1.7   0.9
C      0.5   1.3   2.7   1.8
D      1.2   0.8   1.4   2.9
```

Without a causal mask, every value could participate in softmax.

But this would allow future information.

So we need to modify the future positions.

---

# 8. Applying the Causal Mask

After masking:

```text
        A     B     C     D

A      2.1   -∞    -∞    -∞
B      1.0   2.4   -∞    -∞
C      0.5   1.3   2.7   -∞
D      1.2   0.8   1.4   2.9
```

The future positions have been replaced conceptually with:

```text
-∞
```

This tells softmax:

> These positions should receive zero attention probability.

---

# 9. Why Use `-∞`?

Softmax converts scores into probabilities:

```text
softmax(xᵢ)
=
eˣⁱ / Σeˣʲ
```

If a score is:

```text
-∞
```

then:

```text
e⁻∞ = 0
```

Therefore:

```text
-∞
  ↓
Softmax
  ↓
0
```

So the blocked position receives zero attention weight.

This is the main mathematical idea behind causal masking.

---

# 10. Why the Mask Comes Before Softmax

The correct order is:

```text
Attention Scores
      ↓
Causal Mask
      ↓
Softmax
      ↓
Attention Weights
```

Not:

```text
Attention Scores
      ↓
Softmax
      ↓
Causal Mask
```

Why?

Because softmax converts all available scores into a normalized distribution.

If future positions are allowed during softmax, they can receive non-zero probability.

By masking first, future positions contribute zero probability from the beginning.

---

# 11. Mathematical Form

Normal scaled dot-product attention is:

```text
Attention(Q, K, V)
=
softmax(QKᵀ / √dₖ)V
```

With causal masking:

```text
Attention(Q, K, V)
=
softmax(
    Mask(QKᵀ / √dₖ)
)V
```

Conceptually:

```text
QKᵀ / √dₖ
       ↓
Causal Mask
       ↓
Softmax
       ↓
Attention Weights
       ↓
× V
```

The exact implementation may use a large negative value or an optimized masking operation instead of literally storing `-∞`.

---

# 12. Example With Four Tokens

Consider:

```text
The cat is sleeping
```

The positions are:

```text
1 = The
2 = cat
3 = is
4 = sleeping
```

The causal mask is:

```text
        1  2  3  4

1       1  0  0  0
2       1  1  0  0
3       1  1  1  0
4       1  1  1  1
```

Therefore:

```text
"The"
    → The

"cat"
    → The, cat

"is"
    → The, cat, is

"sleeping"
    → The, cat, is, sleeping
```

---

# 13. Why Can the Current Token Attend to Itself?

The causal rule is:

> A token cannot attend to **future** tokens.

It can still attend to itself.

Therefore:

```text
A → A
B → A B
C → A B C
D → A B C D
```

This is useful because the current token representation can participate in its own attention calculation.

---

# 14. Causal Mask Does Not Delete Tokens

This is an important distinction.

Suppose the sequence is:

```text
A B C D
```

Causal masking does **not** remove:

```text
C
D
```

The tokens still exist.

Instead, it blocks certain attention connections:

```text
A → B ❌
A → C ❌
A → D ❌
```

So:

```text
Causal Mask
    ≠
Token Removal
```

It controls information flow.

---

# 15. Causal Mask Does Not Change Token IDs

Suppose token IDs are:

```text
[15, 82, 31, 104]
```

The causal mask does not change them.

The process is:

```text
Token IDs
    ↓
Embeddings
    ↓
Q, K, V
    ↓
Attention Scores
    ↓
Causal Mask
```

The mask operates on the attention calculation, not on the tokenizer output.

---

# 16. Causal Mask During Training

Causal masking is extremely important during autoregressive training.

Suppose the sequence is:

```text
The cat is sleeping
```

The model needs to learn:

```text
The              → cat
The cat           → is
The cat is        → sleeping
```

During one forward pass, the model can process many positions in parallel.

The mask ensures:

```text
Position 1
→ sees position 1

Position 2
→ sees positions 1–2

Position 3
→ sees positions 1–3

Position 4
→ sees positions 1–4
```

So:

```text
Parallel computation
        +
Causal masking
        ↓
Efficient autoregressive training
```

---

# 17. Causal Mask During Inference

During generation, suppose the current sequence is:

```text
The cat is
```

The model predicts:

```text
sleeping
```

After adding the token:

```text
The cat is sleeping
```

the model predicts the next token.

The causal rule continues to apply:

```text
Earlier tokens
      ↓
Current prediction
      ↓
Future token
```

The future token does not exist yet, so it cannot provide information.

---

# 18. Training vs Inference

| Feature                               | Training  | Inference                                 |
| ------------------------------------- | --------- | ----------------------------------------- |
| Causal masking                        | Yes       | Conceptually yes                          |
| Future information blocked            | Yes       | Yes                                       |
| Multiple positions processed together | Often yes | Usually new tokens generated sequentially |
| Target tokens available               | Yes       | No future target                          |
| Parameter updates                     | Yes       | No                                        |

The mask is especially important during training because the complete training sequence is already present.

---

# 19. Causal Mask and Autoregressive Generation

Causal masking creates the correct information flow:

```text
Previous Tokens
      ↓
Attention
      ↓
Current Representation
      ↓
Next Token
```

Then:

```text
New Token
    ↓
Added to Context
    ↓
Attention
    ↓
Next Token
```

So the model generates text autoregressively.

---

# 20. Causal Mask vs Causal Self-Attention

These terms are closely related but not identical.

### Causal Mask

The **restriction** that blocks future positions.

```text
Future positions → blocked
```

### Causal Self-Attention

The complete self-attention operation using that restriction.

```text
Q, K, V
  ↓
Attention Scores
  ↓
Causal Mask
  ↓
Softmax
  ↓
Weighted Values
```

So:

```text
Causal Mask
      ↓
Part of
      ↓
Causal Self-Attention
```

---

# 21. Causal Mask vs Normal Self-Attention

### Normal self-attention

Depending on the architecture and masks used:

```text
A → A B C D
B → A B C D
C → A B C D
D → A B C D
```

### Causal self-attention

```text
A → A
B → A B
C → A B C
D → A B C D
```

The difference is the restriction on future positions.

---

# 22. Encoder vs Decoder Masking

A simplified comparison:

### Encoder

Normally uses non-causal self-attention:

```text
████
████
████
████
```

A token can normally use information from both earlier and later positions.

### Decoder-only LLM

Uses causal self-attention:

```text
█
██
███
████
```

Future positions are blocked.

Padding-related masks can also be used when necessary.

---

# 23. Causal Mask and Padding Mask

These two masks solve different problems.

### Causal Mask

Prevents:

```text
Future-token attention
```

### Padding Mask

Prevents attention to:

```text
Padding tokens
```

For example, if sequences have different lengths:

```text
Sequence 1:
I love AI

Sequence 2:
I love machine learning
```

Padding may be added to make their lengths equal.

The model may then need padding-related masking in addition to causal masking.

---

# 24. Combining Masks

In some implementations, multiple masking requirements can be combined.

For example:

```text
Causal Mask
     +
Padding Mask
     ↓
Final Attention Mask
     ↓
Attention Calculation
```

The exact implementation depends on the model and framework.

The important idea is that different masks can control different visibility constraints.

---

# 25. Causal Mask in Multi-Head Attention

Decoder-only Transformers commonly use multiple attention heads.

Each head performs attention over the sequence.

The causal restriction applies to the attention computation of the heads.

Conceptually:

```text
                 Input
                   ↓
        ┌──────────┼──────────┐
        ↓          ↓          ↓
      Head 1     Head 2     Head 3
        ↓          ↓          ↓
   Causal Mask Causal Mask Causal Mask
        ↓          ↓          ↓
        └──────────┼──────────┘
                   ↓
             Concatenate
                   ↓
           Output Projection
```

---

# 26. Causal Mask and Attention Scores

The mask operates on the relationship between:

```text
Query positions
```

and:

```text
Key positions
```

For example:

```text
Query → Current token position
Key   → Token being attended to
```

The causal rule is:

```text
Key position > Query position
          ↓
       Blocked
```

In simpler words:

> A query position cannot attend to a key position that occurs later in the sequence.

---

# 27. A More Formal View

Let:

```text
i = query position
j = key position
```

Causal attention allows the connection when:

```text
j ≤ i
```

and blocks it when:

```text
j > i
```

So:

```text
Allowed:

j ≤ i

Blocked:

j > i
```

For example, if the query is at position `3`:

```text
j = 1 → allowed
j = 2 → allowed
j = 3 → allowed
j = 4 → blocked
```

---

# 28. Why This Is Called a Lower-Triangular Mask

For a sequence of length `4`:

```text
1 0 0 0
1 1 0 0
1 1 1 0
1 1 1 1
```

All the allowed positions are on and below the diagonal.

Therefore, the mask is called **lower triangular**.

The diagonal represents:

```text
Current token → itself
```

The lower part represents:

```text
Current token → previous tokens
```

The upper part represents:

```text
Current token → future tokens
```

and is blocked.

---

# 29. Causal Mask and Information Leakage

Without causal masking:

```text
Future token
     ↓
Current prediction
```

could happen during training.

This creates information leakage.

With causal masking:

```text
Past
 ↓
Current
 ↓
Future
```

Information flows in the correct autoregressive direction.

This makes the training objective match the generation process.

---

# 30. Why Causal Masking Is Important for GPT-Style Models

GPT-style models are decoder-only language models.

Their basic objective is:

```text
Previous Tokens
      ↓
Predict Next Token
```

Causal masking makes sure the model cannot cheat by using future tokens during training.

Therefore:

```text
Decoder-Only Transformer
        ↓
Causal Self-Attention
        ↓
Causal Masking
        ↓
Future Information Blocked
        ↓
Next-Token Prediction
```

---

# 31. Causal Mask and Context

Causal masking does not decide how much context the model can store.

That is determined by the model's **context window**.

For example:

```text
Context Window
      ↓
How many tokens can be processed
```

while:

```text
Causal Mask
      ↓
Which token positions can attend to which positions
```

Therefore:

```text
Context Window ≠ Causal Mask
```

---

# 32. Causal Mask Does Not Mean the Model Has No Future Information

During training, the entire sequence may physically exist in the input:

```text
The cat is sleeping
```

But the model's attention computation is restricted.

So there is a difference between:

```text
Token exists in the input
```

and:

```text
Token is allowed to influence this position
```

Causal masking controls the second one.

---

# 33. Simple Numerical Example

Suppose one query has these attention scores:

```text
A     B     C     D

2.0   1.0   3.0   4.0
```

If the query is at position `2`, it can attend only to:

```text
A
B
```

So the masked scores become:

```text
2.0   1.0   -∞   -∞
```

After softmax:

```text
A     B     C     D

~0.73 ~0.27  0     0
```

The exact values depend on the scores, but the important point is:

```text
Future positions → 0 attention weight
```

---

# 34. Causal Mask in One Complete Flow

```text
                 Input Sequence
                       ↓
                  Token IDs
                       ↓
                  Embeddings
                       ↓
                    Q, K, V
                       ↓
              Attention Scores
                       ↓
              Scale by √dₖ
                       ↓
                Causal Mask
                       ↓
              Future = -∞
                       ↓
                   Softmax
                       ↓
             Future = 0 weight
                       ↓
              Weighted Values
                       ↓
             Attention Output
```

---

# 35. Common Misunderstandings

### ❌ "Causal masking removes future tokens."

No.

It blocks their attention connections.

---

### ❌ "Causal masking changes token IDs."

No.

Token IDs remain unchanged.

---

### ❌ "The mask is applied to embeddings."

No.

Conceptually, it is applied to the attention scores.

---

### ❌ "The mask is applied after softmax."

Normally, no.

The causal restriction is applied before softmax.

---

### ❌ "Only the immediately previous token is allowed."

No.

All previous available tokens can be attended to.

---

### ❌ "Causal masking is only needed during inference."

No.

It is essential during autoregressive training as well.

---

### ❌ "Causal means real-world cause and effect."

No.

Here, causal refers to the direction of information flow between token positions.

---

# 36. Simple Mental Model

Think of causal masking like a one-way window.

```text
Past  →  Current  →  Future

Current can look backward.
Current cannot look forward.
```

Or:

```text
          👀
           ↓

Past   Past   Current   Future
  ✓      ✓       ✓         ✗
```

The model can use what has already happened in the sequence, but not what comes later.

---

# 37. Key Takeaways

* 🔹 **Causal masking prevents future-token information from being used.**
* 🔹 It is used for autoregressive language modeling.
* 🔹 It creates a lower-triangular attention pattern.
* 🔹 A token can attend to itself and previous tokens.
* 🔹 Future positions are blocked.
* 🔹 The mask is applied to attention scores before softmax.
* 🔹 Blocked scores can be represented conceptually as `-∞`.
* 🔹 After softmax, blocked positions receive zero attention weight.
* 🔹 Causal masking does not remove tokens or change token IDs.
* 🔹 Training can still process multiple positions in parallel.
* 🔹 Causal masking is different from padding masking.
* 🔹 Causal masking is a component of causal self-attention.

The core idea is:

```text
Attention Scores
      ↓
Block Future Positions
      ↓
Softmax
      ↓
Future Positions = 0 Weight
      ↓
Use Only Allowed Context
```
