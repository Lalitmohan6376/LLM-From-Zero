# 🧩 Token Embeddings

A Transformer cannot directly work with words or tokens as human-readable text.

After tokenization, each token is represented by a **Token ID**.
The Token ID is then converted into a numerical vector called a **Token Embedding**.

The basic flow is:

```text
📝 Text
   ↓
🔤 Tokens
   ↓
🔢 Token IDs
   ↓
🧩 Token Embeddings
   ↓
🤖 Transformer
```

Token embeddings are one of the first important numerical representations used inside an LLM.

---

## 📌 1. What Is a Token Embedding?

A **Token Embedding** is a learned numerical vector that represents a token.

For example, suppose the tokenizer produces:

```text
["The", "cat", "is"]
```

These tokens may have IDs:

```text
[125, 842, 91]
```

The model then maps each ID to a vector:

```text
125 → [0.21, -0.14, 0.63, ...]
842 → [0.52,  0.31, -0.27, ...]
 91 → [-0.18, 0.44, 0.12, ...]
```

These vectors are called **token embeddings**.

---

# 🔢 2. From Token to Token ID

Before understanding embeddings, remember the previous step.

The text:

```text
The cat is
```

is first tokenized:

```text
["The", "cat", "is"]
```

Then the tokens are converted into IDs:

```text
[125, 842, 91]
```

The flow is:

```text
📝 "The cat is"
       ↓
🔤 ["The", "cat", "is"]
       ↓
🔢 [125, 842, 91]
```

The IDs are identifiers used by the model's vocabulary.

---

# 🧩 3. From Token ID to Embedding

Now the model uses each Token ID to retrieve its corresponding vector.

Conceptually:

```text
🔢 Token ID
     ↓
📚 Embedding Matrix
     ↓
🧩 Token Embedding
```

For example:

```text
842
 ↓
Embedding Matrix
 ↓
[0.52, 0.31, -0.27, 0.18, ...]
```

So:

```text
"cat"
 ↓
Token ID: 842
 ↓
Embedding Vector
```

---

# 📚 4. Embedding Matrix

Token embeddings are stored in an **embedding matrix**.

Imagine a vocabulary containing 50,000 tokens.

Suppose every token is represented using a 768-dimensional vector.

The embedding matrix can be viewed as:

```text
50,000 × 768
```

Conceptually:

```text
                  Embedding Dimensions
                ↓   ↓   ↓   ↓   ↓
Token 1       [0.2 0.4 0.1 0.7 ...]
Token 2       [0.5 0.1 0.7 0.3 ...]
Token 3       [0.8 0.6 0.2 0.4 ...]
Token 4       [0.1 0.9 0.5 0.2 ...]
   ...
Token 50,000  [0.3 0.2 0.8 0.6 ...]
```

Each row corresponds to a vocabulary token.

```text
📚 Embedding Matrix
       ↓
One row per token
       ↓
🧩 Token Embedding
```

The actual vocabulary size and embedding dimension depend on the model.

---

# 🔍 5. How Does the Model Find an Embedding?

Suppose:

```text
"cat" → Token ID 842
```

The model uses `842` to access the corresponding row in the embedding matrix.

Conceptually:

```text
Token ID: 842
      ↓
Embedding Matrix
      ↓
Row 842
      ↓
[0.52, 0.31, -0.27, ...]
```

This is called an **embedding lookup**.

The model does not need to calculate a completely new vector from the token ID every time.

It retrieves the learned vector associated with that token.

---

# 🧠 6. Are Embeddings Learned?

Yes.

Token embeddings are **learned during model training**.

At the beginning of training, the embedding values are not meaningful representations.

As training continues, the model updates its parameters, including the embedding parameters.

Simplified:

```text
🎓 Training
    ↓
📚 Training Data
    ↓
🧩 Embedding Parameters
    ↓
🔄 Updated During Training
    ↓
🧠 Learned Representations
```

So token embeddings are part of the model's learned parameters.

