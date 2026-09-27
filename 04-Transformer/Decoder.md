# 📤 Decoder

A **Decoder** is a major component of the original **Transformer architecture**.

Its main job is to use available input information and generate an output sequence **one token at a time**.

In the original Transformer, the Decoder works together with the Encoder.

```text
📝 Input Sequence
       ↓
📥 Encoder
       ↓
📊 Encoder Output
       ↓
📤 Decoder
       ↓
📝 Output Sequence
```

Modern **decoder-only LLMs**, such as GPT-style models, use the Decoder side of the Transformer architecture without a separate Encoder.

---

## 1. What Is a Decoder?

A Decoder is a stack of Transformer blocks designed to produce an output sequence.

In the original Transformer, the Decoder receives:

* information from the previous output tokens
* information from the Encoder
* positional information

It then processes this information and produces representations that are used to predict the next output token.

```text
Previous Output Tokens
          +
    Encoder Output
          ↓
       Decoder
          ↓
   Output Representation
          ↓
    Output Projection
          ↓
    Next Output Token
```

---

## 2. Decoder in the Original Transformer

The original Transformer introduced an **Encoder-Decoder architecture**.

```text
                 ┌──────────────┐
Input Sequence → │    Encoder   │
                 └──────┬───────┘
                        ↓
                Encoder Output
                        ↓
                 ┌──────────────┐
Previous Output → │    Decoder   │
Tokens            └──────┬───────┘
                         ↓
                  Output Sequence
```

The Encoder processes the input.

The Decoder generates the output.

For example, in machine translation:

```text
English:
"I love AI"

        ↓

     Encoder

        ↓

French:
"J'aime l'IA"
```

The Decoder generates the translated sequence.

---

## 3. What Does the Decoder Receive?

The Decoder can receive two important types of information in the original Transformer:

### 1. Previous output tokens

These are the tokens that have already been generated or are available during training.

### 2. Encoder output

These are contextual representations produced by the Encoder.

```text
Previous Output Tokens
          ↓
     Decoder Input

Encoder Output
          ↓
    Cross-Attention
```

The Decoder combines these sources of information to generate the next output token.

---

## 4. Decoder Input

The Decoder does not directly receive raw text.

The output text is first converted into tokens and then Token IDs.

```text
📝 Output Text
      ↓
🔤 Tokenization
      ↓
🔢 Token IDs
      ↓
🧩 Token Embeddings
      ↓
📍 Positional Information
      ↓
📤 Decoder
```

For example:

```text
"I love AI"

      ↓

["I", "love", "AI"]

      ↓

[125, 842, 731]
```

The exact tokens and IDs depend on the tokenizer.

---

## 5. Decoder Is a Stack of Transformer Blocks

A Decoder is normally composed of multiple Transformer blocks.

```text
Decoder Input
      ↓
🔄 Decoder Block 1
      ↓
🔄 Decoder Block 2
      ↓
🔄 Decoder Block 3
      ↓
        ...
      ↓
🔄 Decoder Block N
      ↓
Final Representation
```

Each block gradually transforms the token representations.

More blocks allow the model to perform more layers of learned computation.

---

## 6. What Is Inside a Decoder Block?

The original Transformer Decoder block contains three major subcomponents:

```text
Input
  ↓
🎭 Masked Self-Attention
  ↓
➕ Residual Connection
  ↓
📏 Layer Normalization
  ↓
🔗 Cross-Attention
  ↓
➕ Residual Connection
  ↓
📏 Layer Normalization
  ↓
🧠 Feed-Forward Network
  ↓
➕ Residual Connection
  ↓
📏 Layer Normalization
  ↓
Output
```

The exact ordering of residual connections and normalization depends on the Transformer architecture.

The important components are:

* Masked Self-Attention
* Cross-Attention
* Feed-Forward Network
* Residual Connections
* Layer Normalization

---

## 7. Masked Self-Attention

The first attention mechanism in the original Decoder is **masked self-attention**.

It allows each output position to interact with earlier output positions while preventing it from seeing future output tokens.

```text
Token 1 → Token 1

Token 2 → Token 1, Token 2

Token 3 → Token 1, Token 2, Token 3

Token 4 → Token 1, Token 2, Token 3, Token 4
```

The Decoder cannot use future tokens when predicting the current token.

