# 🧠 Feed-Forward Network

A **Feed-Forward Network (FFN)** is one of the main components inside a Transformer Block.

After attention allows tokens to exchange information, the Feed-Forward Network performs additional transformations on the representation of **each token position**.

A simple way to remember the difference is:

> 👀 **Attention mixes information between tokens.**
> 🧠 **FFN transforms the information at each token position.**

---

# 1. What Is a Feed-Forward Network?

A Feed-Forward Network is a small neural network inside a Transformer Block.

Its simplified structure is:

```text id="ifxogl"
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

In a Transformer, the FFN is applied to the representations produced by the attention part of the block.

---

# 2. Why Do We Need an FFN?

Attention is very good at allowing tokens to exchange information.

For example:

```text id="m5d8vk"
"The cat sat on the mat"
```

Attention can help a token representation incorporate information from other relevant tokens.

But the Transformer also needs a component that can **transform and process the resulting features**.

That is one of the main jobs of the FFN.

Simplified:

```text id="l5d4mc"
👀 Attention
     ↓
Mix information between tokens
     ↓
🧠 Feed-Forward Network
     ↓
Transform the features
```

---

# 3. Where Does the FFN Appear?

A simplified Transformer Block looks like:

```text id="f8sl7v"
📊 Input Representation
          ↓
👀 Self-Attention
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
📊 Output Representation
```

The exact ordering of attention, normalization, and residual connections can vary between Transformer architectures.

The important idea is that the FFN is a major component of the Transformer Block.

---

# 4. Basic Structure of an FFN

A simple Feed-Forward Network can be represented as:

```text id="2d8qwm"
Input
  ↓
Linear Layer
  ↓
Activation Function
  ↓
Linear Layer
  ↓
Output
```

Mathematically, a basic version can be written as:

```text id="0bjmbu"
FFN(x) = W₂ σ(W₁x + b₁) + b₂
```

where:

```text id="1k4c8p"
x  → Input
W₁ → First learned weight matrix
b₁ → First bias
σ  → Activation function
W₂ → Second learned weight matrix
b₂ → Second bias
```

This is a simplified standard FFN formulation.

Modern Transformer architectures can use different FFN variants.

---

# 5. The First Linear Transformation

The first linear layer transforms the input representation.

Simplified:

```text id="y9x3q7"
Input
  ↓
Linear Transformation
  ↓
Expanded Representation
```

A linear transformation can be written as:

```text id="2s4m6a"
y = xW + b
```

The model learns the weights during training.

These learned weights determine how the input features are transformed.

---

# 6. Why Does the FFN Expand the Dimension?

A common Transformer design expands the feature dimension inside the FFN.

For example:

```text id="7k2m1p"
Input Dimension
      ↓
     768
      ↓
FFN Hidden Dimension
      ↓
    3072
      ↓
Output Dimension
      ↓
     768
```

So conceptually:

```text id="n4s8xq"
768 → 3072 → 768
```

This is an illustrative example.

The exact dimensions vary between models.

---

# 7. Why Expand and Then Compress?

The expansion gives the FFN a larger intermediate feature space in which to perform transformations.

Conceptually:

```text id="z2k7pf"
📊 Input Features
       ↓
  Expand Features
       ↓
🧠 Larger Feature Space
       ↓
Transform Features
       ↓
  Compress Features
       ↓
📊 Output Features
```

The model can therefore perform more expressive nonlinear transformations before returning to the model's original dimension.

---

# 8. Activation Function

An activation function is placed between the two linear transformations.

For example:

```text id="q8m3yd"
Input
  ↓
Linear
  ↓
GELU
  ↓
Linear
  ↓
Output
```

The activation introduces nonlinearity.

Without a nonlinear activation, multiple linear transformations would still behave like a single linear transformation.

Therefore:

```text id="j4n6sc"
Linear
   +
Activation
   +
Linear
   ↓
Nonlinear Transformation
```

---

# 9. GELU

One activation function commonly used in Transformer architectures is **GELU**.

GELU stands for:

> **Gaussian Error Linear Unit**

A simplified FFN using GELU looks like:

```text id="g5x8qa"
Input
  ↓
Linear
  ↓
GELU
  ↓
Linear
  ↓
