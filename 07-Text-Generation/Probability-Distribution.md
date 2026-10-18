# 📊 Probability Distribution in an LLM

## 1. What Is a Probability Distribution?

When an LLM processes a prompt, it produces logits for possible next tokens. These logits can be converted into a **probability distribution** that represents how the model scores the possible next-token choices after normalization.

In simple words:

> **A probability distribution assigns a probability to each possible next token, with all probabilities adding up to 1.**

For example, suppose the prompt is:

```text
The sky is
```

The model might produce this illustrative probability distribution:

| Possible next token | Probability |
|---|---:|
| blue | 70% |
| clear | 15% |
| cloudy | 10% |
| green | 4% |
| banana | 1% |
| **Total** | **100%** |

These numbers are examples, not actual outputs from a particular model.

The model assigns the highest probability to `blue`, but other tokens remain possible.

**Important:** A probability distribution describes the model's relative predictions. It does not guarantee which token will be generated or whether the resulting statement will be factually correct.

---

## 2. Where Does the Probability Distribution Come From?

A typical text-generation pipeline converts logits into probabilities using the **softmax function**.

```text
User Prompt
     |
     v
Tokenization
     |
     v
Transformer Blocks
     |
     v
Language Modeling Head
     |
     v
    LOGITS
     |
     v
    Softmax
     |
     v
PROBABILITY DISTRIBUTION
     |
     v
  Token Selection
     |
     v
  Generated Token
```

Let's understand the important steps.

1. **Logits:** The model produces raw scores for vocabulary tokens.
2. **Softmax:** Converts those scores into normalized probabilities.
3. **Probability distribution:** Represents the probabilities assigned to the candidate tokens.
4. **Token selection:** A decoding strategy selects the next token using these scores or probabilities.

The distribution is typically calculated for the current prediction position. During ordinary autoregressive generation, this is usually the last position in the current input sequence.

---

## 3. What Is Softmax?

Softmax is a mathematical function that converts a vector of logits into a probability distribution.

Its formula is:

\[
P_i=\frac{e^{z_i}}{\sum_{j=1}^{V}e^{z_j}}
\]

Where:

- \(P_i\) = probability assigned to token \(i\).
- \(z_i\) = logit for token \(i\).
- \(e^{z_i}\) = exponential of that logit.
- \(V\) = number of tokens in the vocabulary.
- The denominator = sum of the exponentials of all logits.

Softmax performs two important operations:

- It transforms the raw scores into positive values.
- It normalizes those values so their sum equals 1.

This makes the output suitable for interpreting as a probability distribution.

### Example

Suppose the model produces these illustrative logits:

| Token | Logit |
|---|---:|
| blue | 2.0 |
| green | 1.0 |
| red | 0.0 |

Applying softmax produces approximately:

| Token | Logit | Probability |
|---|---:|---:|
| blue | 2.0 | 66.5% |
| green | 1.0 | 24.5% |
| red | 0.0 | 9.0% |
| **Total** | — | **100%** |

The highest logit produces the highest probability because softmax preserves the ranking of the logits.

The probabilities are not equal to the logits. Softmax transforms the scores into a normalized distribution.

---

## 4. What Does a Probability Actually Mean?

Suppose the model assigns the following probabilities:

<box gap={3}>
  <box gap={1}>
    <row align="center" justify="between">
      **blue**
      <title size="md" color="success">70%</title>
    </row>
    <box background="surface-tertiary" radius="md" height="10px" clip>
      <box background="#16A34A" width="70%" height="10px" radius="md" />
    </box>
  </box>
  <box gap={1}>
    <row align="center" justify="between">
      **clear**
      <title size="md">15%</title>
    </row>
    <box background="surface-tertiary" radius="md" height="10px" clip>
      <box background="#64748B" width="15%" height="10px" radius="md" />
    </box>
  </box>
  <box gap={1}>
    <row align="center" justify="between">
      **cloudy**
      <title size="md">10%</title>
    </row>
    <box background="surface-tertiary" radius="md" height="10px" clip>
      <box background="#64748B" width="10%" height="10px" radius="md" />
    </box>
  </box>
  <box gap={1}>
    <row align="center" justify="between">
      **green**
      <title size="md">4%</title>
    </row>
    <box background="surface-tertiary" radius="md" height="10px" clip>
      <box background="#64748B" width="4%" height="10px" radius="md" />
    </box>
  </box>
  <box gap={1}>
    <row align="center" justify="between">
      **banana**
      <title size="md">1%</title>
    </row>
    <box background="surface-tertiary" radius="md" height="10px" clip>
      <box background="#64748B" width="1%" height="10px" radius="md" />
    </box>
  </box>
