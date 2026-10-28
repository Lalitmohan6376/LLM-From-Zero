# 🎯 Transformer to Prediction

After an LLM processes input representations through its Transformer blocks, it has a sequence of final hidden states.

These hidden states are numerical representations, not readable words. To predict the next token, the model passes a hidden state through its **language modeling head**, which produces logits for the tokens in its vocabulary.

A probability distribution can then be calculated from those logits, and a decoding strategy selects the next token.

This document explains how an LLM moves from Transformer output to next-token prediction.

---

## 1. The Complete Flow

Consider the prompt:

```text
The sun rises in the
```

A GPT-style LLM processes the prompt and predicts a suitable next token.

```text
Input Prompt
     |
     v
Token IDs
     |
     v
Embeddings and Positional Information
     |
     v
Transformer Blocks
     |
     v
Final Hidden States
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

For this example, the model might assign a high probability to a token corresponding to ` east`.

This is illustrative. Actual predictions depend on the model's learned parameters, tokenizer, context, and decoding settings.

---

## 2. Step 1: Transformer Produces Hidden States

The Transformer processes the input sequence through its stacked blocks.

Each token position has a hidden representation that incorporates information from the permitted context.

For example:

```text
Prompt:
The sun rises in the

       |
       v

Transformer Blocks

       |
       v

Hidden State at Each Position
```

For a decoder-only model, causal self-attention prevents a position from attending to future positions in the same sequence.

During inference, the hidden state at the final current position is typically the one used to predict the next token.

Why? Because that position has access to the preceding context and represents the model's processed state at the end of the prompt.

---

## 3. Step 2: Understand the Hidden-State Shape

Suppose the input contains five tokens and the model's hidden dimension is 768.

For a single input sequence, the final hidden states could have the shape:

\[
[1,5,768]
\]

Here:

- `1` is the batch size.
- `5` is the sequence length.
- `768` is the hidden dimension.

The model has one 768-dimensional hidden vector for each of the five token positions.

```text
Final Hidden States

Position 1  [768 values]
Position 2  [768 values]
Position 3  [768 values]
Position 4  [768 values]
Position 5  [768 values]
```

These dimensions are illustrative. Real models use architecture-specific hidden dimensions and context lengths.

For next-token generation, the model typically uses the hidden state at the last position:

\[
h_{\text{last}} \in \mathbb{R}^{d}
\]

where \(d\) is the hidden dimension.

The last hidden state is then passed to the language modeling head.

---

## 4. Step 3: The Language Modeling Head

The language modeling head maps a hidden representation into a score for every token in the model's vocabulary.

A simplified mathematical representation is:

\[
z = Wh + b
\]

Where:

- \(h\) = final hidden state
- \(W\) = learned output weight matrix
- \(b\) = optional bias
- \(z\) = logits

If the vocabulary contains \(V\) tokens, the output contains \(V\) logits.

The output weight matrix has a shape compatible with mapping the hidden dimension to the vocabulary dimension. Some models tie output weights to the token embedding matrix; others use separate weights.

### Example

Suppose a fictional model has a vocabulary of 50,000 tokens.

```text
Last Hidden State
[768 values]
       |
       v
Language Modeling Head
       |
       v
Logits
[50,000 scores]
```

The model has produced a score for each vocabulary token as a possible next token.

It has not yet selected the next token.

---

## 5. Step 4: What Are Logits?

**Logits are the raw numerical scores produced by the model before converting them into probabilities.**

A simplified example:

| Candidate token | Logit |
|---|---:|
| `east` | 4.8 |
| `west` | 2.1 |
| `bright` | 1.4 |
| `quickly` | -0.7 |

These values are illustrative.

A larger logit generally means a token receives a higher probability relative to other tokens when ordinary softmax is applied.

However, logits are not probabilities:

- Logits can be negative or positive.
- They do not need to sum to one.
- Their numerical scale is not directly interpretable as probability.
- Their relative values determine the distribution after softmax.

At this stage, `east` has the largest logit in the example.

---

## 6. Step 5: Convert Logits into Probabilities

To obtain a probability distribution, the model can apply the softmax function:

\[
P(i)=\frac{e^{z_i}}{\sum_{j=1}^{V}e^{z_j}}
\]

Where:

- \(z_i\) is the logit for token \(i\).
- \(V\) is the vocabulary size.
- \(P(i)\) is the probability assigned to that token.

Softmax converts the logits into non-negative values whose total is one.

### Illustrative example

Suppose the resulting probabilities are:

| Candidate token | Probability |
|---|---:|
| `east` | 70% |
| `west` | 15% |
| `bright` | 10% |
| `quickly` | 5% |
| **Total** | **100%** |

These are example probabilities, not measured outputs from a real model. A real vocabulary contains many more candidates, and the probability distribution can be much more spread out.

In this example, `east` has the highest probability.

The model still needs a token-selection strategy to decide what to generate.

---

## 7. Step 6: Select the Next Token

A decoding strategy determines how the next token is selected from the model's scores or probability distribution.

Common strategies include:

- **Greedy decoding:** Select the highest-scoring token.
- **Temperature-based sampling:** Adjust the probability distribution's sharpness before sampling.
- **Top-K sampling:** Restrict sampling to a fixed number of high-scoring candidates.
- **Top-P sampling:** Restrict sampling to a set of high-probability candidates whose cumulative probability reaches a chosen threshold.

### Example

Given the illustrative distribution:

```text
east     70%
west     15%
bright   10%
quickly   5%
```

Greedy decoding selects:

```text
east
```

Sampling may select another candidate, depending on the distribution and random draw.

The strategy affects how predictable or varied generation is.

**Important:** Token selection is not the same operation as predicting logits. The model produces the scores; the decoding procedure determines how a token is selected.

---

## 8. Step 7: Update the Context

After selecting a token, the generation process appends it to the current sequence.

For example:

```text
Original Prompt:
The sun rises in the

       |
       v