---

## 8. Why Is Causal Masking Needed?

Suppose the target sequence is:

```text
The cat is sleeping
```

When predicting:

```text
The cat is
```

the model should predict:

```text
sleeping
```

It should not already see `"sleeping"` as input while making that prediction.

Without masking, the model could access future information during training.

Causal masking prevents this.

```text
Allowed:

Token 1 → Token 1

Token 2 → Token 1, Token 2

Token 3 → Token 1, Token 2, Token 3

Token 4 → Token 1, Token 2, Token 3, Token 4
```

Conceptually, the mask looks like:

```text
        1   2   3   4
    ┌───────────────
1   │ ✓   ✗   ✗   ✗
2   │ ✓   ✓   ✗   ✗
3   │ ✓   ✓   ✓   ✗
4   │ ✓   ✓   ✓   ✓
```

This is called **causal self-attention**.

---

## 9. Cross-Attention

The second attention mechanism in the original Decoder is **cross-attention**.

Cross-attention allows the Decoder to use information produced by the Encoder.

```text
Decoder Representation
        ↓
      Query
        ↓
   Cross-Attention
        ↑
 Encoder Output
   Key + Value
```

This is different from self-attention.

### Self-Attention

Q, K, and V come from the same sequence.

```text
Decoder Representation
       ↓
    Q, K, V
       ↓
Self-Attention
```

### Cross-Attention

The Query comes from the Decoder, while Keys and Values come from the Encoder output.

```text
Decoder → Q
Encoder → K, V

      ↓

Cross-Attention
```

---

## 10. Why Does Cross-Attention Matter?

Cross-attention allows the Decoder to look at the Encoder's representation of the input.

For example, in translation:

```text
English Input
"I love AI"
      ↓
    Encoder
      ↓
Contextual Representations
      ↓
    Decoder
      ↓
French Output
"J'aime l'IA"
```

While generating the French output, the Decoder can use relevant information from the encoded English input.

---

## 11. Self-Attention vs Cross-Attention

| Feature                  | Self-Attention                          | Cross-Attention              |
| ------------------------ | --------------------------------------- | ---------------------------- |
| Query                    | Same sequence                           | Decoder                      |
| Key                      | Same sequence                           | Encoder                      |
| Value                    | Same sequence                           | Encoder                      |
| Main purpose             | Process relationships within a sequence | Connect Decoder with Encoder |
| Used in original Decoder | Yes                                     | Yes                          |

The two mechanisms solve different problems.

---

## 12. Feed-Forward Network in the Decoder

After attention operations, the Decoder uses a **Feed-Forward Network (FFN)**.

The FFN transforms the representation at each token position.

```text
Attention Output
      ↓
🧠 Feed-Forward Network
      ↓
Transformed Representation
```

A simplified FFN is:

```text
Input
  ↓
Linear Transformation
  ↓
Activation Function
  ↓
Linear Transformation
  ↓
Output
```

The attention mechanisms allow information to move between positions.

The FFN performs additional transformations on each position.

---

## 13. Residual Connections

Residual connections help information flow through the Decoder block.

A simplified idea is:

```text
Input
  ↓
Attention
  ↓
Transformation
  ↓
+
↑
Input
```

The original input is combined with the transformed output.

This helps deeper Transformer networks preserve and refine information.

---

## 14. Layer Normalization

Layer Normalization is used inside Transformer blocks to help stabilize the representations during training.

Conceptually:

```text
Representation
      ↓
Layer Normalization
      ↓
Normalized Representation
```

Different Transformer architectures can place normalization at different points.

Two common designs are:

```text
Post-Norm
Input
 ↓
Attention
 ↓
Add Residual
 ↓
LayerNorm
```

and:

```text
Pre-Norm
Input
 ↓
LayerNorm
 ↓
Attention
 ↓
Add Residual
```

The exact design depends on the architecture.

---

## 15. One Decoder Block

A simplified original Transformer Decoder block can be represented as:

```text
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
                   │
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

Multiple Decoder blocks are stacked together.

---

## 16. Stacking Decoder Blocks

A Transformer Decoder is usually not just one block.

It contains multiple blocks.

```text
Decoder Input
      ↓
┌─────────────────┐
│ Decoder Block 1 │
└────────┬────────┘
         ↓