</box>

The model assigns 70% probability to `blue`, making it the most likely candidate in this example.

However, **70% does not mean the model is guaranteed to generate `blue`**.

- If greedy decoding is used, the highest-probability candidate is selected.
- If sampling is used, a different candidate can be selected according to the sampling distribution.
- If filtering methods are applied, some candidates may be removed before sampling.

A probability describes the model's distribution, not a guarantee about the next token.

---

## 5. Why Must Probabilities Add Up to 1?

A probability distribution produced by softmax assigns normalized probabilities to the tokens included in the distribution.

For example:

\[
0.70+0.15+0.10+0.04+0.01=1
\]

As percentages:

\[
70\%+15\%+10\%+4\%+1\%=100\%
\]

This means the total probability across all included candidates is 1.

In a real LLM, the vocabulary can contain tens of thousands or more tokens. A simplified example shows only a few candidates, but the complete distribution normally includes the model's entire vocabulary before any candidate filtering.

After Top-K or Top-P filtering, the retained logits are commonly renormalized into a new distribution for sampling. The resulting probabilities over the remaining candidates again sum to 1.

---

## 6. Probability Distribution vs Logits

These two concepts are closely related, but they serve different purposes.

| Feature | Logits | Probability distribution |
|---|---|---|
| Meaning | Raw model scores | Normalized probabilities |
| Produced by | Language modeling head | Usually softmax applied to logits |
| Possible values | Negative, zero, or positive | Between 0 and 1 |
| Must sum to 1? | No | Yes |
| Used for | Scoring possible tokens | Understanding or sampling from relative token probabilities |
| Example | `[2, 1, 0]` | Approximately `[0.665, 0.245, 0.090]` |

The overall relationship is:

```text
Transformer Output
        |
        v
      Logits
    [2, 1, 0]
        |
        | Softmax
        v
 Probabilities
 [0.665, 0.245, 0.090]
        |
        v
   Token Selection
```

The logits in this diagram correspond to the probability values shown, rounded to three decimal places.

**Remember:** Logits are raw scores; probabilities are normalized values derived from those scores.

---

## 7. How Does the Model Select the Next Token?

Once a probability distribution is available, the decoding strategy determines how the next token is chosen.

Consider this illustrative distribution:

| Token | Probability |
|---|---:|
| blue | 60% |
| clear | 25% |
| cloudy | 10% |
| green | 5% |

### Greedy decoding

Greedy decoding chooses the token with the highest probability.

```text
blue = 60%
clear = 25%
cloudy = 10%
green = 5%

Selected token: blue
```

Greedy decoding is deterministic when the distribution and tie-breaking rules are fixed.

### Sampling

Sampling selects a token according to the distribution.

For example, `blue` has a 60% probability, but `clear`, `cloudy`, or `green` may also be selected.

The percentages are illustrative probabilities, not a promise that a particular token will appear in any single generation.

### Comparison

| Method | Selection behavior |
|---|---|
| Greedy decoding | Always chooses the highest-probability token, assuming no tie |
| Sampling | Selects randomly according to the distribution |
| Top-K sampling | Samples from a restricted set of high-scoring candidates |
| Top-P sampling | Samples from a set chosen using cumulative probability |

The probability distribution alone does not specify the decoding strategy. Token selection depends on how the model's outputs are used.

---

## 8. How Temperature Changes the Distribution

Temperature adjusts how concentrated or spread out the probabilities become.

A common approach divides logits by a temperature value before applying softmax:

\[
P_i=\frac{e^{z_i/T}}{\sum_j e^{z_j/T}}
\]

Where:

- \(z_i\) = original logit.
- \(T\) = temperature.
- \(P_i\) = probability after temperature scaling and softmax.

### Low temperature

A low positive temperature makes the distribution more concentrated around the highest-scoring tokens.

```text
Before temperature adjustment:

blue  = 60%
clear = 25%
cloudy = 10%
green = 5%

Low temperature:
blue becomes more dominant.
```

### High temperature

A higher temperature makes the distribution more spread out, giving lower-ranked candidates a greater relative share of the probability.

```text
Before temperature adjustment:

blue  = 60%
clear = 25%
cloudy = 10%
green = 5%

Higher temperature:
the probabilities become more even.
```

These diagrams describe the direction of the effect, not exact recalculated percentages.

### Important points

- Temperature changes the distribution used for token selection.
- A lower temperature does not guarantee a correct answer.
- A higher temperature does not guarantee a creative answer.
- Positive temperature scaling alone preserves the ranking of the original logits.
- At temperature 1, the logits are unchanged before softmax.

Temperature affects the probabilities, not the learned parameters of the model.

