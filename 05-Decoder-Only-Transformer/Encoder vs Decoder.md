# ⚖️ Encoder vs Decoder

**Encoder** and **Decoder** are two major architectural components of the original Transformer.

They have different roles:

```text id="p4x8m2"
📥 Encoder
   ↓
Processes the input sequence
   ↓
📊 Contextual Representations


📤 Decoder
   ↓
Uses available context to generate output
   ↓
🎯 Output Tokens
```

The original Transformer combines both:

```text id="n7q3v5"
📝 Input
   ↓
📥 Encoder
   ↓
📊 Encoder Output
   ↓
📤 Decoder
   ↓
📝 Output
```

However, modern Transformer models do not all use both components. Some are **Encoder-only**, while others are **Decoder-only**.

---

# 1. What Is an Encoder?

An **Encoder** processes an input sequence and converts it into contextual representations.

```text id="x5m8q2"
📝 Input
   ↓
🔤 Tokenization
   ↓
🔢 Token IDs
   ↓
🧩 Embeddings
   ↓
📍 Positional Information
   ↓
📥 Encoder
   ↓
📊 Contextual Representations
```

The Encoder does not normally perform autoregressive next-token generation.

Its main role is to create useful representations of the input.

---

# 2. What Is a Decoder?

A **Decoder** is designed to generate an output sequence.

In the original Transformer, it receives:

* Previous output tokens
* Information from the Encoder

```text id="q8v3m6"
Previous Output Tokens
          ↓
       Decoder
          ↑
          │
   Encoder Output
          ↓
    Output Prediction
```

The original Decoder contains:

* Masked self-attention
* Cross-attention
* Feed-forward network
* Residual connections
* Layer normalization

---

# 3. Original Transformer

The original Transformer uses both an Encoder and a Decoder.

```text id="m2x7p4"
                    🏗️ TRANSFORMER
                           │
             ┌─────────────┴─────────────┐
             ↓                           ↓
        📥 ENCODER                  📤 DECODER
             ↓                           ↓
    Process Input                 Generate Output
             │                           ↑
             └──── Encoder Output ──────┘
```

The Encoder and Decoder communicate through **cross-attention**.

---

# 4. Main Difference

The simplest way to remember the difference is:

```text id="v6q2m8"
📥 Encoder
→ Processes the input

📤 Decoder
→ Generates the output
```

Or:

```text id="r4x9p1"
INPUT
  ↓
ENCODER
  ↓
REPRESENTATION
  ↓
DECODER
  ↓
OUTPUT
```

---

# 5. Encoder's Main Job

The Encoder transforms the input sequence into representations that contain contextual information.

For example:

```text id="k7m3x5"
"The cat is sleeping."

        ↓

      Encoder

        ↓

Contextual Representations
```

Each token's representation can be influenced by other relevant input tokens through self-attention.

---

# 6. Decoder's Main Job

The Decoder uses available information to generate the output sequence.

For example, in translation:

```text id="c8q2v6"
English Input
"I love AI"
      ↓
   Encoder
      ↓
Encoder Output
      ↓
   Decoder
      ↓
French Output
"J'aime l'IA"
```

The Decoder generates the target sequence autoregressively.

---

# 7. Encoder Self-Attention

The original Encoder uses self-attention.

```text id="p5x8m3"
Input Representations
        ↓
   Self-Attention
        ↓
Contextual Representations
```

Encoder self-attention is normally **not causal**.

Therefore, a token can generally attend to both earlier and later input positions.

For example:

```text id="y3m7q2"
"The cat sat on the mat"

A token can generally use information
from other positions in the input sequence.
```

Padding masks may still be used where required.

---

# 8. Decoder Self-Attention

The original Decoder also uses self-attention, but it is **masked**.

```text id="n8q4x1"
Previous Output Tokens
        ↓
Masked Self-Attention
        ↓
Decoder Representation
```

The causal mask prevents a position from accessing future output tokens.

For example:

```text id="z6m2p8"
        1   2   3   4
    ┌───────────────
1   │ ✓   ✗   ✗   ✗
2   │ ✓   ✓   ✗   ✗
3   │ ✓   ✓   ✓   ✗
4   │ ✓   ✓   ✓   ✓
```

This is required for autoregressive generation.

---

# 9. Cross-Attention

The original Decoder has another important mechanism: **cross-attention**.

It connects the Decoder to the Encoder.