┌─────────────────┐
│ Decoder Block 2 │
└────────┬────────┘
         ↓
┌─────────────────┐
│ Decoder Block 3 │
└────────┬────────┘
         ↓
        ...
         ↓
┌─────────────────┐
│ Decoder Block N │
└────────┬────────┘
         ↓
Final Representation
```

Each block receives the output of the previous block.

---

## 17. What Is the Decoder Output?

The final Decoder block produces contextual representations.

These representations are not directly words.

They are numerical vectors containing information produced by the Decoder.

```text
Decoder Blocks
      ↓
📊 Final Representations
      ↓
🎯 Output Projection
      ↓
📈 Logits
      ↓
🎲 Probability Distribution
      ↓
🔤 Next Token
```

---

## 18. Output Projection

The final Decoder representation is passed through an output projection, often called a:

* Language Modeling Head
* LM Head
* Output Projection

Its job is to produce a score for every token in the vocabulary.

For example, if the vocabulary contains:

```text
50,000 tokens
```

the output for one position can contain:

```text
50,000 logits
```

Each logit corresponds to one possible token.

---

## 19. Logits

Logits are raw scores produced by the output layer.

For example:

```text
Token       Logit
-------------------
"cat"        2.8
"dog"        1.9
"runs"       4.1
"blue"       0.7
...
```

These values are not probabilities.

Softmax can convert them into a probability distribution.

```text
Logits
  ↓
Softmax
  ↓
Probabilities
```

---

## 20. Next-Token Prediction

The Decoder can use the output probabilities to select the next token.

For example:

```text
Input:

"The cat"

      ↓

Decoder

      ↓

Probabilities:

"runs"    → 0.45
"sleeps"  → 0.30
"is"      → 0.10
"eats"    → 0.08
...

      ↓

Selected Token

"runs"
```

The exact token selection depends on the decoding strategy.

---

## 21. Autoregressive Generation

The Decoder generates output autoregressively.

That means the generated token becomes part of the context for the next prediction.

```text
"The"
  ↓
Predict "cat"
  ↓
"The cat"
  ↓
Predict "is"
  ↓
"The cat is"
  ↓
Predict "sleeping"
  ↓
"The cat is sleeping"
```

The process continues until a stopping condition is reached.

---

## 22. Decoder During Training

During training, the model is trained to predict the next token.

For example:

```text
Input:
"The cat is"

Target:
"sleeping"
```

More generally:

```text
Input Tokens:
The | cat | is | sleeping

Targets:
cat | is | sleeping | ...
```

The causal mask ensures each position cannot use future target tokens as input through self-attention.

This allows many training positions to be processed in parallel while maintaining the next-token prediction objective.

---

## 23. Decoder During Inference

During inference, the model receives the available context and generates tokens step by step.

```text
Prompt
  ↓
Tokenization
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

This is the basic autoregressive generation process.

---

## 24. Decoder-Only Transformers

Modern GPT-style LLMs use a **decoder-only architecture**.

They do not contain a separate Encoder.

```text
📝 Input Text
      ↓
🔤 Tokenization
      ↓
🔢 Token IDs
      ↓
🧩 Embeddings
      ↓
📍 Positional Information
      ↓
🎭 Causal Self-Attention
      ↓
🧠 Feed-Forward Network
      ↓
🔄 Transformer Blocks
      ↓
🎯 LM Head
      ↓
📈 Logits
      ↓
🔤 Next Token
```

The important difference is that decoder-only models do not use Encoder-Decoder cross-attention in the same way as the original Transformer.

---

## 25. Decoder vs Decoder-Only LLM

These terms are related but should not be treated as exactly identical.

### Original Transformer Decoder

```text
Masked Self-Attention
        +
Cross-Attention
        +
Feed-Forward Network
```

It receives information from an Encoder.

### Decoder-Only LLM

```text
Causal Self-Attention
        +
Feed-Forward Network
```

There is no separate Encoder.

This architecture is used by GPT-style autoregressive language models.

---

## 26. Encoder vs Decoder

| Feature               | Encoder                    | Original Decoder       |
| --------------------- | -------------------------- | ---------------------- |
| Main role             | Encode input               | Generate output        |
| Self-attention        | Yes                        | Yes                    |
| Causal masking        | Normally no                | Yes                    |
| Cross-attention       | No                         | Yes                    |
| Output                | Contextual representations | Output representations |
| Next-token generation | Not usually                | Yes                    |
| Original Transformer  | Yes                        | Yes                    |

