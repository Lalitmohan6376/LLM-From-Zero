# 📚 Vocabulary

In the previous file, we learned that an LLM processes text through a sequence of steps:

```text id="vocab01"
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

We saw that every token is associated with a number called a **Token ID**.

But this raises an important question:

> 🤔 **Where do these tokens and Token IDs come from?**

The answer is the model's **Vocabulary**.

---

# 📖 What is a Vocabulary?

A **vocabulary** is the collection of tokens that a tokenizer knows and can convert into Token IDs.

In simple words:

> 💡 **Vocabulary = the complete set of tokens available to a tokenizer/model.**

A simplified vocabulary might look like:

```text id="vocab02"
📚 Vocabulary

Token        ID
----------------
"the"        125
"cat"        842
"dog"        731
"hello"      91
"ing"        456
"."          18
```

Each token has a unique ID.

---

# 🔢 Vocabulary and Token IDs

The vocabulary creates a mapping between:

```text id="vocab03"
🔤 Token
   ↕
🔢 Token ID
```

For example:

```text id="vocab04"
"cat"       ↔ 842
"dog"       ↔ 731
"hello"     ↔ 91
"."         ↔ 18
```

When text is tokenized, the tokenizer uses this mapping to convert tokens into numbers.

---

# 🧩 Vocabulary is Not Just a List of Words

This is a very important point.

A vocabulary does **not** necessarily contain only complete words.

Depending on the tokenizer, vocabulary entries can include:

```text id="vocab05"
📝 Complete words
🧩 Parts of words
🔤 Characters
🔢 Numbers
✍️ Punctuation
🔣 Symbols
⚙️ Special tokens
```

For example, a vocabulary could contain:

```text id="vocab06"
"play"
"ing"
"played"
"the"
"."
","
"?"
```

Therefore:

> ⚠️ **Vocabulary = tokens, not simply words.**

---

# 🔤 Example of Vocabulary Tokens

Suppose our vocabulary contains:

```text id="vocab07"
📚 Vocabulary

ID    Token
-----------
0     "the"
1     "cat"
2     "is"
3     "sleep"
4     "ing"
5     "."
```

Now consider the sentence:

```text id="vocab08"
"The cat is sleeping."
```

Depending on the tokenizer, it could be split into tokens such as:

```text id="vocab09"
["The", "cat", "is", "sleep", "ing", "."]
```

The corresponding IDs might be:

```text id="vocab10"
[0, 1, 2, 3, 4, 5]
```

These numbers are only for illustration.

Real tokenizers have much larger vocabularies and different token IDs.

---

# 🏗️ How is a Vocabulary Created?

A vocabulary is generally created as part of the **tokenizer design and training process**.

A simplified view is:

```text id="vocab11"
📚 Text Data
      ↓
🔍 Analyze Text Patterns
      ↓
🔤 Build Token Vocabulary
      ↓
📚 Vocabulary
      ↓
🔢 Assign Token IDs
```

Different tokenization algorithms create vocabularies in different ways.

For example:

```text id="vocab12"
Character-Level
      ↓
Characters become tokens

Word-Level
      ↓
Words become tokens

Subword-Level
      ↓
Words and word-parts become tokens
```

We will study these approaches later.

---

# 📏 What is Vocabulary Size?

**Vocabulary size** means the total number of tokens in the vocabulary.

For example:

```text id="vocab13"
📚 Vocabulary

Token 1
Token 2
Token 3
...
Token 10,000

Vocabulary Size = 10,000
```

If a tokenizer has:

```text id="vocab14"
50,000 tokens
```

then:

> 📏 **Vocabulary size = 50,000**

The vocabulary size is fixed for a particular tokenizer/model configuration.

---

# 🧠 Why Does Vocabulary Size Matter?

Vocabulary size affects several parts of an LLM.

For example:

```text id="vocab15"
📏 Vocabulary Size
        ↓
🔤 Number of Available Tokens
        ↓
🔢 Token IDs
        ↓
🧩 Embedding Matrix
        ↓
📊 Output Vocabulary
```

A larger vocabulary can contain more token patterns.

A smaller vocabulary may split text into more pieces.

There are trade-offs involved in choosing vocabulary size.

---

# 🪶 Small Vocabulary

Suppose we have a very small vocabulary.

```text id="vocab16"
📚 Small Vocabulary
        ↓
Fewer Available Tokens
        ↓
Words may be split into
more smaller pieces
```

For example:

```text id="vocab17"
"playing"

      ↓

"play" + "ing"
```

Or it could be split into even smaller pieces depending on the tokenizer.

---

# 🚀 Large Vocabulary

With a larger vocabulary:

```text id="vocab18"
📚 Large Vocabulary
        ↓
More Available Tokens
        ↓
Some common words or patterns
can be represented by larger pieces
```

For example, a common word might exist as a single token.

```text id="vocab19"
"computer"
    ↓
