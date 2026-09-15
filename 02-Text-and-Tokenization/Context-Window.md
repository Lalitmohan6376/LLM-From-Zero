# 🪟 Context Window

A **context window** is the maximum amount of tokenized information that a language model can consider as its context at one time.

In simple words:

> 💡 **The context window is the amount of token space available to the model for processing the current input and, depending on the model/system, the generated output.**

---

# 🧠 Why Do We Need a Context Window?

An LLM processes text as a sequence of tokens.

For example:

```text
📝 "The cat is sleeping."
        ↓
🔤 Tokenization
        ↓
🔢 [125, 842, 91, 731, 18]
```

The model processes these tokens as a sequence.

But a model cannot process an unlimited number of tokens in one context.

Therefore, it has a maximum context capacity.

```text
📝 Text
   ↓
🔤 Tokens
   ↓
🔢 Token Sequence
   ↓
🪟 Context Window
   ↓
🤖 LLM
```

---

# 📏 What Does Context Window Mean?

Suppose a model has a context window of:

```text
8,000 tokens
```

This means the model can work with a context containing up to roughly that many tokens under the model's specified limits.

Conceptually:

```text
🪟 Context Window

|----------------------------------------|
|              8,000 Tokens              |
|----------------------------------------|
```

If the relevant context requires more tokens than the model supports, the system must handle the excess somehow.

For example, it may:

* Remove older content
* Truncate the input
* Split the content
* Summarize information
* Use another external mechanism

The exact behavior depends on the application.

---

# 🔢 Context Window Is Measured in Tokens

A context window is generally described in **tokens**, not words or characters.

For example:

```text
Context Window
      ↓
32,000 tokens
```

It does not mean:

```text
32,000 words
```

because one word can correspond to one or multiple tokens.

For example:

```text
📝 "playing"
      ↓
🧩 ["play", "ing"]
      ↓
2 tokens
```

The exact tokenization depends on the tokenizer.

---

# 📝 Words vs Tokens vs Context

Consider:

```text
The cat is sleeping.
```

A tokenizer might produce:

```text
["The", "cat", "is", "sleeping", "."]
```

That's:

```text
5 tokens
```

If a model has a context window of:

```text
8,000 tokens
```

then this sentence uses only a very small part of that available context.

Conceptually:

```text
🪟 8,000 Token Context Window

[The][cat][is][sleeping][.]
 ↑
Only a small portion is being used
```

---

# 🧩 What Can Be Inside the Context Window?

The context can contain different kinds of tokenized information.

For example:

```text
👤 User Input
+
💬 Previous Conversation
+
📄 Provided Text
+
🏷️ Special Tokens
+
🤖 Generated Tokens
```

Depending on the model and application, all of this can contribute to the token context.

A simplified conversation might look like:

```text
🪟 Context

👤 User:
What is machine learning?

🤖 Assistant:
Machine learning is...

👤 User:
Give me an example.

🤖 Assistant:
...
```

The previous messages can become part of the model's context.

---

# 💬 Context in a Conversation

Suppose a conversation contains:

```text
User:
My project is a movie recommendation system.

Assistant:
That's a content recommendation system.

User:
Which model should I use?
```

The model can use the earlier conversation as context.

Conceptually:

```text
🪟 Context Window
┌─────────────────────────────┐
│ My project is...            │
│                             │
│ That's a content...         │
│                             │
│ Which model should I use?   │
└─────────────────────────────┘
              ↓
             🤖
```

This allows the model to generate a response based on information that appeared earlier in the conversation.

---

# 📄 Context for Long Documents

A context window can also contain documents.

For example:

```text
📄 Large Document
      ↓
🔤 Tokenization
      ↓
🔢 Many Tokens
      ↓
🪟 Context Window
      ↓
🤖 LLM
```

If the document fits within the available context, the model can process it as part of the input.

If it is larger than the available context, the entire document may not fit at once.

---

# 📏 Context Window vs Sequence Length

These concepts are closely related but are not exactly the same.

### 📦 Sequence Length

The number of tokens in a particular sequence.

Example:

```text
[125, 842, 91, 731]
```

has:

```text
Sequence Length = 4
```

### 🪟 Context Window

The maximum context capacity supported by the model/system.

Example:

```text
Context Window = 8,000 tokens
```

So:

```text
📦 Sequence Length
        ↓
How many tokens are currently in the sequence?

🪟 Context Window
        ↓
How many tokens can the model handle in its context?
```

---

# 🧠 Context Window vs Vocabulary

