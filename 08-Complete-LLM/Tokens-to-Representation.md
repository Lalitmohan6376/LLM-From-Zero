# 🧠 Tokens to Representation

After an LLM converts text into token IDs, it must transform those IDs into numerical vectors that its neural network can process.

This process involves **token embeddings, positional information, and contextual representations**.

Token IDs identify tokens, but they do not directly express the meaning or context of those tokens. The model uses learned embeddings and Transformer layers to build representations that depend on the surrounding text.

This document explains how an LLM moves from token IDs to contextual representations.

---

## 1. The Complete Flow

Consider the sentence:

```text
The cat is sleeping.
```

A tokenizer converts it into token IDs. The model then uses those IDs to retrieve embedding vectors and processes them through Transformer blocks.

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
Transformer Blocks
   |
   v
Contextual Representations
```

Each stage has a different purpose.

| Stage | Purpose |
|---|---|
| Token IDs | Identify the tokens |
| Token embeddings | Provide learned numerical vectors for the tokens |
| Positional information | Represent token positions or sequence order |
| Transformer blocks | Process token representations using attention and other neural network operations |
| Contextual representations | Represent tokens after processing their context |

The distinction between token embeddings and contextual representations is especially important.

---

## 2. Step 1: Token IDs

Suppose the tokenizer produces the following illustrative sequence:

```text
Text:
The cat is sleeping.

Token IDs:
[101, 205, 310, 415, 12]
```

These IDs are fictional and do not correspond to a specific tokenizer.

Each integer identifies a token in the tokenizer's vocabulary.

However, the numbers themselves do not contain the token's semantic meaning.

For example, token ID `205` is not inherently more important than token ID `101`. The values are identifiers, not numerical measures of similarity or meaning.

The model needs another representation to process these tokens as neural network inputs.

That representation begins with embeddings.

---

## 3. Step 2: Token Embeddings

A token embedding is a learned numerical vector associated with a token ID.

The model contains an embedding matrix, which can be represented as:

\[
E \in \mathbb{R}^{V \times d}
\]

Where:

- \(E\) is the embedding matrix.
- \(V\) is the vocabulary size.
- \(d\) is the embedding dimension.

Each row of the matrix contains a vector associated with one vocabulary token.

When the model receives a token ID, it uses that ID to look up the corresponding row.

### Example

Suppose a simplified model has an embedding dimension of four.

An embedding lookup might produce:

```text
Token ID: 101

Embedding:
[0.12, -0.43, 0.81, 0.25]
```

These numbers are illustrative.

The model performs a similar lookup for every token in the input sequence.

For example:

```text
Token IDs
[101, 205, 310, 415, 12]
          |
          v
     Embedding Lookup
          |
          v
[0.12, -0.43, 0.81, 0.25]
[0.34,  0.17, -0.22, 0.61]
[-0.19, 0.72, 0.11, 0.38]
[0.56, -0.08, 0.42, 0.13]
[0.05,  0.29, -0.14, 0.47]
```

Every row is a vector for one token.

In this simplified example, the resulting embedding matrix has five rows and four columns.

\[
X \in \mathbb{R}^{5 \times 4}
\]

Here, five is the sequence length and four is the embedding dimension.

Real LLMs generally use much larger embedding dimensions.

### What do the embedding values mean?

Individual embedding dimensions usually do not have simple, human-readable meanings.

A dimension should not automatically be interpreted as representing a particular concept such as happiness, intelligence, or grammar.

Instead, the vector participates in learned numerical computations throughout the network.

**Important:** An embedding is a learned representation, not a dictionary definition of a word.

---

## 4. Step 3: Why Token Embeddings Are Not Enough

Token embeddings provide the model with initial representations for the tokens.

However, the same word can appear in different contexts and be used in different ways.

Consider these sentences:

```text
Sentence A:
She deposited money at the bank.

