# 🔄 Encoder-Decoder Architecture

The **Encoder-Decoder architecture** is a Transformer architecture in which one part of the model **processes the input sequence** and another part **generates the output sequence**.

The original Transformer introduced in the paper **“Attention Is All You Need”** uses this architecture.

```text id="x4k2rm"
📝 Input Sequence
       ↓
📥 Encoder
       ↓
📊 Contextual Representations
       ↓
📤 Decoder
       ↓
📝 Output Sequence
```

The key idea is simple:

> **The Encoder understands the input representation, while the Decoder uses that information to generate the output.**

Here, “understands” is used as a simplified description of learned representation processing, not human-like understanding.

---

## 1. What Is Encoder-Decoder Architecture?

Encoder-Decoder architecture divides the Transformer into two main parts:

```text id="3f8r2a"
┌──────────────────┐
│      Encoder     │
│                  │
│ Processes Input  │
└────────┬─────────┘
         ↓
 Encoder Representations
         ↓
┌──────────────────┐
│      Decoder     │
│                  │
│ Generates Output │
└────────┬─────────┘
         ↓
   Output Sequence
```

The Encoder and Decoder have different responsibilities.

### Encoder

The Encoder transforms the input into contextual representations.

### Decoder

The Decoder uses the available output context and Encoder representations to generate the output sequence.

---

## 2. Why Do We Need Two Parts?

Some tasks require transforming one sequence into another.

For example:

* Machine translation
* Text summarization
* Some question-answering systems
* Sequence-to-sequence generation

For translation:

```text id="6v0l3q"
English Input
"I love AI"
      ↓
   Encoder
      ↓
Input Representation
      ↓
   Decoder
      ↓
French Output
"J'aime l'IA"
```

The Encoder processes the source language.

The Decoder generates the target language.

---

## 3. Original Transformer Architecture

The original Transformer contains:

```text id="r0k7de"
Transformer
│
├── 📥 Encoder
│
└── 📤 Decoder
```

The Encoder consists of a stack of Encoder blocks.

The Decoder consists of a stack of Decoder blocks.

```text id="b7y2qf"
              INPUT
                ↓
        ┌───────────────┐
        │    Encoder    │
        │               │
        │ Block 1       │
        │ Block 2       │
        │ Block 3       │
        │ ...           │
        │ Block N       │
        └───────┬───────┘
                ↓
       Encoder Representations
                ↓
        ┌───────────────┐
        │    Decoder    │
        │               │
        │ Block 1       │
        │ Block 2       │
        │ Block 3       │
        │ ...           │
        │ Block N       │
        └───────┬───────┘
                ↓
              OUTPUT
```

---

## 4. Encoder

The Encoder receives the input sequence.

```text id="0t8wq5"
📝 Input Text
      ↓
🔤 Tokenization
      ↓
🔢 Token IDs
      ↓
🧩 Token Embeddings
      ↓
📍 Positional Information
      ↓
📥 Encoder
      ↓
📊 Contextual Representations
```

The Encoder uses self-attention to allow tokens to interact with other relevant input positions.

In the original Transformer, Encoder self-attention is not causal.

This means a token can generally attend to both earlier and later input tokens, subject to any other masks such as padding masks.

---

## 5. Decoder

The Decoder generates the output sequence.

```text id="6g1jpn"
Previous Output Tokens
          ↓
     Token Embeddings
          ↓
       📤 Decoder
          ↑
          │
   Encoder Representations
          ↓
     Output Representation
          ↓
      Output Layer
          ↓
      Next Token
```

The Decoder contains:

* Masked self-attention
* Cross-attention
* Feed-forward network
* Residual connections
* Layer normalization

The exact ordering can vary across Transformer implementations.

---

## 6. Main Data Flow

The complete high-level flow is:

```text id="5c7y0n"
📝 Input
   ↓
📥 Encoder
   ↓
📊 Encoder Output
   ↓
🔗 Cross-Attention
   ↑
📤 Decoder
   ↓
🎯 Output Prediction
   ↓
📝 Generated Output
```

The important connection is:

```text
Encoder → Decoder
```

The Decoder receives information from the Encoder through **cross-attention**.

---

## 7. Encoder Input

Suppose the input is:

```text id="b3z0i9"
"The cat is sleeping."
```

The input goes through:

```text id="h4c7mx"
Text
 ↓
Tokens
 ↓
Token IDs
 ↓
Embeddings
 ↓
Positional Information
 ↓
Encoder
```