One token
```

But this depends entirely on the tokenizer.

---

# ⚖️ Vocabulary Size is a Trade-Off

Choosing a vocabulary size involves trade-offs.

A simplified idea:

```text id="vocab20"
🪶 Smaller Vocabulary
       ↓
More Token Splitting
       +
Smaller Vocabulary

        vs.

🚀 Larger Vocabulary
       ↓
Fewer Splits for Some Text
       +
Larger Vocabulary
```

There is no single vocabulary size that is best for every model.

---

# 🔤 Vocabulary vs Tokenization

These two concepts are closely related but different.

### 📚 Vocabulary

The set of tokens that are available.

```text id="vocab21"
📚 Vocabulary
   ↓
["the", "cat", "ing", ".", ...]
```

### 🔤 Tokenization

The process of breaking text into tokens using that vocabulary.

```text id="vocab22"
📝 "The cat is sleeping."
          ↓
🔤 Tokenization
          ↓
["The", "cat", "is", "sleep", "ing", "."]
```

So:

> 📚 **Vocabulary = what tokens are available.**

> 🔤 **Tokenization = how text is divided into those tokens.**

---

# 🔢 Vocabulary vs Token IDs

These are also different.

### 📚 Vocabulary

Contains the tokens.

```text id="vocab23"
"cat"
"dog"
"hello"
"ing"
"."
```

### 🔢 Token IDs

Give each token a numerical identifier.

```text id="vocab24"
"cat"    → 842
"dog"    → 731
"hello"  → 91
"ing"    → 456
"."      → 18
```

Therefore:

```text id="vocab25"
📚 Vocabulary
      ↓
🔤 Tokens
      ↓
🔢 Token IDs
```

---

# 🧩 Vocabulary and Embeddings

Vocabulary is also directly connected to the embedding layer.

Suppose a model has:

```text id="vocab26"
Vocabulary Size = 50,000
```

and each token is represented using:

```text id="vocab27"
Embedding Dimension = 768
```

The model can have an embedding matrix conceptually shaped like:

```text id="vocab28"
          768 dimensions
       ←──────────────→

Token 1   [ ... ... ... ]
Token 2   [ ... ... ... ]
Token 3   [ ... ... ... ]
   .
   .
Token 50,000
```

So, in simplified terms:

```text id="vocab29"
📚 Vocabulary
      ↓
🔢 Token IDs
      ↓
🧩 Embedding Matrix
      ↓
📊 Token Vectors
```

We will study embeddings in much more detail later.

---

# 🎯 Vocabulary and Next-Token Prediction

Vocabulary also matters during text generation.

Suppose an LLM receives:

```text id="vocab30"
"The sky is"
```

The model produces scores for possible tokens from its vocabulary.

Simplified:

```text id="vocab31"
"The sky is"
      ↓
🧠 LLM
      ↓
📊 Scores for Vocabulary Tokens
      ↓
┌─────────────────────┐
│ "blue"      0.55    │
│ "clear"     0.18    │
│ "dark"      0.05    │
│ ...                 │
└─────────────────────┘
      ↓
🎯 Select Next Token
```

The actual model produces logits first, which are then converted into probabilities.

For now, the important idea is:

> 💡 **The model predicts among tokens in its vocabulary.**

---

# 🔄 Vocabulary During Training and Generation

Vocabulary is used throughout the LLM pipeline.

### 🎓 During Training

```text id="vocab32"
📝 Training Text
      ↓
🔤 Tokenization
      ↓
📚 Vocabulary Lookup
      ↓
🔢 Token IDs
      ↓
🧩 Embeddings
      ↓
🧠 LLM
```

### 🚀 During Generation

```text id="vocab33"
📝 Prompt
   ↓
🔤 Tokenization
   ↓
🔢 Token IDs
   ↓
🧠 LLM
   ↓
📊 Scores for Vocabulary
   ↓
🎯 Next Token
   ↓
🔄 Repeat
```

The same vocabulary is used to interpret input tokens and represent possible output tokens.

---

# ⚙️ Vocabulary is Connected to the Tokenizer

A tokenizer is responsible for converting between text and tokens/IDs.

A simplified view:

```text id="vocab34"
          🔤 Tokenizer
          ↙        ↘
     Text → Tokens → IDs
     IDs → Tokens → Text
```

The vocabulary is one of the key pieces used by the tokenizer.

---

# 🔄 Token → ID → Token

The mapping works in both directions.

For example:

```text id="vocab35"
"hello"
   ↓
🔢 91
   ↓
"hello"
```

This allows the system to convert between human-readable tokens and their numerical IDs.

Simplified:

```text id="vocab36"
📝 Text
   ↓
🔤 Token
   ↓
🔢 Token ID
   ↓
🧠 Model
   ↓
🔢 Token ID
   ↓
🔤 Token
   ↓