Sentence B:
They sat on the river bank.
```

The word `bank` appears in both sentences.

Its token ID and initial embedding may be the same in both cases when the same tokenizer and model are used.

But the surrounding words provide different context.

- In Sentence A, the context suggests a financial institution.
- In Sentence B, the context suggests the land beside a river.

The model needs to process the surrounding tokens to build representations that reflect these differences.

This is where Transformer blocks become important.

---

## 5. Step 4: Positional Information

Token embeddings alone do not explicitly indicate the order in which tokens appear.

Consider:

```text
The dog chased the cat.
```

And:

```text
The cat chased the dog.
```

The sentences contain many of the same tokens, but their order changes the meaning.

A Transformer therefore needs a way to account for token positions and sequence order.

Different architectures use different mechanisms, including:

- Learned positional embeddings
- Sinusoidal positional encodings
- Rotary positional embeddings (RoPE)

The exact mechanism depends on the model.

### Conceptual example

```text
Token Embeddings
       +
Positional Information
       |
       v
Position-Aware Representations
```

In an architecture that adds positional vectors to token embeddings, the combination can be represented as:

\[
X = E_{\text{token}} + E_{\text{position}}
\]

This formula applies to additive positional representations. It is not a universal formula for every Transformer architecture.

For example, RoPE applies positional rotations to query and key representations inside attention rather than simply adding a positional vector to every token embedding.

The key idea is that the model must account for sequence order, although the implementation varies.

---

## 6. Step 5: From Initial Embeddings to Contextual Representations

After the input representations are prepared, they pass through Transformer blocks.

A typical decoder-only LLM block contains:

1. Causal self-attention
2. A feed-forward network
3. Residual connections
4. Normalization operations

The exact ordering and implementation can vary.

### Simplified flow

```text
Token Embeddings
       |
       v
Positional Information
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
Final Transformer Block
       |
       v
Contextual Representations
```

As the representations pass through the blocks, attention allows each token position to incorporate information from relevant positions in the permitted context.

The feed-forward network then transforms the representation at each position.

Repeated across multiple blocks, these operations build increasingly processed, context-dependent representations.

### Why are they called contextual representations?

Because the resulting representation for a token depends on the input context available to the model.

For a decoder-only Transformer using causal self-attention, a token position can attend to permitted earlier positions, not future positions in the same sequence.

For example:

```text
Input:
The cat is sleeping

Representation at "cat":
Can incorporate information from "The" and "cat".

Representation at "sleeping":
Can incorporate information from "The", "cat",
"is", and "sleeping".
```

This is a conceptual illustration of causal attention, not a claim that the model explicitly stores separate dictionary meanings for each word.

---

## 7. Token Embedding vs Contextual Representation

This is one of the most important distinctions in an LLM.

<box border radius="xl" padding={3} gap={3}>
  <box gap={1}>
    <text color="secondary" size="sm">Initial representation</text>
    **Token embedding**

    A learned vector retrieved using the token ID. It does not yet incorporate the current sentence's context through the Transformer layers.
  </box>
  <divider color="subtle" />
  <box gap={1}>
    <text color="secondary" size="sm">After Transformer processing</text>
    **Contextual representation**

    A vector produced after neural network processing. It reflects information from the context available to that token position.
  </box>
</box>

| Feature | Token embedding | Contextual representation |
|---|---|---|
| Obtained from | Embedding lookup | Transformer processing |
| Depends on token ID | Yes | Indirectly, through the input |
| Incorporates surrounding context | Not through Transformer processing yet | Yes |
| Changes with sentence context | Initial lookup generally remains the same for the same ID and model | Can change |
| Role | Initial token representation | Context-aware representation used for downstream predictions |

For example, the initial embedding for `bank` can be the same in two sentences, while its final contextual representation can differ.

That difference helps the model make context-sensitive predictions.

---

## 8. Step 6: Understanding the Tensor Shape

LLMs process batches of token sequences as numerical tensors.

A common representation shape is:

\[
[B,N,d]
\]

Where:

- \(B\) = batch size
- \(N\) = sequence length
- \(d\) = hidden dimension

For a single sequence, the batch size may be one.

Suppose:

- Batch size = 1
- Sequence length = 5
- Hidden dimension = 4

Then the representation has shape:

\[
[1,5,4]
\]

This means:

- One sequence is being processed.
- The sequence contains five token positions.
- Each position has a four-dimensional vector.

In a real LLM, the hidden dimension may be hundreds or thousands of values, and the sequence can contain many more tokens.

### How the shape changes through the network

In a typical Transformer, the hidden representation retains the same batch size, sequence length, and hidden dimension across its main blocks.

```text
Input Embeddings:
[1, 5, 4]

       |
       v

