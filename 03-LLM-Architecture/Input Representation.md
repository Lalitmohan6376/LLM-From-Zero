# 🧩 Input Representation

Before an LLM can process text with its Transformer, the text must be converted into a numerical representation that the neural network can understand.

The process can be simplified as:

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
🤖 Transformer Input
```

This process is called **Input Representation**.

---

## 📌 1. What Is Input Representation?

**Input representation** is the numerical form of text that is given to the Transformer.

An LLM does not directly receive:

```text
The cat is sleeping.
```

Instead, the text goes through several transformations:

```text
📝 Text
  ↓
🔤 Tokens
  ↓
🔢 Token IDs
  ↓
🧩 Embedding Vectors
  ↓
📍 Positional Information
  ↓
🤖 Transformer
```

The final representation is what the Transformer uses as its input.

---

# 🔤 2. Text Is First Tokenized

The process starts with human-readable text.

For example:

```text
The cat is sleeping.
```

The tokenizer breaks this text into tokens.

A simplified example:

```text
["The", "cat", "is", "sleeping", "."]
```

The exact tokens depend on the tokenizer and model.

For subword tokenization, a word may be split into multiple tokens:

```text
playing
   ↓
["play", "ing"]
```

So the first step is:

```text
📝 Text
  ↓
🔤 Tokens
```

---

# 🔢 3. Tokens Become Token IDs

Every token in the tokenizer vocabulary has an associated numerical ID.

For example:

```text
Token        ID
----------------
"The"        125
"cat"        842
"is"          91
"sleeping"  1742
"."           18
```

Therefore:

```text
["The", "cat", "is", "sleeping", "."]
```

can become:

```text
[125, 842, 91, 1742, 18]
```

These are called **Token IDs**.

The Transformer does not treat these IDs as meaningful numerical values.

For example:

```text
842
```

is simply an identifier for a particular vocabulary token.

It does not mean that `842` contains the meaning of `"cat"`.

---

# 🧩 4. Token IDs Are Converted to Embeddings

Token IDs are used to look up vectors from an **embedding table**.

Conceptually:

```text
🔢 Token ID
     ↓
📚 Embedding Table
     ↓
🧩 Embedding Vector
```

For example:

```text
"The" → [0.21, -0.14, 0.63, ...]
"cat" → [0.52,  0.31, -0.27, ...]
"is"  → [-0.18, 0.44, 0.12, ...]
```

These vectors are called **token embeddings**.

The vectors are learned as part of model training.

---

# 📊 5. Embedding Matrix

The embeddings are stored in a large matrix.

A simplified example:

```text
                 Embedding Dimensions
              ↓    ↓    ↓    ↓
Token 1     [ 0.2, 0.4, 0.1, ... ]
Token 2     [ 0.5, 0.1, 0.7, ... ]
Token 3     [-0.2, 0.3, 0.8, ... ]
Token 4     [ 0.6,-0.1, 0.2, ... ]
   ...
```

Conceptually, the shape is:

```text
Vocabulary Size × Embedding Dimension
```

For example:

```text
50,000 × 768
```

would mean:

* 50,000 vocabulary entries
* Each token has a 768-dimensional embedding

The actual values and dimensions depend on the model.

---

# 📍 6. Token Position

The Transformer also needs information about the order of tokens.

Consider:

```text
The dog chased the cat.
```

The tokens have different positions:

```text
Token        Position
---------------------
The             1
dog             2
chased          3
the             4
cat             5
```

Without positional information, the model would have difficulty representing the order of tokens.

---

# 🧭 7. Positional Information

Positional information tells the model where tokens occur in the sequence.

Conceptually:

```text
🧩 Token Embedding
        +
📍 Positional Information
        ↓
🤖 Transformer Input
```

There are different ways to represent positional information.

Examples include:

* Learned positional embeddings
* Rotary Position Embeddings (RoPE)
* Other positional methods

Different Transformer architectures can use different approaches.

So there is no single universal positional representation used by every LLM.

---

# 🧩 8. Combining Token Information and Position

A simplified conceptual representation is:

```text
Token Embedding
      +
Position Information
      ↓
Input Representation
```

For example:

```text
"The"
   ↓
🧩 Token Embedding
   +
📍 Position 1
   ↓
📊 Input Representation
```

Similarly:

```text
"cat"
   ↓
🧩 Token Embedding
   +
📍 Position 2
   ↓
📊 Input Representation
```

The exact mathematical implementation depends on the model architecture.

---

# 📐 9. Input Representation as a Sequence of Vectors

Suppose our token sequence is:

```text
["The", "cat", "is", "sleeping"]
```

After converting the tokens into representations, we can think of the input as:

```text
[
  vector_for_The,
  vector_for_cat,
  vector_for_is,
  vector_for_sleeping
]
```

Conceptually:

```text
🧩 Vector 1 → "The"
🧩 Vector 2 → "cat"
🧩 Vector 3 → "is"
🧩 Vector 4 → "sleeping"
```

So the Transformer receives a **sequence of numerical vectors**, not raw words.

---

# 📦 10. Sequence Representation

If there are `N` tokens and each token is represented using `D` dimensions, the input representation can be viewed conceptually as:

```text
N × D
```

For example:

```text
4 tokens
×
768 dimensions
```

gives:

```text
4 × 768
```

This means there are 4 token representations, each containing 768 numerical values.

The actual dimensions depend on the model.

---

# 🧠 11. What Happens to the Representation?

Once the input representation is created, it is passed into the Transformer.

```text
📝 Text
   ↓