The Encoder then transforms the input into contextual representations.

These representations contain information produced by the Encoder's layers and attention operations.

---

## 8. Encoder Self-Attention

Inside each Encoder block, self-attention allows tokens to interact.

```text id="9a7x0q"
Input Representations
        ↓
   Self-Attention
        ↓
Contextual Representations
```

For example:

```text id="x2z6y5"
"The cat sat on the mat."
```

Different tokens can use information from other positions in the input.

Because the original Encoder is not autoregressive, it does not need the same future-token causal restriction used by the Decoder.

---

## 9. Encoder Output

After passing through the Encoder blocks:

```text id="d5f8k2"
Input Representations
       ↓
Encoder Block 1
       ↓
Encoder Block 2
       ↓
...
       ↓
Encoder Block N
       ↓
📊 Encoder Output
```

The output is a sequence of contextual vectors.

For a sequence of length `N` and model dimension `D`, the conceptual shape is:

```text id="6d1q4f"
N × D
```

With batches:

```text id="z2x9p7"
Batch Size × Sequence Length × Model Dimension
```

The exact representation and dimensions depend on the model.

---

## 10. What Is Cross-Attention?

Cross-attention connects the Decoder to the Encoder.

The Decoder produces the **Queries**.

The Encoder output provides the **Keys and Values**.

```text id="7m4w9b"
Decoder Representation
        ↓
        Q
        │
        ↓
  Cross-Attention
        ↑
        │
Encoder Output
     K + V
```

This allows the Decoder to use information from the input sequence while generating the output.

---

## 11. Self-Attention vs Cross-Attention

This distinction is extremely important.

### Self-Attention

Q, K, and V come from the same sequence representation.

```text id="j5h1c8"
Same Sequence
     ↓
   Q K V
     ↓
Self-Attention
```

### Cross-Attention

Q comes from the Decoder.

K and V come from the Encoder.

```text id="g8r3t6"
Decoder → Q

Encoder → K, V

       ↓

Cross-Attention
```

Therefore:

```text
Self-Attention
→ information within one sequence

Cross-Attention
→ information between Encoder and Decoder
```

---

## 12. Why Does the Decoder Need Cross-Attention?

Suppose the model is translating:

```text id="1u6v3k"
"I love machine learning."
```

The Encoder processes the complete source sentence.

The Decoder then generates the target sentence.

While generating a token, the Decoder can use cross-attention to access relevant information from the Encoder output.

```text id="h3x8p2"
Source Sentence
      ↓
   Encoder
      ↓
Encoder Representations
      ↓
Cross-Attention
      ↑
   Decoder
      ↓
Target Token
```

This creates a communication path between the input and output sequences.

---

## 13. Decoder Self-Attention

The Decoder also has self-attention.

But in the original Transformer, this self-attention is **masked**.

```text id="v8k4r1"
Previous Output Tokens
          ↓
   Masked Self-Attention
          ↓
Decoder Representation
```

The causal mask prevents a position from attending to future output tokens.

For example:

```text id="s7x2q9"
Output:

"I love AI"

Position 1 → "I"

Position 2 → "I", "love"

Position 3 → "I", "love", "AI"
```

A position cannot use future output tokens.

---

## 14. Why Is Decoder Self-Attention Masked?

The Decoder generates output autoregressively.

Suppose the target is:

```text id="k4n8w0"
"The cat sleeps"
```

When predicting:

```text id="x9q3m1"
"The cat"
```

the model should predict:

```text
"sleeps"
```

without seeing `"sleeps"` as future input.

Therefore:

```text id="f2j7v6"
Past Tokens
    ↓
Allowed

Future Tokens
    ↓
Blocked
```

This is the purpose of causal masking.

---

## 15. Encoder vs Decoder Attention

The original Transformer uses different attention patterns.

```text id="q7m4s8"
ENCODER

Input Tokens
     ↓
Self-Attention
     ↓
Can generally attend across input positions
```

```text id="n3x6k1"
DECODER

Output Tokens
     ↓
Masked Self-Attention
     ↓
Can attend only to allowed previous/current positions
```

And then:

```text id="r8v2c5"
DECODER
   ↓
Cross-Attention
   ↑
ENCODER OUTPUT
```

---

## 16. Feed-Forward Network

Both Encoder and Decoder blocks contain Feed-Forward Networks.

```text id="y1q5k7"
Attention
   ↓
Feed-Forward Network
   ↓
Transformed Representation
```

A simplified FFN is:

