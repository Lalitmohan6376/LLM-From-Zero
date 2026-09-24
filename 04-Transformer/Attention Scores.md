# 📊 Attention Scores

**Attention scores** are numerical values that measure how strongly a Query matches the Keys of different token positions.

They are an important step inside the **attention mechanism**.

A simplified flow is:

```text
🧩 Input Representations
          ↓
      Query (Q)
      Key (K)
          ↓
    Compare Q and K
          ↓
   📊 Attention Scores
          ↓
      Scaling
          ↓
       Softmax
          ↓
  🎯 Attention Weights
```

The key idea is:

> **Attention scores help determine which token positions should contribute more information to the current token representation.**

---

# 1. 🧠 What Is an Attention Score?

An **attention score** is a numerical value produced when a Query is compared with a Key.

For example:

```text
Query("cat")
      ↓
Compare with Keys
      ↓
┌─────────────────┐
│ Key("The")      │
│ Key("cat")      │
│ Key("sat")      │
│ Key("mat")      │
└─────────────────┘
      ↓
Attention Scores
```

The scores indicate the strength of the numerical match between the Query and each Key.

For example:

```text
Token       Score
-------------------
The          0.8
cat          2.4
sat          1.5
mat          0.3
```

These values are only illustrative.

---

# 2. 🔎 Why Do We Need Attention Scores?

The model needs to determine how much information should come from different token positions.

Consider:

```text
The cat sat on the mat.
```

When processing one position, different tokens may have different levels of relevance.

The model therefore calculates:

```text
Query
  ↓
Compare with Keys
  ↓
Scores
  ↓
Determine relative relevance
```

These scores are later converted into attention weights.

---

# 3. 🔑 Attention Scores Come From Query and Key

Attention scores are calculated using:

```text
Q
```

and:

```text
K
```

The basic calculation is a dot product.

For a single Query and Key:

```text
Score = Q · K
```

For all Queries and Keys:

```text
QKᵀ
```

This produces a matrix of scores.

---

# 4. 📐 Dot Product

A dot product measures how two vectors align numerically.

Suppose:

```text
Q = [1, 2, 3]

K = [2, 1, 4]
```

The dot product is:

```text
Q · K

= (1 × 2)
+ (2 × 1)
+ (3 × 4)

= 2 + 2 + 12

= 16
```

So the attention score is:

```text
16
```

This is a simplified example.

Real Transformers use high-dimensional vectors.

---

# 5. 📊 Multiple Keys

A Query is compared with multiple Keys.

Suppose:

```text
Q
```

is compared with:

```text
K₁
K₂
K₃
K₄
```

The model calculates:

```text
Q · K₁
Q · K₂
Q · K₃
Q · K₄
```

This produces:

```text
Score₁
Score₂
Score₃
Score₄
```

The process can be visualized as:

```text
                 ┌──→ Q · K₁ → Score₁
                 │
Query Q ─────────┼──→ Q · K₂ → Score₂
                 │
                 ├──→ Q · K₃ → Score₃
                 │
                 └──→ Q · K₄ → Score₄
```

---

# 6. 🧩 Attention Score Matrix

In a Transformer, every Query can be compared with multiple Keys.

Suppose there are four token positions.

The score matrix can look like:

```text
             Keys
          K₁   K₂   K₃   K₄
       ┌────────────────────
Q₁     │ 2.1  0.8  1.5  0.4
Q₂     │ 1.2  2.7  0.9  1.1
Q₃     │ 0.6  1.4  2.5  0.7
Q₄     │ 1.0  0.5  1.8  2.2
```

Each:

* Row = Query position
* Column = Key position
* Value = attention score

So:

```text
Score[i][j]
```

represents the score between:

```text
Query i
```

and:

```text
Key j
```

---

# 7. 🔄 What Happens After the Scores?

The raw attention scores are not directly used as the final attention weights.

The model first scales them.

```text
Attention Scores
       ↓
     Scaling
       ↓
Scaled Scores
       ↓
     Softmax
       ↓
Attention Weights
```

