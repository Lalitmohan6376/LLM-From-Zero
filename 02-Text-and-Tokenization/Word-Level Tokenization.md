# 📝 Word-Level Tokenization

**Word-Level Tokenization** is a tokenization method where each word in a text is treated as a separate token.

Instead of breaking text into individual characters or smaller pieces, the tokenizer tries to represent complete words.

For example:

```text id="g0p5p7"
The cat is sleeping.
```

could become:

```text id="lq9q4x"
["The", "cat", "is", "sleeping", "."]
```

Here, each word is treated as a token, while punctuation may also be represented separately.

---

# 🧠 Simple Idea

The basic idea is:

```text id="x8h8de"
📝 Text
   ↓
🔤 Split Into Words
   ↓
🧩 Word Tokens
```

For example:

```text id="f2j3b4"
I love AI.
```

becomes approximately:

```text id="q7y8z9"
["I", "love", "AI", "."]
```

Each complete word becomes a token.

---

# 🔤 Word = Token

In word-level tokenization, the basic assumption is:

```text id="j1k2l3"
1 Word → 1 Token
```

For example:

```text id="m4n5o6"
machine learning
```

can become:

```text id="p7q8r9"
["machine", "learning"]
```

So there are two word tokens.

However, punctuation, spaces, and other text details can be handled differently depending on the tokenizer.

---

# 📝 Example

Consider:

```text id="a1b2c3"
The cat is sleeping.
```

A simple word-level tokenizer might produce:

```text id="d4e5f6"
["The", "cat", "is", "sleeping", "."]
```

The sequence contains:

```text id="g7h8i9"
The       → Token
cat       → Token
is        → Token
sleeping  → Token
.         → Token
```

So the tokenizer represents the sentence using complete words and punctuation.

---

# 🔢 Words to Token IDs

After the text is divided into words, each word is mapped to a numerical **Token ID**.

Suppose the vocabulary contains:

```text id="j1k2l3"
Word          ID
----------------
"the"         125
"cat"         842
"is"          91
"sleeping"    456
"."           18
```

Then:

```text id="m4n5o6"
The cat is sleeping.
```

could become:

```text id="p7q8r9"
["The", "cat", "is", "sleeping", "."]
```

and then:

```text id="s1t2u3"
[125, 842, 91, 456, 18]
```

The actual IDs depend on the tokenizer.

---

# 📚 Word-Level Vocabulary

Word-level tokenization requires a vocabulary containing words.

For example:

```text id="v4w5x6"
📚 Vocabulary

the
cat
dog
computer
learning
machine
AI
...
```

Each word has a corresponding Token ID.

The vocabulary can become very large because natural language contains a huge number of words and word forms.

---

# 🧠 Why Can the Vocabulary Become Large?

Consider different forms of the same basic word:

```text id="y7z8a9"
play
plays
played
playing
player
players
```

A word-level tokenizer may need separate vocabulary entries for each of these.

Similarly:

```text id="b1c2d3"
learn
learned
learning
learner
learners
```

may all need separate entries.

This can make the vocabulary very large.

---

# 🆕 The Unknown Word Problem

One of the biggest problems with word-level tokenization is handling words that are **not present in the vocabulary**.

Suppose the vocabulary contains:

```text id="e4f5g6"
cat
dog
computer
learning
```

But the input contains:

```text id="h7i8j9"
supercalifragilistic
```

If the complete word is not in the vocabulary, the tokenizer may not know how to represent it directly.

A common solution is an **unknown token**:

```text id="k1l2m3"
<UNK>
```

So:

```text id="n4o5p6"
supercalifragilistic
        ↓
      <UNK>
```

This means information about the original word may be lost.

---

# ❓ Unknown Tokens

`<UNK>` means **Unknown Token**.

It can be used when the tokenizer encounters text that it cannot represent using its vocabulary.

For example:

```text id="q7r8s9"
Vocabulary:

cat
dog
house
```

Input:

```text id="t1u2v3"
elephant
```

If `"elephant"` is not in the vocabulary:

```text id="w4x5y6"
elephant → <UNK>
```

This is one reason pure word-level tokenization can be problematic for large-scale language modeling.

---

# 🧩 Rare Words

Rare words create a similar problem.

Suppose the vocabulary contains common words:

```text id="z7a8b9"
computer
learning
language
model
```

but a rare technical term appears:

```text id="c1d2e3"
electrophotoluminescence
```

If the complete word is not in the vocabulary, a word-level tokenizer may have to represent it as `<UNK>`.

A subword tokenizer can instead break the word into smaller reusable pieces.

---

# 🆚 Word-Level vs Character-Level

Word-level tokenization and character-level tokenization use very different basic units.

### Character-Level

```text id="f4g5h6"
cat
↓
c | a | t
```

### Word-Level