This comparison refers specifically to the **original Encoder-Decoder Transformer architecture**.

---

## 27. Decoder vs GPT-Style LLM

A GPT-style LLM is based on the Decoder side of the Transformer idea, but its architecture is **decoder-only**.

```text
Original Transformer

Encoder
   ↓
Decoder
   ↓
Output
```

Whereas:

```text
GPT-Style LLM

Decoder-Only Transformer
        ↓
     LM Head
        ↓
    Next Token
```

The decoder-only design removes the separate Encoder and cross-attention pathway used in the original Encoder-Decoder Transformer.

---

## 28. Decoder and Causal Attention

Causal attention is one of the most important concepts in decoder-based autoregressive models.

The model must follow:

```text
Past → Current
```

but not:

```text
Future → Current
```

Conceptually:

```text
        Token
         ↓
Can see:
Current + Previous Tokens

Cannot see:
Future Tokens
```

This maintains the autoregressive prediction process.

---

## 29. Decoder and Contextual Representations

Each Decoder block transforms the token representations.

After multiple blocks:

```text
Token Embeddings
      ↓
Decoder Block 1
      ↓
Contextual Representations
      ↓
Decoder Block 2
      ↓
More Refined Representations
      ↓
Decoder Block 3
      ↓
More Refined Representations
      ↓
...
```

The representation of a token can depend on the available context through attention.

---

## 30. Decoder and Model Depth

Adding more Decoder blocks creates a deeper Transformer.

```text
Input
  ↓
Block 1
  ↓
Block 2
  ↓
Block 3
  ↓
...
  ↓
Block N
  ↓
Output
```

Different models use different numbers of layers.

More layers provide more computation capacity, but increasing depth also increases computational and memory requirements.

---

## 31. Decoder Parameters

A Decoder contains many learned parameters.

These can include parameters associated with:

* Attention projections
* Feed-Forward Networks
* Layer Normalization
* Output projection
* Token embeddings, depending on architecture
* Other architecture-specific components

During training, these parameters are updated to reduce the prediction loss.

---

## 32. What Does the Decoder Learn?

The Decoder does not store a simple dictionary of answers.

During training, its parameters are adjusted based on prediction errors.

It learns statistical patterns and relationships useful for predicting tokens.

These can include:

* language patterns
* syntax
* token relationships
* contextual relationships
* common sequences
* patterns in the training data

The exact behavior depends on the training data, architecture, optimization, and other training choices.

---

## 33. Decoder and Attention Relationships

The Decoder's self-attention allows tokens to interact with other allowed positions.

For example:

```text
"The cat sat on the mat"
```

When processing a later token, the Decoder can use information from earlier tokens.

```text
Current Position
      ↓
Query
      ↓
Compare With Earlier Keys
      ↓
Attention Weights
      ↓
Combine Earlier Values
      ↓
Updated Representation
```

In the original Encoder-Decoder Transformer, cross-attention additionally allows the Decoder to use Encoder representations.

---

## 34. Decoder vs Attention

A Decoder is much larger than an attention mechanism.

```text
Decoder
│
├── Masked Self-Attention
├── Cross-Attention
├── Feed-Forward Network
├── Residual Connections
└── Layer Normalization
```

Attention is only one component.

In decoder-only LLMs:

```text
Decoder-Only Transformer
│
├── Causal Self-Attention
├── Feed-Forward Network
├── Residual Connections
└── Layer Normalization
```

---

## 35. Decoder vs Transformer

A Transformer is an architecture.

A Decoder is one major component/design within Transformer architectures.

The original Transformer contains:

```text
Transformer
│
├── Encoder
└── Decoder
```

A decoder-only Transformer contains:

```text
Transformer
│
└── Decoder-Only Stack
```

So the terms should not be used interchangeably.

---

## 36. Decoder vs LLM

A Decoder is an architectural component.

An LLM is a trained language model.

For example:

```text
Decoder Architecture
        ↓
Transformer-Based Model
        ↓
Large-Scale Training
        ↓
Language Model
        ↓
LLM
```

Architecture alone does not make a model an LLM.