```text id="t8m3p0"
Input
  ↓
Linear Transformation
  ↓
Activation
  ↓
Linear Transformation
  ↓
Output
```

The FFN transforms each token position's representation.

---

## 17. Residual Connections

Residual connections are used throughout Transformer blocks.

Conceptually:

```text id="c2v7h9"
Input
  ↓
Transformation
  ↓
   +
  ↑
Original Input
```

They help information flow through deeper networks.

Both Encoder and Decoder use residual connections, although the exact architecture varies.

---

## 18. Layer Normalization

Layer Normalization is another important Transformer component.

It helps stabilize representations during training.

A simplified view is:

```text id="m4z8r2"
Representation
      ↓
Layer Normalization
      ↓
Normalized Representation
```

Different Transformer architectures can use different normalization placement.

---

## 19. Encoder Block

A simplified Encoder block looks like:

```text id="p7d3w6"
Input
  ↓
👀 Self-Attention
  ↓
➕ Residual
  ↓
📏 LayerNorm
  ↓
🧠 Feed-Forward Network
  ↓
➕ Residual
  ↓
📏 LayerNorm
  ↓
Output
```

The exact order can vary.

The key components are:

* Self-attention
* FFN
* Residual connections
* Layer normalization

---

## 20. Decoder Block

A simplified original Decoder block contains an additional attention mechanism:

```text id="x6b1q4"
Input
  ↓
🎭 Masked Self-Attention
  ↓
➕ Residual
  ↓
📏 LayerNorm
  ↓
🔗 Cross-Attention
  ↑
Encoder Output
  ↓
➕ Residual
  ↓
📏 LayerNorm
  ↓
🧠 Feed-Forward Network
  ↓
➕ Residual
  ↓
📏 LayerNorm
  ↓
Output
```

This additional cross-attention is what connects the Decoder to the Encoder.

---

## 21. Complete Encoder-Decoder Architecture

```text id="w5q8n2"
                    📝 INPUT
                       ↓
                🔤 Tokenization
                       ↓
                🔢 Token IDs
                       ↓
              🧩 Input Embeddings
                       ↓
              📍 Positional Info
                       ↓
                ┌──────────────┐
                │    ENCODER   │
                │              │
                │ Self-Attn    │
                │     ↓        │
                │ FFN          │
                │     ↓        │
                │ Block × N    │
                └──────┬───────┘
                       ↓
              📊 Encoder Output
                       │
                       │ K + V
                       ↓
                ┌──────────────┐
                │    DECODER   │
                │              │
                │ Masked       │
                │ Self-Attn    │
                │     ↓        │
                │ Cross-Attn ←─┘
                │     ↓
                │ FFN
                │     ↓
                │ Block × N
                └──────┬───────┘
                       ↓
                📊 Final Output
                       ↓
                  🎯 LM Head
                       ↓
                    📈 Logits
                       ↓
                 🔤 Output Token
```

---

## 22. Example: Machine Translation

Consider:

```text id="j9r2k5"
Input:

"How are you?"
```

The Encoder processes the input:

```text id="f4x8m2"
"How are you?"
      ↓
   Encoder
      ↓
Contextual Representations
```

The Decoder begins generating the translated output.

```text id="a6w3q7"
Decoder
  ↓
"Comment"
  ↓
"Comment allez"
  ↓
"Comment allez-vous"
  ↓
...
```

At each generation step, the Decoder can use:

1. Previous generated tokens through masked self-attention.
2. Encoder representations through cross-attention.

---

## 23. Example: Text Summarization

Encoder-Decoder architecture can also be used for summarization.

Suppose the input is a long document.

```text id="v5c8n3"
📄 Long Document
       ↓
    Encoder
       ↓
Contextual Representations
       ↓
    Decoder
       ↓
📝 Summary
```

The Encoder processes the source document.

The Decoder generates the summary token by token.

---

## 24. Training the Encoder-Decoder Model

During training, the model receives source and target information.

For example:

```text id="q3w7k9"
Source:
"I love AI"

Target:
"J'aime l'IA"
```

The Encoder processes the source.

The Decoder receives the target sequence shifted so that each position predicts the next token.

Conceptually:

```text id="b8m2r5"
SOURCE
"I love AI"
    ↓
Encoder
    ↓
Encoder Output
    ↓
Decoder ← Previous Target Tokens
    ↓
Next Target Token
    ↓
Loss
```

Causal masking prevents the Decoder from seeing future target tokens through its self-attention.