---

# 📐 7. What Does an Embedding Vector Look Like?

An embedding is simply a list of numerical values.

For example:

```text
[0.21, -0.14, 0.63, 0.08, -0.52]
```

A real model can use hundreds or thousands of dimensions.

For example:

```text
768 dimensions
```

means one token embedding contains:

```text
768 numerical values
```

The actual dimension depends on the architecture.

---

# 🔢 8. Token ID vs Embedding

These two concepts are very different.

| Token ID                                    | Token Embedding                  |
| ------------------------------------------- | -------------------------------- |
| Integer identifier                          | Numerical vector                 |
| Identifies a token                          | Represents a token numerically   |
| Example: `842`                              | Example: `[0.52, 0.31, ...]`     |
| Comes from vocabulary                       | Retrieved from embedding matrix  |
| Does not contain semantic meaning by itself | Learned representation           |
| Used for embedding lookup                   | Used as input to the Transformer |

Simple flow:

```text
🔢 Token ID
      ↓
📚 Embedding Lookup
      ↓
🧩 Token Embedding
```

---

# 🧠 9. Token Embeddings Do Not Mean the Model Fully Understands the Token

It is important not to think of an embedding as a simple dictionary definition.

For example:

```text
"cat"
```

does not become a vector where:

```text
dimension 1 = animal
dimension 2 = small
dimension 3 = pet
```

The dimensions do not have such simple human-readable meanings.

Instead, the model learns numerical representations that are useful for its neural computations.

```text
🧩 Token Embedding
        ↓
🔄 Transformer Processing
        ↓
📊 Contextual Representation
```

The meaning and contextual information used by the model are not contained in one simple embedding vector alone.

---

# 🔗 10. Embeddings and Context

A token's initial embedding is associated with the token itself.

But after the token passes through Transformer layers, its representation can be influenced by the surrounding context.

For example:

```text
The cat sat on the mat.
```

The initial representation for:

```text
cat
```

is transformed by the Transformer.

Conceptually:

```text
🧩 Token Embedding
       ↓
👀 Self-Attention
       ↓
🧠 Feed-Forward Network
       ↓
🔄 More Transformer Blocks
       ↓
📊 Contextual Representation
```

So we can distinguish:

```text
🧩 Token Embedding
        ↓
Initial token representation

📊 Contextual Representation
        ↓
Representation after Transformer processing
```

---

# 📍 11. Token Embeddings and Position

A token embedding primarily represents the token.

However, the Transformer also needs information about **where the token occurs in the sequence**.

For example:

```text
The cat is sleeping.
```

The positions are:

```text
The       → 1
cat       → 2
is        → 3
sleeping  → 4
```

A simplified conceptual view is:

```text
🧩 Token Embedding
        +
📍 Positional Information
        ↓
📊 Transformer Input
```

Different models use different methods for representing positional information.

---

# 📦 12. A Sequence of Token Embeddings

Suppose the input is:

```text
The cat is sleeping.
```

After tokenization and embedding lookup, we can represent it conceptually as:

```text
[
  embedding_The,
  embedding_cat,
  embedding_is,
  embedding_sleeping,
  embedding_period
]
```

So instead of one vector for the entire sentence, there is a vector representation associated with each token.

```text
"The"       → 🧩 Vector
"cat"       → 🧩 Vector
"is"        → 🧩 Vector
"sleeping"  → 🧩 Vector
"."         → 🧩 Vector
```

This creates a sequence of vectors that can be processed by the Transformer.

---

# 📊 13. Embedding Shape

Suppose an input contains:

```text
10 tokens
```

and the model's embedding dimension is:

```text
768
```

The token embeddings can be viewed conceptually as:

```text
10 × 768
```

That means:

```text
10 token vectors
×
768 values per vector
```

For a batch of multiple sequences, an additional batch dimension is typically present.

A simplified shape can be:

```text
Batch Size × Sequence Length × Embedding Dimension
```

