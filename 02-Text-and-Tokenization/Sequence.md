# 🔢 Sequence

A **sequence** is an ordered collection of tokens that an LLM processes as a single piece of input.

After text is tokenized and converted into Token IDs, those IDs form a **sequence**.

> 💡 **Simple idea:** A sequence is an ordered list of tokens that the model processes together.

---

# 🧠 From Text to Sequence

Consider:

```text
📝 "The cat sleeps."
```

The tokenizer may produce:

```text
🧩 ["The", "cat", "sleeps", "."]
```

These tokens are then converted into Token IDs:

```text
🔢 [125, 842, 731, 18]
```

This ordered list is a **token sequence**.

```text
📝 Text
   ↓
🔤 Tokenization
   ↓
🧩 Tokens
   ↓
🔢 Token IDs
   ↓
📏 Sequence
```

---

# 📋 What Makes It a Sequence?

The important part of a sequence is **order**.

For example:

```text
The cat sleeps
```

and:

```text
The sleeps cat
```

contain the same words, but their order is different.

The token sequences are therefore different:

```text
[The, cat, sleeps]
```

versus:

```text
[The, sleeps, cat]
```

The order of tokens affects the meaning and interpretation of the input.

---

# 🔢 Token Sequence

A sequence can be represented using Token IDs.

For example:

```text
📝 "I love AI."

       ↓

🧩 ["I", "love", "AI", "."]

       ↓

🔢 [40, 1842, 9552, 18]
```

The model works with the numerical representation.

Conceptually:

```text
🔢 [40, 1842, 9552, 18]
              ↓
          🧠 LLM
```

---

# 📏 Sequence Length

**Sequence length** is the number of tokens in a sequence.

For example:

```text
["I", "love", "AI"]
```

contains:

```text
3 tokens
```

Therefore:

```text
Sequence Length = 3
```

Another example:

```text
["The", "cat", "is", "sleeping", "."]
```

has:

```text
Sequence Length = 5
```

> 💡 Sequence length is measured in **tokens**, not necessarily words.

---

# 📝 Words vs Tokens vs Sequence Length

Consider:

```text
"I am learning machine learning."
```

It contains:

```text
6 words
```

But a tokenizer might produce:

```text
["I", "am", "learning", "machine", "learning", "."]
```

So it could contain:

```text
6 tokens
```

Another tokenizer might split some words differently.

For example:

```text
["I", "am", "learn", "ing", "machine", "learn", "ing", "."]
```

Now the sequence contains:

```text
8 tokens
```

Therefore:

```text
Number of Words
      ≠
Number of Tokens
      ≠
Sequence Length in Every Case
```

---

# 🧩 Sequence Contains Tokens

A sequence can contain different types of tokens:

```text
📝 Words
🔗 Subwords
🔤 Characters
🔢 Numbers
🔣 Punctuation
🏷️ Special Tokens
```

For example:

```text
["Hello", ",", "world", "!"]
```

is a sequence of four tokens.

---

# 🏷️ Special Tokens in a Sequence

A sequence can also contain special tokens.

For example:

```text
<START> Hello world <END>
```

The sequence could be:

```text
[
    <START>,
    Hello,
    world,
    <END>
]
```

So special tokens can also contribute to sequence length.

For example:

```text
<START> + Hello + world + <END>

        = 4 tokens
```

---

# 📍 Order Matters

Each token has a position within the sequence.

For example:

```text
"I love AI"
```

can be represented as:

```text
Token       Position

"I"           0
"love"        1
"AI"          2
```

Or conceptually:

```text
"I" → Position 0
 ↓
"love" → Position 1
 ↓
"AI" → Position 2
```

The model needs information about both:

```text
🔢 Which token?
+
📍 Where is the token?
```

This is why positional information is important in Transformer models.

---

# 🧠 Sequence and Transformer

A Transformer processes a sequence of token representations.

The simplified flow is:

```text
🔢 Token IDs
      ↓
🧩 Token Embeddings
      ↓
📍 Positional Information
      ↓
📦 Input Sequence
      ↓
🤖 Transformer
      ↓
📊 Contextual Representations
```

The Transformer can use information from different tokens in the sequence to build contextual representations.