Output
```

The exact activation function depends on the model architecture.

Modern models may use alternatives such as:

* GELU
* SiLU / Swish
* Gated variants such as SwiGLU

So not every Transformer uses the same FFN activation.

---

# 10. FFN Is Applied to Each Token Position

This is one of the most important ideas.

Suppose the sequence contains:

```text id="x7p3dm"
The   cat   is   sleeping
```

After attention, each position has a representation:

```text id="k5r8qw"
Token 1 → Representation 1
Token 2 → Representation 2
Token 3 → Representation 3
Token 4 → Representation 4
```

The FFN processes these positions.

Conceptually:

```text id="a4n7vz"
Representation 1 → FFN → Output 1
Representation 2 → FFN → Output 2
Representation 3 → FFN → Output 3
Representation 4 → FFN → Output 4
```

The same FFN parameters are generally applied across token positions within that Transformer layer.

---

# 11. Attention vs FFN

This distinction is extremely important.

### Attention

Attention allows information to move between token positions.

```text id="u8k3yp"
Token 1 ─┐
Token 2 ─┼──→ Attention ──→ Updated representations
Token 3 ─┤
Token 4 ─┘
```

### FFN

The FFN transforms the representation at each position.

```text id="q6w2sa"
Token 1 → FFN → Output 1
Token 2 → FFN → Output 2
Token 3 → FFN → Output 3
Token 4 → FFN → Output 4
```

A useful mental model is:

```text id="b8f4n1"
👀 Attention
→ "Which information from other tokens should contribute?"

🧠 FFN
→ "How should the current representation be transformed?"
```

This is a conceptual explanation rather than a literal description of what the model "thinks."

---

# 12. FFN Input Comes From Attention

In a Transformer Block, the FFN generally receives the representation after the attention sublayer and its associated residual/normalization operations.

Simplified:

```text id="n2s7kd"
Input
  ↓
Attention
  ↓
Updated Representation
  ↓
FFN
  ↓
Further Transformed Representation
```

Therefore:

```text id="r9x4mp"
Attention → Information Mixing
FFN       → Feature Transformation
```

Both work together.

---

# 13. Sequence Length Does Not Change

Suppose the input contains:

```text id="x0p9wq"
10 tokens
```

The FFN does not normally change the number of token positions.

For example:

```text id="j7d4sc"
Input:

[10 tokens × 768 features]

        ↓
       FFN

Output:

[10 tokens × 768 features]
```

The intermediate FFN representation may have a larger feature dimension:

```text id="c6v2ak"
10 × 768
    ↓
10 × 3072
    ↓
10 × 768
```

The sequence length remains:

```text id="3p7q1m"
10
```

---

# 14. FFN Dimensions

Suppose:

```text id="b7n3vx"
Sequence Length = 5
Model Dimension = 768
```

The input can be represented conceptually as:

```text id="d2w9ks"
5 × 768
```

The FFN may expand it:

```text id="s4x8mc"
5 × 768
    ↓
5 × 3072
```

Then project it back:

```text id="p6k2za"
5 × 3072
    ↓
5 × 768
```

Therefore:

```text id="n8f3qw"
Sequence Length
      ↓
stays the same

Feature Dimension
      ↓
expands and returns
```

The exact dimensions depend on the model.

---

# 15. A Simple Numerical Example

Suppose a token representation contains three features:

```text id="m2x8vq"
x = [2, 1, 3]
```

A linear layer transforms it:

```text id="e7k3rp"
x
 ↓
Linear Transformation
 ↓
[4, 2, 5]
```

Then an activation function is applied:

```text id="r3w8cz"
[4, 2, 5]
      ↓
   Activation
      ↓
[...]
```

Then another linear transformation produces:

```text id="h4p7ym"
[...]
 ↓
Linear
 ↓
New Representation
```

The numbers here are only illustrative.

The actual model uses learned weight matrices and activation functions.

---

# 16. FFN Parameters Are Learned

The FFN contains learned parameters.

For a simple FFN:

```text id="v7q2nx"
W₁
b₁
W₂
b₂
```

During training:

```text id="a1m8sc"
Training Data
      ↓
Transformer
      ↓
FFN
      ↓
Prediction
      ↓
Loss
      ↓
Backpropagation
      ↓