```text id="q5x8m2"
Decoder Representation
        ↓
        Q
        ↓
 Cross-Attention
        ↑
      K + V
        ↑
Encoder Output
```

The Decoder's Query comes from the Decoder representation.

The Encoder provides the Keys and Values.

---

# 10. Self-Attention vs Cross-Attention

| Feature                  | Self-Attention                | Cross-Attention                           |
| ------------------------ | ----------------------------- | ----------------------------------------- |
| Query                    | Same representation source    | Decoder                                   |
| Key                      | Same representation source    | Encoder                                   |
| Value                    | Same representation source    | Encoder                                   |
| Main purpose             | Interaction within a sequence | Communication between Encoder and Decoder |
| Used in Encoder          | Yes                           | No                                        |
| Used in original Decoder | Yes                           | Yes                                       |

A useful mental model:

```text id="w4p9m6"
Self-Attention
→ "Look within this representation sequence."

Cross-Attention
→ "Use information from another representation sequence."
```

These are conceptual descriptions, not literal human actions.

---

# 11. Causal Masking

Causal masking is one of the biggest differences between Encoder and original Decoder self-attention.

### Encoder

```text id="a7x3q9"
Self-Attention
      ↓
Normally can see both directions
```

### Decoder

```text id="m8q2v5"
Causal Self-Attention
      ↓
Can see current + previous positions
      ↓
Cannot see future positions
```

This difference allows the Decoder to generate tokens autoregressively.

---

# 12. Encoder Block

A simplified Encoder block is:

```text id="r3m7x1"
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

The exact order of normalization and residual operations varies by architecture.

---

# 13. Decoder Block

A simplified original Decoder block is:

```text id="p6x2m8"
Input
  ↓
🎭 Masked Self-Attention
  ↓
➕ Residual + Norm
  ↓
🔗 Cross-Attention
  ↑
Encoder Output
  ↓
➕ Residual + Norm
  ↓
🧠 Feed-Forward Network
  ↓
➕ Residual + Norm
  ↓
Output
```

The Decoder therefore has an additional attention mechanism compared with the original Encoder block.

---

# 14. Encoder vs Decoder Components

| Component              | Encoder        | Original Decoder                  |
| ---------------------- | -------------- | --------------------------------- |
| Token Embeddings       | Yes            | Yes                               |
| Positional Information | Yes            | Yes                               |
| Self-Attention         | Yes            | Yes                               |
| Causal Self-Attention  | Normally No    | Yes                               |
| Cross-Attention        | No             | Yes                               |
| Feed-Forward Network   | Yes            | Yes                               |
| Residual Connections   | Yes            | Yes                               |
| Layer Normalization    | Yes            | Yes                               |
| Output Projection      | Task-dependent | Usually used for generated output |

The exact implementation can vary between models.

---

# 15. Input to the Encoder

The Encoder receives the source sequence.

For example:

```text id="x7m4q2"
"I love machine learning."
```

The input passes through:

```text id="k3p8v6"
Text
 ↓
Tokenization
 ↓
Token IDs
 ↓
Token Embeddings
 ↓
Positional Information
 ↓
Encoder
```

The Encoder then produces contextual representations.

---

# 16. Input to the Decoder

The original Decoder receives information from two sources:

```text id="n5q2x8"
1. Previous Output Tokens
2. Encoder Output
```

Conceptually:

```text id="v8m3p6"
Previous Output Tokens
        ↓
      Decoder
        ↑
        │
 Encoder Output
```

The previous output tokens are processed through masked self-attention.

The Encoder output is accessed through cross-attention.

---

# 17. Output of the Encoder

The Encoder normally produces a sequence of contextual representations.

```text id="q6x1m9"
Input
  ↓
Encoder Blocks
  ↓
Encoder Output
```

These representations are not normally vocabulary probabilities.

They are numerical vectors.

---

# 18. Output of the Decoder

The Decoder produces representations that can be converted into vocabulary logits.

```text id="m4p7x2"
Decoder
  ↓
Final Representation
  ↓
Output Projection
  ↓
Logits
  ↓
Probability Distribution
  ↓
Output Token
```

This allows the Decoder to generate output tokens.

---

# 19. Encoder and Representation Learning

The Encoder is especially useful when the main goal is to create a rich representation of an input.

For example:

```text id="z8q3m5"
Input Text
    ↓
Encoder
    ↓
Contextual Representation
    ↓
