# 🧠 Feed-Forward Network

A **Feed-Forward Network (FFN)** is one of the main components inside a Transformer Block.

After the attention mechanism processes the relationships between tokens, the Feed-Forward Network applies additional learned transformations to the token representations.

A simplified Transformer Block looks like:

```text id="7x4p2m"
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

The exact ordering can vary between Transformer architectures.

---

# 📌 1. What Is a Feed-Forward Network?

A **Feed-Forward Network** is a neural network that transforms the representations produced by the attention mechanism.

The information moves in one direction:

```text id="q7k4md"
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

In a Transformer, the FFN is applied to the representations at each token position.

---

# 🧩 2. Why Do We Need an FFN?

Attention and the Feed-Forward Network perform different jobs.

### 👀 Attention

Attention allows token representations to exchange information.

```text id="n6c8zv"
Token A ←→ Token B
    ↕         ↕
Token C ←→ Token D
```

### 🧠 Feed-Forward Network

The FFN then transforms the representation at each position.

```text id="4a2b9p"
Token Representation
        ↓
       FFN
        ↓
Transformed Representation
```

A simple way to remember this is:

> **Attention mixes information between tokens. The FFN transforms the information at each token position.**

This is a conceptual simplification, but it is very useful for understanding the Transformer Block.

---

# 🔄 3. Where Does the FFN Appear?

A simplified Transformer Block is:

```text id="e2c1fz"
📊 Input
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
📊 Output
```

Therefore, the FFN comes **after the attention-related computation** in this simplified view.

The exact arrangement of normalization and residual connections depends on the Transformer architecture.

---

# 🏗️ 4. Basic Structure of an FFN

A simplified Feed-Forward Network contains two main linear transformations with a nonlinear activation between them.

```text id="x2j4pk"
Input
  ↓
🔢 Linear Transformation
  ↓
⚡ Activation Function
  ↓
🔢 Linear Transformation
  ↓
Output
```

For example:

```text id="v9j3nf"
📊 Input Representation
        ↓
      Linear
        ↓
      ReLU/GELU
        ↓
      Linear
        ↓
📊 Output Representation
```

Modern Transformer models commonly use activation functions such as **GELU** or related gated variants rather than plain ReLU.

---

# 🔢 5. Linear Transformation

A linear layer transforms the input representation using learned parameters.

Conceptually:

```text id="n8j4zq"
Input
  ↓
Weights + Bias
  ↓
Linear Transformation
  ↓
Output
```

A simplified mathematical form is:

```text id="g7y2ds"
y = xW + b
```

where:

* `x` = input representation
* `W` = learned weight matrix
* `b` = learned bias, when used
* `y` = transformed representation

The actual implementation can vary between architectures.

---

# ⚡ 6. Activation Function

An activation function introduces **nonlinearity**.

Without nonlinear activation functions, stacking linear transformations would still behave like a single linear transformation.

Conceptually:

```text id="j4r5mx"
Input
  ↓
Linear Transformation
  ↓
⚡ Activation
  ↓
Linear Transformation
  ↓
Output
```

Common activation functions include:

* ReLU
* GELU
* SiLU / Swish
* Gated activation variants

Transformer architectures may use different choices.

---

# 🧠 7. GELU

Many Transformer models use **GELU (Gaussian Error Linear Unit)** or related activation functions.

The important beginner-level idea is:

```text id="8w9x6t"
Linear Transformation
        ↓
      GELU
        ↓
Nonlinear Representation
```

You do not need to memorize the mathematical formula at this stage.

The important point is that the activation allows the network to learn more complex transformations.

---

# 📐 8. FFN Dimensions

The Feed-Forward Network often expands the representation to a larger intermediate dimension and then projects it back.

For example:

```text id="c2k8sm"
Input
  │
  │  Embedding Dimension = 768
  ↓
┌──────────────┐
│     FFN      │
│              │
│  768 → 3072  │
│      ↓       │
│    GELU      │
│      ↓       │
│  3072 → 768  │
└──────────────┘
  │
  ↓
Output
```

The numbers above are only an example.