```text id="i7j8k9"
cat
↓
cat
```

So:

```text id="l1m2n3"
🔤 Character-Level
→ Smaller units

📝 Word-Level
→ Larger units
```

---

# 📏 Sequence Length

Word-level tokenization usually produces fewer tokens than character-level tokenization for normal text.

For example:

```text id="o4p5q6"
The cat is sleeping.
```

Character-level:

```text id="r7s8t9"
T | h | e |   | c | a | t |   | i | s | ...
```

Word-level:

```text id="u1v2w3"
The | cat | is | sleeping | .
```

Therefore:

```text id="x4y5z6"
Word-Level
     ↓
Fewer Tokens
     ↓
Shorter Sequence
```

This can make the representation more efficient in terms of sequence length.

---

# 🧠 But Fewer Tokens Does Not Mean Better

A smaller number of tokens is not automatically better.

Word-level tokenization has to deal with:

* 📚 Very large vocabularies
* ❓ Unknown words
* 🆕 New words
* 🔤 Different word forms
* 🌍 Multiple languages
* 💻 Code and unusual text

So there is a trade-off:

```text id="a7b8c9"
📚 Larger Vocabulary
        +
📏 Shorter Sequences
```

versus:

```text id="d1e2f3"
📚 Smaller Vocabulary
        +
📏 Longer Sequences
```

This trade-off is one reason subword tokenization became important.

---

# 🌍 Different Languages

Word-level tokenization can behave differently across languages.

Some languages use spaces to separate words clearly.

For example:

```text id="g4h5i6"
I love AI.
```

can naturally be separated into:

```text id="j7k8l9"
I | love | AI
```

But languages with different writing systems or different word-boundary rules can make word-level tokenization more complicated.

For example:

```text id="m1n2o3"
नमस्ते दुनिया
```

requires language-aware handling of text.

Therefore, creating a single word-based vocabulary for many languages can become difficult.

---

# 💻 Word-Level Tokenization and Code

Programming code does not always behave like normal language.

Consider:

```python id="p4q5r6"
total_price = item_price + tax
```

A simple word-level tokenizer might identify pieces such as:

```text id="s7t8u9"
total_price
=
item_price
+
tax
```

But programming languages contain many symbols and structures:

```text id="v1w2x3"
(
)
[
]
{
}
=
+
-
*
/
:
;
```

A pure word-level tokenizer is therefore not ideal for representing all possible code.

Modern tokenizers often use smaller pieces to handle code more flexibly.

---

# 🧩 Word-Level Tokenization and Word Forms

Consider:

```text id="y4z5a6"
play
playing
played
player
```

A word-level tokenizer treats them as separate words:

```text id="b7c8d9"
play
playing
played
player
```

A subword tokenizer can potentially reuse common pieces:

```text id="e1f2g3"
play + ing
play + ed
play + er
```

This allows a smaller vocabulary to represent many related words.

---

# ⚖️ Advantages of Word-Level Tokenization

## ✅ 1. Easy to Understand

The concept is simple:

```text id="h4i5j6"
Word → Token
```

This makes it useful for learning the basic idea of tokenization.

---

## ✅ 2. Shorter Sequences

Compared with character-level tokenization, normal sentences require fewer tokens.

```text id="k7l8m9"
📝 Sentence
   ↓
🧩 Fewer Word Tokens
```

---

## ✅ 3. Tokens Can Represent Complete Words

A complete word can be directly represented as a token.

For example:

```text id="n1o2p3"
computer → Token
```

This makes word boundaries easy to understand.

---

## ✅ 4. Simple Token IDs

Each vocabulary word can have its own ID.

```text id="q4r5s6"
"computer" → 1204
```

---

# ❌ Disadvantages of Word-Level Tokenization

## ❌ 1. Very Large Vocabulary

A vocabulary containing every possible word and word form can become huge.

```text id="t7u8v9"
📚 Huge Vocabulary
```

---

## ❌ 2. Unknown Words

Words outside the vocabulary may become:

```text id="w1x2y3"
<UNK>
```

---

## ❌ 3. Poor Handling of Rare Words

Rare words may not exist as complete vocabulary entries.

---

## ❌ 4. New Words Are Difficult

Language constantly creates new words, names, technical terms, and variations.

A fixed word vocabulary cannot easily contain every possible word.

---

## ❌ 5. Different Word Forms Increase Vocabulary

For example:

```text id="z4a5b6"
run
runs
running
ran
runner
```

may require separate entries.

---

# 🧠 Word-Level Tokenization Pipeline

A simplified pipeline is:

```text id="c7d8e9"
📝 Human Text
      ↓
🔤 Split Into Words
      ↓
🧩 Word Tokens
      ↓
🔢 Token IDs
      ↓
🧩 Embeddings
      ↓
📍 Positional Information
      ↓
🔄 Transformer
      ↓
🎯 Prediction
```