Classification / Similarity / Other Task
```

This is one reason Encoder-only architectures are useful for tasks involving understanding or representation extraction.

“Understanding” here refers to learned representations and task behavior, not human-like understanding.

---

# 20. Decoder and Generation

The Decoder is particularly suited to autoregressive generation.

```text id="c5x9m3"
Prompt
  ↓
Decoder
  ↓
Next Token
  ↓
Add Token
  ↓
Decoder Again
  ↓
Next Token
  ↓
Repeat
```

For example:

```text id="r7m2q6"
"The"
 ↓
"The cat"
 ↓
"The cat is"
 ↓
"The cat is sleeping"
```

---

# 21. Encoder-Decoder Example: Translation

Consider:

```text id="h3x8m5"
Input:
"How are you?"
```

The Encoder processes the source:

```text id="p6q2v9"
"How are you?"
      ↓
   Encoder
      ↓
Encoder Representations
```

The Decoder generates the target:

```text id="m4x7q1"
Encoder Representations
        ↓
      Decoder
        ↓
"Comment"
        ↓
"Comment allez"
        ↓
"Comment allez-vous"
```

At each step, the Decoder can use:

* Previous target tokens
* Encoder representations

---

# 22. Encoder-Decoder Example: Summarization

Suppose the input is a long document.

```text id="q8m3x6"
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

The Decoder generates the summary.

---

# 23. Encoder-Only Models

An Encoder does not always need to be paired with a Decoder.

An Encoder can be the complete model architecture.

```text id="x5q7m2"
Input
  ↓
Encoder
  ↓
Contextual Representations
  ↓
Task Output
```

A well-known example is **BERT**.

BERT is an Encoder-only Transformer model.

---

# 24. Decoder-Only Models

A Decoder can also be used without an Encoder.

This is called a **Decoder-only architecture**.

```text id="m8x4p1"
Input
  ↓
Decoder-Only Transformer
  ↓
Causal Self-Attention
  ↓
Next-Token Prediction
  ↓
Generated Text
```

GPT-style autoregressive language models use this general architecture.

---

# 25. Encoder-Only vs Decoder-Only

| Feature         | Encoder-Only                 | Decoder-Only                |
| --------------- | ---------------------------- | --------------------------- |
| Encoder         | Yes                          | No                          |
| Decoder         | No                           | Yes                         |
| Self-Attention  | Usually bidirectional        | Causal                      |
| Cross-Attention | No                           | No separate Encoder pathway |
| Main use        | Representation-focused tasks | Autoregressive generation   |
| Example         | BERT                         | GPT-style models            |

These are broad architectural patterns, and individual models can contain additional design choices.

---

# 26. Encoder-Decoder vs Decoder-Only

| Feature              | Encoder-Decoder      | Decoder-Only                |
| -------------------- | -------------------- | --------------------------- |
| Encoder              | Yes                  | No                          |
| Decoder              | Yes                  | Yes                         |
| Cross-Attention      | Yes                  | No separate Encoder pathway |
| Input processing     | Encoder              | Decoder stack               |
| Generation           | Decoder              | Decoder                     |
| Typical task pattern | Sequence-to-sequence | Autoregressive continuation |

For example:

```text id="f2m6q8"
Encoder-Decoder:

Input → Encoder → Decoder → Output
```

Whereas:

```text id="v7x3p1"
Decoder-Only:

Input → Decoder → Next Token → Repeat
```

---

# 27. Encoder vs Decoder: Attention Pattern

A simple comparison:

```text id="j4m8x2"
ENCODER

Token 1 ↔ Token 2 ↔ Token 3 ↔ Token 4
      ↕        ↕        ↕        ↕
      Information can flow across input positions
```

While:

```text id="q6p2x9"
DECODER

Token 1
  ↓
Token 2
  ↓
Token 3
  ↓
Token 4
```

The Decoder's causal mask prevents future positions from contributing to earlier predictions.

The diagrams are simplified; actual attention is represented by matrices and can contain many different weights.

---

# 28. Encoder vs Decoder: Information Flow

### Encoder

```text id="m3x7q5"
Input
 ↓
Self-Attention
 ↓
FFN
 ↓
Representation
```

### Original Decoder

```text id="p8q4v2"
Previous Output
 ↓
Masked Self-Attention
 ↓
Cross-Attention ← Encoder Output
 ↓
FFN
 ↓
Output Representation
```

---

# 29. Encoder vs Decoder: Sequence Direction

