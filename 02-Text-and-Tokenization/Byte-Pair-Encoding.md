# 🔗 Byte-Pair Encoding (BPE)

**Byte-Pair Encoding (BPE)** is a **subword tokenization algorithm** used to break text into smaller pieces called **tokens**.

Instead of treating every complete word as one token, BPE learns which smaller pieces occur frequently and combines them into reusable tokens.

> 💡 **Simple idea:** BPE repeatedly merges the most frequent pair of neighboring pieces.

---

## 🧠 Why Do We Need BPE?

Before subword tokenization, we can think about two simple approaches:

### 🔤 Character-Level

```text
playing
↓
p l a y i n g
```

This gives a small vocabulary, but sequences become very long.

### 📝 Word-Level

```text
playing
↓
playing
```

This gives shorter sequences, but the vocabulary can become very large.

There is also a problem with rare or unknown words.

### 🔗 BPE

BPE tries to find a balance:

```text
🔤 Character-Level
       ↓
   Very Small Vocabulary
   Very Long Sequences

📝 Word-Level
       ↓
   Very Large Vocabulary
   Shorter Sequences

🔗 BPE
       ↓
   Manageable Vocabulary
   Reasonable Sequence Length
```

---

# 🔗 What Does BPE Do?

BPE starts with small pieces and repeatedly combines frequently occurring neighboring pieces.

For example:

```text
l o w
```

If `l + o` appears frequently:

```text
l + o → lo
```

Then:

```text
lo + w → low
```

So the word can eventually become:

```text
low
```

The important idea is that **BPE learns these merges from a training corpus**.

---

# 📚 BPE Has Two Main Stages

It is useful to separate BPE into two different stages:

```text
1️⃣ Learn the BPE Vocabulary
        ↓
2️⃣ Tokenize New Text
```

The first stage happens when the tokenizer is built.

The second stage happens when we actually use the tokenizer.

---

# 1️⃣ Learning BPE

Suppose our small training corpus contains:

```text
low
lower
lowest
low
lower
```

Initially, we can represent words using small units:

```text
low
↓
l o w

lower
↓
l o w e r

lowest
↓
l o w e s t
```

Now BPE looks for **frequent neighboring pairs**.

For example:

```text
l + o
o + w
w + e
e + r
e + s
```

Suppose:

```text
l + o
```

is one of the most frequent pairs.

BPE can merge it:

```text
l + o → lo
```

Now the representation becomes:

```text
lo w
```

If:

```text
lo + w
```

is also frequently found, BPE can merge it:

```text
lo + w → low
```

Now:

```text
low
```

can become a reusable token.

---

# 🔄 BPE Merge Process

The process can be simplified as:

```text
📚 Training Text
       ↓
🔤 Start with Small Pieces
       ↓
🔎 Find Frequent Neighboring Pairs
       ↓
🔗 Merge a Frequent Pair
       ↓
📚 Add New Token
       ↓
🔄 Repeat
```

BPE continues this process many times.

---

# 📊 Simple Example

Suppose the training data contains:

```text
low
lower
lowest
low
lower
```

### Step 1 — Start Small

```text
low
↓
l o w

lower
↓
l o w e r

lowest
↓
l o w e s t
```

### Step 2 — Find Frequent Pairs

BPE checks neighboring pieces:

```text
l + o
o + w
w + e
e + r
e + s
```

The frequent pairs are candidates for merging.

### Step 3 — Merge

For example:

```text
l + o → lo
```

Then:

```text
lo + w → low
```

Now we may have:

```text
low
```

as a learned token.

### Step 4 — More Merges

Other frequent combinations can also be learned.

For example:

```text
e + r → er
```

Then an illustrative tokenization could become:

```text
lower
↓
low + er
```

Similarly, another word could contain:

```text
low + est
```

⚠️ These are **illustrative examples**. The exact tokens produced by a real BPE tokenizer depend on the training data, vocabulary size, and learned merge rules.

---

# 📋 BPE Merge Rules

During BPE training, the tokenizer learns **merge rules**.