🔤 Tokens
   ↓
🔢 Token IDs
   ↓
🧩 Embeddings
   ↓
📍 Positional Information
   ↓
📊 Input Representation
   ↓
🔄 Transformer Blocks
```

The Transformer then processes these representations using components such as:

* 👀 Self-Attention
* 🧠 Feed-Forward Networks
* ➕ Residual Connections
* 📏 Layer Normalization

---

# 🔍 12. Input Representation vs Token IDs

These two concepts are different.

| Token IDs                  | Input Representation                   |
| -------------------------- | -------------------------------------- |
| Numerical identifiers      | Numerical vectors                      |
| Identify vocabulary tokens | Represent tokens for neural processing |
| Usually integers           | Usually floating-point values          |
| Example: `[125, 842, 91]`  | Example: `[[0.2, 0.4, ...], ...]`      |
| Used to look up embeddings | Passed into the Transformer            |

Simple flow:

```text
🔢 Token IDs
      ↓
🧩 Embedding Lookup
      ↓
📊 Input Representation
```

---

# 🔍 13. Input Representation vs Token Embeddings

These terms can sometimes be used differently depending on the context.

A simplified distinction is:

### Token Embedding

The learned vector associated with a token.

```text
Token ID
   ↓
Embedding Lookup
   ↓
🧩 Token Embedding
```

### Input Representation

The representation actually prepared for the Transformer, including token information and positional information according to the architecture.

```text
🧩 Token Embedding
       +
📍 Positional Information
       ↓
📊 Input Representation
```

This distinction is useful when learning how a Transformer receives its input.

---

# 🧪 14. Complete Example

Let's follow a simple sentence:

```text
The cat sleeps.
```

### Step 1 — Text

```text
📝 "The cat sleeps."
```

### Step 2 — Tokenization

```text
🔤 ["The", "cat", "sleeps", "."]
```

### Step 3 — Token IDs

```text
🔢 [125, 842, 631, 18]
```

These IDs are only illustrative.

### Step 4 — Token Embeddings

Each ID is mapped to a vector:

```text
125 → [ ... ]
842 → [ ... ]
631 → [ ... ]
 18 → [ ... ]
```

### Step 5 — Positional Information

The tokens also have positions:

```text
The    → Position 1
cat    → Position 2
sleeps → Position 3
.      → Position 4
```

### Step 6 — Input Representation

The model now has numerical representations corresponding to the sequence:

```text
[
  representation_The,
  representation_cat,
  representation_sleeps,
  representation_.
]
```

### Step 7 — Transformer

The representations are passed into the Transformer:

```text
📊 Input Representation
          ↓
🔄 Transformer Blocks
          ↓
📊 Contextual Representations
```

---

# 🔄 15. Input Representation During Generation

Input representation is also created during text generation.

Suppose the user gives:

```text
The cat
```

The process is:

```text
📝 "The cat"
      ↓
🔤 Tokens
      ↓
🔢 Token IDs
      ↓
🧩 Embeddings
      ↓
📍 Positional Information
      ↓
📊 Input Representation
      ↓
🔄 Transformer
      ↓
🎯 Next-Token Prediction
```

Suppose the model generates:

```text
is
```

The sequence becomes:

```text
The cat is
```

The model continues the generation process.

---

# 🎓 16. Input Representation During Training

During training, text also goes through the same basic representation process.

```text
📚 Training Text
      ↓
🔤 Tokenization
      ↓
🔢 Token IDs
      ↓
🧩 Token Embeddings
      ↓
📍 Positional Information
      ↓
📊 Input Representation
      ↓
🔄 Transformer
      ↓
🎯 Prediction
      ↓
📉 Loss
```

The model then uses the loss to update its parameters during training.

---

# 🔗 17. Complete Input Pipeline

The complete process can be summarized as:

```text
                    🧩 INPUT REPRESENTATION

📝 Human Text
      ↓
🔤 Tokenization
      ↓
🔢 Token IDs
      ↓
📚 Embedding Lookup
      ↓
🧩 Token Embeddings
      ↓
📍 Positional Information
      ↓
📊 Input Representation
      ↓
🔄 Transformer Blocks
```

Each stage prepares the information for the next stage.

---

# 🧠 18. Simple Mental Model

You can remember Input Representation like this:

```text
📝 TEXT
   ↓
🔤 TOKENS
   ↓
🔢 IDs
   ↓
🧩 VECTORS
   ↓
📍 POSITION
   ↓
📊 MODEL INPUT
   ↓
🤖 TRANSFORMER
```

Or in one sentence:

> **Input representation is the process of converting tokenized text into numerical vector representations that can be processed by the Transformer.**

---

# 🎯 Key Takeaways

* 🧩 Input representation is the numerical representation of text prepared for the Transformer.
* 🔤 Text is first converted into tokens.
* 🔢 Tokens are converted into Token IDs.
* 📚 Token IDs are used to look up learned embedding vectors.
* 🧩 Token embeddings provide numerical representations for tokens.
* 📍 Positional information represents token order.
* 📊 The resulting representations are passed into the Transformer.
* 🔢 Token IDs are identifiers, not semantic vectors.
* 🧩 Embeddings are learned numerical vectors.
* 📐 The input can be viewed as a sequence of vectors.
* 🔄 Transformer blocks process these representations and build contextual information.
* 🎓 The same basic input-representation process is used during both training and inference.
* ⚙️ The exact implementation of positional information and other components depends on the model architecture.