---

## 25. Teacher Forcing

During training, the Decoder can receive the correct previous target tokens as input.

This is commonly called **teacher forcing**.

For example:

```text id="r4k7x1"
Target:
"I love AI"

Decoder Input:
"I love"

Target Prediction:
"AI"
```

The model learns to predict the next token using the correct previous context.

The exact training setup can vary.

---

## 26. Inference With Encoder-Decoder Architecture

During inference, the target sequence is generated step by step.

```text id="n7v3p5"
Source Input
     ↓
  Encoder
     ↓
Encoder Output
     ↓
  Decoder
     ↓
First Output Token
     ↓
Add Token
     ↓
  Decoder
     ↓
Next Output Token
     ↓
Repeat
```

Unlike training, the correct future target sequence is not available.

The model must generate it.

---

## 27. Training vs Inference

| Training                                                        | Inference                                |
| --------------------------------------------------------------- | ---------------------------------------- |
| Source input is available                                       | Source input is available                |
| Target sequence is available for supervision                    | Target output must be generated          |
| Decoder can use previous target tokens                          | Decoder uses previously generated tokens |
| Loss is calculated                                              | Tokens are selected/generated            |
| Many positions can be processed in parallel with causal masking | Generation is autoregressive             |

The model parameters are learned during training and then used during inference.

---

## 28. Encoder-Decoder vs Decoder-Only

These architectures should be clearly distinguished.

### Encoder-Decoder

```text id="m8q4z2"
Input
 ↓
Encoder
 ↓
Encoder Output
 ↓
Decoder
 ↓
Output
```

Used commonly for sequence-to-sequence tasks.

### Decoder-Only

```text id="c7x1v5"
Input
 ↓
Decoder-Only Transformer
 ↓
Next Token
 ↓
Repeat
```

Used by GPT-style autoregressive LLMs.

---

## 29. Why Are GPT-Style LLMs Decoder-Only?

Decoder-only architectures can perform autoregressive next-token prediction without requiring a separate Encoder.

```text id="d2n6p8"
Prompt
  ↓
Causal Self-Attention
  ↓
Transformer Blocks
  ↓
Next-Token Prediction
  ↓
Generated Token
  ↓
Repeat
```

This makes the architecture naturally suited to continuing a sequence from a prompt.

However, encoder-decoder models remain useful for many sequence-to-sequence tasks.

---

## 30. Encoder-Decoder vs GPT-Style Architecture

| Feature               | Encoder-Decoder                       | Decoder-Only                     |
| --------------------- | ------------------------------------- | -------------------------------- |
| Encoder               | Yes                                   | No                               |
| Decoder               | Yes                                   | Yes                              |
| Cross-attention       | Yes                                   | No separate Encoder pathway      |
| Causal self-attention | Decoder uses it                       | Yes                              |
| Typical design        | Sequence-to-sequence                  | Autoregressive language modeling |
| Example family        | Original Transformer, T5-style models | GPT-style models                 |

The exact architecture of a specific model can vary, so these categories describe broad architectural patterns.

---

## 31. Encoder-Decoder vs BERT

BERT uses an **Encoder-only** architecture.

```text id="e2p6r9"
BERT
 ↓
Encoder Stack
 ↓
Contextual Representations
```

It does not use the original Transformer Decoder.

This makes BERT different from both:

```text
Encoder-Decoder
```

and:

```text
Decoder-Only
```

---

## 32. Three Major Transformer Architecture Patterns

A useful high-level comparison is:

```text id="y7m3k2"
                 Transformer
                     │
        ┌────────────┼────────────┐
        ↓            ↓            ↓
   Encoder-Only  Decoder-Only  Encoder-Decoder
        │            │            │
      BERT          GPT       Original Transformer
```

### Encoder-Only

Focuses mainly on producing contextual representations.

### Decoder-Only

Focuses on autoregressive generation.

### Encoder-Decoder

Transforms one sequence into another.

---

## 33. Communication Between Encoder and Decoder

The Encoder and Decoder communicate through the Encoder's output.

```text id="q8r4m1"
Encoder
   ↓
Encoder Output
   ↓
K + V
   ↓
Cross-Attention
   ↑
Q
   ↑
Decoder
```

This allows the Decoder to retrieve relevant information from the source sequence.

---

## 34. Attention Flow

The complete attention flow in the original Transformer can be simplified as:

```text id="v3n7x5"
ENCODER
   ↓
Self-Attention
   ↓
Encoder Representations
   │
   │
   │ K + V
   ↓
DECODER
   ↑
Masked Self-Attention
   ↑
Previous Output Tokens
   ↓
Cross-Attention
   ↓
Feed-Forward Network
```

This shows the different roles of the attention mechanisms.

---

## 35. Sequence Lengths Can Be Different

An important property of Encoder-Decoder models is that input and output sequences do not need to have the same length.

For example:

```text id="h6p2q8"
Input:
"I am learning AI."

      ↓

Output:
"J'apprends l'IA."
```

The source and target token sequences can have different lengths.

Conceptually:

```text id="0x7m4c"
Source Length ≠ Target Length
```

This is useful for translation and summarization.

---

## 36. Encoder-Decoder and Contextual Representations

The Encoder produces contextual representations for the input.

The Decoder then creates its own evolving representations while generating output.

```text id="s5q9w3"
Input Tokens
     ↓
Encoder
     ↓
Encoder Contextual Representations
     ↓
Decoder Cross-Attention
     ↓
Decoder Representations
     ↓
Output Prediction
```

The representations are numerical vectors, not human-readable text.

---

## 37. Encoder-Decoder and Positional Information

Both input and output sequences need positional information.

```text id="r2v8k6"
Input Sequence
      ↓
Token Embeddings
      +
Positional Information
      ↓
Encoder
```

And:

```text id="n5x3j7"
Output Sequence
      ↓
Token Embeddings
      +
Positional Information
      ↓
Decoder
```

The exact positional mechanism depends on the architecture.

It can involve methods such as:

* Learned positional embeddings
* Sinusoidal positional encoding
* Rotary Position Embeddings (RoPE)
* Other position-aware mechanisms

---

## 38. Encoder-Decoder and Output Prediction

The Decoder's final representation is converted into vocabulary logits.

```text id="c9w4p1"
Decoder
  ↓
Final Representation
  ↓
Output Projection
  ↓
Logits
  ↓
Softmax / Generation Strategy
  ↓
Output Token
```

The output token is then added to the generated sequence.

---

## 39. Autoregressive Generation

Generation can be represented as:

```text id="m4q7z8"
Start
 ↓
Decoder
 ↓
Token 1
 ↓
Token 1 + Context
 ↓
Decoder
 ↓
Token 2
 ↓
Token 1 + Token 2 + Context
 ↓
Decoder
 ↓
Token 3
 ↓
Repeat
```

The Decoder continues until an appropriate stopping condition is reached.

---

## 40. Complete Training Flow

```text id="w8p2m6"
             📚 Training Data
                    ↓
             Source + Target
                    ↓
        ┌──────────────────────┐
        │       Encoder        │
        │                      │
        │ Self-Attention       │
        │ FFN                  │
        │ × N Blocks           │
        └──────────┬───────────┘
                   ↓
          Encoder Representations
                   ↓
        ┌──────────────────────┐
        │       Decoder        │
        │                      │
        │ Masked Self-Attention│
        │ Cross-Attention      │
        │ FFN                  │
        │ × N Blocks           │
        └──────────┬───────────┘
                   ↓
              Output Logits
                   ↓
                 Loss
                   ↓
            Backpropagation
                   ↓
          Parameter Updates
```

The training process repeats over many batches and iterations.

---

## 41. Complete Inference Flow

```text id="x5n8q2"
📝 Source Input
      ↓
📥 Encoder
      ↓
📊 Encoder Output
      ↓
📤 Decoder
      ↓
🎯 Next Token
      ↓
➕ Add Token
      ↓
📤 Decoder Again
      ↓
🎯 Next Token
      ↓
🔄 Repeat
      ↓
📝 Final Output
```

The Encoder can process the source input, while the Decoder generates the target sequence autoregressively.

---

## 42. Encoder-Decoder vs Simple Pipeline

It is useful to distinguish the architecture from a simple function.

A simplified sequence-to-sequence view is:

```text id="k3v7p1"
Input Sequence
      ↓
Encoder
      ↓
Representation
      ↓
Decoder
      ↓
Output Sequence
```

But internally, there are many operations:

```text id="t8m2q6"
Input
 ↓
Tokenization
 ↓
Embeddings
 ↓
Position
 ↓
Encoder Blocks
 ↓
Encoder Output
 ↓
Decoder Embeddings
 ↓
Masked Self-Attention
 ↓
Cross-Attention
 ↓
FFN
 ↓
Decoder Blocks
 ↓
Output Projection
 ↓
Logits
 ↓
Output Tokens
```

