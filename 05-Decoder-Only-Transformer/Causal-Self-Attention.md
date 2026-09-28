# 🔒 Causal Self-Attention

**Causal Self-Attention** is the attention mechanism used in decoder-only language models to make **next-token prediction** possible without allowing the model to see future tokens.

It is a special form of **self-attention** where each token can attend only to itself and the tokens that came before it.

---

## 1. What Is Self-Attention?

Self-attention allows tokens in a sequence to interact with other tokens in the same sequence.

For example:

```text
The cat is sleeping
```

When processing `sleeping`, the model can use information from:

```text
The
cat
is
sleeping
```

The model calculates which available tokens are useful for the current token representation.

A simplified view is:

```text
Tokens
  ↓
Queries, Keys, Values
  ↓
Attention Scores
  ↓
Attention Weights
  ↓
Weighted Values
  ↓
New Representations
```

---

# 2. The Problem With Normal Self-Attention

For language generation, we want to predict the next token.

Suppose the sequence is:

```text
The cat is sleeping
```

To predict:

```text
sleeping
```

the model should be able to use:

```text
The cat is
```

But it should **not** be able to look at:

```text
sleeping
```

because that is the answer it is supposed to predict.

If normal bidirectional self-attention were used during next-token training, a position could potentially see future tokens.

That would cause **information leakage**.

---

# 3. Causal Self-Attention Solves This

Causal self-attention restricts the attention connections.

Each position can attend to:

```text
Itself
+
Previous positions
```

but not:

```text
Future positions
```

For example:

```text
Tokens:

The   cat   is   sleeping
```

The attention pattern is:

```text
The       → The
cat       → The, cat
is        → The, cat, is
sleeping  → The, cat, is, sleeping
```

Future tokens are blocked.

---

# 4. Why Is It Called "Causal"?

The word **causal** describes the direction of information flow.

Earlier tokens can influence later predictions:

```text
The
 ↓
cat
 ↓
is
 ↓
sleeping
```

But later tokens cannot influence earlier predictions.

```text
Future
  ✕
Earlier
```

This creates a left-to-right dependency that matches autoregressive language generation.

---

# 5. The Main Rule

The easiest rule to remember is:

> **A token can attend to itself and tokens before it, but not tokens after it.**

For a sequence:

```text
A B C D
```

the allowed attention is:

```text
A → A
B → A B
C → A B C
D → A B C D
```

The blocked connections are:

```text
A → B C D
B → C D
C → D
```

---

# 6. Attention Matrix

Causal attention can be visualized using a matrix.

For:

```text
A B C D
```

we can represent allowed positions using:

```text
1 = allowed
0 = blocked

        A  B  C  D

A       1  0  0  0
B       1  1  0  0
C       1  1  1  0
D       1  1  1  1
```

This creates a triangular pattern.

```text
█
██
███
████
```

The upper-right part represents future positions that are blocked.

---

# 7. Causal Mask

The restriction is implemented using a **causal mask**.

Before softmax, the model modifies attention scores so that future positions cannot receive attention.

The simplified process is:

```text
Q, K, V
  ↓
QKᵀ
  ↓
Scale by √dₖ
  ↓
Apply Causal Mask
  ↓
Softmax
  ↓
Attention Weights
  ↓
Weighted Values
```

The important point is:

> **The causal mask is applied before softmax.**

---

# 8. Attention Without the Mask

Standard scaled dot-product attention is:

```text
Attention(Q, K, V)
=
softmax(QKᵀ / √dₖ)V
```

Without a causal mask, every token could potentially attend to every other token.

For example:

```text
A B C D
```

could produce:

```text
A → A B C D
B → A B C D
C → A B C D
D → A B C D
```

That is useful for many Encoder-style applications, but it is not suitable for ordinary autoregressive next-token prediction.

---

# 9. Attention With the Causal Mask

With causal masking:

```text
A → A
B → A B
C → A B C
D → A B C D
```

