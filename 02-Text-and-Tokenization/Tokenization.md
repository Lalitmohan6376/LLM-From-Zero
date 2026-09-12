# 🔤 Tokenization

**Tokenization** is the process of breaking text into smaller pieces called **tokens** so that an LLM can process the text.

Humans work with words and sentences.

LLMs work with **tokens and numbers**.

A simplified process is:

```text
📝 Human Text
      ↓
🔤 Tokenization
      ↓
🧩 Tokens
      ↓
🔢 Token IDs
      ↓
🧠 Embeddings
      ↓
🤖 Transformer
```

Tokenization is one of the first important steps in the LLM pipeline.

---

# 🧠 Why Do We Need Tokenization?

An LLM cannot directly process a sentence like:

```text
The cat is sleeping.
```

The model needs the text to be converted into a numerical form.

Tokenization helps transform the text into manageable pieces.

For example:

```text
📝 Text

The cat is sleeping.

        ↓

🔤 Tokenization

["The", " cat", " is", " sleeping", "."]

        ↓

🔢 Token IDs

[125, 842, 91, 456, 18]
```

The actual tokens and IDs depend on the tokenizer.

---

# 🔤 What is a Token?

A **token** is an individual piece produced by a tokenizer.

A token can be:

* 📝 A complete word
* 🧩 Part of a word
* ✏️ Punctuation
* 🔢 Part of a number
* 💻 Part of code
* ⚙️ A special token

For example:

```text
The cat is sleeping.
```

could be represented approximately as:

```text
["The", " cat", " is", " sleeping", "."]
```

Each item is a token.

---

# 📝 Tokenization Example

Consider:

```text
I love machine learning.
```

A tokenizer might produce:

```text
["I", " love", " machine", " learning", "."]
```

Then each token receives an ID:

```text
["I", " love", " machine", " learning", "."]
              ↓
[21, 84, 912, 456, 18]
```

The numbers above are only examples.

A real tokenizer will have its own vocabulary and Token IDs.

---

# ❌ One Word Does Not Always Mean One Token

This is one of the most important things to understand.

It is tempting to think:

```text
1 word = 1 token
```

But modern tokenizers do not always work this way.

A word can be:

```text
1 word → 1 token
```

or:

```text
1 word → multiple tokens
```

For example, a long or uncommon word might be split approximately like:

```text
unhappiness
      ↓
["un", "happi", "ness"]
```

The exact result depends on the tokenizer.

---

# 🧩 Why Split Words Into Smaller Pieces?

Suppose we tried to create a vocabulary containing every possible complete word.

There would be an enormous number of possible words.

We would also have problems with:

* New words
* Rare words
* Misspelled words
* Different word forms
* Technical terms
* Names
* Programming code

Instead, tokenizers can reuse smaller pieces.

For example:

```text
play
playing
played
player
```

may share common token pieces.

This allows a tokenizer to represent many different words using a manageable vocabulary.

---

# 🧩 Subword Tokenization

Modern LLMs commonly use tokenization approaches that can represent words using **subword pieces**.

For example:

```text
playing
```

could be split approximately as:

```text
["play", "ing"]
```

Another word:

```text
played
```

could be represented approximately as:

```text
["play", "ed"]
```

The tokenizer can reuse pieces such as:

```text
play
ing
ed
```

This makes the vocabulary more flexible.

> ⚠️ These are simplified examples. Actual token boundaries depend on the tokenizer.

---

# ✏️ Punctuation Can Be Tokens

Tokenization is not limited to words.

Consider:

```text
Hello, world!
```

A tokenizer may represent it approximately as:

```text
["Hello", ",", " world", "!"]
```

Here:

```text
Hello → token
,     → token
world → token
!     → token
```

This allows punctuation to be represented as part of the input sequence.

---

# 🔢 Numbers Can Be Tokenized

Numbers can also be split into one or more tokens.

For example:

```text
2026
```

might be represented as one token or multiple tokens depending on the tokenizer.

Similarly:

```text
123456789
```

could be split into several pieces.

So:

```text
Number ≠ Always One Token
```

The tokenizer decides how the number is represented.

---

# 💻 Code Can Also Be Tokenized

LLMs can process programming code because code can also be converted into tokens.

For example:

```python
print("Hello")
```

could be represented approximately as pieces corresponding to:

```text
print
(
"Hello"
)
```

The exact tokenization depends on the tokenizer.

This is one reason tokenization is important for code-generating LLMs as well.

---

# 🌍 Different Languages

Tokenizers can process languages other than English.

For example:

```text
नमस्ते दुनिया
```

can also be converted into tokens.

The number of tokens may differ between languages.

For the same general meaning, different languages can require different numbers of tokens depending on the tokenizer and vocabulary.

This is one reason token efficiency can vary across languages.

---

# 📚 Tokenization and Vocabulary

Tokenization depends heavily on the model's **Vocabulary**.

The vocabulary contains the tokens that the tokenizer can use.

