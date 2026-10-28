# 🧠 Representation to Transformer

After token IDs are converted into embeddings and positional information is handled, the model has numerical representations ready for Transformer processing.

The Transformer is the part of a modern LLM that processes these representations to build context-dependent information.

Its main components include **self-attention, feed-forward networks, residual connections, and normalization**. These components work together inside Transformer blocks, which are stacked to form the model's main neural network.

This document explains how input representations enter the Transformer, what happens inside each block, and how the final representations are produced.

---

## 1. Where Does Transformer Processing Begin?

Before reaching the Transformer, text has already passed through several stages.

```text
Raw Text
   |
   v
Tokenization
   |
   v
Token IDs
   |
   v
Token Embeddings
   |
   v
Positional Information
   |
   v
Input Representations
   |
   v
Transformer Blocks
```

For example, consider this sentence:

```text
The cat is sleeping.
```

After tokenization, embedding lookup, and positional processing, the model has a numerical vector for each token position.

An illustrative representation might look like this:

```text
The       [0.12, -0.43, 0.81, 0.25]
cat       [0.34,  0.17, -0.22, 0.61]
is        [-0.19, 0.72, 0.11, 0.38]
sleeping  [0.56, -0.08, 0.42, 0.13]
.         [0.05,  0.29, -0.14, 0.47]
```

These numbers are fictional and use a tiny four-dimensional representation for illustration. Real LLMs generally use much larger hidden dimensions.

The Transformer receives these representations and processes them through its layers.

---

## 2. What Is a Transformer Block?

A Transformer block is a collection of neural network operations that transforms a sequence of input representations into a sequence of updated representations.

A typical decoder-only LLM block contains:

- Causal self-attention
- A feed-forward network
- Residual connections
- Normalization

The precise order of these operations varies across architectures. Many modern decoder-only LLMs use a pre-normalization design, where normalization occurs before the attention and feed-forward sublayers.

### Simplified block

```text
Input Representations
         |
         v
   Self-Attention
         |
         v
 Feed-Forward Network
         |
         v
Updated Representations
```

This simplified diagram shows the two main computational sublayers. Residual connections and normalization are also part of the actual block.

A more representative pre-normalization block looks like this:

```text
              Input X
                 |
          +------+----------------+
          |                       |
          v                       |
    Normalization                 |
          |                       |
          v                       |
   Causal Self-Attention          |
          |                       |
          +---- Residual Add <----+
                 |
                 v
                 H
                 |
          +------+----------------+
          |                       |
          v                       |
    Normalization                 |
          |                       |
          v                       |
   Feed-Forward Network           |
          |                       |
          +---- Residual Add <----+
                 |
                 v
              Output
```

This is a conceptual pre-normalization design. Exact implementations differ, and some include additional operations such as gating.

---

## 3. Step 1: Self-Attention

Self-attention allows each token position to combine information from other permitted token positions.

Consider:

```text
The cat sat beside the bowl because it was hungry.
```

To interpret `it` in context, information from other words may be useful.

Self-attention computes relationships between token representations and uses those relationships to combine information.

### How it works

For each input representation, attention produces three vectors:

- **Query (Q):** Used to calculate which positions are relevant.
- **Key (K):** Used to calculate how positions match queries.
- **Value (V):** Carries information that can be combined.

The query and key vectors are compared to calculate attention scores.

A simplified scaled dot-product attention formula is:

\[
\operatorname{Attention}(Q,K,V)
=
\operatorname{softmax}
\left(
\frac{QK^\top}{\sqrt{d_k}}
\right)V
\]

Where:

- \(Q\) = query matrix
- \(K\) = key matrix
- \(V\) = value matrix
- \(d_k\) = key dimension

The resulting attention weights determine how the value vectors contribute to each position's updated representation.

### Causal attention in GPT-style LLMs

A decoder-only LLM normally uses causal self-attention. Each position can attend to itself and permitted earlier positions, but not future positions in the same sequence.

For example:

```text
Input:
The cat is sleeping

Position: The
Can attend to: The

Position: cat
Can attend to: The, cat

Position: is
Can attend to: The, cat, is

Position: sleeping
Can attend to: The, cat, is, sleeping
```

This restriction supports autoregressive next-token prediction.

---

## 4. Step 2: The Attention Output

Self-attention produces updated representations that incorporate information from the permitted context.

Before attention, each position has an input representation.

After attention, each position has an attention output influenced by other positions.

```text
Input Representations
         |
         v
   Self-Attention
         |
         v
Attention Output
```

For example, the representation at `sleeping` can incorporate information from `The`, `cat`, and `is`, as permitted by causal attention.

The resulting vector is not simply a copy of the embedding for `sleeping`. It is computed using learned transformations and attention weights.