The model cannot use future information.

Conceptually:

```text
              Allowed
                 ↓

A → A
B → A B
C → A B C
D → A B C D
```

---

# 10. How the Mask Works Mathematically

Suppose the raw attention scores are:

```text
        A    B    C    D

A      2.1  1.2  0.8  1.5
B      1.0  2.4  1.7  0.9
C      0.5  1.3  2.7  1.8
D      1.2  0.8  1.4  2.9
```

Future positions need to be blocked.

The mask can conceptually transform the scores into:

```text
        A    B    C    D

A      2.1  -∞   -∞   -∞
B      1.0  2.4  -∞   -∞
C      0.5  1.3  2.7  -∞
D      1.2  0.8  1.4  2.9
```

The `-∞` values mean:

> Do not allow attention to these positions.

---

# 11. Why Use Negative Infinity?

Softmax is:

```text
softmax(xᵢ) = eˣⁱ / Σeˣʲ
```

If a score is effectively `-∞`:

```text
e⁻∞ ≈ 0
```

Therefore, after softmax, the blocked position receives approximately:

```text
0
```

attention weight.

So:

```text
Score
 ↓
Mask future position
 ↓
-∞
 ↓
Softmax
 ↓
0 attention weight
```

This prevents the future token from contributing to the attention output.

In actual implementations, a sufficiently large negative value or an equivalent masked operation may be used rather than literally storing mathematical infinity.

---

# 12. Example: Predicting the Next Token

Suppose the training text is:

```text
The cat is sleeping
```

The model learns relationships such as:

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

For the prediction of `sleeping`, the model should only use:

```text
The
cat
is
```

It must not use:

```text
sleeping
```

Causal self-attention enforces this restriction.

---

# 13. Causal Mask During Training

A very important point is that training does **not** necessarily require processing one token at a time.

Suppose we have:

```text
The cat is sleeping
```

The model can process multiple positions in one forward pass.

The causal mask determines what each position can see:

```text
Position 1 → Position 1
Position 2 → Positions 1–2
Position 3 → Positions 1–3
Position 4 → Positions 1–4
```

So:

```text
Parallel computation
+
Causal masking
=
Efficient autoregressive training
```

---

# 14. Training Example

Consider:

```text
Input:

The cat is sleeping
```

The model can make several next-token predictions:

```text
The              → cat
The cat           → is
The cat is        → sleeping
The cat is sleeping → next token
```

These predictions can be calculated together during training.

The causal mask makes sure that each position does not use future information.

---

# 15. Causal Self-Attention During Inference

During generation, suppose the prompt is:

```text
The cat is
```

The model predicts:

```text
sleeping
```

Now the sequence becomes:

```text
The cat is sleeping
```

The model predicts another token.

```text
The cat is sleeping
                    ↓
                 next token
```

This continues autoregressively.

```text
Prompt
  ↓
Causal Self-Attention
  ↓
Next Token
  ↓
Add Token
  ↓
Causal Self-Attention
  ↓
Next Token
  ↓
Repeat
```

---

# 16. Self-Attention vs Causal Self-Attention

| Feature                       | Self-Attention            | Causal Self-Attention                         |
| ----------------------------- | ------------------------- | --------------------------------------------- |
| Same sequence for Q/K/V       | Yes                       | Yes                                           |
| Can attend to previous tokens | Yes                       | Yes                                           |
| Can attend to itself          | Yes                       | Yes                                           |
| Can attend to future tokens   | Depending on masking, yes | No                                            |
| Causal mask                   | Not necessarily           | Yes                                           |
| Common use                    | Encoder-style processing  | Decoder-only autoregressive LLMs              |
| Main purpose                  | Contextual interaction    | Contextual interaction without future leakage |

Causal self-attention is therefore a **masked form of self-attention**.

---

# 17. Encoder Self-Attention vs Causal Self-Attention

### Encoder-style self-attention