Training data, model scale, optimization, and training process also matter.

---

## 37. Decoder During Training vs Inference

| Training                                         | Inference                         |
| ------------------------------------------------ | --------------------------------- |
| Model learns from training examples              | Model generates output            |
| Target tokens are available for calculating loss | Future tokens are not available   |
| Causal mask prevents future information leakage  | Tokens are generated step by step |
| Many positions can be processed in parallel      | Generation is autoregressive      |
| Loss is calculated                               | Output tokens are selected        |

The same learned parameters are used in both stages.

---

## 38. Decoder and KV Cache

During autoregressive generation, the model repeatedly processes growing context.

Previously calculated **Key and Value** representations can be cached.

```text
Previous Tokens
      ↓
Previous K/V
      ↓
💾 KV Cache
      ↓
Reuse During Next Step
```

The KV cache is an inference optimization.

It stores previous Keys and Values so they do not need to be recomputed from scratch at every generation step.

The exact caching implementation depends on the model and inference system.

---

## 39. Complete Original Transformer Flow

The original Transformer can be summarized as:

```text
                 📝 Input
                    ↓
               📥 Encoder
                    ↓
          📊 Encoder Representations
                    ↓
       ┌───────────────────────────┐
       │          Decoder          │
       │                           │
       │ 🎭 Masked Self-Attention │
       │          ↓                │
       │ 🔗 Cross-Attention       │
       │          ↓                │
       │ 🧠 Feed-Forward Network  │
       └────────────┬──────────────┘
                    ↓
             📊 Output
                    ↓
              🎯 LM Head
                    ↓
                📈 Logits
                    ↓
              🔤 Next Token
```

---

## 40. Complete Decoder-Only LLM Flow

A GPT-style decoder-only LLM can be simplified as:

```text
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
🔄 Decoder Block 1
      ↓
🔄 Decoder Block 2
      ↓
🔄 Decoder Block 3
      ↓
        ...
      ↓
🔄 Decoder Block N
      ↓
📊 Final Representation
      ↓
🎯 Language Modeling Head
      ↓
📈 Logits
      ↓
🎲 Probability Distribution
      ↓
🔤 Next Token
      ↓
🔄 Repeat
```

---

## 41. Simple Numerical Example

Suppose a model receives:

```text
"The cat"
```

The tokenizer converts it into Token IDs:

```text
"The" → 125
"cat" → 842
```

The IDs are converted into embeddings.

```text
[125, 842]
     ↓
Embedding Vectors
```

The Decoder processes these representations.

The output layer produces vocabulary logits.

Suppose the model produces:

```text
"runs"   → high score
"sleeps" → medium score
"blue"   → low score
```

The generation system selects a token such as:

```text
"runs"
```

The context becomes:

```text
"The cat runs"
```

The process repeats.

---

## 42. What Happens Inside a Decoder?

At a high level:

```text
Input Representations
        ↓
Masked Self-Attention
        ↓
Use Previous Allowed Context
        ↓
Cross-Attention
        ↓
Use Encoder Information
        ↓
Feed-Forward Network
        ↓
Refine Representations
        ↓
Next Decoder Block
        ↓
Repeat
        ↓
Final Representation
```

For decoder-only LLMs, the cross-attention step is not present because there is no separate Encoder.

---

## 43. Decoder and Sequence Generation

The Decoder is especially important for autoregressive generation.

```text
Prompt
  ↓
Decoder
  ↓
Token 1
  ↓
Prompt + Token 1
  ↓
Decoder
  ↓
Token 2
  ↓
Prompt + Token 1 + Token 2
  ↓
Decoder
  ↓
Token 3
  ↓
Repeat
```

This is how a decoder-only language model can generate a sequence token by token.

---

## 44. Decoder Does Not Directly Produce Words

The Decoder does not directly output human-readable words.

Its final representations are converted into vocabulary logits.

```text
Decoder
  ↓
Hidden Representation
  ↓
Output Projection
  ↓
Logits
  ↓
Probabilities
  ↓
Token ID
  ↓
Token
  ↓
Text
```

So the Decoder and tokenizer work together as different parts of the complete system.

---

## 45. Decoder and Token Embeddings

Token embeddings are the initial numerical representation of tokens.

The Decoder transforms these representations through multiple blocks.

