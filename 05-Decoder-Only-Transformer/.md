# 📚 Stacking Transformer Blocks

## 📌 Introduction

A decoder-only LLM does not use just one Transformer Block.

Instead, it **stacks many Transformer Blocks one after another**.

The output of one block becomes the input to the next block.

The basic idea is:

```text id="4j7k2m"
Input Representation
        ↓
Transformer Block 1
        ↓
Transformer Block 2
        ↓
Transformer Block 3
        ↓
       ...
        ↓
Transformer Block N
        ↓
Final Hidden States
        ↓
Language Model Head
        ↓
Logits
        ↓
Next Token
```

Stacking blocks allows the model to repeatedly transform the token representations before making a prediction.

---

# 1. 🧱 What Does "Stacking" Mean?

**Stacking Transformer Blocks** simply means placing multiple Transformer Blocks sequentially.

For example:

```text id="p8r3xq"
Block 1
   ↓
Block 2
   ↓
Block 3
   ↓
Block 4
```

The output from Block 1 is passed to Block 2.

The output from Block 2 is passed to Block 3.

And so on.

This creates a deep Transformer network.

---

# 2. 🧠 Why Use Multiple Blocks?

A single Transformer Block can perform useful transformations, but an LLM needs to learn much more complex patterns.

Instead of trying to perform everything in one block:

```text id="v5m8qz"
Input
  ↓
One Block
  ↓
Output
```

the model performs repeated transformations:

```text id="x2c7kn"
Input
  ↓
Block 1
  ↓
Block 2
  ↓
Block 3
  ↓
Block 4
  ↓
...
  ↓
Block N
```

Each block receives the representations produced by the previous block.

---

# 3. 🔄 Output of One Block → Input of Next Block

This is the most important idea.

Suppose the first block receives:

```text id="y4n8cp"
H₀
```

It produces:

```text id="q7m2vx"
H₁
```

Then:

```text id="z5r9kd"
H₁
```

becomes the input to the second block.

Mathematically:

```text id="b8w4ns"
H₁ = Block₁(H₀)

H₂ = Block₂(H₁)

H₃ = Block₃(H₂)
```

And so on:

```text id="m6p3qa"
Hₙ = Blockₙ(Hₙ₋₁)
```

So the complete stack can be viewed as a sequence of transformations.

---

# 4. 🗺️ Basic Architecture

A simplified decoder-only LLM looks like:

```text id="t3x9vw"
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
          ┌─────────────────────┐
          │ Transformer Block 1 │
          └─────────────────────┘
                     ↓
          ┌─────────────────────┐
          │ Transformer Block 2 │
          └─────────────────────┘
                     ↓
          ┌─────────────────────┐
          │ Transformer Block 3 │
          └─────────────────────┘
                     ↓
                    ...
                     ↓
          ┌─────────────────────┐
          │ Transformer Block N │
          └─────────────────────┘
                     ↓
             Final Hidden States
                     ↓
              Language Model Head
                     ↓
                   Logits
                     ↓
              Next Token
```

---

# 5. 📐 Representation Shape

Suppose the input has:

```text id="k7v2mb"
Batch Size = 2
Sequence Length = 128
Hidden Dimension = 768
```

The input representation has shape:

```text id="r4c9xz"
[2, 128, 768]
```

After Block 1:

```text id="p6m3qw"
[2, 128, 768]
```

After Block 2:

```text id="h8n5sd"
[2, 128, 768]
```

After Block 3:

```text id="y9x4kc"
[2, 128, 768]
```

The same general shape is maintained through the stack.

The exact dimensions depend on the model.

---

# 6. 🔢 Example With Three Blocks

Suppose we have three Transformer Blocks.

```text id="n8q4mv"
Input
  ↓
H₀
  ↓
Block 1
  ↓
H₁
  ↓
Block 2
  ↓
H₂
  ↓
Block 3
  ↓
H₃
```

Where:

```text id="q5w8zr"
H₀ = Initial Representation
H₁ = Output of Block 1
H₂ = Output of Block 2
H₃ = Output of Block 3
```

The final representation is:

```text id="c3m7xy"
H₃
```

It can then be passed to the language model head.

