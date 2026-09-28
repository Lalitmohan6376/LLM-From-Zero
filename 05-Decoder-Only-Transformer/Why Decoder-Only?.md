# 🤖 Why Decoder-Only?

A modern LLM such as a GPT-style model is commonly built using a **Decoder-only Transformer**.

But why do we use only the Decoder?

To understand this, we first need to understand what the original Transformer was designed to do.

---

## 1. The Original Transformer

The original Transformer introduced in **2017** used two main parts:

```text
Input Text
    ↓
Encoder
    ↓
Contextual Representation
    ↓
Decoder
    ↓
Output Text
```

The Encoder processes the input.

The Decoder generates the output.

This architecture is called an **Encoder-Decoder Transformer**.

It works very well for tasks such as:

* Machine translation
* Text transformation
* Sequence-to-sequence tasks

For example:

```text
English:
"I love machine learning."

        ↓

Encoder

        ↓

Contextual Representation

        ↓

Decoder

        ↓

Hindi:
"मुझे मशीन लर्निंग पसंद है।"
```

---

# 2. What Changed for Language Models?

Large language models often have a different main goal:

> **Given previous tokens, predict the next token.**

For example:

```text
Input:

"The cat is"

        ↓

Model

        ↓

Prediction:

"sleeping"
```

Then the new token is added:

```text
"The cat is sleeping"

        ↓

Model

        ↓

Prediction:

"on"
```

The process continues one token at a time.

This is called **autoregressive generation**.

---

# 3. Do We Really Need an Encoder?

For next-token prediction, the model mainly needs to process:

```text
Previous Tokens
       ↓
Understand their relationships
       ↓
Predict Next Token
```

A separate Encoder is not required for this basic generation setup.

Instead, the model can process the sequence using **causal self-attention**.

```text
Previous Tokens
      ↓
Causal Self-Attention
      ↓
Transformer Blocks
      ↓
Output Representation
      ↓
LM Head
      ↓
Next-Token Prediction
```

This is the basic idea behind a decoder-only language model.

---

# 4. Decoder-Only Does Not Mean "Only Half a Transformer"

This is an important point.

When we say:

> Decoder-only

we do **not** mean that the model is simply missing half of the required functionality.

A decoder-only LLM contains many important Transformer components:

```text
Token Embeddings
       ↓
Positional Information
       ↓
Causal Self-Attention
       ↓
Feed-Forward Network
       ↓
Residual Connections
       ↓
Layer Normalization
       ↓
More Transformer Blocks
       ↓
Language Modeling Head
```

So it is a complete neural architecture designed around autoregressive prediction.

---

# 5. The Main Difference

The biggest difference is the attention pattern.

### Encoder

An Encoder normally uses **non-causal self-attention**.

This means a token can attend to tokens on both sides.

```text
I   love   machine   learning
↕     ↕       ↕          ↕
All tokens can normally interact
```

### Decoder-only LLM

A decoder-only LLM uses **causal self-attention**.

A token can attend only to itself and earlier tokens.

```text
I → love → machine → learning
```

For example, when predicting `machine`:

```text
I       ✓
love    ✓
machine ✗
learning ✗
```

The model cannot use future tokens.

This prevents the model from seeing the answer before predicting it.

---

# 6. Why Causal Attention Is Important

Suppose the training sequence is:

```text
The cat is sleeping
```

During training, we can create:

```text
Input:   The cat is
Target:      cat is sleeping
```

More precisely, the model learns next-token relationships:

```text
"The"          → "cat"
"The cat"      → "is"
"The cat is"   → "sleeping"
```

The model must not be allowed to look at the future target token.

Therefore:

```text
The → cat → is → sleeping
```

The attention pattern is approximately:

```text
The
↓
The   cat
↓     ↓
The   cat   is
↓     ↓     ↓
The   cat   is   sleeping
```

Future tokens are blocked.

---