---

# 👀 Context Within a Sequence

Consider:

```text
The animal didn't cross the road because it was tired.
```

The meaning of:

```text
"it"
```

can depend on other tokens in the sequence.

The Transformer uses relationships between tokens to build contextual representations.

Conceptually:

```text
The ───────────────┐
animal ────────────┤
didn't ────────────┤
cross ─────────────┤
the ───────────────┤
road ──────────────┤
because ───────────┤
it ────────────────┤
was ───────────────┤
tired ─────────────┘
          ↓
   🧠 Contextual Processing
```

This is one reason sequence context is important.

---

# 🎯 Sequence During Next-Token Prediction

Decoder-only LLMs use the sequence to predict the next token.

For example:

```text
Input Sequence:

The cat
```

The model predicts:

```text
The cat → sleeps
```

The new token is then added to the sequence:

```text
The cat sleeps
```

The model can predict again:

```text
The cat sleeps → peacefully
```

So the sequence grows over time.

```text
"The cat"
    ↓
"The cat sleeps"
    ↓
"The cat sleeps peacefully"
    ↓
...
```

---

# 🔄 Sequence During Autoregressive Generation

The generation process can be represented as:

```text
📝 Initial Prompt
      ↓
🔢 Token Sequence
      ↓
🤖 Transformer
      ↓
🎯 Predict Next Token
      ↓
➕ Add Token
      ↓
🔢 Updated Sequence
      ↓
🤖 Transformer Again
      ↓
🎯 Predict Next Token
      ↓
🔄 Repeat
```

For example:

```text
Step 1:
["The", "cat"]

Step 2:
["The", "cat", "is"]

Step 3:
["The", "cat", "is", "sleeping"]

Step 4:
["The", "cat", "is", "sleeping", "."]
```

---

# 📚 Sequence During Training

Sequences are also important during LLM training.

Large amounts of text are converted into token IDs and divided into sequences.

For example:

```text
📚 Large Training Corpus
          ↓
🔤 Tokenization
          ↓
🔢 Long Token Stream
          ↓
✂️ Split into Sequences
          ↓
📦 Training Sequences
```

Suppose the tokenized data looks like:

```text
[12, 45, 78, 91, 33, 56, 72, 84, 19, ...]
```

It can be divided into fixed-length sequences:

```text
Sequence 1:
[12, 45, 78, 91]

Sequence 2:
[33, 56, 72, 84]

Sequence 3:
[19, ...]
```

The exact way training data is divided depends on the training setup.

---

# 📏 Fixed-Length Sequences

Training systems often use a chosen sequence length.

For example:

```text
Sequence Length = 8
```

A token stream might be divided like:

```text
[1, 2, 3, 4, 5, 6, 7, 8]
[9, 10, 11, 12, 13, 14, 15, 16]
[17, 18, 19, 20, 21, 22, 23, 24]
```

Each sequence contains eight tokens.

This makes batch processing easier.

---

# 📦 Sequences in Batches

Multiple sequences can be processed together in a **batch**.

For example:

```text
Sequence 1 → [10, 20, 30, 40]
Sequence 2 → [15, 25, 35, 45]
Sequence 3 → [11, 21, 31, 41]
```

Together:

```text
📦 Batch
│
├── Sequence 1
├── Sequence 2
└── Sequence 3
```

Conceptually:

```text
📦 Batch
   ↓
🔢 Multiple Token Sequences
   ↓
🤖 Transformer
```

Processing multiple sequences together can make training more efficient.

---

# 🟨 Padding and Sequences

Not all sequences have to naturally have the same length.

For example:

```text
Sequence 1 → [10, 20, 30]
Sequence 2 → [15, 25, 35, 45, 55]
Sequence 3 → [11, 21, 31, 41]
```

If a system needs equal-length sequences, shorter sequences can be padded:

```text
Sequence 1 → [10, 20, 30, <PAD>, <PAD>]
Sequence 2 → [15, 25, 35, 45, 55]
Sequence 3 → [11, 21, 31, 41, <PAD>]
```

Now every sequence has length 5.

A padding mask can tell the model which positions contain padding rather than real content.

---

