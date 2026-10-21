# 🎯 Greedy Decoding in an LLM

## 1. What Is Greedy Decoding?

**Greedy decoding is a text-generation strategy that selects the token with the highest probability at each generation step.**

In an LLM, the model produces logits for possible next tokens. These logits can be converted into probabilities, and greedy decoding selects the token with the highest probability.

For example, suppose the prompt is:

```text
The sky is
```

The model produces this illustrative probability distribution:

| Possible next token | Probability |
|---|---:|
| blue | 70% |
| clear | 15% |
| cloudy | 10% |
| green | 5% |

Greedy decoding selects `blue` because it has the highest probability.

The sequence becomes:

```text
The sky is blue
```

The model then predicts the next token using the updated context.

**The key idea:** At every step, greedy decoding chooses the single highest-probability token rather than randomly sampling from multiple candidates.

---

## 2. How Does Greedy Decoding Work?

The process follows a simple sequence.

```text
Input Prompt
     |
     v
Transformer Model
     |
     v
Next-Token Logits
     |
     v
Probability Distribution
     |
     v
Select Highest-Probability Token
     |
     v
Append Token to Context
     |
     v
Predict the Next Token
     |
     v
Repeat Until Generation Stops
```

Let's break it down:

1. The model receives the current prompt or sequence.
2. The Transformer processes the available context.
3. The language modeling head produces logits for the vocabulary.
4. The logits are converted into probabilities, typically using softmax.
5. Greedy decoding selects the token with the highest probability.
6. The selected token is appended to the sequence.
7. The model predicts again using the updated context.
8. The process continues until a stopping condition is reached.

Greedy decoding does not require random sampling to select each token.

---

## 3. Step-by-Step Example

Suppose the prompt is:

```text
I am learning
```

Imagine the model produces the following probabilities at each step.

<box border radius="xl" padding={3} gap={3}>
  <box gap={2}>
    <row align="center" justify="between">
      <title size="md">Step 1</title>
      <badge color="success">Selected</badge>
    </row>
    <text color="secondary" size="sm">Current context: `I am learning`</text>
    <row align="center" justify="between">
      `Python` — 60%
      <icon name="check-circle" color="success" size="lg" />
    </row>
    <box background="surface-tertiary" radius="md" height="8px" clip>
      <box background="#16A34A" width="60%" height="8px" radius="md" />
    </box>
    <row align="center" justify="between">
      `English` — 25%
      <text color="secondary" size="sm">25%</text>
    </row>
    <box background="surface-tertiary" radius="md" height="8px" clip>
      <box background="#64748B" width="25%" height="8px" radius="md" />
    </box>
    <row align="center" justify="between">
      `quickly` — 15%
      <text color="secondary" size="sm">15%</text>
    </row>
    <box background="surface-tertiary" radius="md" height="8px" clip>
      <box background="#64748B" width="15%" height="8px" radius="md" />
    </box>
    <text weight="medium">Updated sequence: `I am learning Python`</text>
  </box>
  <divider color="subtle" />
  <box gap={2}>
    <title size="md">Step 2</title>
    <text color="secondary" size="sm">Current context: `I am learning Python`</text>
    <row align="center" justify="between">
      `programming` — 75%
      <icon name="check-circle" color="success" size="lg" />
    </row>
    <box background="surface-tertiary" radius="md" height="8px" clip>
      <box background="#16A34A" width="75%" height="8px" radius="md" />
    </box>
    <row align="center" justify="between">
      `online` — 15%
      <text color="secondary" size="sm">15%</text>
    </row>
    <box background="surface-tertiary" radius="md" height="8px" clip>
      <box background="#64748B" width="15%" height="8px" radius="md" />
    </box>
    <row align="center" justify="between">
      `today` — 10%
      <text color="secondary" size="sm">10%</text>
    </row>
    <box background="surface-tertiary" radius="md" height="8px" clip>
      <box background="#64748B" width="10%" height="8px" radius="md" />
    </box>
    <text weight="medium">Updated sequence: `I am learning Python programming`</text>
  </box>
</box>

The probabilities above are illustrative.

Notice what happens:

- At Step 1, the model selects `Python` because it has the highest probability.
- At Step 2, the model uses the updated context and selects `programming`.
- The same selection rule is applied again at every step.

Greedy decoding makes a locally optimal choice at each step: it selects the highest-probability next token for the current context.

It does not compare every possible complete sentence before making that choice.

---

## 4. The Mathematical Idea Behind Greedy Decoding

Let \(x\) represent the current sequence and \(v\) represent a candidate next token.

The model estimates a probability for each candidate:

\[
P(v\mid x)
\]

Greedy decoding chooses the token with the largest probability:

\[
v^*=\arg\max_v P(v\mid x)
\]

Here:

- \(x\) = the current context.
- \(v\) = a possible next token.
- \(P(v\mid x)\) = the probability assigned to that token given the context.
- \(v^*\) = the selected next token.
- \(\arg\max\) = choose the candidate with the largest value.

In simple words:

> Calculate the probabilities, compare the candidates, and select the token with the highest probability.

Because softmax preserves the ranking of logits, selecting the highest logit produces the same choice as selecting the highest probability when the same unfiltered logits and temperature are used.

If multiple tokens tie for the maximum, the implementation's tie-breaking rule determines which one is selected.

---

## 5. Does Greedy Decoding Always Produce the Best Answer?

No.

Greedy decoding chooses the best next token according to the model's current distribution. That does not guarantee the best overall sentence or answer.

Consider this simplified example:

```text
Prompt:
The animal

Possible next tokens:

is   → 55%
was  → 30%
can  → 15%
```

Greedy decoding chooses `is`.

But selecting the highest-probability token at the current step does not mean that the complete continuation will have the highest possible sequence probability among all alternatives.

A token with a slightly lower probability at the current step could lead to a continuation that is better overall under a chosen sequence-level scoring objective.

Greedy decoding does not look ahead and compare all possible future continuations.

**Important distinction:**

- **Locally optimal:** The highest-probability token at the current step.
- **Globally optimal:** The best complete sequence according to a defined scoring objective.

Greedy decoding guarantees the first choice, not the second.

---

## 6. Greedy Decoding vs Sampling

Both strategies use the model's next-token predictions, but they select tokens differently.

Suppose the model produces this distribution:

| Token | Probability |
|---|---:|
| blue | 60% |
| green | 25% |
| red | 15% |

### Greedy decoding

Greedy decoding always selects `blue` for this distribution because it has the highest probability.

```text
blue  = 60%  ← Selected
green = 25%
red   = 15%
```

### Sampling

Sampling selects a token randomly according to the probability distribution.

```text
blue  = 60%
green = 25%
red   = 15%
```

`Blue` is more likely to be selected, but `green` or `red` can also be selected.

| Feature | Greedy decoding | Sampling |
|---|---|---|
| Selection | Highest-probability token | Random selection based on probabilities |
| Randomness in token choice | No, assuming fixed outputs and tie-breaking | Yes |
| Output for the same context | Same token under fixed settings | Can differ |
| Diversity | Often lower | Can be higher |
| Can select a lower-probability token? | No, unless tied for the maximum | Yes, if it remains eligible |
| Main consideration | Predictable, locally highest-probability choices | Variety controlled by the sampling distribution |

Sampling is not automatically better, and greedy decoding is not automatically worse. The suitable strategy depends on the task.

---

## 7. Does Greedy Decoding Use Temperature?

Greedy decoding does not need temperature to choose the highest-probability token.

With the original logits, selecting the largest logit gives the same token as selecting the largest softmax probability.

Dividing all logits by a positive temperature before applying softmax does not change their ranking.

For example:

```text
Original logits:

blue  = 3.0
green = 2.0
red   = 1.0
```

The highest logit is `blue`.

With any positive temperature applied uniformly to these logits, `blue` remains the highest-scoring token.

Temperature can change the distribution's probabilities, but it does not change the greedy choice unless additional processing changes candidate eligibility or the selection setup.

---

## 8. What Happens When Greedy Decoding Repeats?

Greedy decoding can sometimes produce repetitive or overly predictable text.

For example, a model might generate a continuation like:

```text
The answer is very important.
The answer is very important.
The answer is very important.
```

This is an illustrative failure case, not a guaranteed behavior.

Why can repetition happen?

- The current context may favor a token that reinforces a previous phrase.
- The model's highest-probability choices can repeatedly lead into similar patterns.
- Greedy decoding does not randomly explore alternative tokens.
- Some generation setups can apply repetition penalties or other processing, which may affect the selected tokens.

Greedy decoding itself does not require repetition. It simply selects the highest-probability eligible token at each step.

---

## 9. When Is Greedy Decoding Useful?

Greedy decoding can be useful when predictable, straightforward output is desirable.

Examples include:

- Simple text completion.
- Some structured-output tasks.
- Predictable, short responses.
- Tasks where variation between generations is undesirable.

However, its suitability depends on the model, task, and output constraints. Greedy decoding does not guarantee valid JSON, correct code, factual answers, or the best possible result.

For creative writing or applications that benefit from diverse outputs, sampling methods may be preferable.

---

## 10. Common Misconceptions

| Misconception | Correct explanation |
|---|---|
| Greedy decoding selects a complete sentence at once. | It selects one next token per generation step. |
| It randomly selects a token. | It selects the highest-probability eligible token, with tie-breaking determined by the implementation. |
| It always produces the globally best sequence. | It makes locally highest-probability choices without exhaustive lookahead. |
| It always produces repetitive text. | Repetition is possible, but not inevitable. |
| Temperature must be used for greedy decoding. | Greedy selection can be performed directly from logits. |
| The highest-probability token must be factually correct. | Model probabilities do not guarantee correctness. |
| Greedy decoding and beam search are identical. | Greedy decoding chooses one token at a time; beam search maintains multiple candidate sequences. |

---

## 🧠 Simple Mental Model

Imagine that the model gives you three choices for the next token:

```text
blue  → 70%
green → 20%
red   → 10%
```

Greedy decoding always picks `blue` because it has the highest probability.

Then the model processes the updated context and produces a new set of probabilities for the next token.

The process repeats:

```text
Current Context
      |
      v
Calculate Next-Token Scores
      |
      v
Choose the Highest-Probability Token
      |
      v
Append the Token
      |
      v
Repeat
```

**Remember:** Greedy decoding is a simple selection strategy, not a guarantee that the complete generated answer will be optimal or correct.

## ✅ Key Takeaways

- Greedy decoding selects the highest-probability next token at each step.
- The model repeats this process using the updated context.
- It is deterministic when model outputs, settings, and tie-breaking are fixed.
- It makes locally optimal choices, not necessarily globally optimal sequence choices.
- Unlike sampling, it does not intentionally select lower-probability tokens.
- It can be predictable and efficient, but may produce repetitive or less diverse text.
- The quality of the result still depends on the model, prompt, and generation setup.