# 7. Why Not Use a Normal Encoder?

A normal Encoder can see the complete sequence.

For example:

```text
The cat is sleeping
```

When processing `cat`, an Encoder can use:

```text
The
cat
is
sleeping
```

But during autoregressive training, we want the model to behave as if it does not know the future.

So we need:

```text
The → cat → is → sleeping
```

with future information blocked.

Causal self-attention provides this behavior.

---

# 8. Decoder-Only Architecture

A simplified decoder-only LLM looks like this:

```text
                 Input Text
                     ↓
                Tokenization
                     ↓
                  Token IDs
                     ↓
               Token Embeddings
                     ↓
          Positional Information
                     ↓
        ┌────────────────────────┐
        │   Transformer Block    │
        │                        │
        │ Causal Self-Attention  │
        │          ↓             │
        │       FFN              │
        │          ↓             │
        │ Residual + Normalization│
        └────────────────────────┘
                     ↓
              More Blocks
                     ↓
           Final Representation
                     ↓
                LM Head
                     ↓
                  Logits
                     ↓
              Probabilities
                     ↓
             Next Token
```

The Transformer block is repeated many times.

---

# 9. Original Decoder vs Decoder-Only LLM

These two terms can be confusing.

The **original Transformer Decoder** contains:

```text
Masked Self-Attention
        ↓
Cross-Attention
        ↓
Feed-Forward Network
```

The cross-attention allows the Decoder to use information produced by the Encoder.

A decoder-only LLM does not have a separate Encoder.

Therefore:

```text
Decoder-only LLM

Causal Self-Attention
        ↓
Feed-Forward Network
        ↓
Repeat
```

There is no separate Encoder output to attend to.

---

# 10. What Happened to Cross-Attention?

Cross-attention is useful when there are two different sequences.

For example:

```text
English Input
      ↓
Encoder
      ↓
Encoder Representation
      ↓
Cross-Attention
      ↑
    Decoder
      ↓
Hindi Output
```

The Decoder can use the Encoder's representation while generating the output.

But in a decoder-only LLM:

```text
Input Tokens
     ↓
Same Transformer
     ↓
Next Token
```

There is no separate Encoder representation.

Therefore, a standard decoder-only language model does not need the original Transformer's cross-attention pathway.

---

# 11. Why This Works Well for Text Generation

Text generation is naturally sequential.

Suppose the prompt is:

```text
Artificial intelligence is
```

The model predicts:

```text
powerful
```

Now:

```text
Artificial intelligence is powerful
```

The model predicts another token:

```text
technology
```

Then:

```text
Artificial intelligence is powerful technology
```

The process continues.

```text
Prompt
  ↓
Tokenize
  ↓
Transformer
  ↓
Next Token
  ↓
Add Token
  ↓
Transformer
  ↓
Next Token
  ↓
Add Token
  ↓
...
```

This fits naturally with a decoder-only architecture.

---

# 12. Decoder-Only and Autoregressive Generation

The key relationship is:

```text
Decoder-only Transformer
          +
Causal Self-Attention
          +
Next-Token Prediction
          ↓
Autoregressive Language Generation
```

The model generates one token at a time while using previously generated tokens as context.

---

# 13. Training a Decoder-Only LLM

During training, we usually have a sequence such as:

```text
The cat is sleeping
```

The training pairs can be represented as:

```text
Input:

The cat is sleeping

Target:

cat is sleeping <END>
```

The model produces predictions for the appropriate positions.

Conceptually:

```text
Input tokens
     ↓
Decoder-only Transformer
     ↓
Logits
     ↓
Next-token predictions
     ↓
Compare with target
     ↓
Loss
     ↓
Backpropagation
     ↓
Parameter updates
```

The causal mask ensures each prediction cannot use future tokens.

---

# 14. Training Can Still Be Parallel

A common misunderstanding is:

> "If generation is one token at a time, must training also process one token at a time?"