The standard scaled calculation is:

```text
Scores = QKᵀ / √dₖ
```

where:

```text
dₖ = dimension of the Key vectors
```

---

# 8. 📏 Why Are Scores Scaled?

When the vectors have many dimensions, their dot products can become large.

For example:

```text
Small Dimension
      ↓
Smaller typical dot products

Large Dimension
      ↓
Potentially larger dot products
```

Very large values can make softmax extremely concentrated.

The scaling factor:

```text
√dₖ
```

helps keep the values in a more suitable range.

Therefore:

```text
QKᵀ
  ↓
Divide by √dₖ
  ↓
Scaled Scores
```

---

# 9. 🎲 Softmax Converts Scores Into Weights

After scaling, the model applies **softmax**.

```text
Scaled Scores
      ↓
    Softmax
      ↓
Attention Weights
```

For example:

```text
Scores:

[1.0, 2.0, 0.5]
```

After softmax, we might get approximately:

```text
[0.23, 0.63, 0.14]
```

These values are illustrative.

The important idea is:

```text
Raw Scores
    ↓
Relative Distribution
    ↓
Attention Weights
```

The weights sum to approximately:

```text
1
```

---

# 10. 📊 Score vs Attention Weight

These two terms should not be confused.

| Attention Score                 | Attention Weight                      |
| ------------------------------- | ------------------------------------- |
| Raw matching value              | Normalized value                      |
| Comes from Query-Key comparison | Comes from softmax                    |
| Can be positive or negative     | Usually between 0 and 1               |
| Not a probability               | Forms a probability-like distribution |
| Used before softmax             | Used to combine Values                |

The simplified flow is:

```text
Query + Key
     ↓
Attention Score
     ↓
Scale
     ↓
Softmax
     ↓
Attention Weight
```

---

# 11. 🔢 Simple Numerical Example

Suppose a Query is compared with three Keys.

The raw scores are:

```text
Key 1 → 1.0
Key 2 → 2.0
Key 3 → 0.5
```

After scaling, suppose they become:

```text
0.5
1.0
0.25
```

Softmax then converts them into weights.

Conceptually:

```text
Scaled Scores
[0.5, 1.0, 0.25]
       ↓
    Softmax
       ↓
Weights
[0.31, 0.51, 0.18]
```

The exact values here are illustrative.

The second Key receives the largest weight because its score was relatively larger.

---

# 12. 📦 Scores Are Used to Select Information

Attention scores themselves do not contain the final information that gets passed forward.

They determine the weights used on the **Value vectors**.

Suppose:

```text
Weights:

w₁
w₂
w₃
```

and:

```text
Values:

V₁
V₂
V₃
```

Then:

```text
Attention Output
=
w₁V₁ + w₂V₂ + w₃V₃
```

So:

```text
Attention Scores
      ↓
Attention Weights
      ↓
How much to use each Value
      ↓
Weighted Values
      ↓
Attention Output
```

---

# 13. 🧠 Higher Score Does Not Mean "More Important" in Every Sense

A common misunderstanding is:

> "The highest attention score means that token is the most important token in the entire sentence."

That is too strong.

An attention score represents the numerical compatibility between a particular:

```text
Query
```

and:

```text
Key
```

at a particular layer and attention head.

Therefore, it is better to say:

> A higher score means a stronger Query-Key match before normalization, within that particular attention calculation.

---

# 14. 🔄 Every Query Gets Its Own Scores

Suppose we have:

```text
The cat sat on the mat.
```

Each Query can produce a different set of scores.

For example:

```text
Q₁ → [s₁₁, s₁₂, s₁₃, s₁₄, ...]
Q₂ → [s₂₁, s₂₂, s₂₃, s₂₄, ...]
Q₃ → [s₃₁, s₃₂, s₃₃, s₃₄, ...]
...
```

Therefore, the complete score matrix contains many different Query-Key comparisons.

---

# 15. 📐 Matrix Calculation

Let:

```text
Q = Query Matrix
K = Key Matrix
```