Different models use different dimensions.

The general pattern is:

```text id="b7v1xc"
📊 Model Dimension
        ↓
📈 Larger FFN Dimension
        ↓
📉 Back to Model Dimension
```

---

# 🔄 9. Why Expand and Then Compress?

The expansion gives the network a larger intermediate space in which to perform transformations.

Conceptually:

```text id="r2q5hd"
768
 ↓
3072
 ↓
768
```

The larger intermediate representation provides more capacity for computation.

This does **not** mean the model permanently changes the sequence length.

The number of token positions remains the same.

Only the feature dimension is temporarily expanded inside the FFN.

---

# 📊 10. Sequence Length Does Not Change

Suppose the input contains 5 tokens:

```text id="m3k7vp"
Token 1
Token 2
Token 3
Token 4
Token 5
```

The FFN processes the representations at those positions.

The number of positions remains:

```text id="q8m2fw"
5 tokens → 5 tokens
```

The feature dimension may change internally:

```text id="f3t9ka"
5 × 768
    ↓
5 × 3072
    ↓
5 × 768
```

So:

> **The FFN changes the feature representation, not the number of tokens in the sequence.**

---

# 👥 11. FFN Is Applied to Each Token Position

Suppose we have:

```text id="m6k1xz"
The   cat   is   sleeping
```

After attention, each position has a representation.

The FFN processes these representations.

Conceptually:

```text id="3y7p9a"
The Representation
        ↓
       FFN
        ↓
Updated Representation

cat Representation
        ↓
       FFN
        ↓
Updated Representation

is Representation
        ↓
       FFN
        ↓
Updated Representation

sleeping Representation
        ↓
       FFN
        ↓
Updated Representation
```

The same FFN parameters are generally applied across positions within a layer.

This is why the FFN is often described as operating **position-wise**.

---

# 🔗 12. Attention vs Feed-Forward Network

These two components have different roles.

| Component    | Main Idea                                                           |
| ------------ | ------------------------------------------------------------------- |
| 👀 Attention | Allows information to be mixed across token positions               |
| 🧠 FFN       | Applies learned transformations to representations at each position |

Simplified:

```text id="t8n5qa"
Token A ─────┐
Token B ─────┼──→ 👀 Attention
Token C ─────┘
                  ↓
           Contextual Information
                  ↓
             🧠 FFN
                  ↓
         Transformed Representations
```

A useful mental model is:

> **Attention decides how information from different positions is combined; the FFN performs additional computation on the resulting representation.**

---

# 🧩 13. FFN Input Comes From Attention

Consider a simplified Transformer Block:

```text id="e8v2qz"
📊 Input Representation
          ↓
👀 Self-Attention
          ↓
📊 Attention Output
          ↓
➕ Residual + Normalization
          ↓
🧠 Feed-Forward Network
          ↓
📊 FFN Output
```

So the FFN does not normally receive raw text.

It receives numerical representations produced by earlier stages of the Transformer.

---

# 🔢 14. A Simple Numerical Example

Suppose one token has a simplified representation:

```text id="b5k9py"
[0.2, 0.7, 0.4]
```

The FFN may transform it through several operations:

```text id="2c4f7a"
[0.2, 0.7, 0.4]
        ↓
   Linear Layer
        ↓
[0.5, 1.2, 0.3, 0.8]
        ↓
      GELU
        ↓
[0.3, 1.0, 0.2, 0.6]
        ↓
   Linear Layer
        ↓
[0.4, 0.8, 0.5]
```

These numbers are purely illustrative.

The real model uses learned weights and much larger vectors.

---

# 🧠 15. FFN Parameters Are Learned

The weights inside the Feed-Forward Network are learned during training.

During training:

```text id="u5w2hj"
📚 Training Data
      ↓
🔄 Transformer
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

Over many training iterations, the FFN parameters are adjusted to help the model reduce its training loss.

---

# 🚀 16. FFN During Inference

During inference, the trained FFN parameters are used to process new inputs.

```text id="y2s8dn"
📝 Prompt
   ↓
🔢 Token IDs
   ↓