Normally:

```text
A B C D
↕ ↕ ↕ ↕
All positions can interact
```

### Decoder-only causal self-attention

```text
A
↙
B
↙ ↙
C
↙ ↙ ↙
D
```

Or as a matrix:

```text
Encoder:

████
████
████
████


Decoder-only:

█
██
███
████
```

The exact masking behavior can vary with padding and other implementation details, but the key distinction is the restriction on future positions.

---

# 18. Causal Self-Attention Inside a Transformer Block

A simplified decoder-only Transformer block looks like:

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

Modern architectures may use a different normalization order, such as **pre-normalization**.

The important part here is:

```text
Causal Self-Attention
```

is the attention mechanism that prevents future-token access.

---

# 19. Query, Key, and Value

Causal self-attention still uses the normal Q, K, and V mechanism.

Given an input representation `X`:

```text
Q = XWQ
K = XWK
V = XWV
```

Then:

```text
Scores = QKᵀ / √dₖ
```

After applying the causal mask:

```text
Masked Scores
      ↓
Softmax
      ↓
Attention Weights
```

Finally:

```text
Attention Output
=
Attention Weights × V
```

So causal self-attention is not a completely different attention algorithm.

The main difference is the **causal restriction**.

---

# 20. Complete Mathematical Flow

The simplified calculation is:

```text
Q = XWQ
K = XWK
V = XWV
```

Then:

```text
Scores = QKᵀ / √dₖ
```

Then:

```text
Masked Scores = Apply Causal Mask(Scores)
```

Then:

```text
Weights = softmax(Masked Scores)
```

Finally:

```text
Output = Weights V
```

In one expression:

```text
Attention(Q,K,V)
=
softmax(
    CausalMask(QKᵀ / √dₖ)
)V
```

The exact implementation may represent masking differently, but the conceptual order is:

```text
Scores
  ↓
Mask
  ↓
Softmax
  ↓
Weighted Values
```

---

# 21. Why the Mask Must Come Before Softmax

This is an important detail.

Correct:

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
Mask
```

Why?

Because softmax converts scores into normalized attention weights.

If future tokens are already converted into non-zero probabilities, simply removing them afterward would require renormalizing the remaining weights.

Applying the mask before softmax directly makes the forbidden positions receive zero probability after softmax.

---

# 22. Multi-Head Causal Self-Attention

Modern Transformer blocks usually use **Multi-Head Attention**.

Instead of one attention operation:

```text
Input
  ↓
Attention
```

we have multiple attention heads:

```text
             Input
               ↓
      ┌────────┼────────┐
      ↓        ↓        ↓
    Head 1   Head 2   Head 3   ...
      ↓        ↓        ↓
      └────────┼────────┘
               ↓
           Concatenate
               ↓
         Output Projection
```

Each head applies causal masking.

So:

```text
Head 1 → Causal Attention
Head 2 → Causal Attention
Head 3 → Causal Attention
...
```

The heads can learn different patterns from the sequence, although their learned behavior is not guaranteed to have a simple human-interpretable meaning.

---

# 23. What Does Causal Self-Attention Actually Do?

A useful conceptual description is:

> **It allows each token position to combine information from the available previous context while preventing information from future positions from entering that representation.**

For example:

```text
The cat is sleeping
```

When processing `is`, the model can use:

```text
The
cat
is
```

but not:

```text
sleeping
```

The attention weights determine how much information comes from each allowed position.

---

# 24. Causal Attention Does Not Mean "Only the Previous Token"

This is a common misunderstanding.

Causal attention does **not** mean:

```text
Current token → immediately previous token only
```

Instead:

```text
Current token
      ↓