---

# 7. 🔍 What Happens Inside Every Block?

Each Transformer Block performs several operations.

A simplified decoder-only block is:

```text id="f6r2wp"
Input
  ↓
Causal Self-Attention
  ↓
Residual Connection
  ↓
Normalization
  ↓
Feed-Forward Network
  ↓
Residual Connection
  ↓
Normalization
  ↓
Output
```

Therefore, stacking blocks means repeatedly applying this type of processing.

```text id="w4k9ns"
Input
  ↓
[Attention + FFN]
  ↓
[Attention + FFN]
  ↓
[Attention + FFN]
  ↓
...
```

The exact ordering of normalization and residual operations can vary across architectures.

---

# 8. 👀 Attention Across the Stack

Every decoder block contains causal self-attention.

This means every block can process information from the allowed context.

For example:

```text id="x9p5vz"
The cat is sleeping
```

At each layer, the token representations can interact through causal attention.

```text id="b2m7qc"
Block 1
  ↓
Initial contextual processing

Block 2
  ↓
Further contextual processing

Block 3
  ↓
Further contextual processing

...
```

The model repeatedly updates the representations.

---

# 9. 🎭 Causal Masking Is Used in Every Block

In a decoder-only LLM, causal masking is generally applied to the self-attention operation in every Transformer block.

For example:

```text id="h7s3km"
          The Cat Is Sleeping
The       ✓   ✗  ✗    ✗
Cat       ✓   ✓  ✗    ✗
Is        ✓   ✓  ✓    ✗
Sleeping  ✓   ✓  ✓    ✓
```

The restriction remains throughout the stack.

A later Transformer block does not suddenly gain access to future tokens.

---

# 10. 🧠 Do Blocks Have Different Parameters?

Yes.

Each Transformer Block generally has its **own learned parameters**.

For example:

```text id="v8q2rm"
Block 1 → Parameters 1
Block 2 → Parameters 2
Block 3 → Parameters 3
```

They have similar architectural structure, but they are not simply copies sharing the same weights.

Conceptually:

```text id="x5n9wb"
Block 1
Attention₁
FFN₁

Block 2
Attention₂
FFN₂

Block 3
Attention₃
FFN₃
```

The parameters are learned during training.

---

# 11. 🧩 Same Structure, Different Learned Parameters

The blocks usually follow the same general design:

```text id="m4y7kp"
Attention
   ↓
FFN
```

But each block can have different learned weights.

For example:

```text id="q8w3zn"
Block 1 → W₁
Block 2 → W₂
Block 3 → W₃
```

This allows different layers to perform different learned transformations.

---

# 12. 🔄 Representations Become More Contextual

Consider:

```text id="s6c2mx"
"The bank is near the river."
```

The representation of `bank` is influenced by its surrounding context.

As the representation moves through multiple Transformer blocks:

```text id="z4n8qw"
Token Embedding
      ↓
Block 1
      ↓
Updated Representation
      ↓
Block 2
      ↓
Further Updated Representation
      ↓
Block 3
      ↓
Further Updated Representation
      ↓
...
```

The representation is repeatedly transformed using information from the context.

It is better to think of the model as progressively transforming representations rather than assigning one fixed human-readable meaning at each layer.

---

# 13. 🏗️ Depth of the Model

The number of Transformer Blocks is an important part of model architecture.

For example, a hypothetical model could have:

```text id="d5q8mx"
12 Blocks
```

Another model could have:

```text id="j3w7pc"
24 Blocks
```

Another could have:

```text id="r9k4vz"
48 Blocks
```

The exact number varies between models.

More blocks means the network is **deeper**, but deeper does not automatically mean better in every situation.

Model quality depends on many factors, including:

* Architecture
* Data
* Parameter count
* Training procedure
* Compute
* Optimization
* Model size
* Data quality

---

# 14. 📊 Hidden Dimension Usually Stays Consistent

A Transformer stack usually maintains a fixed model hidden dimension.

For example:

```text id="k8m2xp"
Block 1 → [B, N, 768]
Block 2 → [B, N, 768]
Block 3 → [B, N, 768]
...
Block N → [B, N, 768]
```

Here:

```text id="f5x9qc"
B = Batch Size
N = Sequence Length
768 = Hidden Dimension
```

The exact hidden dimension depends on the model.

---

# 15. 🔀 Internal Dimensions Can Change

Although the main representation dimension often stays constant, some operations inside a block temporarily change dimensions.

For example, an FFN might do:

```text id="w6p3rz"
768
 ↓
3072
 ↓
768
```

So:

```text id="a9k5qm"
Block Input
[Batch, Sequence, 768]

        ↓

FFN internal representation
[Batch, Sequence, 3072]

        ↓

Block Output
[Batch, Sequence, 768]
```

The numbers are only illustrative.

---

# 16. 🧠 Why Not Make One Huge Block?

Instead of:

```text id="c7x2np"
One extremely large block
```

the architecture uses multiple blocks:

```text id="m5q8vz"
Block 1
Block 2
Block 3
...
Block N
```

This creates a deep neural network where each layer performs another learned transformation.

Depth is a fundamental part of the model's capacity.

---

# 17. 📚 Stacking and Hierarchical Processing

A useful conceptual view is:

```text id="y3w7kc"
Initial Representation
        ↓
   Block 1
        ↓
Basic contextual transformations
        ↓
   Block 2
        ↓
More transformations
        ↓
   Block 3
        ↓
More transformations
        ↓
      ...
        ↓
   Block N
        ↓
Final representation
```

However, we should not assume that each block has one specific human-defined job.

The model learns distributed representations and transformations across its layers.

---

# 18. 🧠 What Does "Deeper" Mean?

If a model has more Transformer Blocks, it has greater **depth**.

For example:

```text id="u4n7px"
Model A:

Block 1
Block 2
Block 3
Block 4
```

has fewer layers than:

```text id="e8q2mv"
Model B:

Block 1
Block 2
Block 3
...
Block 24
```

Model B is deeper in terms of Transformer layers.

But:

```text id="r6m9kw"
More Blocks ≠ Automatically Better Model
```

Other factors matter too.

---

# 19. 🔗 Complete Flow From Input to Output

The full flow is:

```text id="h2v8qm"
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
          ┌─────────────────────┐
          │ Transformer Block 1 │
          └─────────────────────┘
                     ↓
          ┌─────────────────────┐
          │ Transformer Block 2 │
          └─────────────────────┘
                     ↓
          ┌─────────────────────┐
          │ Transformer Block 3 │
          └─────────────────────┘
                     ↓
                    ...
                     ↓
          ┌─────────────────────┐
          │ Transformer Block N │
          └─────────────────────┘
                     ↓
             Final Hidden States
                     ↓
              Language Model Head
                     ↓
                   Logits
                     ↓
             Probability Distribution
                     ↓
                Next Token
```

---

# 20. 🏋️ Stacking During Training

During training, the entire stack participates in learning.

The flow is:

```text id="x6r3np"
Training Data
     ↓
Tokenization
     ↓
Input / Target Sequences
     ↓
Embeddings
     ↓
Transformer Block 1
     ↓
Transformer Block 2
     ↓
...
     ↓
Transformer Block N
     ↓
Logits
     ↓
Loss
     ↓
Backpropagation
     ↓
Parameter Updates
```

The loss provides a training signal that propagates backward through the entire stack.

---

# 21. 🔙 Backpropagation Through All Blocks

Suppose the model contains:

```text id="q7m3xb"
Block 1
Block 2
Block 3
```

During backpropagation:

```text id="v8k5rz"
Loss
 ↓
Block 3
 ↓
Block 2
 ↓
Block 1
 ↓
Earlier Layers
```

The gradients are used to update the learned parameters throughout the network.

Therefore, the blocks are trained together as one model.

---

# 22. 🚀 Stacking During Inference

During inference, the model uses the learned parameters.

The input passes through the entire stack:

```text id="s5x9qm"
Prompt
  ↓
Embeddings
  ↓
Block 1
  ↓
Block 2
  ↓
...
  ↓
Block N
  ↓
Logits
  ↓
Next Token
```

When another token is generated, the process continues autoregressively.

---

# 23. ⚡ KV Cache Across Stacked Blocks