Then:

```text
QKᵀ
```

calculates all Query-Key dot products together.

For example:

```text
Q
 ↓
┌─────────────┐
│ Query 1     │
│ Query 2     │
│ Query 3     │
└─────────────┘

K
 ↓
┌─────────────┐
│ Key 1       │
│ Key 2       │
│ Key 3       │
└─────────────┘
```

The multiplication:

```text
QKᵀ
```

produces:

```text
┌─────────────────┐
│ S₁₁ S₁₂ S₁₃    │
│ S₂₁ S₂₂ S₂₃    │
│ S₃₁ S₃₂ S₃₃    │
└─────────────────┘
```

where:

```text
Sᵢⱼ = Query i · Key j
```

---

# 16. 🔒 Attention Scores and Causal Masking

Decoder-only LLMs use causal self-attention.

This means future positions cannot contribute to the current position.

Before softmax, forbidden positions are masked.

For example:

```text
             Key
          1   2   3   4
       ┌─────────────────
Q₁     │ ✓   ✗   ✗   ✗
Q₂     │ ✓   ✓   ✗   ✗
Q₃     │ ✓   ✓   ✓   ✗
Q₄     │ ✓   ✓   ✓   ✓
```

Conceptually, the masked positions receive a very large negative value before softmax.

```text
Allowed position
      ↓
Normal score

Masked position
      ↓
Very negative score
      ↓
Softmax
      ↓
Near-zero weight
```

This prevents future tokens from contributing.

---

# 17. 🎯 Why Mask Before Softmax?

Suppose the scores are:

```text
[2.0, 1.0, 3.0, 4.0]
```

If the fourth position is not allowed, it should not receive attention.

The model therefore applies the mask **before softmax**.

Conceptually:

```text
Raw Scores
[2.0, 1.0, 3.0, 4.0]

       ↓

Apply Mask

[2.0, 1.0, 3.0, -∞]

       ↓

Softmax

[weight₁, weight₂, weight₃, ~0]
```

The exact implementation may use a sufficiently large negative value rather than literal negative infinity.

---

# 18. 🧩 Attention Scores in Self-Attention

In self-attention:

```text
Q, K, V
```

are derived from the same sequence representation.

Therefore:

```text
QKᵀ
```

calculates relationships between positions within that sequence.

```text
Input Sequence
      ↓
   Q, K, V
      ↓
   QKᵀ
      ↓
Attention Scores
```

For causal self-attention, the mask is applied before softmax.

---

# 19. 🌐 Attention Scores in Cross-Attention

In cross-attention, Query and Key can come from different representations.

```text
Sequence A
    ↓
    Q

Sequence B
    ↓
    K
```

The scores are still calculated using:

```text
QKᵀ
```

But the Query and Key originate from different sources.

The Values come from the same source as the Keys in standard cross-attention.

```text
Q ← Sequence A

K, V ← Sequence B
```

---

# 20. 🧠 Attention Scores Are Learned Indirectly

The model does not manually store a fixed table of attention scores.

Instead, it learns the parameters used to create:

```text
Q
K
V
```

during training.

```text
Training Data
      ↓
Input Representations
      ↓
Q, K, V
      ↓
Attention Scores
      ↓
Attention Output
      ↓
Prediction
      ↓
Loss
      ↓
Backpropagation
      ↓
Update Parameters
```

Therefore, attention scores are **computed dynamically from the input**.

---

# 21. 🔄 Attention Scores Change With the Input

The same token can produce different attention scores in different contexts.

For example:

```text
The bank approved my loan.
```

and:

```text
The boat reached the river bank.
```

The surrounding context is different.

Therefore, the numerical representations and attention calculations can also differ.

Conceptually:

```text
Same Token
    +
Different Context
    ↓
Different Representations
    ↓
Different Attention Scores
```

---

# 22. 🧠 Attention Scores Change Across Layers

A Transformer usually contains multiple layers or blocks.

Attention scores can differ across:

```text
Layer 1
Layer 2
Layer 3
...
Layer N
```