**Important:** Attention does not guarantee that the model identifies the correct meaning or focuses on the most human-relevant information. It is a learned numerical operation.

---

## 5. Step 3: Residual Connections

A residual connection allows a sublayer's input to be added to its output.

Instead of using only the attention output, the block combines it with the representation that entered the attention sublayer.

A simplified residual operation is:

\[
H = X + \operatorname{Attention}(X)
\]

Here, the attention notation hides the query, key, value, normalization, and masking operations used in a real block.

Residual connections help information and gradients flow through deep neural networks.

They are especially useful when many Transformer blocks are stacked together.

### Conceptual example

```text
Input Representation
         |
         +--------------------+
         |                    |
         v                    |
   Self-Attention              |
         |                    |
         v                    |
  Attention Output            |
         |                    |
         +------ Add <--------+
                 |
                 v
          Updated State
```

The addition requires compatible tensor dimensions. Transformer sublayers are designed to satisfy the required shape constraints.

In a pre-normalization architecture, the sublayer may receive a normalized version of the input while the residual path carries the original state.

---

## 6. Step 4: Normalization

Normalization helps control the scale and distribution of values used inside the network.

Many decoder-only LLMs use LayerNorm or related normalization methods, such as RMSNorm.

A common pre-normalization design applies normalization before the attention and feed-forward sublayers.

```text
Input
  |
  v
Normalization
  |
  v
Attention or Feed-Forward
  |
  v
Residual Addition
```

The exact arrangement depends on the model architecture.

Normalization does not mean that the model understands the sentence, and it does not itself decide which words are relevant. It is a numerical operation that supports stable neural network computation.

---

## 7. Step 5: Feed-Forward Network

After attention and its residual operation, the representation passes through a feed-forward network (FFN).

Attention combines information across permitted token positions. The FFN transforms each position's representation using learned neural network layers.

A simplified FFN can be written as:

\[
\operatorname{FFN}(x)
=
W_2\,\sigma(W_1x+b_1)+b_2
\]

Where:

- \(x\) = input vector
- \(W_1\) and \(W_2\) = learned weight matrices
- \(b_1\) and \(b_2\) = biases
- \(\sigma\) = a nonlinear activation function

Many modern LLMs use gated feed-forward designs rather than this simple form.

### Example of dimensional changes

Suppose a representation has 768 dimensions.

A conventional feed-forward network might expand it to 3072 dimensions and then project it back to 768:

```text
Input Vector
[768 dimensions]
       |
       v
First Linear Layer
[3072 dimensions]
       |
       v
Activation
       |
       v
Second Linear Layer
[768 dimensions]
       |
       v
Output Vector
[768 dimensions]
```

These dimensions are illustrative, not a universal LLM configuration.

The sequence length remains unchanged through this typical FFN operation. The FFN processes the representation at each position separately, using shared learned weights across positions.

---

## 8. Step 6: Another Residual Connection

After the feed-forward network, a residual connection combines its output with the representation entering that sublayer.

A simplified pre-normalization block can be expressed as:

\[
H = X + \operatorname{Attention}(\operatorname{Norm}(X))
\]

\[
Y = H + \operatorname{FFN}(\operatorname{Norm}(H))
\]

These equations illustrate the main residual paths. They omit implementation details such as projections, causal masks, attention heads, and architecture-specific operations.

The final result \(Y\) is the block's output representation.

```text
Input
  |
  v
Normalized Input
  |
  v
Self-Attention
  |
  v
Residual Addition
  |
  v
Normalized Representation
  |
  v
Feed-Forward Network
  |
  v
Residual Addition
  |
  v
Block Output
```

This block output becomes the input to the next Transformer block.

---

## 9. Step 7: Stacking Transformer Blocks

An LLM typically contains multiple Transformer blocks stacked sequentially.

The output of one block becomes the input to the next.

```text
Input Representations
         |
         v
   Transformer Block 1
         |
         v
   Transformer Block 2
         |
         v
   Transformer Block 3
         |
         v
         ...
         |
         v
   Transformer Block N
         |
         v
Final Hidden States
```

Each block applies learned transformations to the representations.

Across the stack, the representations can incorporate increasingly processed contextual information.

A model's depth, width, attention configuration, and feed-forward design depend on its architecture.

**More blocks do not automatically guarantee better performance.** Model quality also depends on training data, parameter count, optimization, and other design choices.

---

## 10. What Happens to Tensor Shapes?

Transformer blocks commonly preserve the main hidden-state shape.

Suppose the input tensor has shape:

\[
[B,N,d]
\]

Where:

- \(B\) = batch size
- \(N\) = sequence length
- \(d\) = hidden dimension