---

## 9. How Top-K and Top-P Change the Distribution

Temperature changes how probabilities are distributed across candidates. Top-K and Top-P instead restrict which candidates remain available for sampling.

### Top-K

Top-K retains the K highest-scoring candidates.

For example, if \(K=3\), only the three highest-logit candidates remain eligible for sampling.

```text
Original candidates:

blue   = 60%
clear  = 25%
cloudy = 10%
green  = 5%

Top-K (K = 3):

blue
clear
cloudy

green is excluded.
```

After filtering, the remaining candidates are commonly renormalized. The percentages shown before filtering therefore will not necessarily remain the same afterward.

### Top-P

Top-P retains a set of high-probability candidates based on cumulative probability.

For example, using the distribution above and a top-p threshold of 0.90, the first three candidates collectively account for 95% of the original probability mass, so they are sufficient to reach the threshold.

The exact retained set depends on the distribution, threshold, and implementation's inclusion rules.

### Comparison

| Method | What determines the retained candidates? |
|---|---|
| Temperature | How concentrated the probability distribution is |
| Top-K | The number of highest-scoring candidates |
| Top-P | The cumulative probability of candidate tokens |

These controls are often used together, although the exact order of transformations can vary by implementation.

---

## 10. Probability Distribution at Each Token Position

An LLM can produce a different probability distribution for each input position.

Consider:

```text
The cat is
```

The model's predictions depend on the context available at each position.

```text
Token positions:

[The] [cat] [is]
  |     |    |
  v     v    v
Distribution at each position
               |
               v
      Last position's distribution
               |
               v
       Predict the next token
```

In a causal language model, the representation at a position cannot use future tokens from the same sequence through causal self-attention.

For next-token generation, the distribution at the last input position is typically used to select the next token.

After the model selects a token, it is appended to the sequence. The model then computes the next prediction using the updated context.

For example:

```text
Prompt:
The cat is

First prediction:
sleeping

Updated sequence:
The cat is sleeping

Next prediction:
peacefully
```

These are illustrative tokens. The actual predictions depend on the model and decoding settings.

This repeated process is called **autoregressive generation**.

---

## 11. Does a High Probability Mean the Model Is Correct?

No. A probability distribution describes the model's predictions, not guaranteed factual truth.

Suppose a model assigns a very high probability to a token that fits a familiar but incorrect pattern. It can still generate an incorrect statement.

Several factors matter:

- The information available during training.
- The prompt and its context.
- Patterns learned by the model.
- Ambiguity in the input.
- The decoding strategy.
- Whether the task requires facts that are missing or outdated.

A high next-token probability means that the token is favored by the model under the current distribution. It does not automatically mean the model's overall answer is true.

Also, next-token probabilities should not be confused with a calibrated probability that an entire answer is correct.

---

## 12. Common Misconceptions

| Misconception | Correct explanation |
|---|---|
| The probability distribution contains only one token. | It generally assigns a probability to each vocabulary token before filtering. |
| The highest-probability token must always be selected. | Sampling can select another candidate. |
| Probabilities are the same as logits. | Probabilities are normalized values derived from logits, usually using softmax. |
| A token with a 1% probability is impossible. | It remains possible under sampling if it has not been excluded. |
| Temperature retrains the model. | Temperature changes the distribution used for decoding, not the learned parameters. |
| Top-K and Top-P are the same. | Top-K limits candidate count; Top-P uses cumulative probability. |
| A 90% next-token probability means a 90% chance the entire answer is correct. | Next-token probability is not the same as whole-answer factual confidence. |
| The distribution stays the same throughout generation. | It generally changes as new tokens are added to the context. |

---

## 🧠 Simple Mental Model

Imagine the LLM preparing a list of possible next tokens.

Each candidate receives a score. Softmax turns those scores into probabilities, forming a distribution over the vocabulary.

The decoding method then decides how to choose from that distribution.

```text
Raw Scores
   |
   v
Softmax
   |
   v
Probability Distribution
   |
   v
Greedy or Sampling Strategy
   |
   v
Selected Token
   |
   v
Updated Context
   |
   v
New Probability Distribution
```

The process repeats until generation stops.

## ✅ Key Takeaways

- A probability distribution assigns normalized probabilities to possible next tokens.
- Softmax is commonly used to convert logits into probabilities.
- Probabilities across the complete distribution sum to 1.
- Greedy decoding selects the highest-probability token, while sampling can select other candidates.
- Temperature changes how concentrated the distribution is.
- Top-K and Top-P restrict the candidate tokens available for sampling.
- The distribution generally changes after each generated token.
- A high next-token probability does not guarantee factual correctness.