---

## 43. Encoder-Decoder Architecture Is Not One Fixed Implementation

The original Transformer provides the foundational Encoder-Decoder design.

Modern models can modify many details, including:

* Number of layers
* Attention implementation
* Positional mechanism
* Normalization
* Feed-Forward Network
* Vocabulary
* Output projection
* Attention optimizations
* Training objective

Therefore, “Encoder-Decoder Transformer” describes an architectural pattern rather than one identical implementation.

---

## 44. Encoder-Decoder vs Transformer Block

A **Transformer Block** is one building block.

An **Encoder** is a stack of Encoder blocks.

A **Decoder** is a stack of Decoder blocks.

The complete original Transformer combines both.

```text id="q7m1z4"
Transformer
│
├── Encoder
│   ├── Block 1
│   ├── Block 2
│   └── Block N
│
└── Decoder
    ├── Block 1
    ├── Block 2
    └── Block N
```

---

## 45. Encoder-Decoder vs LLM

Encoder-Decoder is an **architecture pattern**.

LLM is a **trained language model**.

Therefore:

```text id="m9x2c5"
Architecture
     ↓
Model
     ↓
Training
     ↓
Trained Language Model
```

An Encoder-Decoder model can be a language model, but not every Encoder-Decoder Transformer is necessarily what people mean by an LLM.

---

## 46. Simple Mental Model

Think of the architecture as a two-stage system:

```text id="v6r3k8"
📥 ENCODER
"Process the input"
        ↓
📊 Represent the input
        ↓
📤 DECODER
"Generate the output"
        ↓
📝 Output sequence
```

The Decoder communicates with the Encoder through cross-attention.

For the original Transformer:

```text id="p2w7n4"
Input
 ↓
Encoder
 ↓
Encoder Output
 ↓
Cross-Attention
 ↓
Decoder
 ↓
Output
```

---

## 47. Complete Architecture in One Diagram

```text id="a8m4q1"
                         📝 INPUT
                            ↓
                       🔤 Tokenize
                            ↓
                       🔢 Token IDs
                            ↓
                    🧩 Input Embeddings
                            ↓
                    📍 Positional Info
                            ↓
                 ┌────────────────────┐
                 │      ENCODER       │
                 │                    │
                 │  Self-Attention    │
                 │        ↓           │
                 │      FFN           │
                 │        ↓           │
                 │   Transformer      │
                 │   Blocks × N       │
                 └─────────┬──────────┘
                           ↓
                 📊 Encoder Output
                           │
                           │ K + V
                           ↓
                 ┌────────────────────┐
                 │      DECODER       │
                 │                    │
                 │ Masked Self-Attn   │
                 │        ↓           │
                 │ Cross-Attention ←──┘
                 │        ↓
                 │      FFN           │
                 │        ↓           │
                 │   Transformer      │
                 │   Blocks × N       │
                 └─────────┬──────────┘
                           ↓
                    📊 Final Output
                           ↓
                     🎯 Output Layer
                           ↓
                       📈 Logits
                           ↓
                    🎲 Probabilities
                           ↓
                      🔤 Token
                           ↓
                       🔄 Repeat
                           ↓
                     📝 OUTPUT
```

---

## 48. Key Takeaways

* 🔄 **Encoder-Decoder** is a Transformer architecture pattern with two main parts.
* 📥 The **Encoder** processes the input sequence and produces contextual representations.
* 📤 The **Decoder** generates the output sequence.
* 👀 The Encoder uses self-attention to process relationships within the input.
* 🎭 The original Decoder uses masked self-attention so future output tokens cannot be used.
* 🔗 The original Decoder uses **cross-attention** to access Encoder representations.
* 🧠 Both Encoder and Decoder contain Transformer blocks.
* 🎯 The Decoder's final representation is converted into vocabulary logits for output prediction.
* 🔁 Sequence generation can be autoregressive, producing one token at a time.
* 🌐 Encoder-Decoder architectures are especially useful for sequence-to-sequence tasks such as translation and summarization.
* 🚀 GPT-style models generally use a **decoder-only** architecture rather than the original Encoder-Decoder design.
* 🧩 BERT uses an **encoder-only** architecture.
* ⚠️ Encoder-Decoder, Encoder-only, and Decoder-only are different architectural patterns and should not be treated as interchangeable.
* 🧠 The architecture describes how components are connected; the model's actual capabilities depend on its data, parameters, training, and optimization.