Parameter Updates
```

The optimizer updates the FFN parameters so that the model becomes better at its training objective.

---

# 17. FFN During Inference

During inference, the FFN uses the learned parameters.

For example:

```text id="q3n6wb"
Input Representation
       ↓
Attention
       ↓
FFN
       ↓
Transformer Output
       ↓
Prediction
```

There is no parameter update during normal inference.

The model is using the parameters learned during training.

---

# 18. FFN Inside Multiple Transformer Blocks

An LLM does not normally contain just one Transformer Block.

It may contain many stacked blocks.

Conceptually:

```text id="r7m3qx"
Input
  ↓
🔄 Transformer Block 1
  ↓
🔄 Transformer Block 2
  ↓
🔄 Transformer Block 3
  ↓
...
  ↓
🔄 Transformer Block N
  ↓
Final Representation
```

Each block has its own learned parameters.

Therefore, each block generally contains its own attention and FFN components.

---

# 19. FFN Across Different Layers

Different Transformer layers can learn different transformations.

For example:

```text id="c8q2vk"
Block 1
  ↓
FFN 1

Block 2
  ↓
FFN 2

Block 3
  ↓
FFN 3

...

Block N
  ↓
FFN N
```

The FFNs are not all the same.

Each Transformer layer has its own learned parameters.

This allows different layers to transform representations differently.

---

# 20. Standard FFN vs Gated FFN

The simple FFN is often represented as:

```text id="z7x4pc"
Input
  ↓
Linear
  ↓
Activation
  ↓
Linear
  ↓
Output
```

Modern Transformer architectures can use **gated FFN variants**.

For example:

```text id="y2m8qs"
Input
  ↓
Multiple Projections
  ↓
Gating
  ↓
Nonlinear Transformation
  ↓
Output Projection
```

One important example is **SwiGLU**.

The exact structure varies by model.

Therefore, when learning the basic concept, it is useful to understand the standard two-linear-layer FFN first.

---

# 21. FFN Is Not a Separate Model

A common misunderstanding is:

> "Is the Feed-Forward Network another neural network outside the Transformer?"

No.

It is a component **inside each Transformer Block**.

Conceptually:

```text id="u3x7qp"
🤖 Transformer
      ↓
🔄 Transformer Block
      ↓
┌───────────────────────┐
│ 👀 Attention          │
│                       │
│ 🧠 Feed-Forward       │
│    Network            │
│                       │
│ ➕ Residual Connections│
│ 📏 Layer Normalization│
└───────────────────────┘
```

The FFN is part of the Transformer architecture.

---

# 22. FFN and Residual Connections

The FFN is usually used together with a residual connection.

A simplified structure is:

```text id="v5k1zr"
Input
  ↓
FFN
  ↓
FFN Output
  ↓
➕ Add Original Representation
  ↓
Output
```

Conceptually:

```text id="n4x8pm"
x ───────────────────┐
                     ↓
                     +
                     ↓
FFN(x) ─────────────→ Output
```

This helps the network preserve and transform information across layers.

The exact residual and normalization ordering varies by architecture.

---

# 23. FFN and Layer Normalization

A simplified Transformer Block can contain:

```text id="q9w2ks"
Attention
   ↓
Residual
   ↓
Layer Normalization
   ↓
FFN
   ↓
Residual
   ↓
Layer Normalization
```

Different architectures may use normalization before rather than after these sublayers.

For example, modern Transformer implementations often use **Pre-Norm** designs.

Therefore, the exact ordering should not be treated as universal.

---

# 24. Attention and FFN Work Together

A Transformer Block can be understood at a high level as two major computational stages:

```text id="s6n3yp"
👀 Attention
      ↓
Information from other token positions
      ↓
🧠 Feed-Forward Network
      ↓
Transform the resulting features
```

Together:

```text id="m8r2qw"
Token Relationships
        ↓
      Attention
        ↓
Contextual Information
        ↓
        FFN
        ↓
Transformed Representation
```

This process is repeated across many Transformer Blocks.

---

# 25. FFN and Contextual Representations

The attention mechanism allows a token representation to incorporate information from surrounding tokens.

Then the FFN transforms that representation.

For example:

```text id="e4x7km"
Token Embedding
      ↓
Position Information
      ↓
Attention
      ↓
Contextual Representation
      ↓
