# ➕ Residual Connections

Residual Connections are an important component of Transformer Blocks.

They provide a **shortcut path** that allows the original input of a layer to be combined with the layer's output.

The basic idea is simple:

```text
Input
  ↓
Layer
  ↓
Layer Output
  ↓
➕ Add Original Input
  ↓
Output
```

Instead of forcing every layer to completely transform the input, the model can learn an **additional transformation** while keeping the original information available.

---

## 1. What Is a Residual Connection?

A residual connection, also called a **skip connection**, passes information around a layer and adds it back to the layer's output.

The basic equation is:

```text
Output = Input + Transformation(Input)
```

For example:

```text
        ┌──────────────────────┐
        │                      │
        │                      ↓
Input ──┼──→ Transformation ──→ ➕ ──→ Output
        │                      ↑
        └──────────────────────┘
```

The shortcut is the **residual connection**.

---

## 2. Why Do We Need Residual Connections?

Transformer models can contain many stacked layers.

For example:

```text
Input
  ↓
Transformer Block 1
  ↓
Transformer Block 2
  ↓
Transformer Block 3
  ↓
...
  ↓
Transformer Block 32
  ↓
Output
```

As the number of layers increases, training a deep neural network becomes more difficult.

Residual connections help information and gradients move through the network more easily.

They make it easier for deeper networks to learn useful transformations.

---

## 3. The Basic Idea

Without a residual connection:

```text
Input
  ↓
Transformation
  ↓
Output
```

The transformation must directly produce the desired output.

With a residual connection:

```text
Input ───────────────────┐
  ↓                      │
Transformation           │
  ↓                      │
Transformation Output ──→➕
                          ↓
                        Output
```

The layer only needs to learn the transformation that should be added to the original input.

This is why residual connections are sometimes described as learning a **residual**.

---

## 4. What Is the Residual?

Suppose the desired transformation is:

```text
Desired Output = Input + Something
```

The `"Something"` is the residual.

So the layer can learn:

```text
Residual = Transformation(Input)
```

Then:

```text
Output = Input + Residual
```

This gives residual connections their name.

---

## 5. Residual Connections in a Transformer

Residual connections are used around major components inside Transformer Blocks.

A simplified Transformer Block looks like:

```text
Input
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
Output
```

The exact order can vary between Transformer architectures.

Some architectures use normalization before the attention/FFN sublayer, while others use it after.

The important idea is that the **attention and FFN transformations have shortcut paths around them**.

---

## 6. Residual Connection Around Attention

Consider the attention part of a Transformer Block.

Simplified:

```text
                 ┌─────────────────────┐
                 │                     │
                 │                     ↓
Input ───────────┼──→ Self-Attention ─→ ➕ ──→ Output
                 │                     ↑
                 └─────────────────────┘
```

Mathematically:

```text
Output = Input + SelfAttention(Input)
```

In an actual Transformer, normalization and other details may appear around this operation depending on the architecture.

---

## 7. Residual Connection Around the FFN

The Feed-Forward Network also has a residual connection.

```text
                 ┌─────────────────────┐
                 │                     │
                 │                     ↓
Input ───────────┼──→ FFN ────────────→ ➕ ──→ Output
                 │                     ↑
                 └─────────────────────┘
```

Simplified:

```text
Output = Input + FFN(Input)
```

Again, the exact normalization order depends on the Transformer architecture.

---

## 8. Residual Connections and Information Flow

A residual connection provides two paths:

```text
                    ┌───────────────┐
                    │               │
                    ↓               │
Input ─────────────→ Transformation │
  │                 ↓               │
  │              New Information    │
  │                 │               │
  └─────────────────┴──────→  ➕ ───┘
                              ↓
                            Output
```

One path carries the existing representation.

The other path produces a transformation.

The two are combined.

---

## 9. Residual Connections Do Not Copy the Input Instead of Processing It