The Encoder can process the input using information from both directions.

```text id="c7m2x9"
Previous ← Current → Future
```

The original Decoder uses causal self-attention.

```text id="v4q8p3"
Previous → Current
             ✗ Future
```

This is why Encoder and Decoder self-attention behave differently.

---

# 30. Encoder vs Decoder: Generation

The Encoder is not normally used for autoregressive generation.

```text id="x5m8q1"
Encoder
 ↓
Representation
```

The Decoder is designed for autoregressive output generation.

```text id="n3q7v6"
Decoder
 ↓
Next Token
 ↓
Next Token
 ↓
Next Token
```

An Encoder can still be part of a generative Encoder-Decoder system, where the Decoder performs the generation.

---

# 31. Encoder vs Decoder: Training

Both Encoder and Decoder parameters are learned during training in an Encoder-Decoder model.

```text id="q8x3m5"
Input
 ↓
Encoder
 ↓
Encoder Output
 ↓
Decoder
 ↓
Prediction
 ↓
Loss
 ↓
Backpropagation
 ↓
Parameter Updates
```

The loss signal can update parameters throughout the model.

---

# 32. Encoder vs Decoder: Inference

During inference in an Encoder-Decoder model:

```text id="m7p2x8"
Source Input
    ↓
 Encoder
    ↓
Encoder Output
    ↓
 Decoder
    ↓
Output Token
    ↓
 Decoder
    ↓
Next Output Token
    ↓
Repeat
```

The Encoder processes the source input, while the Decoder generates the target sequence.

---

# 33. Encoder vs Decoder: Position Information

Both sides need information about token positions.

```text id="r5x9m2"
Encoder:
Token Embeddings + Position
          ↓
       Encoder
```

```text id="v3q7p6"
Decoder:
Token Embeddings + Position
          ↓
       Decoder
```

The exact position mechanism can differ across architectures.

---

# 34. Encoder vs Decoder: Transformer Blocks

Both use Transformer blocks, but the blocks are not identical in the original architecture.

```text id="x8m2q4"
Encoder Block
│
├── Self-Attention
├── FFN
├── Residual Connections
└── LayerNorm
```

```text id="p6q3v9"
Decoder Block
│
├── Masked Self-Attention
├── Cross-Attention
├── FFN
├── Residual Connections
└── LayerNorm
```

The additional cross-attention is the key architectural difference.

---

# 35. Encoder vs Decoder: Q, K, V

For Encoder self-attention:

```text id="m4x8q1"
Encoder
  ↓
Q, K, V
  ↓
Self-Attention
```

All three come from the Encoder's representation source.

For original Decoder self-attention:

```text id="v7p3m5"
Decoder
  ↓
Q, K, V
  ↓
Masked Self-Attention
```

For cross-attention:

```text id="q2m6x8"
Decoder → Q
Encoder → K, V
```

This allows the Decoder to access Encoder information.

---

# 36. Encoder vs Decoder: Contextual Representations

The Encoder creates contextual representations of the input.

```text id="c8x3m7"
Input Tokens
     ↓
Encoder
     ↓
Contextual Representations
```

The Decoder also creates contextual representations, but its representations are shaped by:

* Previous output tokens
* Causal masking
* Encoder information through cross-attention in the original architecture

```text id="n5q8v2"
Previous Output
      +
Encoder Information
      ↓
    Decoder
      ↓
Decoder Representations
```

---

# 37. Encoder vs Decoder: Main Question

A simple conceptual question for each component is:

### Encoder

> **How should the input sequence be represented using its available context?**

### Decoder

> **Given the available output context, and Encoder information when present, what should be generated next?**

These are simplified descriptions of their computational roles.

---

# 38. Complete Encoder-Decoder Comparison

| Feature                   | Encoder                                           | Decoder                                    |
| ------------------------- | ------------------------------------------------- | ------------------------------------------ |
| Main role                 | Process input                                     | Generate output                            |
| Input                     | Source sequence                                   | Previous target tokens + Encoder output    |
| Self-attention            | Yes                                               | Yes                                        |
| Self-attention type       | Normally non-causal                               | Causal/masked in original Transformer      |
| Cross-attention           | No                                                | Yes in original Transformer                |
| Future tokens visible?    | Input positions can generally see both directions | Future output positions are blocked        |
| FFN                       | Yes                                               | Yes                                        |
| Residual connections      | Yes                                               | Yes                                        |
| Layer normalization       | Yes                                               | Yes                                        |
| Output                    | Contextual representations                        | Output representations / token predictions |
| Autoregressive generation | Not normally                                      | Yes                                        |
| Standalone architecture   | Encoder-only models                               | Decoder-only models                        |