Can attend to all previous available tokens
```

For example:

```text
The cat is sleeping
```

When processing `sleeping`, the model can potentially use:

```text
The
cat
is
sleeping
```

The attention mechanism decides how much each position contributes.

---

# 25. Long-Range Context

Because a token can attend to earlier tokens, causal self-attention can connect information across a long sequence.

Example:

```text
The movie was released many years ago.
...
...
...
The director later won an award.
```

When processing later tokens, the model can potentially use earlier context if it remains within the model's available context window.

This helps Transformer models model relationships that may span many tokens.

---

# 26. Causal Mask and Context Window

Causal masking does not determine how much total text the model can process.

That is controlled by the model's **context window**.

For example:

```text
Context Window
      ↓
Maximum available sequence length
```

Inside that sequence:

```text
Causal Mask
      ↓
Controls which positions can attend to future positions
```

So these are different concepts:

```text
Context Window
= How much token context can be available

Causal Mask
= Which positions are allowed to interact
```

---

# 27. Causal Mask Does Not Remove Tokens

The causal mask does not delete future tokens from the input sequence.

For example:

```text
A B C D
```

The tokens still exist.

The mask only controls attention connections:

```text
A → A
B → A B
C → A B C
D → A B C D
```

So:

```text
Mask ≠ Token Removal
```

---

# 28. Causal Mask Does Not Change Token IDs

Suppose token IDs are:

```text
[15, 82, 31, 104]
```

The causal mask does not change them.

It controls the attention calculation after the token representations are formed.

Conceptually:

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

---

# 29. Causal Self-Attention and Next-Token Prediction

The relationship can be summarized as:

```text
Previous Tokens
      ↓
Causal Self-Attention
      ↓
Contextual Representation
      ↓
LM Head
      ↓
Logits
      ↓
Probability Distribution
      ↓
Next Token
```

This is the core generation mechanism of decoder-only language models.

---

# 30. Causal Self-Attention and GPT-Style Models

GPT-style models use a decoder-only Transformer architecture.

A simplified GPT-style flow is:

```text
Text
 ↓
Tokenizer
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
Transformer Block
 ↓
Repeat Many Times
 ↓
LM Head
 ↓
Logits
 ↓
Next Token
```

Causal self-attention is therefore one of the central mechanisms that allows these models to generate text autoregressively.

---

# 31. Causal Self-Attention During Generation

Suppose the current sequence is:

```text
I want to learn
```

The model predicts:

```text
Python
```

Now:

```text
I want to learn Python
```

The next prediction can use the expanded context.

```text
I
want
to
learn
Python
```

The model still cannot use a future token that has not been generated yet.

So the information flow remains:

```text
Past → Present → Future
```

not:

```text
Future → Present
```

---

# 32. KV Cache

During autoregressive generation, the model repeatedly performs attention.

Previously calculated **Keys and Values** can be stored in a KV cache.

```text
Previous Tokens
      ↓
Previous K/V
      ↓
KV Cache
      ↓
Current Token
      ↓
Attention
      ↓
Next Token
```

This avoids recomputing the same previous K/V representations at every generation step.

The cache stores:

```text
K
V
```

not:

```text
Q
```

The exact caching strategy can vary across model architectures and implementations.

---

# 33. Computational Cost

Standard self-attention creates an attention score matrix with approximately:

```text
Sequence Length × Sequence Length
```

If the sequence length is `N`, the attention matrix is approximately:

```text
N × N
```

So increasing sequence length can significantly increase attention computation and memory usage.

Causal masking does not remove the basic quadratic structure of standard attention computation.

It only restricts which entries are allowed to contribute.

---

# 34. A Simple Example

Consider:

```text
"I love machine learning"
```

Tokens:

```text
I | love | machine | learning
```

The causal attention pattern is:

```text
             I  love  machine  learning

