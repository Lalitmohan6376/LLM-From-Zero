# 🎯 Logits in an LLM

## 1. What Are Logits?

When an LLM processes a prompt, it uses its Transformer layers to produce a representation of the input. The **language modeling head** converts that representation into a score for every token in the model's vocabulary.

These raw scores are called **logits**.

In simple words:

> **Logits are the raw scores an LLM produces for possible next tokens before converting those scores into probabilities.**

For example, suppose the prompt is:

```text
The sky is
```

The model might assign these illustrative logits to possible next tokens:

| Possible next token | Logit |
|---|---:|
| blue | 5.2 |
| clear | 3.1 |
| dark | 1.8 |
| banana | -2.0 |

Here, `blue` has the highest logit, while `banana` has the lowest.

These are example values for learning, not actual outputs from a specific model.

**Important:** Logits are scores, not probabilities. They can be positive, negative, or zero, and they do not have to add up to 1.

---

## 2. Where Do Logits Come From?

Logits are produced near the end of the model's forward pass during inference.

The process looks like this:

```text
User Prompt
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
Transformer Blocks
     |
     v
Final Hidden Representation
     |
     v
Language Modeling Head
     |
     v
    LOGITS
     |
     v
Probability Distribution
     |
     v
Next Token Selection
```

Let's understand the final steps.

1. **Transformer blocks:** Process the input tokens and build contextual representations.
2. **Final hidden representation:** Contains the model's processed representation at each token position.
3. **Language modeling head:** Maps the hidden representation to one score per vocabulary token.
4. **Logits:** The resulting raw scores.
5. **Probability distribution:** Softmax can convert logits into probabilities.
6. **Next token selection:** The generation method chooses or samples a token.

The language modeling head typically uses a learned linear transformation to produce these scores.

A simplified mathematical representation is:

\[
\mathbf{z}=\mathbf{h}W+b
\]

Where:

- \(\mathbf{h}\) = final hidden representation.
- \(W\) = learned output weight matrix.
- \(b\) = bias, if used.
- \(\mathbf{z}\) = vector of logits.

The exact implementation can vary between models.

---

## 3. Logits vs Probabilities

Logits and probabilities are related, but they are not the same thing.

Consider these illustrative logits:

| Token | Logit |
|---|---:|
| blue | 3.0 |
| green | 1.0 |
| red | 0.0 |

The model has assigned a higher raw score to `blue` than to `green` or `red`.

However, these scores are not probabilities. For example, a logit of `3.0` does **not** mean a 300% probability or a 3% probability.

To obtain probabilities, we can apply the **softmax function**.

### Softmax formula

\[
P_i=\frac{e^{z_i}}{\sum_j e^{z_j}}
\]

Where:

- \(z_i\) = the logit for a particular token.
- \(e^{z_i}\) = the exponential of that logit.
- The denominator = the sum of exponentials of all logits.
- \(P_i\) = the resulting probability for that token.

Applying softmax to our example gives approximately:

| Token | Logit | Probability |
|---|---:|---:|
| blue | 3.0 | 84.4% |
| green | 1.0 | 11.4% |
| red | 0.0 | 4.2% |
| **Total** | — | **100%** |

The probabilities sum to 100%, apart from possible rounding.

Notice that softmax preserves the ranking of logits: the highest logit produces the highest probability when the same temperature and no additional filtering are used.

### The important difference

```text
LOGITS
  Raw scores
  [-1.0, 2.0, 0.5]
       |
       | Softmax
       v
PROBABILITIES
  Normalized values
  [0.04, 0.79, 0.17]
```

The numbers in this second diagram are illustrative and rounded.

- Logits can be negative or positive.
- Probabilities are between 0 and 1.
- Probabilities from one softmax distribution sum to 1.
- Logits do not need to sum to any particular value.

---

## 4. Why Can Logits Be Negative?

A logit is an unrestricted numerical score. It is not limited to the range used by probabilities.

For example:

| Token | Logit |
|---|---:|
| apple | 4.0 |
| mango | 1.5 |
| orange | 0.0 |
| airplane | -3.0 |

The negative score for `airplane` means it received a lower raw score than the tokens with larger logits in this example.

It does not mean that the token has a negative probability.

After applying softmax, even a token with a negative logit receives a positive probability, provided it remains in the distribution.

For instance, a logit of `-3.0` can produce a small positive probability.

**Remember:** Negative logits are normal.

---

## 5. Does the Highest Logit Always Become the Next Token?

No. It depends on the decoding strategy.

Suppose the model produces the following logits:

| Token | Logit |
|---|---:|
| blue | 3.0 |
| green | 2.0 |
| red | 1.0 |

There are different ways to select the next token.

### Greedy decoding

Greedy decoding chooses the token with the highest logit, which is also the token with the highest softmax probability before any filtering or temperature changes.

```text
Highest logit
      |
      v
     blue
```

### Sampling

Sampling selects a token randomly according to its probability distribution.

For example, `blue` might have the highest probability, but `green` or `red` could still be selected.

The probability of selecting each token depends on the distribution used for sampling.

### Comparison

| Decoding strategy | How the next token is selected |
|---|---|
| Greedy decoding | Selects the highest-scoring token |
| Sampling | Randomly selects according to probabilities |
| Top-K sampling | Restricts candidates to the K highest-scoring tokens before sampling |
| Top-P sampling | Restricts candidates using cumulative probability before sampling |

Therefore, the highest logit does not always determine the final generated token.

---

## 6. How Temperature Changes Logits

Temperature controls how concentrated or spread out the probability distribution becomes.

A common formula applies temperature \(T\) to logits before softmax:

\[
P_i=\frac{e^{z_i/T}}{\sum_j e^{z_j/T}}
\]

Here:

- \(z_i\) = the original logit.
- \(T\) = temperature.
- \(P_i\) = probability after temperature scaling and softmax.

### High vs low temperature

- **Low temperature:** Makes differences between logits more influential, concentrating probability on the highest-scoring tokens.
- **High temperature:** Makes differences less influential, spreading probability more evenly across tokens.
- **Temperature of 1:** Leaves logits unchanged before softmax.

For example, if the logits are:

```text
blue  = 3.0
green = 2.0
red   = 1.0
```

A lower temperature makes `blue` more dominant in the probability distribution. A higher temperature makes `green` and `red` relatively more likely.

Temperature does not change the original learned model parameters. It changes how the logits are transformed for token selection.

**Important:** Temperature scaling alone does not change the ranking of the logits when \(T\) is positive. It changes the probabilities produced from them.

---

## 7. How Top-K and Top-P Use Logits

Top-K and Top-P are sampling methods that restrict which tokens can be considered.

### Top-K sampling

Top-K keeps the K tokens with the highest logits and excludes the others before sampling.

For example, if \(K=2\):

```text
Original candidates:

blue   = 3.0
green  = 2.0
red    = 1.0
yellow = -1.0

        Top-K (K = 2)
               |
               v

blue   = 3.0
green  = 2.0

red and yellow are excluded
```

The remaining candidates are then converted into a sampling distribution, typically using softmax over the retained logits.

### Top-P sampling

Top-P uses cumulative probability to select a set of likely candidate tokens.

The model first obtains probabilities, then retains a set of high-probability tokens whose cumulative probability reaches the selected threshold, following the implementation's inclusion rule.

For example, with a top-p threshold of 0.90, the retained tokens collectively cover approximately 90% or more of the original probability mass.

The exact candidate set depends on the probability distribution.

### Key difference

| Method | Main criterion |
|---|---|
| Top-K | Number of candidate tokens |
| Top-P | Cumulative probability of candidate tokens |

Both methods influence which token can be selected. Neither changes the underlying model's learned parameters.

---

## 8. Logits at Different Token Positions

An LLM does not necessarily produce just one logit for an entire prompt.

During a forward pass, a causal language model generally produces logits for each input position.

Suppose the input is:

```text
The cat sleeps
```

The model can produce a separate vocabulary-sized logit vector at each position.

Conceptually:

```text
Input tokens:

[The] [cat] [sleeps]
   |     |      |
   v     v      v
  Logits Logits Logits
                  |
                  v
      Predict the next token
```

For next-token generation, the model typically uses the logits at the **last input position** to predict what comes after `sleeps`.

During training, logits at multiple positions are usually used to calculate the next-token prediction loss.

During inference, the prompt is initially processed in a step called **prefill**. After that, generation usually uses the logits from the current final position to select the next token.

---

## 9. What Is the Shape of Logits?

The vocabulary determines the number of logits produced for each position.

Let:

- \(B\) = batch size.
- \(N\) = sequence length.
- \(V\) = vocabulary size.

A typical language model produces logits with the shape:

\[
[B,N,V]
\]

For example:

```text
Batch size       = 2
Sequence length  = 4
Vocabulary size  = 10,000

Logits shape:

[2, 4, 10000]
```

This means:

- 2 sequences are processed in the batch.
- Each sequence has 4 positions.
- Each position has 10,000 vocabulary scores.

