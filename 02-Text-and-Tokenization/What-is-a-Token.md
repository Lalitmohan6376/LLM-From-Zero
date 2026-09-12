# 🔤 What is a Token?

A **token** is a small piece of text that an LLM works with.

Before an LLM can process human-readable text, the text is broken into tokens. These tokens are then converted into numbers called **Token IDs**, which are used by the model.

A token can be:

* 📝 A complete word
* 🧩 Part of a word
* 🔤 A character
* 🔢 A number
* ✏️ Punctuation
* 💻 Part of code
* ⚙️ A special token

The exact way text is divided into tokens depends on the **tokenizer** and the model.

---

## 🧠 Simple Example

Consider this sentence:

```text
The cat is sleeping.
```

A tokenizer might split it into:

```text
["The", " cat", " is", " sleeping", "."]
```

These pieces are called **tokens**.

The important thing is that tokens are not always the same as words.

---

# 📝 Token vs Word

A common beginner mistake is to think:

> One word = one token

This is **not always true**.

For example:

```text
I love AI.
```

A tokenizer might produce something like:

```text
["I", " love", " AI", "."]
```

Here, there are 4 tokens.

But a longer or uncommon word may be split into multiple tokens.

For example:

```text
unbelievable
```

could be represented approximately as:

```text
["un", "believ", "able"]
```

The exact split depends on the tokenizer.

So:

```text
1 Word ≠ Always 1 Token
```

---

# 🧩 Why Do LLMs Use Tokens?

Computers cannot directly process human language as words and sentences.

An LLM works with numerical representations.

Therefore, the text goes through several steps:

```text
📝 Human Text
      ↓
🔤 Tokens
      ↓
🔢 Token IDs
      ↓
🧩 Embeddings
      ↓
🧠 Transformer
```

Tokens provide a practical way to convert text into something the model can process.

---

# 🔤 What Can Be a Token?

Tokens can represent different kinds of text.

## 1️⃣ Complete Words

Some common words may appear as individual tokens.

```text
"hello"
"the"
"computer"
```

Example:

```text
Hello world
```

Could become:

```text
["Hello", " world"]
```

---

## 2️⃣ Parts of Words

Long, rare, or complex words may be divided into smaller pieces.

For example:

```text
unhappiness
```

could be split approximately as:

```text
["un", "happi", "ness"]
```

This allows the tokenizer to represent words that may not exist as complete vocabulary entries.

---

## 3️⃣ Punctuation

Punctuation can also be represented as tokens.

For example:

```text
Hello, world!
```

could contain tokens representing:

```text
Hello
,
 world
!
```

So punctuation is also part of the model's input.

---

## 4️⃣ Numbers

Numbers can also be represented using one or more tokens.

For example:

```text
2026
```

may be represented as one token or several tokens depending on the tokenizer.

The exact result depends on the model's vocabulary and tokenization rules.

---

## 5️⃣ Code

Tokens are not limited to normal English text.

Programming code can also be divided into tokens.

For example:

```python
print("Hello")
```

may be split into pieces representing:

```text
print
(
"Hello"
)
```

The exact tokenization depends on the tokenizer.

---

## 6️⃣ Special Tokens

Some tokenizers also contain special tokens used for specific purposes.

Examples include:

```text
<START>
<END>
<PAD>
<UNK>
```

Different models use different special tokens.

These tokens can help represent things such as:

* ▶️ Beginning of a sequence
* 🛑 End of a sequence
* 📦 Padding
* ❓ Unknown or unsupported text

---

# 🔄 Tokenization

The process of converting text into tokens is called **Tokenization**.

For example:

```text
📝 Text
   ↓
🔤 Tokenizer
   ↓
🧩 Tokens
```

Example:

```text
Input:

The cat is sleeping.
```

Possible tokenization:

```text
["The", " cat", " is", " sleeping", "."]
```

The individual pieces are **tokens**.

The process that creates them is **tokenization**.

---

# 🔢 Tokens and Token IDs

The LLM does not normally send the text tokens directly into the neural network.