For example:

```text
📚 Vocabulary

"the"
"cat"
"dog"
"play"
"ing"
"."
","
...
```

When text is given to the tokenizer, it tries to represent that text using tokens from its vocabulary.

Simplified flow:

```text
📝 Text
   ↓
🔤 Tokenizer
   ↓
📚 Vocabulary
   ↓
🧩 Tokens
```

So:

```text
Vocabulary = Available Tokens
Tokenization = Process of Splitting Text
```

---

# 🔢 Tokenization to Token IDs

After the tokenizer creates tokens, each token is mapped to a numerical ID.

For example:

```text
📝 Text

The cat
```

↓

```text
🔤 Tokens

["The", " cat"]
```

↓

```text
🔢 Token IDs

[125, 842]
```

The complete process is:

```text
📝 Text
   ↓
🔤 Tokenization
   ↓
🧩 Tokens
   ↓
🔢 Token IDs
```

The model then uses these IDs to retrieve their learned representations.

---

# 🧠 Token IDs Are Not Meaning

A Token ID is simply an identifier.

For example:

```text
"cat" → 842
```

The number `842` does not mean that 842 represents the concept of a cat.

It simply identifies the token `"cat"` in that tokenizer's vocabulary.

Later, the Token ID is mapped to an embedding.

```text
🔤 Token
   ↓
🔢 Token ID
   ↓
🧩 Embedding
   ↓
🧠 Transformer
```

The learned representation is handled by the model's parameters and embeddings.

---

# ⚙️ How Tokenization Works at a High Level

A tokenizer generally performs several conceptual steps.

```text
📝 Raw Text
     ↓
🔍 Analyze Text
     ↓
🧩 Find Token Pieces
     ↓
🔢 Assign Token IDs
     ↓
📦 Create Token Sequence
```

The exact algorithm depends on the tokenizer.

Different tokenizers use different strategies.

---

# 🧠 Common Tokenization Approaches

There are several important approaches to tokenization.

## 1️⃣ Character-Level Tokenization

Each character can be treated as a token.

Example:

```text
Hello
```

could become:

```text
["H", "e", "l", "l", "o"]
```

### ✅ Advantages

* Simple
* Small basic vocabulary
* Can represent almost any text

### ❌ Disadvantages

* Creates very long sequences
* The model has to process many tokens
* Learning meaningful word-level patterns can be harder

---

# 2️⃣ Word-Level Tokenization

Each word can be treated as a token.

Example:

```text
The cat sleeps.
```

could become:

```text
["The", "cat", "sleeps", "."]
```

### ✅ Advantages

* Easy to understand
* Shorter sequences
* Tokens can correspond closely to words

### ❌ Disadvantages

* Vocabulary can become very large
* Rare words can be difficult to represent
* New words can create problems
* Different word forms increase vocabulary requirements

---

# 3️⃣ Subword Tokenization

Subword tokenization breaks text into reusable pieces.

Example:

```text
unhappiness
```

could become:

```text
["un", "happi", "ness"]
```

This provides a balance between character-level and word-level approaches.

### ✅ Advantages

* Handles rare words better
* Vocabulary can remain manageable
* Reuses common word pieces
* Works well for many languages and text types

Modern LLM tokenizers commonly use subword-style approaches.

---

# 🧩 Byte-Pair Encoding

**Byte-Pair Encoding (BPE)** is one important tokenization algorithm used in the LLM ecosystem.

The basic idea is to start with smaller units and learn common combinations.

A simplified example:

```text
l o v e
```

If `"l"` + `"o"` frequently occurs together, the tokenizer can learn:

```text
"lo"
```

Then frequent combinations can be merged further.

Over time:

```text
l + o → lo
lo + v → lov
lov + e → love
```

This is a simplified illustration of the idea.

Actual BPE implementations are more precise and tokenizer-specific.

---

# ⚙️ Different Tokenizers Can Produce Different Results

The same sentence can be tokenized differently by different tokenizers.

For example:

```text
I love AI.
```

One tokenizer might produce:

```text
["I", " love", " AI", "."]
```

Another tokenizer could produce a different sequence.

Therefore:

> ⚠️ There is no single universal tokenization for all LLMs.

The tokenizer is part of the model's input-processing system.

---

# 📏 Token Count

Tokenization determines how many tokens a piece of text contains.

For example:

```text
📝 Sentence
      ↓
🔤 Tokenization
      ↓
🧩 Tokens
      ↓
📏 Token Count
```

A sentence containing 10 words might contain:

```text
8 tokens
```

or:

```text
12 tokens
```

or more.

The exact number depends on the tokenizer.

This matters because LLM context windows are measured in tokens.

---

# 🪟 Tokenization and Context Window

An LLM can only process a certain amount of tokens within its context window.

For example:

```text
📝 Large Text
      ↓
🔤 Tokenization
      ↓
📏 Token Count
      ↓
🪟 Context Window
```