A simplified example:

| Step | Pair     | New Token |
| ---- | -------- | --------- |
| 1    | `l + o`  | `lo`      |
| 2    | `lo + w` | `low`     |
| 3    | `e + r`  | `er`      |
| 4    | `e + s`  | `es`      |

These learned rules can later be used to tokenize new text.

---

# 🆕 Tokenizing New Text

After BPE has learned its vocabulary and merge rules, we can use them on new text.

For example:

```text
lower
```

The tokenizer starts with smaller pieces and applies the learned merges.

A simplified result could be:

```text
lower
↓
low + er
```

Then these tokens are converted into IDs:

```text
["low", "er"]
        ↓
[125, 456]
```

The actual IDs depend on the tokenizer's vocabulary.

---

# 🔢 BPE and Token IDs

BPE creates **tokens**, but the LLM works with numbers.

So the process is:

```text
📝 Text
   ↓
🔗 BPE Tokenizer
   ↓
🧩 Subword Tokens
   ↓
🔢 Token IDs
   ↓
🧠 Embeddings
   ↓
🤖 Transformer
```

For example:

```text
"playing"
     ↓
["play", "ing"]
     ↓
[1254, 456]
     ↓
🧩 Embeddings
```

The numbers are simply identifiers for tokens.

> 💡 **Token ID does not contain the meaning of the token.**

The meaning-related information is learned through the model's parameters and representations.

---

# 📚 BPE Vocabulary

The tokenizer builds a vocabulary containing tokens that can include:

```text
Complete words
      +
Word pieces
      +
Punctuation
      +
Numbers
      +
Other text units
```

For example:

```text
📚 Vocabulary

Token       ID
----------------
"the"       125
"play"      421
"ing"       456
"low"       731
"."         18
```

The exact vocabulary depends on the tokenizer.

---

# 🧩 Why Can BPE Handle Rare Words?

Suppose the tokenizer has never learned a complete token for:

```text
unbelievable
```

Instead of requiring the entire word to exist in the vocabulary, it can represent it using smaller pieces.

For example:

```text
unbelievable
↓
un + believe + able
```

Or another tokenizer may split it differently.

The important idea is:

```text
🆕 Rare Word
      ↓
🔗 Smaller Known Pieces
      ↓
🔢 Token IDs
```

This makes subword tokenization much more flexible than strict word-level tokenization.

---

# 🌍 BPE and Different Languages

BPE can also be useful for multilingual text.

Different languages contain different:

* words
* characters
* writing systems
* word forms
* punctuation patterns

A subword tokenizer can learn reusable pieces from the training data.

However, token efficiency can vary between languages.

One language may represent a sentence using fewer tokens than another.

---

# 💻 BPE and Code

BPE can also tokenize programming code.

For example:

```python
print("Hello")
```

can be broken into smaller pieces representing things such as:

```text
print
(
"
Hello
"
)
```

The exact tokenization depends on the tokenizer.

This is one reason subword tokenization is useful beyond normal English text.

---

# 📦 Classic BPE vs Byte-Level BPE

The name **Byte-Pair Encoding** comes from the original BPE idea of repeatedly merging pairs.

In classic BPE, the starting units can be characters.

Modern tokenizers may use **byte-level BPE**, where the initial representation is based on bytes.

The simplified idea is:

```text
📝 Text
   ↓
🔢 Byte Representation
   ↓
🔗 Learn Frequent Merges
   ↓
🧩 Subword Tokens
```

Byte-level approaches can represent arbitrary text without needing a separate unknown token for every unusual character.

> 💡 **Important:** BPE is not simply "splitting text into bytes." The important part is the **learned pair-merging process**.

Different tokenizers can use different variations of BPE.

---

# 🤖 BPE and GPT

BPE has an important historical connection with GPT-style language models.

For example, **GPT-2 used a byte-level BPE tokenizer**.

However, different GPT-family models can use different tokenizer implementations or vocabulary systems, so it is better not to assume that every GPT model uses exactly the same BPE tokenizer.

The general pipeline remains:

```text
📝 Text
   ↓
🔗 Tokenizer
   ↓
🔢 Token IDs
   ↓
🧩 Embeddings
   ↓
🤖 Transformer
```

---

# ⚖️ Advantages of BPE

### ✅ 1. Manageable Vocabulary

BPE does not need a separate token for every possible complete word.

---

### ✅ 2. Handles Rare Words

Rare words can often be represented using smaller known pieces.

```text
Rare Word
   ↓
Smaller Pieces
   ↓
Known Tokens
```

---

### ✅ 3. Reuses Common Patterns

Frequently occurring pieces can become tokens.

For example:

```text
play
ing
tion
un
```

may be useful across many different words.

---

### ✅ 4. Better Balance

BPE provides a balance between:

```text
🔤 Characters
        ↕
🔗 Subwords
        ↕
📝 Complete Words
```

This helps keep both vocabulary size and sequence length manageable.

---

# ⚠️ Limitations of BPE

### ❌ 1. Splits Can Look Strange

BPE is based largely on learned frequency patterns.

A token boundary does not necessarily represent a meaningful linguistic unit.

---

### ❌ 2. Tokenization Depends on Training

Different BPE tokenizers trained on different data can produce different tokens.

```text
Same Text
   ↓
Different Tokenizer
   ↓
Different Tokenization
```

---

### ❌ 3. Token Efficiency Varies

Some languages, domains, numbers, or code may require more tokens than others.

---

### ❌ 4. Sequences Can Still Be Long

BPE reduces sequence length compared with character-level tokenization, but it does not make every word a single token.

---

### ❌ 5. Vocabulary Is Fixed After Training

Once a tokenizer has been trained, its vocabulary and merge rules are generally fixed.

New text is tokenized using the learned system rather than continuously creating new vocabulary tokens.

---

# 🆚 BPE vs Character-Level vs Word-Level

| Feature          | Character-Level          | Word-Level    | BPE                         |
| ---------------- | ------------------------ | ------------- | --------------------------- |
| Basic Unit       | Character                | Word          | Subword                     |
| Vocabulary       | Small                    | Very Large    | Moderate                    |
| Sequence Length  | Long                     | Short         | Moderate                    |
| Rare Words       | Handles well             | Problematic   | Handles well                |
| Unknown Words    | Usually less problematic | Major problem | Usually handled with pieces |
| Flexibility      | High                     | Lower         | High                        |
| Modern LLM Usage | Uncommon                 | Uncommon      | Common variant              |

---

# 🔄 Complete BPE Pipeline

The complete simplified process looks like this:

```text
📚 Training Corpus
       ↓
🔤 Initial Small Units
       ↓
🔎 Count Frequent Pairs
       ↓
🔗 Merge Frequent Pair
       ↓
📚 Update Vocabulary
       ↓
🔄 Repeat
       ↓
📖 Learned Vocabulary
       +
📋 Learned Merge Rules
```

Then, for new text:

```text
📝 New Text
      ↓
🔗 BPE Tokenizer
      ↓
🧩 Subword Tokens
      ↓
🔢 Token IDs
      ↓
🧠 Embeddings
      ↓
🤖 Transformer
```

---

# 🧠 BPE in One Example

Let's simplify everything with:

```text
playing
```

A BPE tokenizer may learn:

```text
play
ing
```

So:

```text
📝 playing
      ↓
🔗 BPE
      ↓
🧩 ["play", "ing"]
      ↓
🔢 [1254, 456]
      ↓
🧠 Embeddings
      ↓
🤖 Transformer
```

The exact split may be different for another tokenizer.

---

# 🎯 Key Idea

BPE does not simply memorize complete words.

It learns **frequent reusable pieces** and combines them to represent text efficiently.

```text
📚 Text
   ↓
🔎 Find Frequent Patterns
   ↓
🔗 Merge Frequent Pairs
   ↓
📚 Build Vocabulary
   ↓
🧩 Create Subword Tokens
   ↓
🔢 Token IDs
   ↓
🧠 LLM
```