These are also different concepts.

### 📚 Vocabulary

The collection of tokens known by the tokenizer.

For example:

```text
Vocabulary Size = 50,000 tokens
```

### 🪟 Context Window

The number of tokens that can be considered in one context.

For example:

```text
Context Window = 8,000 tokens
```

So:

```text
📚 Vocabulary
→ Which tokens can the tokenizer represent?

🪟 Context Window
→ How many tokens can be present in the context?
```

---

# 🔢 Vocabulary Size ≠ Context Window

Suppose:

```text
Vocabulary = 50,000 tokens
Context Window = 8,000 tokens
```

This does **not** mean the model can only use 8,000 different tokens.

It means:

```text
📚 50,000 possible vocabulary entries
              +
🪟 Up to 8,000 token positions in the context
```

The same token can appear multiple times in a sequence.

---

# 🎯 Context and Next-Token Prediction

Context is especially important for next-token prediction.

Suppose the model receives:

```text
The capital of France is
```

The tokenized sequence represents the available context.

The model uses that context to predict the next token:

```text
The capital of France is
                    ↓
                  Paris
```

Then the sequence becomes:

```text
The capital of France is Paris
```

The model can use the updated context to predict another token.

```text
The capital of France is Paris
                         ↓
                       ...
```

---

# 🔄 Context During Autoregressive Generation

Decoder-only LLMs generate text one token at a time.

The sequence grows as new tokens are generated:

```text
📝 Prompt
   ↓
🔢 Token Sequence
   ↓
🤖 LLM
   ↓
🎯 Next Token
   ↓
➕ Add Token
   ↓
🔢 Updated Sequence
   ↓
🤖 LLM
   ↓
🎯 Next Token
   ↓
🔄 Repeat
```

For example:

```text
Step 1:
The cat

Step 2:
The cat is

Step 3:
The cat is sleeping

Step 4:
The cat is sleeping peacefully
```

Each generated token becomes part of the growing sequence.

---

# ⚠️ What Happens When the Context Gets Too Long?

Suppose:

```text
🪟 Context Window = 8,000 tokens
```

and the current input plus required context exceeds that limit.

The model cannot simply keep adding tokens beyond its supported context capacity.

A system may need to reduce the amount of information being considered.

For example:

```text
Old Context
     ↓
✂️ Remove / Truncate
     ↓
Recent Context
     +
New Input
     ↓
🪟 Context Window
```

Possible strategies include:

### ✂️ Truncation

Remove some older tokens.

### 📝 Summarization

Replace older information with a shorter summary.

### 📄 Chunking

Split a large document into smaller pieces.

### 🔎 Retrieval

Select only relevant information from a larger external collection.

⚠️ Retrieval systems such as RAG are separate from the basic concept of the context window.

---

# 🧠 Context Window Does Not Mean Permanent Memory

A context window should not automatically be thought of as the model's permanent memory.

For example:

```text
🪟 Context Window
      ↓
Information available in the current context
```

When information is no longer included in the context, the model may not have access to it through that conversation context.

Persistent memory is a separate concept that depends on the model or application.

---

# 📚 Context Window and Long Documents

Suppose a document contains:

```text
50,000 tokens
```

and a model's context window is:

```text
8,000 tokens
```

The entire document cannot fit into one 8,000-token context.

Conceptually:

```text
📄 50,000 Tokens

├──────── 8,000 ────────┤
├──────── 8,000 ────────┤
├──────── 8,000 ────────┤
├──────── 8,000 ────────┤
├──────── 8,000 ────────┤
├──────── 8,000 ────────┤
└──────── 2,000 ────────┘
```

An application could process the document in smaller chunks.

---

# 📦 Context Window and Batches

Do not confuse **context window** with **batch size**.

### 🪟 Context Window

How many tokens can belong to one model context.

### 📦 Batch Size

How many separate sequences are processed together in one batch.

For example:

```text
Batch Size = 4
Context Length = 2,000 tokens
```

Conceptually:

```text
📦 Batch
│
├── Sequence 1 → 2,000 tokens
├── Sequence 2 → 2,000 tokens
├── Sequence 3 → 2,000 tokens
└── Sequence 4 → 2,000 tokens
```

These are different concepts.

---

# 🧠 Context Window and Attention

The Transformer uses attention to process relationships between tokens in its context.

For example:

```text
🪟 Context
┌──────────────────────────────┐
│ Token 1                      │
│ Token 2                      │
│ Token 3                      │
│ Token 4                      │
│ ...                          │
│ Token N                      │
└──────────────────────────────┘
              ↓
        🔄 Attention
              ↓
     📊 Contextual Representations
```