Transformer Block 1:
[1, 5, 4]

       |
       v

Transformer Block 2:
[1, 5, 4]

       |
       v

Final Hidden States:
[1, 5, 4]
```

This is an illustrative shape example. Some internal operations use different dimensions, and implementations may vary.

The important point is that the main Transformer blocks usually preserve one hidden vector per input token position.

---

## 9. Step 7: What Happens to the Representations Next?

Contextual representations are not normally the final output of a standard next-token language model.

They are passed to the language modeling head, which maps the hidden dimension to the vocabulary dimension.

```text
Contextual Representations
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
      Token Selection
```

For example, if the vocabulary contains \(V\) tokens, the output logits for one position commonly contain \(V\) scores.

The logits indicate the model's relative scores for possible next tokens. A softmax operation can convert them into a probability distribution.

During autoregressive generation, the logits at the final current position are typically used to select the next token.

The selected token is appended to the context, and the model continues generating.

---

## 10. Training vs Inference: How Representations Are Used

The conversion from token IDs to representations occurs in both training and inference.

### During training

```text
Training Token IDs
        |
        v
Token Embeddings
        |
        v
Positional Information
        |
        v
Transformer Blocks
        |
        v
Contextual Representations
        |
        v
Logits and Loss
        |
        v
Backpropagation
        |
        v
Parameter Updates
```

The model compares its predictions with target tokens. Backpropagation and the optimizer update trainable parameters.

The embedding matrix and Transformer parameters can be updated during full-model training, depending on which parameters are trainable.

### During inference

```text
Prompt Token IDs
        |
        v
Token Embeddings
        |
        v
Positional Information
        |
        v
Transformer Blocks
        |
        v
Contextual Representations
        |
        v
Logits and Token Selection
        |
        v
Generated Token
```

During ordinary inference, the learned parameters remain fixed.

The model computes representations to predict tokens rather than calculating gradients to update its parameters.

---

## 11. Common Misconceptions

**Misconception 1: Token IDs already contain meaning.**

Token IDs are identifiers. The model retrieves learned embedding vectors using those identifiers.

**Misconception 2: Token embeddings and contextual representations are the same.**

Token embeddings are initial vectors. Contextual representations are produced after Transformer processing.

**Misconception 3: An embedding dimension has an obvious meaning.**

Individual dimensions generally do not have straightforward, human-readable interpretations.

**Misconception 4: Positional information is always added to embeddings.**

Some architectures use additive positional representations, while others, such as RoPE-based models, handle positional information differently.

**Misconception 5: Every token can attend to every other token in a GPT-style LLM.**

Causal self-attention restricts each position from attending to future positions in the same sequence.

**Misconception 6: Contextual representations are the final generated words.**

They are internal numerical representations. The language modeling head produces logits, and the generation process selects tokens that can later be decoded into text.

**Misconception 7: The model updates its parameters whenever it processes a prompt.**

Ordinary inference computes representations without updating the learned parameters.

---

## 12. Complete Tokens-to-Representation Flow

```text
                TOKEN IDs
                    |
                    v
             EMBEDDING LOOKUP
                    |
                    v
             TOKEN EMBEDDINGS
                    |
                    v
           POSITIONAL INFORMATION
                    |
                    v
           INPUT REPRESENTATIONS
                    |
                    v
          +---------------------+
          |   TRANSFORMER BLOCK |
          |                     |
          |  Causal Attention   |
          |         |           |
          |         v           |
          |  Feed-Forward Net   |
          |                     |
          | Residual Connections|
          |    Normalization    |
          +---------------------+
                    |
                    v
          Repeat Across Blocks
                    |
                    v
         CONTEXTUAL REPRESENTATIONS
                    |
                    v
          LANGUAGE MODELING HEAD
                    |
                    v
                  LOGITS
```

The essential transformation is:

**Token IDs → Token embeddings → Position-aware input representations → Transformer processing → Contextual representations.**

The token IDs identify the input tokens. Embeddings turn those IDs into learned vectors, positional mechanisms account for sequence order, and Transformer blocks process the vectors in context.

These contextual representations provide the information used by the language modeling head to predict the next token.