Each token is mapped to a number called a **Token ID**.

For example, a simplified vocabulary might look like:

```text
Token        ID
----------------
"the"        125
"cat"        842
"dog"        731
"hello"      91
"ing"        456
"."          18
```

If the text contains:

```text
the cat
```

the tokenizer could produce:

```text
["the", " cat"]
```

and then convert them into IDs:

```text
[125, 842]
```

The actual IDs depend on the tokenizer.

---

# 🧠 Token → Token ID → Embedding

After tokenization, the process continues:

```text
📝 Text
   ↓
🔤 Tokens
   ↓
🔢 Token IDs
   ↓
🧩 Embeddings
   ↓
🧠 Transformer
```

For example:

```text
"The cat"
```

might become:

```text
Tokens:

["The", " cat"]
```

Then:

```text
Token IDs:

[125, 842]
```

Then the IDs are converted into numerical vectors called **embeddings**.

These embeddings are what the Transformer processes.

---

# 📚 Tokens Come From the Vocabulary

A tokenizer uses a **Vocabulary** containing the tokens that it knows how to represent.

For example:

```text
📚 Vocabulary

"the"
"cat"
"dog"
"hello"
"ing"
"."
","
...
```

Each token has an associated ID.

Therefore:

```text
Vocabulary
     ↓
Available Tokens
     ↓
Token IDs
```

You can learn more about this in:

👉 [Vocabulary](./Vocabulary.md)

---

# 📏 Token Count

LLMs work with tokens rather than simply counting words.

For example:

```text
📝 Text
   ↓
🔤 Tokenization
   ↓
🔢 Token Count
```

The number of tokens can be different from the number of words.

For example:

```text
5 words
```

might become:

```text
7 tokens
```

or:

```text
5 tokens
```

or even more.

There is no universal fixed relationship between words and tokens.

---

# 🪟 Tokens and Context Window

An LLM has a maximum amount of text it can process at one time.

This is called its **Context Window**.

The context window is generally measured in tokens.

For example:

```text
🪟 Context Window
        ↓
Maximum number of tokens
        ↓
Input + Available Context
```

If the input becomes too large for the model's context window, the model cannot process the entire input as one sequence.

So token count is important when working with LLMs.

---

# 🌍 Tokens Are Not Only English Words

Tokenizers can represent many types of text.

For example:

### English

```text
Hello world
```

### Hindi

```text
नमस्ते दुनिया
```

### Numbers

```text
123456
```

### Code

```python
print("Hello")
```

### Symbols

```text
AI → ML → DL
```

All of these can be converted into tokens.

The exact tokenization depends on the tokenizer and vocabulary.

---

# 🤔 Why Not Simply Use Words?

Using only complete words would create problems.

Imagine a vocabulary containing every possible word:

```text
beautiful
beautifully
beautification
beautified
...
```

There could be a huge number of possible words.

Instead, modern tokenizers can reuse smaller pieces.

For example:

```text
beautiful
beauty
beautifully
```

may share some token pieces.

This allows the vocabulary to represent many different words using a manageable set of tokens.

---

# 🧩 Subwords

One important idea behind modern tokenization is **subword tokenization**.

Instead of requiring every complete word to exist in the vocabulary, words can be represented using smaller pieces.

For example:

```text
playing
```

could be represented approximately as:

```text
["play", "ing"]
```

Then another word:

```text
played
```

might share:

```text
["play", "ed"]
```

This allows the tokenizer to reuse common pieces.

> ⚠️ These examples are only for understanding. Actual token splits depend on the tokenizer.

---

# 🔄 Token Sequence

Once text is tokenized, the tokens form a sequence.

For example:

```text
The cat is sleeping.
```

could become:

```text
[The] [cat] [is] [sleeping] [.]
```

This sequence is then converted into Token IDs:

```text
[125] [842] [91] [456] [18]
```

The order of these tokens is important.

The model needs to know not only **which tokens exist**, but also **where they occur in the sequence**.

This is where positional information becomes important.

---

# 🎯 Tokens and Next-Token Prediction