When generating the next token, an implementation can select the logits for the last position:

\[
[B,N,V]\rightarrow[B,V]
\]

For a batch size of 2, the resulting shape would be:

```text
[2, 10000]
```

Each sequence now has one score for every vocabulary token.

The exact tensor shapes exposed by a model API may differ depending on its implementation and how the outputs are requested.

---

## 10. Logits During Training vs Inference

Logits are used in both training and inference, but their roles differ.

| Aspect | Training | Inference |
|---|---|---|
| Main purpose | Learn by measuring prediction errors | Generate predictions from a trained model |
| Logits | Usually produced at multiple sequence positions | Next-token selection usually uses the last position |
| Probability conversion | Used to calculate prediction loss | Used to form a distribution for token selection |
| Loss calculation | Used to calculate training loss | Not normally required for ordinary text generation |
| Parameter updates | Gradients and an optimizer update parameters | Model parameters ordinarily remain fixed |
| Repeated token generation | Training uses supplied input sequences and targets | Newly selected tokens are fed back into the model |

During training, the model's logits are compared with the correct next tokens to calculate a loss, often cross-entropy loss.

During inference, logits help determine which token should be generated next.

The same model can produce logits in both situations. The difference is what the surrounding process does with them.

---

## 11. Are Logits a Measure of Confidence?

Not necessarily.

A larger logit means a higher relative score among the candidates under the model's current output transformation. It does not automatically mean the model is factually correct or that its confidence is well calibrated.

For example, a model might assign a high probability to an incorrect answer because of patterns learned during training or limitations in its knowledge.

Also, logits are relative to the other candidate scores. Adding the same constant to every logit leaves the softmax probabilities unchanged.

Therefore:

- A high logit does not guarantee a correct answer.
- A low logit does not mean a token is impossible.
- A probability is not automatically a reliable measure of factual correctness.
- Logits describe model scores, not human-like certainty.

---

## 12. Common Misconceptions

| Misconception | Correct explanation |
|---|---|
| Logits are probabilities. | Logits are raw scores; softmax can convert them into probabilities. |
| Logits must be positive. | Logits can be negative, zero, or positive. |
| A logit of 2 means a 2% probability. | There is no direct percentage interpretation. |
| The highest-logit token is always selected. | Greedy decoding selects it, but sampling may select another token. |
| Logits exist only during inference. | They are also produced during training. |
| The model produces only one logit. | It generally produces one score per vocabulary token at each processed position. |
| A high logit guarantees correctness. | Logits are model scores, not guarantees of factual accuracy. |
| Temperature retrains the model. | Temperature changes the scores used for probability calculation, not the learned parameters. |

---

## 13. Complete Flow: From Logits to Generated Text

Let's connect the concepts.

Suppose the user enters:

```text
The sky is
```

The model processes the prompt and produces a vocabulary-sized vector of logits at the final position.

```text
Prompt: "The sky is"
          |
          v
   Transformer Model
          |
          v
        Logits
          |
          v
 Temperature / Filtering
  (if configured)
          |
          v
   Probability Distribution
          |
          v
   Select the Next Token
          |
          v
         "blue"
          |
          v
 Append "blue" to the sequence
          |
          v
 Recompute the next prediction
          |
          v
      Continue generating
```

The actual generated token is not guaranteed to be `blue`. The example illustrates the process, not a fixed model output.

The process repeats until the model reaches a stopping condition, such as an end-of-sequence token or a generation limit.

---

## 🧠 Simple Mental Model

Think of logits as a **scoreboard for possible next tokens**.

- The Transformer processes the prompt.
- The language modeling head assigns a raw score to each vocabulary token.
- Those scores are logits.
- Softmax can convert them into probabilities.
- The decoding strategy determines how a token is selected.
- The selected token is added to the sequence, and generation continues.

**The key distinction:**

> **Logits are raw scores. Probabilities express a normalized distribution over candidates. Decoding determines how the next token is selected.**

## ✅ Key Takeaways

- Logits are raw numerical scores produced by the language modeling head.
- A typical output contains one logit per vocabulary token at each sequence position.
- Logits can be negative, positive, or zero.
- Softmax converts logits into a probability distribution.
- Greedy decoding chooses the highest-scoring token, while sampling can choose other candidates.
- Temperature, Top-K, and Top-P can influence token selection.
- During training, logits contribute to the prediction loss; during inference, they guide text generation.
- Logits do not guarantee factual correctness or perfectly calibrated confidence.