A common misunderstanding is:

> "If there is a shortcut, does the model ignore the Transformer layer?"

No.

Both paths contribute:

```text
Original Information
        +
Transformed Information
        ↓
      Output
```

The transformation can modify the representation while the shortcut preserves access to the previous representation.

---

## 10. Residual Connections Preserve Information

Suppose a representation contains useful information:

```text
Input
 ↓
[Useful Information]
```

A transformation might change the representation.

With a residual connection:

```text
Input ─────────────────────┐
 ↓                         │
Transformation             │
 ↓                         │
New Information ──────────→➕
                            ↓
                       Combined Output
```

The original representation remains available through the shortcut.

This is especially useful when many Transformer Blocks are stacked.

---

## 11. Residual Connections Help Deep Networks

Modern LLMs can contain many Transformer Blocks.

For example:

```text
Input
  ↓
┌─────────────────┐
│ Transformer     │
│ Block 1         │
└─────────────────┘
  ↓
┌─────────────────┐
│ Transformer     │
│ Block 2         │
└─────────────────┘
  ↓
┌─────────────────┐
│ Transformer     │
│ Block 3         │
└─────────────────┘
  ↓
        ...
  ↓
┌─────────────────┐
│ Transformer     │
│ Block N         │
└─────────────────┘
```

Without good information flow, training such deep networks can become difficult.

Residual connections provide shortcut paths through these layers.

---

## 12. Residual Connections and Gradients

Residual connections are also important during training.

Training uses:

```text
Prediction
   ↓
Loss
   ↓
Backpropagation
   ↓
Gradients
   ↓
Parameter Updates
```

The shortcut provides an additional path through which gradients can propagate backward.

Conceptually:

```text
Forward:

Input
  ↓
Transformation
  ↓
Output


Backward:

Gradient
  ↓
┌───────────────┐
│               │
↓               ↓
Transformation  Shortcut
│               │
└───────┬───────┘
        ↓
      Earlier Layer
```

This can make optimization of deep networks easier.

---

## 13. Residual Connections and Vanishing Gradients

Very deep neural networks can suffer from problems where gradients become extremely small as they move backward through many layers.

Residual connections can help reduce this problem by providing shorter paths for gradient flow.

The simplified idea is:

```text
Without shortcut:

Gradient
   ↓
Layer
   ↓
Layer
   ↓
Layer
   ↓
Layer
   ↓
Earlier Layer
```

With shortcuts:

```text
Gradient
   ↓
───────────────┐
↓              │
Layer          │
↓              │
Layer          │
↓              │
Layer          │
└──────────────→ Earlier Layer
```

This is one reason residual connections are useful in very deep networks.

---

## 14. Residual Connections and the Identity Function

Consider:

```text
Output = Input + Transformation(Input)
```

If the transformation learns something close to zero:

```text
Transformation(Input) ≈ 0
```

then:

```text
Output ≈ Input
```

So a layer can approximately preserve the existing representation when a large transformation is not useful.

This provides a useful identity path through the network.

---

## 15. Residual Connections Do Not Change Sequence Length

Residual connections combine representations with the same compatible shape.

For example:

```text
Input:
[Sequence Length × Model Dimension]

Transformation Output:
[Sequence Length × Model Dimension]

        ↓

Addition

        ↓

Output:
[Sequence Length × Model Dimension]
```

The residual connection does not normally change:

* Sequence length
* Number of token positions
* Model dimension

It combines information.

---

## 16. Residual Connections and Token Positions

Suppose the input contains:

```text
"The cat sleeps"
```

After tokenization:

```text
["The", "cat", "sleeps"]
```

The Transformer represents these tokens as vectors.

Conceptually:

```text
The      → Vector
cat      → Vector
sleeps   → Vector
```

After attention:

```text
The      → Updated Vector
cat      → Updated Vector
sleeps   → Updated Vector
```

The residual connection combines the original and transformed representations:

```text
Original Vector
      +
Attention Output
      ↓
Updated Representation
```

This happens across the token positions.

---

## 17. Residual Connections and Attention

Attention allows tokens to exchange information.

For example:

```text
The ───────┐
           ↓
cat ───→ Attention ───→ Updated Representation
           ↑
sleeps ────┘
```

The attention output contains information produced by the attention operation.

The residual connection then combines it with the original input:

```text
Original Representation
          +
Attention Output
          ↓
Updated Representation
```

So:

```text
Attention
   ↓
Information Mixing

Residual Connection
   ↓
Information Preservation + Combination
```

---

## 18. Residual Connections and the Feed-Forward Network

The FFN transforms each token representation independently across positions.

Simplified:

```text
Attention Output
      ↓
     FFN
      ↓
Transformed Representation
```

The residual connection combines it with the FFN input:

```text
FFN Input
   +
FFN Output
   ↓
Updated Representation
```

Therefore:

```text
Attention → mixes information between tokens

FFN → transforms each token representation

Residual → combines the original representation with the transformation
```

---

## 19. Residual Connections and Layer Normalization

Residual connections and Layer Normalization are often used together in Transformer Blocks.

A simplified architecture might look like:

```text
Input
  ↓
Self-Attention
  ↓
➕ Add Input
  ↓
Layer Normalization
  ↓
FFN
  ↓
➕ Add Input
  ↓
Layer Normalization
  ↓
Output
```

Another architecture may use **Pre-Norm**:

```text
Input
  ↓
Layer Normalization
  ↓
Self-Attention
  ↓
➕ Add Input
  ↓
Layer Normalization
  ↓
FFN
  ↓
➕ Add Input
  ↓
Output
```

The exact arrangement varies.

The important idea is that residual connections and normalization are separate mechanisms that work together inside Transformer Blocks.

---

## 20. Post-Norm vs Pre-Norm

Two common designs are:

### Post-Norm

```text
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
Input
  ↓
FFN
  ↓
Add Residual
  ↓
LayerNorm
```

### Pre-Norm

```text
Input
  ↓
LayerNorm
  ↓
Attention
  ↓
Add Residual
```

and:

```text
Input
  ↓
LayerNorm
  ↓
FFN
  ↓
Add Residual
```

Modern Transformer implementations often use Pre-Norm or related normalization designs, but there is no single universal ordering.

---

## 21. Residual Connections Across Transformer Blocks

A Transformer contains many blocks.

Each block receives a representation from the previous block.

Inside each block, residual connections provide shortcut paths.

Conceptually:

```text
Input
  │
  ├──────────────┐
  ↓              │
Attention        │
  ↓              │
  └──────→  ➕ ←─┘
             ↓
            FFN
             ↓
       ┌─────┴─────┐
       │           │
       └────→  ➕ ←─┘
                ↓
             Block Output
                ↓
          Next Transformer Block
```

This structure repeats throughout the model.

---

## 22. Residual Connections in a Decoder-Only LLM

GPT-style decoder-only LLMs use Transformer Blocks containing residual connections.

Simplified:

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
🔄 Transformer Block
      │
      ├── 👀 Self-Attention
      │       ↓
      │      ➕ Residual
      │
      ├── 🧠 Feed-Forward Network
      │       ↓
      │      ➕ Residual
      │
      ↓
🔄 Transformer Block
      ↓
      ...
      ↓
📊 Final Representation
      ↓
🎯 Output Layer
      ↓
📈 Logits
```

Residual connections are therefore a repeated part of the internal architecture of decoder-only LLMs.

---

## 23. Residual Connections During Training

During training, the model processes input sequences and calculates predictions.

A simplified flow is:

```text
Training Text
      ↓
Tokenization
      ↓
Token IDs
      ↓
Embeddings
      ↓
Transformer Blocks
      ↓
Residual Connections
      ↓
