# 🏷️ Special Tokens

**Special tokens** are predefined tokens used by a tokenizer or language model for specific purposes.

Unlike normal text tokens such as words, word pieces, or punctuation, special tokens provide **additional information about the structure or processing of the input**.

For example:

```text
📝 Normal Tokens
"Hello"
"world"
"."

🏷️ Special Tokens
<START>
<END>
<PAD>
<UNK>
```

> 💡 **Simple idea:** Special tokens are tokens with a specific purpose beyond representing ordinary text.

---

# 🧠 Why Do We Need Special Tokens?

A model needs to process sequences of tokens.

Sometimes, the model also needs information such as:

* Where a sequence starts
* Where a sequence ends
* Which positions are padding
* How different parts of input are separated
* How unknown or unusual content should be represented

Special tokens can provide this information.

A simplified sequence might look like:

```text
id="s8m2qp"
<START> Hello world <END>
```

Here:

```text
<START> → tells the system where the sequence begins
<END>   → tells the system where the sequence ends
```

The exact tokens used depend on the tokenizer and model.

---

# 🏷️ Common Types of Special Tokens

Some commonly encountered special tokens include:

```text
<START>
<END>
<PAD>
<UNK>
<SEP>
<MASK>
```

⚠️ Not every tokenizer or LLM uses all of these.

Modern decoder-only LLMs can use a different set of special tokens depending on their architecture and training setup.

---

# 🟢 Start Token

A **start token** can represent the beginning of a sequence.

For example:

```text
<START> Hello world
```

The simplified flow is:

```text
🏷️ <START>
      ↓
📝 Hello
      ↓
📝 world
```

A tokenizer might assign it an ID:

```text
<START> → 1
```

This ID is only an example.

---

# 🔴 End Token

An **end token** can represent the end of a sequence.

For example:

```text
Hello world <END>
```

The model or surrounding system can use this information to identify that the sequence has ended.

During text generation, an end-of-sequence token can be used as a signal to stop generating.

```text
🤖 Generate Token
       ↓
🔤 Normal Token
       ↓
🤖 Generate Again
       ↓
🏷️ <END>
       ↓
🛑 Stop
```

---

# 🟨 Padding Token

A **padding token**, often represented as `<PAD>`, is used to make sequences the same length when required.

Suppose we have:

```text
Hello
Hello world
Hello world today
```

These sequences have different lengths.

They can be padded:

```text
Hello
Hello world
Hello world today
```

Conceptually:

```text
Sequence 1:
[Hello, <PAD>, <PAD>]

Sequence 2:
[Hello, world, <PAD>]

Sequence 3:
[Hello, world, today]
```

Now all sequences have the same length.

---

# 🎭 Why Is Padding Useful?

Suppose a batch contains:

```text
📝 Sequence A → 3 tokens
📝 Sequence B → 5 tokens
📝 Sequence C → 4 tokens
```

A system may represent them as:

```text
A → [token, token, token, <PAD>, <PAD>]
B → [token, token, token, token, token]
C → [token, token, token, token, <PAD>]
```

Now they have the same length.

```text
📦 Batch
   ↓
Same Sequence Length
   ↓
🧠 Easier Batch Processing
```

The model needs to know that padding is not real content. This is usually handled using a **padding mask** or related mechanism.

---

# ❓ Unknown Token

An **unknown token**, commonly written as `<UNK>`, can represent content that the tokenizer cannot directly represent.

For example:

```text
📝 Unrecognized Text
       ↓
     <UNK>
```

This was particularly important in older or simpler tokenization systems.

However, many modern subword and byte-level tokenizers can represent a much wider range of text without relying heavily on an `<UNK>` token.

---

# 🔀 Separator Token

A **separator token** can indicate a boundary between different pieces of input.

For example:

```text
Sentence A <SEP> Sentence B
```

The separator tells the model that two parts of the input are distinct.

Separator tokens have been especially common in certain encoder-based Transformer architectures.

They are not universally required by decoder-only LLMs.

---

# 🎭 Mask Token

A **mask token**, often written as `<MASK>`, represents a hidden or masked piece of text.

For example:

```text
The sky is <MASK>.
```

A model trained with masked language modeling can learn to predict the missing content.

For example:

```text
The sky is <MASK>.
              ↓
             blue
```

This is associated with **masked language modeling**, used by models such as BERT.

⚠️ This is different from the causal next-token prediction used by GPT-style decoder-only language models.

---

# 🤖 Special Tokens in LLMs

Special tokens can also be used to structure information for modern LLMs.

For example, a conversation may conceptually contain:

```text
<SYSTEM>
You are an AI assistant.

<USER>
What is AI?

<ASSISTANT>
AI is...
```

The exact format is model-specific.

Modern LLMs may use special tokens or control tokens to distinguish:

* System instructions
* User messages
* Assistant responses
* Different turns
* Tool-related content
* Beginning and ending boundaries

These tokens help the model understand the structure of the input.

---

# 💬 Conversation Example

Consider a simplified conversation:

```text
User:
What is AI?

Assistant:
AI is a field of computer science.
```

A model-specific tokenizer may represent the structure conceptually as:

```text
🏷️ <USER>
      ↓
📝 What is AI?
      ↓
🏷️ <ASSISTANT>
      ↓
📝 AI is a field of computer science.
```

The actual special-token format depends on the model.

> 💡 Do not assume that every LLM uses the same special tokens.

---

# 🔢 Special Tokens Also Have Token IDs

Special tokens are part of the tokenizer's vocabulary and can have their own IDs.

For example:

```text
Token       ID

<PAD>       0
<START>     1
<END>       2
<UNK>       3
```

These IDs are only illustrative.

The actual IDs depend on the tokenizer.

The process is:

```text
🏷️ Special Token
       ↓
🔢 Token ID
       ↓
📊 Embedding
       ↓
🤖 Transformer
```

So special tokens ultimately become numerical inputs just like other tokens.

---

# 🧩 Special Tokens vs Normal Tokens

| Feature                                   | Normal Token | Special Token |
| ----------------------------------------- | ------------ | ------------- |
| Represents normal text                    | ✅            | Usually ❌     |
| Has a Token ID                            | ✅            | ✅             |
| Part of vocabulary                        | ✅            | Usually ✅     |
| Has a specific control/structural purpose | ❌            | ✅             |
| Can be used by the model                  | ✅            | ✅             |

For example:

```text
"hello"
```

is a normal text token.

While:

```text
<END>
```

is a special token.

---

# 🔄 Special Tokens in the Tokenization Pipeline

Special tokens fit into the same overall text-processing pipeline:

```text
📝 Text
   ↓
🔤 Tokenizer
   ↓
🧩 Tokens
   ↓
🏷️ Special Tokens
   ↓
🔢 Token IDs
   ↓
📊 Embeddings
   ↓
📍 Positional Information
   ↓
🤖 Transformer
```

The exact placement of special tokens depends on the tokenizer and model.

---

# 🎯 Special Tokens During Training

Special tokens can be included in training examples.

For example:

```text
<START> The cat sleeps <END>
```

The model receives token IDs representing the sequence.

Conceptually:

```text
[START_ID, THE_ID, CAT_ID, SLEEPS_ID, END_ID]
```

The model can learn how these special tokens relate to the structure of the training data.

---

# 🎯 Special Tokens During Generation

Special tokens can also affect generation.

For example:

```text
🤖 Generate Text
       ↓
📝 Token
       ↓
📝 Token
       ↓
📝 Token
       ↓
🏷️ <END>
       ↓
🛑 Stop
```

The end token can act as a signal that generation is complete.

Some systems instead use other stopping conditions, such as a maximum token limit or application-level rules.

---

# 📏 Special Tokens Count as Tokens

Special tokens are still tokens.

Therefore, when they are included in a sequence, they can contribute to the sequence length.

For example:

```text
<START> Hello world <END>
```

contains:

```text
1 special token
+
2 normal tokens
+
1 special token
```

So the sequence contains **4 tokens** in this simplified example.

This matters when working with a model's **context window**.

---

# 🪟 Special Tokens and Context Window

A model has a maximum amount of tokenized input it can process at once.

For example:

```text
📝 Text
   ↓
🔤 Tokenization
   ↓
🔢 Token IDs
   ↓
📏 Sequence Length
   ↓
🪟 Context Window
```

If special tokens are added, they can also take up positions in that sequence.

So:

```text
Normal Text Tokens
+
Special Tokens
=
Total Tokens
```

---

# ⚠️ Special Tokens Are Model-Specific

There is no universal rule that every LLM must use:

```text
<START>
<END>
<PAD>
<UNK>
<SEP>
<MASK>
```

Different tokenizers and architectures use different special tokens.

Some models may:

* Use an end-of-sequence token
* Reuse one token for multiple purposes
* Not use a separate start token
* Not require padding
* Use model-specific control tokens
* Use different names for similar concepts

Therefore:

> 💡 **Always check the tokenizer/model documentation when working with special tokens.**

---

# 🧠 Special Tokens vs Token IDs

These concepts should not be confused.

### 🏷️ Special Token

A token with a specific structural or control purpose.

```text
<END>
```

### 🔢 Token ID

The numerical identifier assigned to it.

```text
2
```

### 📊 Embedding

The numerical vector retrieved using that ID.

```text
[0.12, -0.45, 0.71, ...]
```

So:

```text
🏷️ <END>
     ↓
🔢 Token ID
     ↓
📊 Embedding
     ↓
🤖 Transformer
```

---

# 🔥 Complete Example

Consider:

```text
Hello world
```

A simplified tokenizer might create:

```text
<START> Hello world <END>
```

Then:

```text
🧩 Tokens
[
    <START>,
    Hello,
    world,
    <END>
]
```

These are converted into IDs:

```text
🔢 Token IDs
[
    1,
    15496,
    995,
    2
]
```

The IDs are then used to obtain embeddings:

```text
🔢 Token IDs
      ↓
📊 Embedding Lookup
      ↓
🧩 Embedding Vectors
      ↓
📍 Positional Information
      ↓
🤖 Transformer
```

The actual tokens, IDs, and special-token behavior depend on the model.

---

# 🔄 Complete View

Special tokens are one part of the larger LLM input pipeline:

```text
📝 Human Text
      ↓
🔤 Tokenization
      ↓
🧩 Normal Tokens
      +
🏷️ Special Tokens
      ↓
🔢 Token IDs
      ↓
📊 Embeddings
      ↓
📍 Positional Information
      ↓
🔄 Transformer Blocks
      ↓
🎯 Model Output
```

---

# 🎯 Key Takeaways

```text
🏷️ Special Tokens
        ↓
Tokens with specific structural or control purposes
```

Remember:

* 🏷️ Special tokens are still tokens.
* 🔢 They can have their own Token IDs.
* 📊 Their IDs can be used to obtain embeddings.
* 🧩 They can mark boundaries or provide structure.
* 🛑 An end token can signal that generation should stop.
* 📦 Padding tokens can help create equal-length batches.
* ❓ Unknown tokens can represent unrecognized content in some tokenizers.
* 🎭 Mask tokens are used in masked-language-modeling systems.
* 🤖 Modern LLMs can use model-specific control or special tokens.
* ⚠️ Not every model uses the same special tokens.

> 🚀 **Special tokens give the tokenizer and model additional information about how a sequence is structured and processed.**