---

# 39. Original Transformer in One Diagram

```text id="k6m2x8"
                       🏗️ TRANSFORMER
                              │
                ┌─────────────┴─────────────┐
                ↓                           ↓
           📥 ENCODER                  📤 DECODER
                │                           │
                ↓                           ↓
        Self-Attention              Masked Self-Attention
                │                           │
                ↓                           ↓
               FFN                    Cross-Attention
                │                           ↑
                ↓                           │
          Encoder Output ────────────────┘
                                            │
                                            ↓
                                           FFN
                                            │
                                            ↓
                                     Output Projection
                                            │
                                            ↓
                                       Output Tokens
```

---

# 40. Modern Transformer Families

The original Encoder-Decoder design led to several common Transformer patterns.

```text id="p9x4m7"
                 Transformer
                      │
          ┌───────────┼───────────┐
          ↓           ↓           ↓
     Encoder-Only Decoder-Only Encoder-Decoder
          │           │           │
        BERT       GPT-style    T5-style /
                                Original Transformer
```

These architectures can serve different modeling objectives.

---

# 41. Common Misunderstandings

### ❌ “Encoder means it encodes text into a single number.”

Not necessarily.

The Encoder normally produces a **sequence of contextual vectors**.

---

### ❌ “Decoder always means it has cross-attention.”

Not necessarily.

The original Transformer Decoder has cross-attention, but a **decoder-only LLM does not have a separate Encoder to attend to**.

---

### ❌ “Decoder can see the complete output during generation.”

No.

Causal masking prevents future output tokens from being used when predicting the current token.

---

### ❌ “Encoder cannot generate anything.”

An Encoder by itself does not normally perform autoregressive generation, but an Encoder can be part of a generative Encoder-Decoder system.

---

### ❌ “Encoder is always bidirectional in every architecture.”

The original Transformer Encoder uses non-causal self-attention, but exact masking and architecture can vary.

---

### ❌ “Encoder and Decoder are two separate neural networks.”

In the original Transformer they are two major stacks within one overall Transformer model, trained together for the task.

---

# 42. Simple Mental Model

Remember:

```text id="x7q3m8"
📥 ENCODER
     ↓
"Process the input"
     ↓
📊 Contextual Representation
```

and:

```text id="m2v8p5"
📤 DECODER
     ↓
"Use available context"
     ↓
🎯 Generate Output
```

For the original Transformer:

```text id="q6x4m9"
INPUT
  ↓
ENCODER
  ↓
ENCODER OUTPUT
  ↓
CROSS-ATTENTION
  ↓
DECODER
  ↓
OUTPUT
```

For GPT-style models:

```text id="v8m3q1"
PROMPT
  ↓
DECODER-ONLY TRANSFORMER
  ↓
NEXT TOKEN
  ↓
REPEAT
```

---

# 43. Key Takeaways

* 📥 **Encoder** processes an input sequence and produces contextual representations.
* 📤 **Decoder** generates an output sequence.
* 🏗️ The original Transformer uses **both Encoder and Decoder**.
* 👀 Encoder self-attention is normally non-causal, allowing information from both directions of the input sequence.
* 🎭 Original Decoder self-attention is causal/masked to prevent future-token information from leaking into predictions.
* 🔗 The original Decoder uses **cross-attention** to access Encoder representations.
* 🧠 Both Encoder and Decoder contain Transformer blocks, FFNs, residual connections, and normalization.
* 📊 The Encoder normally produces contextual representations rather than next-token probabilities.
* 🎯 The Decoder's final representations can be mapped to vocabulary logits for output prediction.
* 🔄 Encoder-Decoder models are useful for sequence-to-sequence tasks such as translation and summarization.
* 🧩 **Encoder-only** models such as BERT can use the Encoder stack without a Decoder.
* 🚀 **Decoder-only** models such as GPT-style LLMs use a Decoder-style stack without a separate Encoder.
* ⚠️ A decoder-only Transformer does **not** have the Encoder-to-Decoder cross-attention pathway of the original Encoder-Decoder architecture.
* 🧠 Encoder and Decoder describe architectural roles, not human-like “understanding” or “thinking.”