FFN
      ↓
Further Transformed Representation
```

After multiple Transformer Blocks, the representation becomes increasingly contextualized.

---

# 26. FFN Does Not Look at Other Token Positions Directly

This is another important distinction.

For a standard position-wise FFN:

```text id="f2q8vc"
Token 1 → FFN → Token 1 Output
Token 2 → FFN → Token 2 Output
Token 3 → FFN → Token 3 Output
```

The FFN applies the same learned transformation independently at each position.

It is the **attention mechanism** that directly mixes information across positions.

So:

```text id="w7x4np"
Attention
→ Across token positions

FFN
→ Within each token representation
```

---

# 27. FFN and Token Relationships

The FFN does not directly calculate:

```text id="s4v9km"
Token A ↔ Token B
```

That is primarily handled by attention.

Instead, after attention has produced a representation containing information from the context, the FFN transforms its features.

Conceptually:

```text id="c8y2pq"
Token A
  ↓
Attention
  ↓
Information from context
  ↓
FFN
  ↓
Transformed Token A Representation
```

---

# 28. FFN and Nonlinearity

The activation function is important because it introduces nonlinearity.

Without an activation:

```text id="k4q7xm"
Linear
  ↓
Linear
```

can be mathematically combined into another linear transformation.

With an activation:

```text id="z6n2pv"
Linear
  ↓
GELU / SiLU / Other Activation
  ↓
Linear
```

the network can represent more complex nonlinear transformations.

This gives the FFN more expressive power.

---

# 29. FFN and Model Parameters

A large Transformer contains many FFN parameters.

For each Transformer Block, the FFN may contain large weight matrices.

For example:

```text id="p3m7xq"
Input Dimension
      ↓
   Large Matrix
      ↓
Expanded Dimension
      ↓
   Large Matrix
      ↓
Output Dimension
```

Because these matrices can be large, FFNs can account for a substantial portion of the parameters in a Transformer model.

The exact parameter distribution depends on the architecture.

---

# 30. FFN in the Complete LLM Architecture

The FFN is one part of a much larger pipeline:

```text id="q6x9wm"
📝 Text
   ↓
🔤 Tokenization
   ↓
🔢 Token IDs
   ↓
🧩 Token Embeddings
   ↓
📍 Positional Information
   ↓
🔄 Transformer Block
   ↓
👀 Multi-Head Attention
   ↓
➕ Residual + Normalization
   ↓
🧠 Feed-Forward Network
   ↓
➕ Residual + Normalization
   ↓
🔄 More Transformer Blocks
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
```

---

# 31. Standard FFN vs Attention

A useful comparison:

| Feature                  | Attention                     | Feed-Forward Network                     |
| ------------------------ | ----------------------------- | ---------------------------------------- |
| Main purpose             | Mix information across tokens | Transform token features                 |
| Uses Q/K/V               | Yes                           | No                                       |
| Looks across positions   | Yes                           | No, in the standard position-wise design |
| Uses activation          | Softmax for attention weights | Nonlinear activation such as GELU/SiLU   |
| Main operation           | Weighted information mixing   | Learned feature transformation           |
| Output sequence length   | Same                          | Same                                     |
| Inside Transformer Block | Yes                           | Yes                                      |

The two components complement each other.

---

# 32. A Complete Transformer Block

A simplified Transformer Block can be represented as:

```text id="k8w3qp"
📊 Input
   ↓
👀 Multi-Head Attention
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
📊 Block Output
```

Remember:

> The exact ordering of residual connections and normalization depends on the Transformer architecture.

---

# 33. Simple Numerical Dimension Example

Suppose:

```text id="a5v7nx"
Model Dimension = 768
FFN Dimension = 3072
```

For one sequence with 4 tokens:

```text id="d7q2mc"
Input
[4 × 768]
     ↓
First Linear Layer
[4 × 3072]
     ↓
Activation
[4 × 3072]
     ↓
Second Linear Layer
[4 × 768]
     ↓
Output
```

Notice:

```text id="j9p4sw"
Sequence Length:
4 → 4 → 4 → 4

Feature Dimension:
768 → 3072 → 3072 → 768
```

The FFN expands the features and then projects them back.

---

# 34. FFN During Autoregressive Generation

During autoregressive generation, the current token representations pass through the Transformer Blocks.

For example:

```text id="w2n7qx"
The cat is
     ↓