Selected Token:
east

       |
       v

Updated Sequence:
The sun rises in the east
```

The model can now predict another token using the updated context.

```text
The sun rises in the east
              |
              v
      Transformer Processing
              |
              v
        New Logits
              |
              v
      Select Another Token
```

This loop continues until the model reaches a stopping condition, such as generating an end-of-sequence token or reaching a configured maximum number of new tokens.

The generated continuation depends on the model and decoding settings.

---

## 9. Why Does the Last Position Matter?

During inference, a decoder-only model processes the prompt and produces hidden states for its token positions.

For next-token generation, the final position represents the end of the currently processed sequence.

Consider:

```text
Prompt:
The sun rises in the
```

Conceptually:

```text
Token:       The    sun    rises    in    the
Position:     1      2       3       4      5
                                              |
                                              v
                                    Last Hidden State
                                              |
                                              v
                                         Logits
                                              |
                                              v
                                    Next-Token Prediction
```

The last position can attend to the permitted preceding context, so its hidden state can be used to predict the token that comes next.

During training, the model commonly computes logits for many positions because each position can contribute a next-token prediction loss. During inference, the next-token selection generally uses the logits for the last current position.

---

## 10. Training vs Inference

The Transformer-to-prediction path is related to both training and inference, but the purpose differs.

### During training

```text
Input Token IDs
      |
      v
Transformer Blocks
      |
      v
Hidden States
      |
      v
Language Modeling Head
      |
      v
Logits
      |
      v
Compare with Target Tokens
      |
      v
Loss
      |
      v
Backpropagation and Parameter Updates
```

Training uses target tokens to measure prediction error. Gradients and an optimizer update the trainable parameters.

### During inference

```text
Prompt Token IDs
      |
      v
Transformer Blocks
      |
      v
Hidden States
      |
      v
Language Modeling Head
      |
      v
Logits
      |
      v
Token Selection
      |
      v
Context Update
```

Ordinary inference uses the existing learned parameters to make predictions. It does not require target tokens, backpropagation, or optimizer updates.

Loss can still be calculated during evaluation when reference targets are available, but it is not required for ordinary text generation.

---

## 11. What Happens During Repeated Generation?

An LLM does not normally generate an entire response in one next-token selection.

Instead, it predicts a token, adds it to the sequence, and predicts another token.

```text
Prompt
"The sun rises in the"
        |
        v
Prediction 1
" east"
        |
        v
Updated Context
"The sun rises in the east"
        |
        v
Prediction 2
" every"
        |
        v
Updated Context
"The sun rises in the east every"
        |
        v
Prediction 3
" morning"
```

This is a conceptual example, not a guaranteed continuation.

The process is called **autoregressive generation**.

### What about the KV cache?

During generation, attention calculations can reuse previously computed keys and values through a KV cache.

Instead of repeatedly recomputing attention information for the entire prior sequence, the model can reuse cached values and process the newly added token.

The cache is temporary inference state. It does not mean the model's learned parameters are being updated.

---

## 12. Common Misconceptions

**Misconception 1: The Transformer directly produces words.**

The Transformer produces hidden representations. The language modeling head maps them to logits, and the generation process selects token IDs.

**Misconception 2: Logits are probabilities.**

Logits are raw scores. Softmax can convert them into probabilities.

**Misconception 3: The highest-probability token must always be selected.**

That is true for greedy decoding, but sampling strategies can select other candidates.

**Misconception 4: The model predicts the entire response at once during ordinary autoregressive generation.**

It generally selects one next token at a time, repeatedly updating the context.

**Misconception 5: The language modeling head always has the same shape as the hidden state.**

The head maps the hidden dimension to the vocabulary dimension, so the output dimension typically corresponds to the vocabulary size.

**Misconception 6: Inference updates the learned model weights.**

Ordinary inference uses fixed learned parameters. The context and temporary KV cache can change during generation.

**Misconception 7: The highest-probability next token guarantees the best complete response.**

Greedy selection optimizes the immediate next-token choice, not necessarily the quality of the entire continuation.

---

## 13. Complete Transformer-to-Prediction Flow

```text
                INPUT PROMPT
                     |
                     v
                 TOKEN IDs
                     |
                     v
          EMBEDDINGS AND POSITION
                     |
                     v
             TRANSFORMER BLOCKS
                     |
                     v
            FINAL HIDDEN STATES
                     |
                     v
          SELECT LAST POSITION
                     |
                     v
          LANGUAGE MODELING HEAD
                     |
                     v
                   LOGITS
                     |
                     v
          PROBABILITY DISTRIBUTION
                     |
                     v
              DECODING STRATEGY
                     |
                     v
              SELECT NEXT TOKEN
                     |
                     v
              APPEND TO CONTEXT
                     |
                     v
               REPEAT OR STOP
```

The essential flow is:

**Transformer processing → Final hidden state → Language modeling head → Logits → Probability distribution → Next-token selection.**

The Transformer builds context-dependent representations. The language modeling head converts those representations into vocabulary scores, and the decoding procedure uses those scores to select the next token.

This is the connection between the internal computations of an LLM and its ability to generate text.