Output Layer
      ↓
Logits
      ↓
Loss
      ↓
Backpropagation
      ↓
Parameter Updates
```

The residual connection itself does not have to learn a separate set of parameters.

The addition operation simply combines compatible representations.

The transformations inside the attention and FFN contain learned parameters.

---

## 24. Residual Connections During Inference

Residual connections are also used during inference.

For example:

```text
Prompt
  ↓
Tokenization
  ↓
Embeddings
  ↓
Transformer Block
  ↓
Attention + Residual
  ↓
FFN + Residual
  ↓
Output
  ↓
Next Token
```

The same learned model structure is used to process the input.

---

## 25. Do Residual Connections Have Parameters?

The simple residual addition:

```text
Output = Input + Transformation(Input)
```

does not require its own learned weight matrix.

The learned parameters are primarily inside the transformation being added, such as:

```text
Attention:
WQ, WK, WV, WO

FFN:
W1, W2
```

depending on the architecture.

So residual connections are mainly an **information-flow mechanism**, not a separate parameter-heavy layer.

---

## 26. Residual Connection vs Transformer Layer

These are not the same thing.

### Transformer Layer / Block

A Transformer Block contains components such as:

```text
Self-Attention
FFN
Normalization
Residual Connections
```

### Residual Connection

A residual connection is one mechanism inside that block:

```text
Input
  +
Transformation
  ↓
Output
```

So:

```text
Transformer Block
        ↓
┌────────────────────────┐
│ Attention              │
│ Residual Connection    │
│ Normalization          │
│ FFN                    │
│ Residual Connection    │
│ Normalization          │
└────────────────────────┘
```

---

## 27. Residual Connection vs Attention

These perform different jobs.

| Component              | Main Role                                |
| ---------------------- | ---------------------------------------- |
| 👀 Attention           | Allows token representations to interact |
| 🧠 FFN                 | Transforms representations               |
| ➕ Residual Connection  | Combines input with transformed output   |
| 📏 Layer Normalization | Normalizes representations               |

A useful mental model is:

```text
Attention
   ↓
Mix information

FFN
   ↓
Transform information

Residual
   ↓
Preserve + combine information

LayerNorm
   ↓
Normalize representation
```

---

## 28. Residual Connection vs Skip Connection

The terms are usually used interchangeably in this context.

```text
Residual Connection
      ≈
Skip Connection
```

The word **skip** describes the shortcut path around a transformation.

The word **residual** comes from the idea of learning a residual transformation:

```text
Output = Input + Residual
```

---

## 29. A Simple Numerical Example

Suppose the input representation is:

```text
Input = [2, 4]
```

The transformation produces:

```text
Transformation(Input) = [1, 3]
```

The residual connection adds them:

```text
[2, 4]
 +
[1, 3]
 =
[3, 7]
```

Therefore:

```text
Output = [3, 7]
```

The original information and transformed information are combined.

---

## 30. Another Example: Small Transformation

Suppose:

```text
Input = [5, 8]

Transformation(Input) = [0.2, -0.1]
```

Then:

```text
Output = [5, 8] + [0.2, -0.1]

Output = [5.2, 7.9]
```

The transformation makes a relatively small adjustment to the existing representation.

This illustrates how a layer can refine an existing representation instead of completely replacing it.

---

## 31. Residual Connections and Deep Representations

As information moves through many Transformer Blocks:

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
```

Each block can refine the representation.

Residual connections help maintain a path for the existing representation while each block adds new transformations.

Conceptually:

```text
Initial Representation
        ↓
   + Transformation 1
        ↓
   Representation 1
        ↓
   + Transformation 2
        ↓
   Representation 2
        ↓
   + Transformation 3
        ↓
        ...
        ↓
   Final Representation
```

---

## 32. Residual Connections Do Not Mean Information Never Changes

Another common misunderstanding is:

> "If the input is added back, the representation stays the same."