No.

During training, the model can process many positions in parallel.

For example:

```text
Input:

The cat is sleeping on the bed
```

The model can calculate predictions for multiple positions in one forward pass.

The causal mask controls what each position is allowed to see.

```text
Position 1 → sees position 1
Position 2 → sees 1, 2
Position 3 → sees 1, 2, 3
Position 4 → sees 1, 2, 3, 4
...
```

So:

```text
Training:
Parallel computation
+
Causal masking
```

while:

```text
Generation:
Usually one new token at a time
```

---

# 15. Decoder-Only During Inference

Suppose the user gives:

```text
The weather today is
```

The model processes the prompt.

It produces logits for the next token.

For example:

```text
sunny     → 0.45
beautiful → 0.20
good      → 0.12
cold      → 0.08
...
```

A token is selected.

Suppose:

```text
sunny
```

Now the sequence becomes:

```text
The weather today is sunny
```

The model predicts again.

```text
The weather today is sunny
                    ↓
                 next token
```

This continues until a stopping condition is reached.

---

# 16. Why Decoder-Only Models Became Popular for LLMs

Decoder-only architectures have several properties that fit large-scale language modeling well.

### 1. Simple objective

The model can be trained using:

```text
Predict the next token
```

### 2. Natural text generation

The same objective used during training directly supports autoregressive generation.

```text
Training:

Previous tokens → Next token

Generation:

Previous tokens → Next token
```

### 3. One main Transformer stack

There is no separate Encoder stack.

```text
Token Input
    ↓
Transformer Blocks
    ↓
Prediction
```

This gives a relatively straightforward architecture for large autoregressive language models.

### 4. Flexible prompting

A prompt can contain many kinds of text:

```text
Question
Instructions
Examples
Conversation
Code
Documents
```

The model processes them as a sequence of tokens and continues the sequence.

---

# 17. Decoder-Only Models Can Handle Many Tasks

A decoder-only language model does not need a completely different architecture for every text task.

Many tasks can be represented as text.

For example:

### Question Answering

```text
Question:
What is Python?

Answer:
Python is a programming language...
```

### Summarization

```text
Article:
...

Summary:
...
```

### Translation

```text
English:
Hello, how are you?

French:
Bonjour, comment allez-vous ?
```

### Code Generation

```text
Write a Python function to add two numbers.

def add(a, b):
    return a + b
```

The model can treat all of these as sequences of tokens.

---

# 18. The Important Idea: Everything Becomes a Sequence

This is one of the most important reasons decoder-only LLMs are powerful.

Different tasks can be converted into text sequences.

```text
Question
   ↓
Text Sequence

Summary
   ↓
Text Sequence

Translation
   ↓
Text Sequence

Code
   ↓
Text Sequence

Conversation
   ↓
Text Sequence
```

The model learns:

```text
Sequence Context
      ↓
Next Token
```

So the same core mechanism can be used across many tasks.

---

# 19. Decoder-Only vs Encoder-Decoder

| Feature               | Encoder-Decoder                | Decoder-Only                                 |
| --------------------- | ------------------------------ | -------------------------------------------- |
| Encoder               | Yes                            | No separate Encoder                          |
| Decoder               | Yes                            | Transformer stack with causal self-attention |
| Causal self-attention | In Decoder                     | Yes                                          |
| Cross-attention       | Yes                            | No separate Encoder pathway                  |
| Main generation style | Sequence-to-sequence           | Autoregressive                               |
| Typical use           | Translation, seq2seq           | Text generation, code, conversation          |
| Example family        | Original Transformer, T5-style | GPT-style                                    |

These are broad architectural patterns. Individual models can differ in details.

---

# 20. Decoder-Only vs Encoder-Only

An Encoder-only model and a Decoder-only model have different goals.

### Encoder-only

```text
Input
  ↓
Encoder
  ↓
Contextual Representation
  ↓
Task-specific Output
```