During autoregressive generation, KV caching is maintained for the attention layers.

Importantly, each Transformer Block has its own attention computation and therefore its own cached K/V states.

Conceptually:

```text id="n4w7pz"
Block 1 → K/V Cache 1
Block 2 → K/V Cache 2
Block 3 → K/V Cache 3
...
Block N → K/V Cache N
```

When a new token is generated, cached keys and values can be reused at each layer.

This helps make autoregressive generation more efficient.

---

# 24. 🧮 A Simple Mathematical View

Let the initial representation be:

```text id="p8m4xc"
H₀
```

Each Transformer Block applies a learned function.

For Block 1:

```text id="q2v7zn"
H₁ = Block₁(H₀)
```

For Block 2:

```text id="k5x8mw"
H₂ = Block₂(H₁)
```

For Block 3:

```text id="r4n9qp"
H₃ = Block₃(H₂)
```

Therefore:

```text id="z6w3mc"
Hₙ = Blockₙ(Blockₙ₋₁(...Block₂(Block₁(H₀))...))
```

The final representation is:

```text id="y7q2vx"
Hₙ
```

which is then used by the output layer.

---

# 25. 🔢 Example With Four Blocks

Suppose:

```text id="c8m5zr"
Input:
"The cat is"
```

After tokenization and embedding:

```text id="w4x7np"
H₀
```

Then:

```text id="s2q9km"
H₀
 ↓
Block 1
 ↓
H₁
 ↓
Block 2
 ↓
H₂
 ↓
Block 3
 ↓
H₃
 ↓
Block 4
 ↓
H₄
```

Finally:

```text id="f6v3qx"
H₄
 ↓
Language Model Head
 ↓
Logits
 ↓
Probability Distribution
 ↓
Next Token
```

---

# 26. 🎯 Stacking Does Not Mean Repeating the Same Calculation Exactly

The blocks have a similar overall structure, but they do not perform the exact same computation.

For example:

```text id="n8w4yp"
Block 1
Attention₁ + FFN₁

Block 2
Attention₂ + FFN₂

Block 3
Attention₃ + FFN₃
```

The parameters are different.

Therefore, each block can learn a different transformation of the representations.

---

# 27. 🧩 Block Parameters

A Transformer Block can contain parameters associated with:

### Attention

```text id="v7x2mq"
WQ
WK
WV
WO
```

### Feed-Forward Network

```text id="r3n8kp"
W₁
W₂
```

and corresponding biases or gating parameters depending on the architecture.

### Normalization

Normalization layers may also contain learned parameters.

The exact parameterization varies between models.

---

# 28. 📈 Parameter Count and Stacking

If one Transformer Block contains many parameters, stacking many blocks can create a model with a very large number of parameters.

Conceptually:

```text id="q9m4vx"
Parameters in Block 1
+
Parameters in Block 2
+
Parameters in Block 3
+
...
+
Parameters in Block N
+
Other Model Parameters
=
Total Model Parameters
```

This is one reason large LLMs can contain billions of learned parameters.

The exact total depends on the architecture and parameter-sharing choices.

---

# 29. 🧠 Stacking vs Context Window

These two concepts should not be confused.

### Transformer Blocks

Control the **depth** of the network.

```text id="c5r8mz"
Block 1
Block 2
...
Block N
```

### Context Window

Controls how many tokens can be processed as context within the model's supported sequence length.

```text id="x3w7qp"
Token 1
Token 2
Token 3
...
Token N
```

So:

```text id="m8k2vy"
More Blocks ≠ Larger Context Window
```

They are different architectural concepts.

---

# 30. 🆚 Depth vs Sequence Length

Another useful distinction:

| Concept           | Meaning                                      |
| ----------------- | -------------------------------------------- |
| Transformer depth | Number of Transformer Blocks                 |
| Sequence length   | Number of tokens in a sequence               |
| Hidden dimension  | Size of each token representation            |
| Batch size        | Number of sequences processed together       |
| Vocabulary size   | Number of tokens in the tokenizer vocabulary |

For example:

```text id="p7v4nx"
Model:

Blocks       = 24
Sequence     = 2048 tokens
Hidden size  = 1024
Batch size   = 8
```