For example:

```text
4 × 10 × 768
```

This represents:

* `4` sequences
* `10` tokens per sequence
* `768` values for each token representation

Actual tensor shapes can vary depending on the framework and implementation.

---

# 🎓 14. Embeddings During Training

During training, token embeddings are part of the parameters that can be updated.

Simplified:

```text
📚 Training Text
      ↓
🔤 Tokens
      ↓
🔢 Token IDs
      ↓
🧩 Embedding Lookup
      ↓
🤖 Transformer
      ↓
🎯 Prediction
      ↓
📉 Loss
      ↓
🔄 Backpropagation
      ↓
⚙️ Parameter Updates
```

The embedding parameters are adjusted through training along with other learnable parameters.

Over many training steps, the model learns representations that are useful for its language-modeling objective.

---

# 🚀 15. Embeddings During Inference

During inference, the model uses its already learned embedding parameters.

For example:

```text
📝 Prompt
   ↓
🔤 Tokenization
   ↓
🔢 Token IDs
   ↓
🧩 Embedding Lookup
   ↓
📍 Positional Information
   ↓
🔄 Transformer
   ↓
🎯 Prediction
```

The embeddings are used as part of the input representation.

The model normally does not update its parameters during standard inference.

---

# 🧪 16. Complete Example

Let's follow a simple sentence:

```text
The cat sleeps.
```

### Step 1 — Input Text

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

The IDs are illustrative.

### Step 4 — Embedding Lookup

Each ID retrieves one vector:

```text
125 → [ ... ]
842 → [ ... ]
631 → [ ... ]
 18 → [ ... ]
```

### Step 5 — Token Embeddings

The sequence is now represented by vectors:

```text
[
  vector_1,
  vector_2,
  vector_3,
  vector_4
]
```

### Step 6 — Positional Information

The model also represents their positions:

```text
The     → Position 1
cat     → Position 2
sleeps  → Position 3
.       → Position 4
```

### Step 7 — Transformer

The representations are passed into the Transformer:

```text
🧩 Token Embeddings
        +
📍 Positional Information
        ↓
🔄 Transformer Blocks
        ↓
📊 Contextual Representations
```

---

# 🔄 17. Complete Flow

The complete process can be summarized as:

```text
                    🧩 TOKEN EMBEDDING FLOW

📝 Human Text
      ↓
🔤 Tokenization
      ↓
🔢 Token IDs
      ↓
📚 Embedding Matrix
      ↓
🔍 Embedding Lookup
      ↓
🧩 Token Embeddings
      ↓
📍 Positional Information
      ↓
📊 Transformer Input
      ↓
🔄 Transformer Blocks
```

---

# 🧠 18. Simple Mental Model

Remember token embeddings with this simple idea:

```text
🔤 Token
   ↓
🔢 Token ID
   ↓
📚 Look up in Embedding Matrix
   ↓
🧩 Vector
   ↓
🤖 Transformer
```

In one sentence:

> **A token embedding is a learned numerical vector associated with a token, obtained from the model's embedding parameters and used as part of the input to the Transformer.**

---

# 🎯 Key Takeaways

* 🧩 A **Token Embedding** is a learned numerical vector associated with a token.
* 🔢 Token IDs are used to find the corresponding embeddings.
* 📚 Embeddings are stored in an embedding matrix.
* 🔍 The process of obtaining a vector from a Token ID is called an embedding lookup.
* 🎓 Token embeddings are learned during model training.
* 📐 An embedding can contain hundreds or thousands of numerical dimensions.
* 🔢 Token IDs and embeddings are not the same thing.
* ⚠️ A Token ID is an identifier, while an embedding is a learned vector representation.
* 🧩 Each token in a sequence has its own embedding.
* 📍 Positional information is also needed so the model can represent token order.
* 👀 Transformer layers then transform the initial token embeddings into contextual representations.
* 🚀 During inference, the model uses its learned embeddings to process new input text.