# 🪟 Sequence and Context Window

A model has a maximum amount of tokenized context it can process.

This is called the **context window**.

For example, if a model supports:

```text
Context Window = 8,000 tokens
```

then the relevant input sequence cannot simply grow beyond that limit.

Conceptually:

```text
🔢 Token Sequence
       ↓
📏 Sequence Length
       ↓
🪟 Context Window
       ↓
🤖 Model
```

The context window is therefore closely related to sequence length.

---

# ⚠️ Sequence Length Is Not Character Length

These are different measurements.

For example:

```text
📝 "Hello"
```

has:

```text
5 characters
```

But a tokenizer might represent it as:

```text
["Hello"]
```

which is:

```text
1 token
```

Another tokenizer could split it differently.

Therefore:

```text
Characters
   ≠
Words
   ≠
Tokens
```

---

# 🧠 Sequence Representation

A sequence can be represented at different stages.

### 1️⃣ Text Sequence

```text
"The cat sleeps."
```

### 2️⃣ Token Sequence

```text
["The", "cat", "sleeps", "."]
```

### 3️⃣ ID Sequence

```text
[125, 842, 731, 18]
```

### 4️⃣ Embedding Sequence

```text
[
  vector₁,
  vector₂,
  vector₃,
  vector₄
]
```

The same underlying input is represented differently as it moves through the LLM pipeline.

```text
📝 Text
   ↓
🧩 Tokens
   ↓
🔢 Token IDs
   ↓
📊 Embeddings
   ↓
📍 Positional Information
   ↓
🤖 Transformer
```

---

# 🔥 Complete Example

Let's take:

```text
📝 "The cat is sleeping."
```

### Step 1 — Tokenization

A tokenizer may produce:

```text
["The", "cat", "is", "sleeping", "."]
```

### Step 2 — Token IDs

For example:

```text
[125, 842, 91, 731, 18]
```

### Step 3 — Sequence

Therefore:

```text
🔢 Sequence

[125, 842, 91, 731, 18]
```

Sequence length:

```text
5 tokens
```

### Step 4 — Embeddings

Each Token ID is used to obtain an embedding:

```text
[125, 842, 91, 731, 18]
            ↓
     📊 Embedding Vectors
```

### Step 5 — Transformer

The representations are processed:

```text
📊 Embeddings
      ↓
📍 Positional Information
      ↓
🔄 Transformer Blocks
      ↓
📊 Contextual Representations
```

### Step 6 — Prediction

The model can use the sequence to predict the next token:

```text
"The cat is sleeping."
                  ↓
             🎯 Next Token
```

---

# 🆚 Sequence vs Token

These two concepts are related but different.

| Concept            | Meaning                          |
| ------------------ | -------------------------------- |
| 🧩 Token           | One piece of text                |
| 🔢 Token ID        | Numerical ID of one token        |
| 📦 Sequence        | Ordered collection of tokens     |
| 📏 Sequence Length | Number of tokens in the sequence |

For example:

```text
"The cat sleeps."
```

might become:

```text
Tokens:
["The", "cat", "sleeps", "."]

Token IDs:
[125, 842, 731, 18]

Sequence:
[125, 842, 731, 18]

Sequence Length:
4
```

---

# 🧠 Key Idea

A sequence is the **ordered set of tokens that the model processes together**.

```text
📝 Text
   ↓
🔤 Tokenization
   ↓
🧩 Tokens
   ↓
🔢 Token IDs
   ↓
📦 Sequence
   ↓
📊 Embeddings
   ↓
📍 Positional Information
   ↓
🤖 Transformer
```

Remember:

* 🔢 A sequence contains Token IDs after tokenization.
* 📏 Sequence length is measured in tokens.
* 📍 Token order matters.
* 🏷️ Special tokens can be part of a sequence.
* 📦 Multiple sequences can be processed together in a batch.
* 🪟 Sequence length is constrained by the model's context window.
* 🎯 During generation, the sequence can grow as new tokens are produced.
* 🧠 During training, text is commonly divided into token sequences for processing.

> 🚀 **The sequence is the ordered stream of token information that moves into the Transformer and provides the context used for processing and prediction.**