For example:

```text
Input
  ↓
🔄 Block 1 → Attention Scores₁
  ↓
🔄 Block 2 → Attention Scores₂
  ↓
🔄 Block 3 → Attention Scores₃
  ↓
...
```

Each layer has its own learned parameters.

Therefore, attention patterns can change as representations become more contextual.

---

# 23. 👀 Attention Scores Can Differ Across Heads

In Multi-Head Attention, there are multiple attention heads.

Each head can calculate its own attention patterns.

Conceptually:

```text
Input
  │
  ├──→ Head 1 → Score Matrix 1
  │
  ├──→ Head 2 → Score Matrix 2
  │
  ├──→ Head 3 → Score Matrix 3
  │
  └──→ Head 4 → Score Matrix 4
```

Different heads may learn different relationships.

However, we should not assume a specific human-readable meaning for every head without analyzing the model.

---

# 24. 📊 Attention Score Matrix vs Attention Weight Matrix

These are closely related but different.

### Attention Score Matrix

Before softmax:

```text
QKᵀ / √dₖ
```

Example:

```text
[ 1.2   0.5   2.0
  0.8   1.5   0.2
  2.1   0.4   1.0 ]
```

### Attention Weight Matrix

After softmax:

```text
[ 0.27  0.13  0.60
  0.28  0.57  0.15
  0.66  0.12  0.22 ]
```

The second matrix represents normalized weights.

Simplified:

```text
QKᵀ
 ↓
Scores
 ↓
Scale
 ↓
Mask
 ↓
Softmax
 ↓
Weights
```

---

# 25. 📐 Shape of the Attention Scores

Suppose:

```text
Sequence Length = N
```

Then:

```text
Q shape = N × dₖ
K shape = N × dₖ
```

Therefore:

```text
Kᵀ shape = dₖ × N
```

So:

```text
QKᵀ
```

has shape:

```text
N × N
```

For example:

```text
Sequence Length = 5

Attention Score Matrix:

5 × 5
```

This means every Query position can have a score for every Key position before masking.

---

# 26. ⚡ Why Long Sequences Can Be Expensive

If the sequence length is:

```text
N
```

the attention score matrix has:

```text
N × N
```

entries.

Therefore, the number of pairwise Query-Key interactions grows approximately with:

```text
N²
```

For example:

```text
N = 100

100 × 100 = 10,000
```

while:

```text
N = 1,000

1,000 × 1,000 = 1,000,000
```

This is one reason long-context attention can require substantial computation and memory.

Modern architectures and inference systems use various optimizations to reduce practical costs.

---

# 27. 🔢 Complete Numerical Example

Let's use a very small example.

Suppose:

```text
Q = [1, 2]

K₁ = [1, 0]
K₂ = [0, 1]
```

Calculate the scores.

### Query vs Key 1

```text
Q · K₁

= (1 × 1) + (2 × 0)

= 1
```

### Query vs Key 2

```text
Q · K₂

= (1 × 0) + (2 × 1)

= 2
```

So:

```text
Raw Scores:

[1, 2]
```

If:

```text
dₖ = 2
```

then:

```text
√dₖ = √2
```

Scaled scores:

```text
[1 / √2, 2 / √2]
```

Approximately:

```text
[0.71, 1.41]
```

Then softmax converts them into attention weights.

The second Key receives a larger weight because its Query-Key score is larger.

---

# 28. 📦 From Scores to Final Attention Output

Now suppose the Values are:

```text
V₁ = [1, 0]

V₂ = [0, 2]
```

After softmax, suppose the weights are approximately:

```text
w₁ = 0.33

w₂ = 0.67
```

Then:

```text
Output
=
0.33 × V₁
+
0.67 × V₂
```

So:

```text
Output
=
0.33 × [1, 0]
+
0.67 × [0, 2]
```

which gives approximately:

```text
[0.33, 1.34]
```

This demonstrates the complete idea:

```text
Query + Keys
      ↓
Scores
      ↓
Softmax
      ↓
Weights
      ↓
Values
      ↓
Weighted Output
```