📝 Text
```

---

# ⭐ Special Tokens

A vocabulary can also contain **special tokens**.

These are tokens used for specific purposes rather than ordinary words.

Examples can include:

```text id="vocab37"
<START>
<END>
<PAD>
<UNK>
```

The exact special tokens depend on the tokenizer and model.

For example:

```text id="vocab38"
<START> → Beginning
<END>   → End
<PAD>   → Padding
```

Special tokens help the tokenizer/model represent information that ordinary text tokens cannot always express directly.

We will study them separately in:

➡️ **[Special Tokens](./Special-Tokens.md)**

---

# 🌍 Vocabulary Can Contain Multiple Languages

A vocabulary does not necessarily belong to only one language.

Modern tokenizers can contain tokens representing patterns from many languages.

For example:

```text id="vocab39"
📚 Vocabulary
    ↓
🇬🇧 English
🇮🇳 Hindi
🇪🇸 Spanish
🇫🇷 French
🇩🇪 German
...
```

However, the exact language coverage depends on how the tokenizer and model were designed and trained.

---

# 💻 Vocabulary Can Contain Code

For models trained on code as well as natural language, the vocabulary can also represent programming-related text.

For example:

```text id="vocab40"
def
(
)
:
=
print
import
```

These can be represented as tokens or combinations of tokens depending on the tokenizer.

This is one reason tokenization is also important for code-generating LLMs.

---

# 🧠 Vocabulary Does Not Contain "Knowledge"

This is another important distinction.

Suppose:

```text id="vocab41"
"Paris" → Token ID 512
```

The vocabulary containing the token `"Paris"` does **not** mean that the vocabulary itself contains all knowledge about Paris.

The vocabulary mainly defines the tokens that can be represented.

Knowledge and learned patterns are stored in the model's **parameters** during training.

Simplified:

```text id="vocab42"
📚 Vocabulary
      ↓
Defines Tokens

🧠 Model Parameters
      ↓
Learned Patterns
```

Do not confuse the two.

---

# 🧩 Vocabulary, Tokenizer, and Model

These three concepts are closely connected:

```text id="vocab43"
📚 Vocabulary
   ↓
Defines Available Tokens

🔤 Tokenizer
   ↓
Converts Text ↔ Tokens / IDs

🧠 Model
   ↓
Processes Token Representations
```

A simplified complete flow:

```text id="vocab44"
📝 Text
   ↓
🔤 Tokenizer
   ↓
📚 Vocabulary
   ↓
🔢 Token IDs
   ↓
🧩 Embeddings
   ↓
🧠 LLM
```

---

# 🎯 A Simple Example

Let's imagine a tiny vocabulary:

```text id="vocab45"
ID    Token
-----------
0     "I"
1     "love"
2     "AI"
3     "."
4     "!"
```

Input:

```text id="vocab46"
"I love AI!"
```

Tokenization:

```text id="vocab47"
["I", "love", "AI", "!"]
```

Token IDs:

```text id="vocab48"
[0, 1, 2, 4]
```

Then:

```text id="vocab49"
[0, 1, 2, 4]
       ↓
🧩 Embeddings
       ↓
🧠 Transformer
```

If the model generates:

```text id="vocab50"
"."
```

the tokenizer can map that token back to text.

---

# 🔄 Complete Vocabulary Flow

We can now connect the entire concept:

```text id="vocab51"
📚 Vocabulary
      ↓
🔤 Available Tokens
      ↓
🔢 Token IDs
      ↓
🧩 Embeddings
      ↓
🧠 Transformer
      ↓
📊 Output Scores
      ↓
🎯 Select Token
      ↓
🔢 Token ID
      ↓
🔤 Token
      ↓
📝 Text
```

---

# 🎯 Key Takeaways

* 📚 A **vocabulary** is the collection of tokens available to a tokenizer/model.
* 🔤 Vocabulary contains tokens, not necessarily complete words.
* 🧩 Tokens can represent words, word parts, characters, punctuation, symbols, or special tokens.
* 🔢 Each token is associated with a Token ID.
* 📏 **Vocabulary size** is the total number of tokens in the vocabulary.
* 🔤 Tokenization is the process of breaking text into tokens using the tokenizer.
* 📚 Vocabulary and tokenization are related but are not the same thing.
* 🔢 Token IDs identify tokens; they do not themselves contain the token's meaning.
* 🧩 Token IDs are converted into embeddings before being processed by the neural network.
* 🎯 During generation, the model predicts among tokens represented in its vocabulary.
* ⚙️ The tokenizer, vocabulary, and model work together as part of the text-processing pipeline.
* 🧠 The vocabulary itself does not contain the model's learned knowledge; the model's parameters store learned patterns.

The simplest way to remember:

```text id="vocab52"
📚 VOCABULARY
      ↓
🔤 What tokens are available?
      ↓
🔢 TOKEN IDs
      ↓
🧩 EMBEDDINGS
      ↓
🧠 MODEL
```