```text
Token
  ↓
Token ID
  ↓
Token Embedding
  ↓
Decoder Blocks
  ↓
Contextual Representation
```

Therefore:

```text
Token Embedding
      ≠
Decoder Representation
```

The representation changes as it passes through the Decoder.

---

## 46. Decoder and Context

The Decoder uses the available context to produce the next-token prediction.

For example:

```text
"The weather today is"
```

The Decoder processes the available tokens and produces a representation for the current prediction position.

The output layer then assigns scores to possible next tokens.

```text
"The weather today is"
              ↓
           Decoder
              ↓
            Logits
              ↓
       Possible Tokens
              ↓
            "sunny"
```

The model can then continue generating.

---

## 47. Decoder Does Not Mean Human-Like Understanding

The word **Decoder** can be misleading.

It does not mean that the model literally “understands” information in the same way a human does.

It refers to an architectural component that transforms representations and, in generative settings, helps produce output sequences.

Similarly:

```text
Attention
```

does not mean human attention.

These are names for computational mechanisms.

---

## 48. Important Difference: Original Decoder vs Modern Decoder-Only LLM

This distinction is important.

### Original Transformer Decoder

```text
Masked Self-Attention
        +
Cross-Attention
        +
Feed-Forward Network
```

### Decoder-Only LLM

```text
Causal Self-Attention
        +
Feed-Forward Network
        +
Repeated Transformer Blocks
```

Therefore, when learning GPT-style LLMs, the Decoder concept should not be assumed to include cross-attention.

---

## 49. Complete Decoder Architecture

```text
                    📥 Decoder Input
                          ↓
                 🧩 Token Embeddings
                          +
                  📍 Positional Info
                          ↓
                ┌──────────────────┐
                │  Decoder Block 1 │
                │                  │
                │ 🎭 Causal /      │
                │    Masked Self-  │
                │    Attention     │
                │        ↓         │
                │ 🔗 Cross-Attn    │
                │        ↓         │
                │ 🧠 FFN           │
                └────────┬─────────┘
                         ↓
                ┌──────────────────┐
                │  Decoder Block 2 │
                └────────┬─────────┘
                         ↓
                        ...
                         ↓
                ┌──────────────────┐
                │  Decoder Block N │
                └────────┬─────────┘
                         ↓
                 📊 Final Representation
                         ↓
                    🎯 Output Layer
                         ↓
                     📈 Logits
                         ↓
                 🎲 Probabilities
                         ↓
                    🔤 Next Token
```

For a decoder-only LLM, remove the separate Encoder and cross-attention pathway.

---

## 50. Simple Mental Model

Think of the Decoder as a **generation engine inside the Transformer architecture**.

```text
📝 Available Context
        ↓
📤 Decoder
        ↓
👀 Look at Allowed Previous Context
        ↓
🔗 Combine Relevant Information
        ↓
🧠 Transform Representations
        ↓
🎯 Predict Next Token
        ↓
🔄 Repeat
```

For the original Transformer:

```text
Encoder → provides input information
Decoder → uses it to generate output
```

For GPT-style LLMs:

```text
Decoder-Only Transformer
        ↓
Next-Token Prediction
        ↓
Autoregressive Generation
```

---

## 51. Key Takeaways

* 📤 A **Decoder** is a major component of the original Transformer architecture.
* 🏗️ The original Transformer uses an **Encoder-Decoder** architecture.
* 🎭 The Decoder uses **masked/causal self-attention** to prevent access to future output tokens.
* 🔗 The original Decoder also uses **cross-attention** to access Encoder representations.
* 🧠 The Decoder contains Transformer blocks with attention, FFNs, residual connections, and normalization.
* 🔄 Multiple Decoder blocks are stacked together.
* 🎯 The final Decoder representation is mapped to vocabulary logits by an output layer or language modeling head.
* 🔤 The model can use those logits to predict the next token.
* 🔁 Autoregressive generation repeatedly predicts and adds new tokens.
* 🚀 GPT-style LLMs use a **decoder-only Transformer** rather than the complete original Encoder-Decoder architecture.
* 💾 KV caching can speed up autoregressive inference by reusing previously computed Keys and Values.
* ⚠️ The exact Decoder architecture varies across Transformer models.
* 🧠 A Decoder is an architectural component; an LLM is a trained language model.