The important difference is that the tokenizer chooses **words** as the basic units.

---

# 🎯 Next-Token Prediction

A language model can predict the next word token.

For example:

```text id="f1g2h3"
The sun rises in the
```

The model may predict:

```text id="i4j5k6"
east
```

giving:

```text id="l7m8n9"
The sun rises in the east
```

The next prediction can then continue from the updated sequence.

In a pure word-level language model, the prediction would be among vocabulary words.

---

# 🔄 Generation Example

A simplified process:

```text id="o1p2q3"
📝 Input:

The sun rises in the
```

↓

```text id="r4s5t6"
🧠 Model
```

↓

```text id="u7v8w9"
🎯 Predict:

east
```

↓

```text id="x1y2z3"
📝 Updated Text:

The sun rises in the east
```

↓

```text id="a4b5c6"
🎯 Predict Next Word
```

This continues autoregressively.

---

# 🆚 Word-Level vs Character-Level vs Subword

| Feature            | Character-Level            | Word-Level                       | Subword               |
| ------------------ | -------------------------- | -------------------------------- | --------------------- |
| 🔤 Basic unit      | Character                  | Word                             | Word piece            |
| 📚 Vocabulary      | Small                      | Large                            | Medium                |
| 📏 Sequence length | Long                       | Short                            | Medium                |
| 🆕 Rare words      | Good                       | Poor                             | Good                  |
| ❓ Unknown words    | Usually easy to represent  | Problematic                      | Usually handled well  |
| 🧠 Word structure  | Must learn from characters | Direct                           | Partially represented |
| ⚖️ Efficiency      | Lower                      | Can be efficient for common text | Good balance          |

Subword tokenization attempts to combine useful properties of both character-level and word-level approaches.

---

# 🚀 Why Modern LLMs Usually Use Subwords

Pure word-level tokenization has an important weakness:

```text id="d7e8f9"
New / Rare Word
      ↓
❓ Not in Vocabulary
      ↓
<UNK>
```

Subword tokenization provides another option:

```text id="g1h2i3"
New / Rare Word
      ↓
🧩 Smaller Known Pieces
      ↓
🔢 Token IDs
```

For example, a rare word might be represented using several known pieces rather than becoming completely unknown.

This gives modern LLMs a useful balance:

```text id="j4k5l6"
📚 Manageable Vocabulary
          +
📏 Reasonable Sequence Length
          +
🆕 Better Rare-Word Handling
```

---

# 🧠 Important: Word-Level Tokenization Is a Concept

When learning tokenization, word-level tokenization is useful because it makes the basic idea very easy to understand:

```text id="m7n8o9"
Text
 ↓
Words
 ↓
Token IDs
```

However, modern LLM tokenizers generally use more flexible approaches, especially subword-based methods.

---

# 🏗️ Complete Example

Suppose the input is:

```text id="p1q2r3"
I love machine learning.
```

### Step 1 — Input Text

```text id="s4t5u6"
📝 I love machine learning.
```

### Step 2 — Word Tokenization

```text id="v7w8x9"
["I", "love", "machine", "learning", "."]
```

### Step 3 — Token IDs

For example:

```text id="y1z2a3"
[21, 84, 912, 456, 18]
```

### Step 4 — Embeddings

```text id="b4c5d6"
🔢 Token IDs
      ↓
🧩 Embeddings
```

### Step 5 — Transformer

```text id="e7f8g9"
🧠 Transformer
```

### Step 6 — Prediction

```text id="h1i2j3"
🎯 Next Token
```

So the complete flow is:

```text id="k4l5m6"
📝 Text
   ↓
📝 Words
   ↓
🧩 Word Tokens
   ↓
🔢 Token IDs
   ↓
🧩 Embeddings
   ↓
🧠 Transformer
   ↓
🎯 Next-Token Prediction
```

---

# 💡 Key Takeaways

* 📝 **Word-Level Tokenization** treats complete words as tokens.
* 🔤 The basic idea is `Word → Token`.
* 📚 It requires a vocabulary containing words.
* 📏 It usually produces shorter sequences than character-level tokenization.
* ❓ Words that are not in the vocabulary can become `<UNK>`.
* 🆕 Rare and newly created words can be difficult to represent.
* 📚 Supporting many word forms can make the vocabulary very large.
* 🌍 Different languages create additional challenges for word-level tokenization.
* 💻 Code and unusual text are not always handled efficiently by pure word-level tokenization.
* ⚖️ Word-level tokenization provides shorter sequences but requires a much larger vocabulary.
* 🧩 Subword tokenization provides a useful balance between word-level and character-level approaches.
* 🚀 Modern LLMs generally use subword-style tokenization rather than pure word-level tokenization.

---