For an illustrative input with batch size 1, five tokens, and hidden dimension 768:

\[
[1,5,768]
\]

The main block output commonly retains the same shape:

```text
Input:
[1, 5, 768]

        |
        v

Transformer Block 1:
[1, 5, 768]

        |
        v

Transformer Block 2:
[1, 5, 768]

        |
        v

Final Hidden States:
[1, 5, 768]
```

Internal operations can use other dimensions. For example, attention projects the hidden states into query, key, and value representations, and the FFN may expand the intermediate dimension.

The main hidden-state sequence generally retains one vector per token position.

---

## 11. What Comes Out of the Transformer?

After the final Transformer block, the model has final hidden states.

These are contextual numerical representations, not readable text.

A typical decoder-only language model then uses a final normalization layer, depending on the architecture, and a language modeling head to map hidden representations to vocabulary-sized logits.

```text
Final Transformer Block
          |
          v
    Final Hidden States
          |
          v
  Optional Final Normalization
          |
          v
  Language Modeling Head
          |
          v
         Logits
          |
          v
 Probability Distribution
          |
          v
    Next-Token Selection
```

For a vocabulary of size \(V\), the logits at one position generally contain \(V\) scores.

During inference, the logits from the last current position are typically used to select the next token. The selected token is appended to the context, and generation continues until a stopping condition is met.

---

## 12. Training vs Inference Inside the Transformer

The Transformer blocks are used in both training and inference, but the surrounding operations differ.

### During training

```text
Training Token IDs
        |
        v
Embeddings and Position
        |
        v
Transformer Blocks
        |
        v
Logits
        |
        v
Loss Calculation
        |
        v
Backpropagation
        |
        v
Optimizer Updates Parameters
```

The model compares predictions with target tokens. Gradients are used to update trainable parameters.

### During inference

```text
Prompt Token IDs
        |
        v
Embeddings and Position
        |
        v
Transformer Blocks
        |
        v
Logits
        |
        v
Token Selection
        |
        v
Context Update
        |
        v
Repeat Generation
```

During ordinary inference, the learned parameters remain fixed. The model uses its existing parameters to calculate predictions.

KV caching can also reuse previously computed attention keys and values during autoregressive generation, reducing repeated computation.

---

## 13. Common Misconceptions

**Misconception 1: The Transformer receives raw text directly.**

The tokenizer converts text into token IDs, and the model uses embeddings and positional mechanisms to prepare numerical representations for Transformer processing.

**Misconception 2: Attention is the entire Transformer block.**

Attention is one major sublayer. A typical block also contains a feed-forward network, residual connections, and normalization.

**Misconception 3: Attention and the feed-forward network do the same thing.**

Attention combines information across permitted token positions. The feed-forward network transforms each position's representation.

**Misconception 4: Residual connections and normalization are interchangeable.**

Residual connections add a sublayer's input to its output. Normalization transforms values according to a normalization rule. They have different roles.

**Misconception 5: Every Transformer uses the exact same block design.**

The original encoder-decoder Transformer and modern decoder-only LLMs differ, and implementations also vary in normalization, attention, positional mechanisms, and feed-forward design.

**Misconception 6: The Transformer directly produces the final readable sentence.**

It produces hidden representations. The language modeling head generates logits, and the generation process selects tokens that can be converted back into text.

**Misconception 7: Transformer blocks update model weights during every forward pass.**

A forward pass calculates outputs. Parameter updates occur during training when gradients and an optimizer are used; ordinary inference does not update the learned weights.

---

## 14. Complete Representation-to-Transformer Flow

```text
             INPUT REPRESENTATIONS
                       |
                       v
             +-------------------+
             | TRANSFORMER BLOCK |
             |                   |
             |   Normalization   |
             |         |         |
             |         v         |
             |  Causal Attention |
             |         |         |
             |         v         |
             |  Residual Addition|
             |         |         |
             |         v         |
             |   Normalization   |
             |         |         |
             |         v         |
             |  Feed-Forward Net |
             |         |         |
             |         v         |
             |  Residual Addition|
             +-------------------+
                       |
                       v
              NEXT TRANSFORMER BLOCK
                       |
                       v
                Repeat as Needed
                       |
                       v
              FINAL HIDDEN STATES
                       |
                       v
              LANGUAGE MODELING HEAD
                       |
                       v
                     LOGITS
```

The essential flow is:

**Input representations → Self-attention → Feed-forward processing → Residual and normalization operations → Stacked Transformer blocks → Final hidden states.**

The Transformer turns the initial token representations into context-dependent representations that can be used to predict the next token.

Understanding this flow connects tokenization and embeddings to the internal operations that power modern decoder-only LLMs.
