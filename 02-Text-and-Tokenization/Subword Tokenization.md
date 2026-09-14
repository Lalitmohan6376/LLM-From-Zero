# 🧩 Subword Tokenization

**Subword Tokenization** is a tokenization method that breaks text into **smaller pieces of words**, called **subwords**.

A subword can be:

* 📝 A complete word
* 🧩 Part of a word
* 🔤 A common word piece
* ✏️ Punctuation
* ⚙️ A special token

The important idea is that a word does **not** always need to be stored as one complete token.

For example:

```text
playing
```

could be represented approximately as:

```text
["play", "ing"]
```

The exact split depends on the tokenizer.

---

# 🧠 Why Do We Need Subword Tokenization?

Word-level tokenization has a major problem.

Suppose the vocabulary contains:

```text
play
played
player
```

But a new word appears:

```text
playfulness
```

If the complete word is not in the vocabulary, a word-level tokenizer may have difficulty representing it.

Subword tokenization can break it into smaller known pieces:

```text
playfulness
      ↓
["play", "ful", "ness"]
```

This allows the tokenizer to reuse pieces it already knows.

---

# 🔤 Simple Idea

The basic idea is:

```text
📝 Text
   ↓
🔤 Find Useful Word Pieces
   ↓
🧩 Subword Tokens
   ↓
🔢 Token IDs
```

For example:

```text
unhappiness
```

could be represented approximately as:

```text
["un", "happi", "ness"]
```

Instead of requiring:

```text
"unhappiness"
```

to exist as one complete vocabulary entry.

---

# 📝 Word vs Subword

Consider:

```text
playing
```

### Word-Level

```text
["playing"]
```

### Character-Level

```text
["p", "l", "a", "y", "i", "n", "g"]
```

### Subword-Level

```text
["play", "ing"]
```

So:

```text
🔤 Character
→ Very small pieces

📝 Word
→ Complete words

🧩 Subword
→ Reusable pieces between characters and words
```

This is the main idea behind subword tokenization.

---

# 🧩 What Is a Subword?

A **subword** is a smaller piece of a word that can be reused across different words.

For example:

```text
playing
played
player
```

may contain reusable pieces such as:

```text
play
ing
ed
er
```

So a tokenizer can potentially represent:

```text
playing → play + ing
played  → play + ed
player  → play + er
```

The exact tokenization depends on the tokenizer.

> ⚠️ Subwords are not necessarily linguistic morphemes. A tokenizer learns useful pieces based on its algorithm and training data.

---

# 📚 Subword Vocabulary

A subword tokenizer has a vocabulary containing a mixture of token types.

For example:

```text
📚 Vocabulary

the
cat
play
ing
ed
er
un
ness
.
,
...
```

Notice that the vocabulary can contain:

```text
📝 Complete Words
+
🧩 Word Pieces
+
✏️ Punctuation
```

This makes the vocabulary more flexible than a pure word-level vocabulary.

---

# 🔄 How Subword Tokenization Helps

Consider these words:

```text
play
playing
played
player
playful
```

A word-level tokenizer may need separate entries:

```text
play
playing
played
player
playful
```

A subword tokenizer can potentially reuse:

```text
play
ing
ed
er
ful
```

So many words can be represented using a smaller set of reusable pieces.

```text
📚 Smaller Vocabulary
        +
🧩 Reusable Pieces
        ↓
🚀 More Flexible Representation
```

---

# 🆕 Handling Rare Words

Rare words are one of the biggest reasons subword tokenization is useful.

Suppose the tokenizer has never seen:

```text
unhappiness
```

as a complete word.

It may still be able to represent it using known pieces:

```text
unhappiness
      ↓
un + happi + ness
```

So the complete word does not necessarily need to exist in the vocabulary.

---

# ❓ Handling Unknown Words

With pure word-level tokenization:

```text
RareWord
   ↓
Not in Vocabulary
   ↓
<UNK>
```

With subword tokenization:

```text
RareWord
   ↓
🧩 Smaller Known Pieces
   ↓
🔢 Token IDs
```

This greatly reduces the need to represent an entire unfamiliar word as `<UNK>`.

However, the exact behavior depends on the tokenizer.

---

# ✏️ Misspelled Words

Subword tokenization can also provide some flexibility with unusual or misspelled text.

For example:

```text
playng
```

might be split into smaller pieces rather than requiring the complete string to exist in the vocabulary.

This does **not** mean the model will automatically understand the spelling mistake correctly.