Example:

```text
BERT
```

It is commonly used for understanding-oriented tasks such as classification or representation learning.

### Decoder-only

```text
Input
  ↓
Causal Transformer
  ↓
Next Token
  ↓
Generated Text
```

Example family:

```text
GPT-style models
```

---

# 21. Three Major Transformer Patterns

It helps to see the three common patterns together.

### Encoder-only

```text
Input
  ↓
Encoder
  ↓
Representation
  ↓
Task Output
```

Example:

```text
BERT
```

### Decoder-only

```text
Input
  ↓
Causal Transformer
  ↓
Next Token
  ↓
Generated Text
```

Example:

```text
GPT-style models
```

### Encoder-Decoder

```text
Input
  ↓
Encoder
  ↓
Representation
  ↓
Decoder
  ↓
Output
```

Example:

```text
Original Transformer
T5-style models
```

---

# 22. Why Not Keep Both Encoder and Decoder?

You can.

In fact, Encoder-Decoder Transformers are still useful.

The question is:

> What architecture matches the main task?

For autoregressive language generation, a separate Encoder is not necessary.

The model can use:

```text
Causal Self-Attention
+
Transformer Blocks
+
Next-Token Prediction
```

This provides a direct path from context to generated text.

---

# 23. The Role of Causal Masking

Causal masking is one of the most important parts of a decoder-only LLM.

Suppose we have:

```text
I love machine learning
```

The attention pattern can be represented as:

```text
             Can Attend To

I            I
love         I love
machine      I love machine
learning     I love machine learning
```

The future is blocked.

```text
I       ✗ love
I       ✗ machine
I       ✗ learning
```

for the first position.

This prevents information leakage during training.

---

# 24. Why This Is Called "Causal"

The model follows a left-to-right dependency:

```text
Token 1
   ↓
Token 2
   ↓
Token 3
   ↓
Token 4
   ↓
...
```

A later token cannot influence the prediction of an earlier token.

This creates the causal structure required for autoregressive next-token prediction.

---

# 25. Decoder-Only Does Not Mean Sequential Computation Everywhere

Another important distinction:

### Training

```text
Many token positions
        ↓
Processed in parallel
        ↓
Causal mask controls visibility
```

### Generation

```text
Current sequence
       ↓
Predict one token
       ↓
Add token
       ↓
Predict next token
       ↓
...
```

Therefore, decoder-only models can still be trained efficiently on GPUs.

---

# 26. KV Cache During Generation

During generation, the model repeatedly processes an expanding sequence.

Without caching:

```text
Prompt
  ↓
Calculate K/V
  ↓
New token
  ↓
Recalculate previous K/V
  ↓
New token
  ↓
...
```

This would repeat work.

A KV cache stores previously computed **Keys and Values**.

```text
Previous K/V
    ↓
KV Cache
    ↓
Current token
    ↓
Attention
    ↓
Next token
```

The exact implementation varies by model, but the important idea is:

> Previously computed attention information can be reused during autoregressive generation.

The cache stores K/V, not Q.

---

# 27. A Simple Mental Model

Think of a decoder-only LLM as a very large next-token prediction machine.

```text
What have I seen so far?
          ↓
Which previous information matters?
          ↓
Causal Self-Attention
          ↓
Transform the information
          ↓
Transformer Blocks
          ↓
What token should come next?
          ↓
LM Head
          ↓
Next Token
```

Then the new token becomes part of the context.

```text
Context
  ↓
Next Token
  ↓
New Context
  ↓
Next Token
  ↓
New Context
  ↓
...
```

---

# 28. Complete Decoder-Only Flow

The complete simplified flow is:

```text
                Raw Text
                   ↓
               Tokenizer
                   ↓
                Tokens
                   ↓
               Token IDs
                   ↓
            Token Embeddings
                   ↓
        Positional Information
                   ↓
        ┌──────────────────────┐
        │  Decoder-Only Block  │
        │                      │
        │ Causal Self-Attention│
        │          ↓           │
        │      FFN             │
        │          ↓           │
        │ Residual + Norm      │
        └──────────────────────┘
                   ↓
              Repeat N Times
                   ↓
        Final Hidden Representation
                   ↓
                LM Head
                   ↓
                 Logits
                   ↓
          Probability Distribution
                   ↓
             Next Token
                   ↓
          Add Token to Context
                   ↓
             Repeat Process
```

---

# 29. Training vs Generation

| Stage            | Training                           | Generation                      |
| ---------------- | ---------------------------------- | ------------------------------- |
| Input            | Training token sequences           | Prompt/current sequence         |
| Attention        | Causal                             | Causal                          |
| Computation      | Many positions can be parallelized | Usually one new token at a time |
| Target           | Known next tokens                  | Unknown next token              |
| Loss             | Calculated                         | Usually not used for generation |
| Parameter update | Yes                                | No                              |
| Output           | Predictions for training positions | Selected/generated token        |

---

# 30. Why GPT-Style Models Use Decoder-Only Architecture

GPT-style models are designed around:

```text
Generative
+
Pre-trained
+
Transformer
```

Their core language-modeling objective is next-token prediction.

Therefore, the architecture naturally uses:

```text
Decoder-only Transformer
        +
Causal Self-Attention
        +
Next-Token Prediction
```

This allows the model to learn statistical patterns in large text datasets and generate text autoregressively.

---

# 31. Important Terminology

### Decoder

A Transformer component originally designed as part of an Encoder-Decoder architecture.

### Decoder-only

A model architecture that uses a Transformer stack with causal self-attention and does not have a separate Encoder.

### Causal Self-Attention

Self-attention where each position cannot attend to future positions.

### Autoregressive Generation

Generating tokens sequentially using previously available tokens as context.

### Cross-Attention

Attention where Queries come from one sequence and Keys/Values come from another sequence.

A standard decoder-only LLM does not have the separate Encoder-to-Decoder cross-attention pathway of the original Transformer.

---

# 32. Common Misunderstanding

### ❌ "Decoder-only means the model only has a small part of the Transformer."

Not correct.

A decoder-only LLM contains many complete Transformer blocks.

---

### ❌ "The Decoder always needs an Encoder."

Not always.

The original Transformer Decoder was designed to work with Encoder outputs.

A decoder-only architecture removes that separate Encoder pathway.

---

### ❌ "Decoder-only models cannot understand context."

They use causal self-attention to build contextual representations from previous tokens.

They simply cannot use future tokens when making an autoregressive prediction.

---

### ❌ "Training must also happen one token at a time."

Not necessarily.

Training can process many sequence positions in parallel while causal masking prevents future information from being used.

---

### ❌ "Decoder-only means there is no attention."

The opposite is true.

Causal self-attention is a central component.

---

# 33. The Core Reason in One Sentence

> **Decoder-only architecture is well suited to autoregressive language modeling because it can use causal self-attention to process previous tokens and predict the next token without requiring a separate Encoder.**

---

# 34. Final Mental Model

Remember this simple picture:

```text
             Decoder-Only LLM

Previous Tokens
      ↓
Causal Self-Attention
      ↓
Transformer Blocks
      ↓
Contextual Representation
      ↓
LM Head
      ↓
Next-Token Prediction
      ↓
Add New Token
      ↓
Repeat
```

And the key difference from the original Transformer is:

```text
Original Transformer:

Encoder → Decoder
             ↑
       Cross-Attention


Decoder-Only LLM:

Causal Transformer
        ↓
Next Token
```

So the main idea is not that the Encoder is "bad" or unnecessary for every task.

The idea is that for **autoregressive language generation**, a separate Encoder is not required, and a causal Transformer stack can directly model the relationship between previous tokens and the next token.