In a decoder-only Transformer, causal attention ensures that a token cannot use future tokens that have not yet been generated when making the next-token prediction.

The details of attention and causal masking are covered later in the architecture and Transformer sections.

---

# 📈 Larger Context Windows

Modern language models can support much larger context windows than early language models.

Conceptually:

```text
Earlier Models
🪟 Smaller Context
        ↓
Modern Models
🪟 Much Larger Context
```

A larger context window can make it possible to work with:

* Longer conversations
* Larger documents
* More code
* More instructions
* More examples
* More surrounding context

However:

> ⚠️ **A larger context window does not automatically mean better understanding of every piece of information inside it.**

The model still has limitations.

---

# 💰 Larger Context Can Require More Resources

Processing more tokens generally requires more computation and memory.

Conceptually:

```text
📈 More Context
      ↓
📈 More Tokens to Process
      ↓
💻 More Computation
      +
🧠 More Memory Requirements
```

The exact computational cost depends on the architecture and implementation.

This is one reason efficient attention and other optimization techniques are important for long-context models.

---

# ⚠️ Context Window Is Not the Same as Model Knowledge

Suppose a model has a large context window.

That does not mean:

```text
Large Context Window
       =
More Training Knowledge
```

These are different things.

### 🧠 Model Knowledge

Patterns learned during training and stored in the model's parameters.

### 🪟 Context

Information provided to the model for the current processing task.

For example:

```text
📚 Training
   ↓
🧠 Learned Parameters
```

while:

```text
📝 Current Input
   +
💬 Conversation
   +
📄 Provided Information
   ↓
🪟 Current Context
```

---

# 🔥 Complete Example

Suppose a model supports:

```text
🪟 Context Window = 8,000 tokens
```

A user provides:

```text
📝 Prompt = 500 tokens
```

The conversation history contains:

```text
💬 Previous Messages = 2,000 tokens
```

And the application adds:

```text
📄 Additional Context = 1,500 tokens
```

The current context would contain approximately:

```text
500
+
2,000
+
1,500
=
4,000 tokens
```

So conceptually:

```text
🪟 8,000 Token Context Window

[500 Prompt]
[2,000 Conversation]
[1,500 Additional Context]

Total ≈ 4,000 tokens
```

There is still capacity available within the example limit.

The exact accounting of input/output tokens depends on the model and API/system definition.

---

# 🔄 Context Window in the LLM Pipeline

The overall process can be simplified as:

```text
📝 Human Text
      ↓
🔤 Tokenization
      ↓
🔢 Token IDs
      ↓
📦 Token Sequence
      ↓
🪟 Context Window
      ↓
🧩 Embeddings
      ↓
📍 Positional Information
      ↓
🔄 Transformer Blocks
      ↓
🎯 Next-Token Prediction
```

During generation:

```text
🎯 Next Token
      ↓
➕ Add to Sequence
      ↓
🪟 Updated Context
      ↓
🤖 Transformer
      ↓
🎯 Next Token
      ↓
🔄 Repeat
```

---

# 🆚 Sequence Length vs Context Window

| Concept            | Meaning                        |
| ------------------ | ------------------------------ |
| 📦 Sequence        | Ordered collection of tokens   |
| 📏 Sequence Length | Number of tokens in a sequence |
| 🪟 Context Window  | Maximum context capacity       |
| 🔢 Token           | Small piece of text            |
| 📚 Vocabulary      | Collection of available tokens |

A simple relationship is:

```text
📦 Sequence
      ↓
📏 Sequence Length
      ↓
🪟 Must Fit Within Context Limit
```

---

# 🎯 Key Takeaways

Remember:

* 🪟 **Context window** is the model's available context capacity.
* 🔢 It is generally measured in **tokens**.
* 📦 A sequence has a specific number of tokens.
* 📏 Sequence length and context-window size are different concepts.
* 💬 Conversation history can become part of the context.
* 📄 Documents can also be included in the context.
* 🎯 Generated tokens can become part of the growing context.
* ✂️ When context becomes too large, systems may truncate, summarize, chunk, or otherwise manage the information.
* 🧠 Context is not the same as permanent model memory.
* 📚 Context window is not the same as model knowledge.
* 📈 A larger context window does not automatically mean better understanding.
* 💻 Processing more context can require more computation and memory.

> 🚀 **The context window defines how much tokenized information an LLM can work with as context at a given time.**