It only means the text can often be represented without requiring one complete vocabulary entry.

---

# 💻 Subword Tokenization and Code

Subword tokenization is also useful for programming code.

Consider:

```python
get_user_name()
```

A tokenizer may represent parts of the identifier using reusable pieces.

For example, approximately:

```text
get
_
user
_
name
(
)
```

The exact result depends on the tokenizer.

This is useful because code contains many possible:

* Variable names
* Function names
* Class names
* Keywords
* Operators
* Symbols

A vocabulary containing every possible identifier would be impractical.

Subword tokenization allows smaller pieces to be reused.

---

# 🔢 Numbers

Numbers can also be represented using one or more tokens.

For example:

```text
2026
```

may be one token or several tokens depending on the tokenizer.

Similarly:

```text
123456789
```

may be divided into multiple pieces.

So:

```text
Number ≠ Always One Token
```

---

# 🌍 Multiple Languages

Subword tokenization is useful when working with multiple languages because it does not require every complete word to be present in the vocabulary.

A tokenizer can represent text using smaller pieces.

For example:

```text
English
learning
```

and text from another language can both be represented using the tokenizer's available token pieces.

However, token efficiency can vary significantly between languages.

Some languages may require more tokens to represent the same amount of information.

---

# 📏 Sequence Length

Subword tokenization creates a middle ground between character-level and word-level tokenization.

For example:

```text
playing
```

### Character-Level

```text
p | l | a | y | i | n | g
```

7 tokens

### Word-Level

```text
playing
```

1 token

### Subword-Level

```text
play | ing
```

2 tokens

This gives us:

```text
Character-Level → Longer Sequences
Word-Level      → Shorter Sequences
Subword-Level   → Middle Ground
```

The actual number of tokens depends on the tokenizer.

---

# ⚖️ The Main Trade-Off

Subword tokenization tries to balance two important problems.

### Word-Level Problem

```text
📚 Very Large Vocabulary
        +
❓ Unknown Words
```

### Character-Level Problem

```text
📚 Small Vocabulary
        +
📏 Very Long Sequences
```

### Subword Approach

```text
📚 Manageable Vocabulary
        +
📏 Reasonable Sequence Length
        +
🆕 Better Rare-Word Handling
```

This balance is one of the main reasons subword tokenization became widely used.

---

# 🧠 How Subword Vocabulary Is Created

A tokenizer needs to decide which pieces should become tokens.

A simplified process is:

```text
📚 Large Text Dataset
        ↓
🔍 Analyze Text
        ↓
📊 Find Common Patterns
        ↓
🧩 Create Useful Pieces
        ↓
📚 Build Vocabulary
```

Different tokenization algorithms use different methods to create this vocabulary.

Examples include:

* 🔄 Byte-Pair Encoding (BPE)
* 🌳 WordPiece
* 🧩 Unigram

These methods have different algorithms, but they share the general goal of creating a useful vocabulary of reusable text pieces.

---

# 🔄 Subword Tokenization During LLM Processing

Once the tokenizer has a vocabulary, the input text can be converted into subword tokens.

For example:

```text
The cat is playing.
```

could become approximately:

```text
["The", " cat", " is", " play", "ing", "."]
```

Then:

```text
🧩 Subword Tokens
        ↓
🔢 Token IDs
        ↓
🧩 Embeddings
        ↓
📍 Positional Information
        ↓
🔄 Transformer
```

The exact token boundaries depend on the tokenizer.

---

# 🔢 Subwords to Token IDs

Every subword token has a corresponding ID.

Suppose:

```text
📚 Vocabulary

"play" → 500
"ing"  → 501
"."    → 18
```

Then:

```text
playing.
```

could become:

```text
["play", "ing", "."]
```

and then:

```text
[500, 501, 18]
```

These IDs are then used to obtain embeddings.

---

# 🧩 Subword Tokenization and Embeddings

After tokenization:

```text
🧩 Tokens
   ↓
🔢 Token IDs
   ↓
🧩 Token Embeddings
```

Each Token ID is associated with a learned embedding vector.

For example:

```text
"play" → 500 → Embedding Vector
"ing"  → 501 → Embedding Vector
```

The Transformer processes these numerical representations rather than directly processing the text strings.

---

# 🎯 Subwords and Next-Token Prediction

In a modern LLM, the model predicts the next **token**, not necessarily the next complete word.

For example:

```text
The player is run
```

The next token could be a piece that completes:

```text
running
```

For example:

```text
The player is run
                 ↓
                ning
```

This is only an illustrative example.

The actual predicted token depends on the model and tokenizer.

This is an important difference from thinking of an LLM as simply predicting complete words.

---

# 🔄 Autoregressive Generation

During generation, tokens are predicted one at a time.

```text
📝 Input
   ↓
🔤 Tokenization
   ↓
🔢 Token IDs
   ↓
🧠 Transformer
   ↓
🎯 Next Token
   ↓
➕ Add Token
   ↓
🧠 Transformer Again
   ↓
🎯 Next Token
   ↓
🔄 Repeat
```

A token might be:

```text
📝 Complete Word
```

or:

```text
🧩 Word Piece
```

depending on the tokenizer.

---

# 🆚 Character vs Word vs Subword

| Feature            | Character-Level   | Word-Level       | Subword        |
| ------------------ | ----------------- | ---------------- | -------------- |
| 🔤 Basic unit      | Character         | Word             | Word piece     |
| 📚 Vocabulary      | Small             | Large            | Medium         |
| 📏 Sequence length | Long              | Short            | Medium         |
| 🆕 Rare words      | Good              | Poor             | Good           |
| ❓ Unknown words    | Easy to represent | Problematic      | Usually better |
| 🔄 Reusable pieces | Very small        | Limited          | High           |
| ⚖️ Overall balance | Low efficiency    | Vocabulary-heavy | Good balance   |

This is a simplified comparison; real tokenizer behavior varies.

---

# 🚀 Why Modern LLMs Commonly Use Subword Tokenization

Modern LLMs need to process many different kinds of text:

```text
📝 Words
🌍 Languages
🔢 Numbers
💻 Code
✏️ Punctuation
🆕 New Words
```

A pure word-level vocabulary would become extremely large.

A pure character-level representation would create very long sequences.

Subword tokenization provides a practical middle ground:

```text
📝 Text
   ↓
🧩 Reusable Subword Pieces
   ↓
📚 Manageable Vocabulary
   ↓
📏 Reasonable Sequence Length
   ↓
🧠 Efficient Model Input
```

This is why subword-style tokenization is an important concept in modern LLMs.

---

# ⚙️ Important Tokenization Algorithms

Several important tokenization approaches can create subword vocabularies.

### 🔄 Byte-Pair Encoding (BPE)

BPE learns frequent combinations of smaller units and merges them into larger tokens.

```text
small pieces
     ↓
frequent combinations
     ↓
larger reusable tokens
```

---

### 🌳 WordPiece

WordPiece builds a vocabulary of useful subword units and chooses pieces that efficiently represent words.

It is associated with models such as BERT.

---

### 🧩 Unigram

Unigram tokenization starts with a large set of possible pieces and selects a vocabulary that provides an effective representation of the training data.

---

These algorithms are different, but the general goal is similar:

```text
🧩 Create Useful Reusable Pieces
```

Detailed BPE mechanics are covered separately in:

👉 [Byte-Pair Encoding](./Byte-Pair-Encoding.md)

---

# 🏗️ Complete Subword Tokenization Flow

Putting everything together:

```text
📝 Human Text
      ↓
🔤 Subword Tokenizer
      ↓
🧩 Subword Tokens
      ↓
🔢 Token IDs
      ↓
🧩 Token Embeddings
      ↓
📍 Positional Information
      ↓
🔄 Transformer Blocks
      ↓
📊 Output
      ↓
🎯 Next-Token Prediction
```

---

# 💡 Key Takeaways

* 🧩 **Subword Tokenization** breaks words into reusable pieces.
* 🔤 A token can be a complete word or a smaller word piece.
* 🧠 Subword tokenization provides a balance between word-level and character-level tokenization.
* 📚 It can maintain a manageable vocabulary.
* 🆕 Rare and new words can often be represented using smaller known pieces.
* ❓ It greatly reduces the need to convert unfamiliar complete words into `<UNK>`.
* 📏 It usually creates shorter sequences than character-level tokenization.
* ⚖️ It avoids some of the vocabulary problems of word-level tokenization.
* 💻 It can represent programming code and unusual text more flexibly.
* 🌍 Token efficiency can vary between languages.
* 🔄 BPE, WordPiece, and Unigram are important tokenization approaches.
* 🚀 Modern LLMs commonly use subword-style tokenization.
* ⚠️ Exact tokens always depend on the tokenizer and model.

---