These are separate architectural or runtime dimensions.

---

# 31. 🧠 Simple Analogy

Think of the Transformer stack like a series of processing stages.

```text id="w2m8qy"
Stage 1
  ↓
Stage 2
  ↓
Stage 3
  ↓
Stage 4
  ↓
Final Result
```

Each stage receives the result of the previous stage and performs another transformation.

The analogy is only for understanding the sequential structure; the actual computation is a learned neural network, not a set of manually programmed stages.

---

# 32. ⚠️ Common Misunderstandings

### ❌ "All blocks share the same weights."

Usually no.

Each block generally has its own learned parameters.

---

### ❌ "Every block has a completely different architecture."

Usually no.

They generally follow the same broad Transformer Block design, while their parameters and sometimes specific implementation details differ.

---

### ❌ "More blocks automatically means better."

No.

Model quality depends on many factors, including architecture, data, training, optimization, and compute.

---

### ❌ "Stacking blocks increases the number of tokens."

No.

The number of tokens is determined by the sequence.

Stacking increases the network's depth.

---

### ❌ "Every layer sees the whole future sequence."

No.

In decoder-only models, causal masking prevents future-token access in self-attention.

---

### ❌ "The first block predicts the first token and the second block predicts the second token."

No.

The Transformer blocks are layers of representation processing.

The final output layer produces the prediction logits.

---

# 33. 🗺️ Complete Mental Model

The entire concept can be remembered as:

```text id="d8q4mx"
             Input Tokens
                  ↓
          Initial Representation
                  ↓
        ┌─────────────────┐
        │   Block 1       │
        │ Attention + FFN │
        └─────────────────┘
                  ↓
        ┌─────────────────┐
        │   Block 2       │
        │ Attention + FFN │
        └─────────────────┘
                  ↓
        ┌─────────────────┐
        │   Block 3       │
        │ Attention + FFN │
        └─────────────────┘
                  ↓
                 ...
                  ↓
        ┌─────────────────┐
        │   Block N       │
        │ Attention + FFN │
        └─────────────────┘
                  ↓
          Final Representation
                  ↓
             Output Layer
                  ↓
              Next Token
```

---

# 34. 🔗 Where Stacking Fits in the Complete LLM

The complete pipeline is:

```text id="k6m2wp"
Raw Text
   ↓
Tokenization
   ↓
Token IDs
   ↓
Token Embeddings
   ↓
Positional Information
   ↓
────────────────────────────
   Transformer Stack
────────────────────────────
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
────────────────────────────
   ↓
Final Hidden States
   ↓
Language Model Head
   ↓
Logits
   ↓
Probability Distribution
   ↓
Next Token
```

The **Transformer Stack** is the collection of all Transformer Blocks.

---

# 35. 🧠 One-Line Definition

> **Stacking Transformer Blocks means placing multiple Transformer Blocks sequentially so that the output representation of one block becomes the input to the next, creating the deep Transformer network used inside an LLM.**

---

# 36. 🎯 Key Takeaways

* 📚 An LLM contains many Transformer Blocks stacked together.
* 🔄 The output of one block becomes the input of the next.
* 🧱 Each block contains attention, FFN, residual connections, and normalization in an architecture-dependent arrangement.
* 👀 Decoder-only LLMs use causal self-attention in these blocks.
* 🎭 Causal masking prevents future-token information from being used.
* 🔑 Each block generally has its own learned parameters.
* 📐 The main hidden representation shape is usually preserved across blocks.
* 📈 More blocks increase model depth, but more depth alone does not guarantee better performance.
* 🧠 Representations are repeatedly transformed as they move through the stack.
* 🏋️ During training, gradients flow through the entire stack.
* 🚀 During inference, the same learned blocks transform the prompt and generated tokens.
* ⚡ KV caching can store attention K/V states separately for each block during autoregressive generation.
* 🔗 The final block produces representations that are passed to the language model head.

The core idea is:

```text id="r5n9xw"
Initial Representation
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
Final Representation
        ↓
Next-Token Prediction
```

**Many Transformer Blocks → One Transformer Stack → Final Representation → Next-Token Prediction**