I            ✓   ✗      ✗         ✗
love         ✓   ✓      ✗         ✗
machine      ✓   ✓      ✓         ✗
learning     ✓   ✓      ✓         ✓
```

When processing `machine`, the model can use:

```text
I
love
machine
```

but not:

```text
learning
```

When processing `learning`, all previous tokens are available.

---

# 35. Causal Self-Attention in One Diagram

```text
                   Input Tokens
                        ↓
                Q, K, V Projections
                        ↓
                 Attention Scores
                        ↓
                 Causal Mask
                        ↓
                     Softmax
                        ↓
                Attention Weights
                        ↓
                Weighted Values
                        ↓
               Attention Output
                        ↓
              Feed-Forward Network
                        ↓
             Transformer Block Output
```

This process is repeated across many Transformer blocks.

---

# 36. Common Misunderstandings

### ❌ "Causal means the model only sees one previous token."

No.

It can attend to all allowed previous tokens.

---

### ❌ "The future tokens are deleted."

No.

They remain in the sequence; their attention connections are blocked.

---

### ❌ "The mask is applied after softmax."

Normally, the causal restriction is applied to the attention scores before softmax.

---

### ❌ "Causal self-attention is different from self-attention in every way."

No.

It is self-attention with a causal restriction.

---

### ❌ "Causal masking is only needed during generation."

No.

It is also essential during training for autoregressive language modeling.

---

### ❌ "Causal masking makes training sequential."

Not necessarily.

Training can process many positions in parallel while using the mask to prevent future information leakage.

---

### ❌ "Causal self-attention means the model understands causality in the real world."

No.

"Causal" here refers to the **direction of information flow between token positions**, not scientific or real-world causal reasoning.

---

# 37. Causal Self-Attention vs Cross-Attention

These mechanisms should not be confused.

### Causal Self-Attention

```text
Same sequence
     ↓
Q, K, V
     ↓
Future positions blocked
```

### Cross-Attention

```text
Sequence A → Queries

Sequence B → Keys + Values
```

Cross-attention is used in the original Encoder-Decoder Transformer to allow the Decoder to use Encoder representations.

A standard decoder-only LLM does not have that separate Encoder-to-Decoder cross-attention pathway.

---

# 38. Causal Self-Attention vs Padding Mask

These are also different.

### Causal Mask

Controls:

```text
Future token visibility
```

### Padding Mask

Controls:

```text
Padding-token visibility
```

For example:

```text
Sequence 1:
I love AI

Sequence 2:
I like AI today
```

If sequences are padded to the same length, padding positions may need to be ignored.

A model can use both causal and padding-related masking depending on the implementation.

---

# 39. Complete Mental Model

Remember these four steps:

```text
1. Calculate attention scores
             ↓
2. Block future positions
             ↓
3. Apply softmax
             ↓
4. Mix information from allowed tokens
```

In other words:

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
    ↓
Attention Output
```

---

# 40. Final Summary

Causal Self-Attention is a **masked version of self-attention** used for autoregressive language modeling.

Its core rule is:

> **Each token can attend to itself and earlier tokens, but not future tokens.**

The complete idea is:

```text
Previous Tokens
      ↓
Q, K, V
      ↓
Attention Scores
      ↓
Causal Mask
      ↓
Softmax
      ↓
Attention Weights
      ↓
Weighted Values
      ↓
Contextual Representation
      ↓
Next-Token Prediction
```

The most important points to remember are:

* 🔹 Causal self-attention is used in decoder-only language models.
* 🔹 It prevents future-token information from being used.
* 🔹 The causal mask is applied before softmax.
* 🔹 A token can attend to all allowed previous tokens, not only the immediately previous token.
* 🔹 Training can process many positions in parallel.
* 🔹 Generation is normally autoregressive, producing one new token at a time.
* 🔹 Causal masking controls attention visibility; it does not delete tokens.
* 🔹 The attention mechanism still uses Queries, Keys, and Values.
* 🔹 KV caching can speed up autoregressive generation by reusing previous Keys and Values.
* 🔹 "Causal" here refers to information-flow direction, not real-world causality.

At its core:

```text
Previous Context
       ↓
Causal Self-Attention
       ↓
Current Representation
       ↓
Next-Token Prediction
```