---

# 29. 🔄 Complete Attention Pipeline

The complete scaled dot-product attention mechanism is:

```text id="f3a8p1"
🧩 Input Representation
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
     📊 Raw Scores
          ↓
     Scale by √dₖ
          ↓
   🔒 Apply Mask if Needed
          ↓
    📊 Scaled Scores
          ↓
       Softmax
          ↓
    🎯 Attention Weights
          ↓
       × Values
          ↓
   📦 Attention Output
```

Mathematically:

```text
Attention(Q, K, V)
=
softmax(QKᵀ / √dₖ)V
```

With causal masking, the mask is applied to the scores before softmax.

---

# 30. 🧠 Attention Scores vs Attention Mechanism

It is important to distinguish these concepts.

| Concept          | Meaning                                                 |
| ---------------- | ------------------------------------------------------- |
| Attention        | Complete mechanism for calculating weighted information |
| Query            | Representation used for matching                        |
| Key              | Representation used for matching against Queries        |
| Attention Score  | Raw Query-Key matching value                            |
| Attention Weight | Normalized score after softmax                          |
| Value            | Information combined using the weights                  |
| Attention Output | Weighted combination of Values                          |

Simplified:

```text
Query + Key
      ↓
Attention Score
      ↓
Softmax
      ↓
Attention Weight
      ↓
Value
      ↓
Attention Output
```

---

# 31. ❌ Common Misunderstandings

### ❌ "Attention score is a probability."

Not necessarily.

Raw attention scores are not probabilities.

Softmax converts the scores into normalized weights.

---

### ❌ "The highest score always means the most important word."

Not in a general sense.

It means the Query-Key match is numerically stronger in that particular attention calculation.

---

### ❌ "Attention scores are fixed."

No.

They are computed dynamically from the input representations.

---

### ❌ "Every layer has the same attention scores."

No.

Different layers have different learned parameters and can produce different attention patterns.

---

### ❌ "Every attention head has the same scores."

No.

Different heads can produce different attention patterns.

---

### ❌ "Attention scores directly contain the information passed forward."

No.

The scores are converted into weights, which are then used to combine the Value vectors.

---

# 32. 🧠 Simple Mental Model

Think of attention scores as a **matching signal**.

```text
🔎 Query
   ↓
Compare with
   ↓
🔑 Keys
   ↓
📊 Attention Scores
   ↓
🎲 Softmax
   ↓
🎯 Attention Weights
   ↓
📦 Values
   ↓
🧠 Attention Output
```

The easiest distinction to remember is:

```text
📊 Score
= How strong is the Query-Key match?

🎯 Weight
= After normalization, how much should this Value contribute?
```

---

# 33. 🔑 Key Takeaways

* 📊 **Attention scores** measure the numerical match between Queries and Keys.
* 🔎 A Query is compared with the Keys of relevant token positions.
* 📐 The basic score calculation is based on a dot product.
* 🧩 For all positions, the calculation is:

```text
QKᵀ
```

* 📏 Scaled dot-product attention uses:

```text
QKᵀ / √dₖ
```

* 🎲 Softmax converts scaled scores into attention weights.
* 📦 Attention weights determine how much each Value contributes.
* 🔒 Causal masking prevents future positions from contributing in decoder-only LLMs.
* 📐 For a sequence of length `N`, the attention score matrix has shape `N × N`.
* ⚡ This quadratic relationship is one reason long sequences can be computationally expensive.
* 🔄 Attention scores are computed dynamically from the input.
* 🧠 Scores can differ across inputs, layers, and attention heads.
* 🎯 A high attention score means a stronger Query-Key match in that particular calculation; it should not automatically be interpreted as overall token importance.
* 💡 The complete idea is:

```text
Q + K
  ↓
📊 Attention Score
  ↓
📏 Scaling
  ↓
🎲 Softmax
  ↓
🎯 Attention Weight
  ↓
📦 Weighted Values
  ↓
🧠 Attention Output
```