Token Representations
     ↓
Attention
     ↓
FFN
     ↓
Transformer Output
     ↓
Language Modeling Head
     ↓
Next Token
```

After generating a token:

```text id="y5m8pc"
The cat is sleeping
```

the process continues for the next token.

The FFN uses the learned parameters; it does not learn new parameters during normal inference.

---

# 35. FFN and Training

During training, the FFN parameters are updated along with the other model parameters.

Simplified:

```text id="u8x3km"
📚 Training Data
       ↓
🔤 Tokens
       ↓
🧩 Representations
       ↓
👀 Attention
       ↓
🧠 FFN
       ↓
🎯 Prediction
       ↓
📉 Loss
       ↓
🔄 Backpropagation
       ↓
⚙️ Update FFN Parameters
```

Therefore, the FFN is part of the learned neural network.

---

# 36. Common Misunderstandings

### ❌ "The FFN is used to connect different tokens."

Not directly.

Attention is responsible for mixing information across token positions.

The standard FFN transforms each position independently.

---

### ❌ "The FFN predicts the next word."

Not directly.

The FFN contributes to the hidden representation.

The language modeling head converts the final representation into vocabulary logits used for next-token prediction.

---

### ❌ "The FFN changes the number of tokens."

Normally, no.

It changes feature dimensions internally while preserving the sequence length.

---

### ❌ "Every Transformer uses the same FFN."

No.

Different architectures can use different FFN dimensions, activation functions, and gated designs.

---

### ❌ "The FFN is the same across every Transformer Block."

No.

Each block generally has its own learned parameters.

---

### ❌ "Attention and FFN do the same thing."

No.

A useful simplified distinction is:

```text id="e7k2mq"
Attention
→ Mixes information across token positions

FFN
→ Transforms features at each token position
```

---

# 37. Complete FFN Flow

The basic FFN process is:

```text id="r3m8qk"
📊 Input Representation
          ↓
🔢 Linear Transformation
          ↓
📈 Expanded Representation
          ↓
⚡ Activation Function
          ↓
📉 Second Linear Transformation
          ↓
📊 Output Representation
```

Inside a Transformer Block:

```text id="v6x2pn"
👀 Attention
      ↓
➕ Residual / Normalization
      ↓
🧠 FFN
      ↓
➕ Residual / Normalization
      ↓
📊 Block Output
```

---

# 38. Simple Mental Model

Think of a Transformer Block as having two major jobs:

```text id="h7q3mx"
👀 Attention
      ↓
"Bring useful information from other tokens."

          +

🧠 Feed-Forward Network
      ↓
"Transform the information at each position."
```

Together:

```text id="p4x8nk"
Token Relationships
        ↓
      Attention
        ↓
Contextual Information
        ↓
        FFN
        ↓
Transformed Features
```

This process is repeated through many Transformer Blocks.

---

# 39. Key Takeaways

* 🧠 **Feed-Forward Network is a major component inside a Transformer Block.**
* 👀 Attention mixes information across token positions.
* 🧠 FFN transforms the representation at each token position.
* 🔢 A basic FFN uses two linear transformations with a nonlinear activation between them.
* 📈 FFNs commonly expand the feature dimension and then project it back.
* 📏 The sequence length normally stays unchanged.
* ⚡ GELU, SiLU, and gated variants such as SwiGLU are examples of FFN designs.
* 🔄 The same FFN parameters are generally applied independently across token positions within a layer.
* ⚙️ FFN parameters are learned during training.
* 🚀 Different Transformer Blocks generally have different FFN parameters.
* 🧩 FFN works together with attention, residual connections, and normalization.
* 🎯 The FFN does not directly produce the next token; it contributes to the representation used by the output layer.
* ⚠️ The exact FFN structure varies between Transformer architectures.

The central idea is:

```text id="k2v7mp"
🧩 Token Representations
        ↓
👀 Attention
        ↓
Information from Other Tokens
        ↓
🧠 Feed-Forward Network
        ↓
Feature Transformation
        ↓
📊 Updated Representations
```

**Feed-Forward Network = a learned nonlinear feature transformation applied to each token position inside a Transformer Block.**