If the token sequence is larger than the model can handle, the entire sequence cannot be processed together.

Therefore, tokenization directly affects how much text can fit into a model's context.

---

# ⚙️ Special Tokens

Tokenizers may also use **special tokens**.

Examples include:

```text
<START>
<END>
<PAD>
<UNK>
```

These tokens are different from normal text tokens.

They can be used to represent things such as:

* ▶️ Beginning of a sequence
* 🛑 End of a sequence
* 📦 Padding
* ❓ Unknown text

Different models and tokenizers use different special tokens.

---

# 🔄 Tokenization During LLM Training

During training, text goes through tokenization before entering the model.

A simplified training pipeline is:

```text
📚 Training Text
       ↓
🔤 Tokenization
       ↓
🔢 Token IDs
       ↓
🧩 Training Sequences
       ↓
🧠 LLM
       ↓
🎯 Next-Token Prediction
       ↓
📉 Loss
       ↓
🔄 Backpropagation
       ↓
⚙️ Parameter Updates
```

The model learns from these token sequences.

---

# 🚀 Tokenization During Text Generation

Tokenization is also used when a user gives an LLM a prompt.

For example:

```text
📝 User Prompt
      ↓
🔤 Tokenization
      ↓
🔢 Token IDs
      ↓
🧠 LLM
      ↓
🎯 Next-Token Prediction
      ↓
🔤 Generated Tokens
      ↓
📝 Generated Text
```

The generated tokens are eventually converted back into human-readable text.

---

# 🔄 Text → Tokens → IDs → Text

The overall idea can be represented as:

```text
📝 Text
   ↓
🔤 Tokenizer
   ↓
🧩 Tokens
   ↓
🔢 Token IDs
   ↓
🧠 LLM
   ↓
🔢 Generated Token IDs
   ↓
🧩 Generated Tokens
   ↓
🔤 Detokenization
   ↓
📝 Text
```

The process of converting tokens back into readable text is commonly called **detokenization** or decoding, depending on the tokenizer/system.

---

# 🆚 Tokenization vs Vocabulary

| Concept         | Meaning                                |
| --------------- | -------------------------------------- |
| 📚 Vocabulary   | Collection of available tokens         |
| 🔄 Tokenization | Process of converting text into tokens |
| 🔤 Token        | Individual piece of text               |
| 🔢 Token ID     | Number identifying a token             |

Example:

```text
Vocabulary
    ↓
["the", "cat", "dog", "ing", "."]
```

Text:

```text
The cat.
```

Tokenization:

```text
["The", " cat", "."]
```

Token IDs:

```text
[125, 842, 18]
```

---

# 🧠 Important Things to Remember

### 1️⃣ Tokens are not always words

```text
Word ≠ Always Token
```

A word can contain multiple tokens.

---

### 2️⃣ Tokenization depends on the tokenizer

Different models can tokenize the same text differently.

---

### 3️⃣ Token IDs are numerical identifiers

```text
Token → Token ID
```

The ID itself does not contain the learned meaning.

---

### 4️⃣ Tokenization happens before the Transformer processes the text

```text
Text
 ↓
Tokenization
 ↓
Token IDs
 ↓
Embeddings
 ↓
Transformer
```

---

### 5️⃣ Token count matters

Context windows are measured in tokens, not simply words.

---

### 6️⃣ Tokenization is not the same as understanding

Tokenization only converts text into pieces.

The model learns patterns later through training.

```text
🔤 Tokenization
       ↓
🔢 Numerical Representation
       ↓
🧠 Model Processing
       ↓
🎓 Learned Patterns
```

---

# 🏗️ Complete Tokenization Flow

Putting everything together:

```text
📝 Human Text
      ↓
🔤 Tokenizer
      ↓
🧩 Tokenization
      ↓
📚 Vocabulary
      ↓
🔤 Tokens
      ↓
🔢 Token IDs
      ↓
🧩 Token Embeddings
      ↓
📍 Positional Information
      ↓
🔄 Transformer
      ↓
🎯 Next-Token Prediction
```

Tokenization is therefore the bridge between **human-readable text** and the **numerical input used by an LLM**.

---

# 💡 Key Takeaways

* 🔤 **Tokenization** converts text into tokens.
* 🧩 A **token** is a piece of text used by an LLM.
* ❌ One word does not always equal one token.
* 🧠 Modern LLMs commonly use subword-style tokenization.
* 📚 Tokenizers use a vocabulary of available tokens.
* 🔢 Tokens are converted into Token IDs.
* 🧩 Token IDs are later converted into embeddings.
* ✏️ Punctuation, numbers, code, and special symbols can also be tokenized.
* 🌍 Different languages can have different tokenization efficiency.
* ⚠️ Different tokenizers can produce different tokens for the same text.
* 📏 Token count affects the amount of text that fits into the context window.
* 🔄 Tokenization is used during both training and inference.
* 🧠 Tokenization itself does not create understanding; it prepares text for the model.