That is not correct.

The output is:

```text
Input + Transformation(Input)
```

If the transformation is significant, the output can be substantially different from the input.

Residual connections preserve a direct path to the original representation while still allowing transformations.

---

## 33. Residual Connections and Contextual Representations

Before attention:

```text
Token Representation
```

After attention:

```text
Context-Aware Representation
```

The residual connection combines the original representation with the attention transformation.

Across many blocks:

```text
Token Embeddings
      ↓
Transformer Block
      ↓
Contextual Representation
      ↓
Transformer Block
      ↓
More Refined Contextual Representation
      ↓
...
      ↓
Final Representation
```

Residual connections help these transformations build on previous representations.

---

## 34. Residual Connections and Model Depth

Increasing the number of Transformer Blocks increases model depth.

For example:

```text
6 Blocks
12 Blocks
24 Blocks
32 Blocks
48 Blocks
...
```

The exact number depends on the model.

Residual connections are especially important in deep architectures because they provide shortcut paths through many transformations.

---

## 35. Residual Connections and Model Parameters

Residual connections themselves do not necessarily add a large number of parameters.

For the simple operation:

```text
Output = Input + Transformation(Input)
```

there is no learned matrix in the addition itself.

The parameters belong mainly to the transformation:

```text
Attention
   ↓
Learned Parameters

FFN
   ↓
Learned Parameters
```

The residual connection combines their output with the previous representation.

---

## 36. Residual Connections in Different Architectures

Residual connections are not exclusive to LLMs.

They are widely used in deep neural networks.

For example:

```text
Computer Vision
      ↓
Residual Networks

Transformers
      ↓
Residual Connections

LLMs
      ↓
Transformer Residual Connections
```

The underlying idea is broadly useful for deep neural networks.

---

## 37. Complete Residual Connection Flow

A simplified Transformer Block can be represented as:

```text
                 ┌─────────────────────────┐
                 │                         │
                 │                         ↓
Input ───────────┼──→ 👀 Self-Attention ─→ ➕
                 │                         ↑
                 └─────────────────────────┘
                                             ↓
                                          Output
                                             ↓
                                      📏 LayerNorm
                                             ↓
                 ┌─────────────────────────┐
                 │                         │
                 │                         ↓
                 └──→ 🧠 FFN ───────────→ ➕
                                             ↑
                 ───────────────────────────┘
                                             ↓
                                      📏 LayerNorm
                                             ↓
                                      Block Output
```

The exact placement of LayerNorm can vary.

The important pattern is:

```text
Transformation
      +
Original Representation
      ↓
Updated Representation
```

---

## 38. Complete LLM View

Residual connections are one part of the larger LLM architecture:

```text
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
   │
   ├── 👀 Attention
   │      ↓
   │     ➕ Residual
   │
   ├── 🧠 FFN
   │      ↓
   │     ➕ Residual
   │
   ↓
🔄 Transformer Block
   ↓
🔄 Transformer Block
   ↓
      ...
   ↓
📊 Final Representation
   ↓
🎯 Output Layer
   ↓
📈 Logits
   ↓
🎲 Probability Distribution
   ↓
🔤 Next Token
```

Residual connections are therefore not the final prediction mechanism.

They are part of the internal computation that helps the Transformer process and refine representations.

---

## 39. Simple Mental Model

Think of a Transformer layer as a person editing a document.

The original document is:

```text
Original
```

The transformation produces:

```text
Suggested Changes
```

The residual connection combines:

```text
Original
   +
Changes
   ↓
Updated Version
```

Similarly, a Transformer Block can be thought of as:

```text
Existing Representation
          +
New Transformation
          ↓
Updated Representation
```

This happens repeatedly across many Transformer Blocks.

---

## 40. Key Takeaways

* ➕ A **Residual Connection** provides a shortcut around a transformation.
* 🔄 It combines the original input with the tr