For a language model, tokens are the basic units used for prediction.

Suppose the input is:

```text
The sun rises in the
```

The model processes the tokens and predicts a probability distribution over possible next tokens.

For example:

```text
east      → 0.70
morning   → 0.10
sky       → 0.05
west      → 0.02
...
```

The model then selects or samples a next token.

```text
The sun rises in the
                 ↓
                east
```

Then the generated token becomes part of the sequence:

```text
The sun rises in the east
```

The model predicts the next token again.

This process continues during text generation.

---

# 🔄 Token Generation Loop

A simplified generation process looks like this:

```text
📝 Input Text
      ↓
🔤 Tokenization
      ↓
🔢 Token IDs
      ↓
🧠 LLM
      ↓
🎯 Predict Next Token
      ↓
➕ Add Token
      ↓
🧠 LLM Again
      ↓
🎯 Predict Next Token
      ↓
🔄 Repeat
```

Eventually, the generated tokens are converted back into text.

```text
🔢 Token IDs
      ↓
🔤 Tokens
      ↓
📝 Human-Readable Text
```

---

# 🧠 Important: Tokens Are Not Meaning

A Token ID is simply an identifier.

For example:

```text
"cat" → 842
```

The number `842` does not mean that the number itself contains the meaning of "cat".

It is simply an ID used to identify that token.

The model learns useful representations through its **embeddings and parameters**.

So:

```text
Token
  ↓
Token ID
  ↓
Embedding
  ↓
Learned Representation
```

---

# ⚠️ Exact Tokens Depend on the Tokenizer

There is no single universal way to tokenize text.

Different tokenizers can split the same sentence differently.

For example:

```text
"I love machine learning."
```

One tokenizer might produce:

```text
["I", " love", " machine", " learning", "."]
```

Another tokenizer could produce a different sequence.

Therefore:

> **Token count and token boundaries depend on the tokenizer and model.**

This is important when comparing different LLMs.

---

# 🆚 Token vs Token ID

These two terms are related but different.

| Concept     | Meaning                       |
| ----------- | ----------------------------- |
| 🔤 Token    | Piece of text                 |
| 🔢 Token ID | Number identifying that token |

Example:

```text
Token:

"hello"

Token ID:

91
```

So:

```text
"hello" → 91
```

---

# 🆚 Token vs Tokenization

These terms are also different.

| Concept         | Meaning                               |
| --------------- | ------------------------------------- |
| 🔤 Token        | Individual piece of text              |
| 🔄 Tokenization | Process of splitting text into tokens |

Example:

```text
Text
 ↓
Tokenization
 ↓
["The", " cat", " sleeps", "."]
```

Here:

* `The` is a token
* `cat` is a token
* `sleeps` is a token
* `.` is a token
* The whole process is tokenization

---

# 🚀 Complete Flow

The role of tokens in an LLM can be summarized as:

```text
📝 Human Text
      ↓
🔤 Tokenization
      ↓
🧩 Tokens
      ↓
🔢 Token IDs
      ↓
🧠 Token Embeddings
      ↓
📍 Positional Information
      ↓
🔄 Transformer Blocks
      ↓
📊 Output
      ↓
🎯 Next-Token Prediction
      ↓
🔢 Next Token ID
      ↓
🔤 Next Token
      ↓
📝 Generated Text
```

---

# 💡 Key Takeaways

* 🔤 A **token** is a piece of text processed by an LLM.
* 📝 A token can be a word, part of a word, punctuation, number, code piece, or special token.
* ❌ One word does not always equal one token.
* 🔄 **Tokenization** is the process of converting text into tokens.
* 🔢 Every token is mapped to a **Token ID**.
* 🧩 Token IDs are converted into **embeddings**.
* 🧠 The Transformer processes these numerical representations.
* 🎯 LLMs use tokens as the basic units for next-token prediction.
* 📏 Context windows are measured in tokens.
* ⚠️ Exact tokenization depends on the tokenizer and model.
* 🧠 Token IDs are identifiers; they do not themselves contain the model's learned meaning.