🧩 Representations
   ↓
👀 Attention
   ↓
🧠 FFN
   ↓
📊 Transformer Output
   ↓
🎯 Prediction
```

The learned parameters are normally not updated during ordinary inference.

---

# 🧱 17. FFN Inside Multiple Transformer Blocks

A Transformer can contain many blocks.

Each block contains its own learned parameters.

```text id="q4v6az"
🔄 Transformer Block 1
   ├── 👀 Attention
   └── 🧠 FFN

🔄 Transformer Block 2
   ├── 👀 Attention
   └── 🧠 FFN

🔄 Transformer Block 3
   ├── 👀 Attention
   └── 🧠 FFN

        ...

🔄 Transformer Block N
   ├── 👀 Attention
   └── 🧠 FFN
```

The FFN in Block 1 and the FFN in Block 2 do not have to use the same learned parameters.

Each layer has its own parameters.

---

# ⚙️ 18. Standard FFN vs Gated FFN

The basic Transformer FFN can be represented as:

```text id="h4c7vp"
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

Modern language models may use **gated feed-forward variants**, such as:

* SwiGLU
* GLU-based variants
* Other gated architectures

These introduce additional learned transformations and gating.

The important idea remains:

> **The feed-forward component performs substantial learned computation on the token representations after attention.**

---

# 🔍 19. FFN Is Not a Separate Model

The Feed-Forward Network is part of the Transformer Block.

It is not a separate language model.

```text id="v7m4cx"
🧠 LLM
   ↓
🔄 Transformer
   ↓
🔄 Transformer Block
   ├── 👀 Attention
   ├── ➕ Residual Connection
   ├── 📏 Normalization
   ├── 🧠 FFN
   └── 📏 Normalization
```

---

# 🏗️ 20. Complete Transformer Block

Putting everything together:

```text id="f5n2qd"
                 Transformer Block

                       Input
                         ↓
                👀 Self-Attention
                         ↓
                 ➕ Residual Add
                         ↓
                 📏 Normalization
                         ↓
              🧠 Feed-Forward Network
                         ↓
                 ➕ Residual Add
                         ↓
                 📏 Normalization
                         ↓
                       Output
```

Again, the exact ordering can vary.

---

# 🔄 21. Complete LLM Flow

The FFN is only one stage in the larger LLM.

```text id="x9k3bw"
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
👀 Attention
      ↓
🧠 Feed-Forward Network
      ↓
🔄 More Transformer Blocks
      ↓
📊 Final Representation
      ↓
🎯 Language Modeling Head
      ↓
📈 Token Probabilities
      ↓
🔤 Next Token
```

---

# 🧠 22. Simple Mental Model

Think of the Transformer Block as having two major computational stages:

```text id="w8c2fz"
👀 ATTENTION
"Which information from other tokens
 should contribute here?"

             ↓

🧠 FFN
"How should this representation
 be transformed?"
```

Together:

```text id="p4m6st"
👀 Attention
      ↓
🔗 Contextual Information
      ↓
🧠 Feed-Forward Network
      ↓
📊 Transformed Representation
```

This is one of the most useful ways to understand the role of the FFN.

---

# 🎯 Key Takeaways

* 🧠 **Feed-Forward Network (FFN)** is a major component of a Transformer Block.
* 👀 Attention and FFN have different roles.
* 👀 Attention allows information to be mixed across token positions.
* 🧠 FFN applies learned transformations to the representations at each position.
* 🔢 A basic FFN commonly uses two linear transformations with a nonlinear activation between them.
* ⚡ Modern Transformers commonly use GELU or gated activation variants.
* 📈 The FFN often expands the feature dimension and then projects it back.
* 📏 The sequence length does not change inside the FFN.
* 🔄 The same FFN parameters are generally applied across token positions within a layer.
* 🎓 FFN parameters are learned during training.
* 🚀 During inference, the trained FFN processes new representations without normally updating its parameters.
* 🧱 Every Transformer Block can have its own FFN parameters.
* 🔗 Attention and FFN work together to transform token representations throughout the Transformer.
