# 🌡️ Temperature in LLMs

## 1. What Is Temperature?

**Temperature is a parameter that controls how predictable or varied an LLM's next-token selection is during text generation.**

It changes the model's logits before they are converted into probabilities.

- **Low temperature:** Makes the model favor higher-probability tokens more strongly.
- **High temperature:** Makes the probability distribution flatter, giving lower-probability tokens a better chance of being selected.
- **Temperature = 1:** Leaves the logits unchanged before softmax.

Temperature does not retrain the model or change its learned parameters. It changes how the model selects tokens during generation.

---

## 2. Where Does Temperature Fit in the LLM Pipeline?

Temperature is applied after the model produces logits and before the next token is selected.

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
       Transformer Model
               |
               v
            Logits
               |
               v
     Apply Temperature
               |
               v
            Softmax
               |
               v
      Probability Distribution
               |
               v
        Select Next Token
               |
               v
       Add Token to Context
               |
               v
        Predict Again...
```

**Important:** Temperature affects token selection probabilities, not the underlying knowledge stored in the model.

---

## 3. How Does Temperature Work?

Suppose an LLM predicts the next token after this prompt:

> The weather today is...

The model produces three possible tokens with the following example logits:

| Token | Logit |
|---|---:|
| sunny | 3.0 |
| cloudy | 2.0 |
| terrible | 1.0 |

A logit is a raw score produced by the model. It is not itself a probability.

Temperature modifies these scores using the following formula.

\[
z_i'=\frac{z_i}{T}
\]

Where:

- \(z_i\) = original logit for a token
- \(T\) = temperature
- \(z_i'\) = adjusted logit
- \(T>0\) = positive temperature value

After adjusting the logits, the model applies softmax to calculate probabilities.

\[
P_i=\frac{e^{z_i/T}}{\sum_j e^{z_j/T}}
\]

Let's understand what happens at different temperatures.

---

## 4. Low Temperature: More Predictable Output

Consider a temperature of \(T=0.5\).

The original logits are divided by 0.5, making their differences larger.

| Token | Original Logit | Adjusted Logit |
|---|---:|---:|
| sunny | 3.0 | 6.0 |
| cloudy | 2.0 | 4.0 |
| terrible | 1.0 | 2.0 |

After softmax, the approximate probabilities become:

<box gap={3}>
  <box gap={1}>
    <row align="center" justify="between">
      **sunny**
      <text color="secondary" size="sm">86.7%</text>
    </row>
    <box background="surface-tertiary" radius="md" height="10px" clip>
      <box background="#16A34A" height="10px" width="86.7%" radius="md" />
    </box>
  </box>
  <box gap={1}>
    <row align="center" justify="between">
      **cloudy**
      <text color="secondary" size="sm">11.7%</text>
    </row>
    <box background="surface-tertiary" radius="md" height="10px" clip>
      <box background="#16A34A" height="10px" width="11.7%" radius="md" />
    </box>
  </box>
  <box gap={1}>
    <row align="center" justify="between">
      **terrible**
      <text color="secondary" size="sm">1.6%</text>
    </row>
    <box background="surface-tertiary" radius="md" height="10px" clip>
      <box background="#16A34A" height="10px" width="1.6%" radius="md" />
    </box>
  </box>
</box>

The model strongly favors `sunny`.

If it samples from this distribution, `sunny` is much more likely to be selected than the other tokens.

**Result:** The output tends to be more predictable and consistent.

### When Is Low Temperature Useful?

- Factual question answering
- Structured output
- Code generation when consistency is preferred
- Tasks where predictable wording is useful

Low temperature does not guarantee factual correctness or bug-free code.

---

## 5. High Temperature: More Varied Output

Now consider a temperature of \(T=2.0\).

The original logits are divided by 2, making their differences smaller.

| Token | Original Logit | Adjusted Logit |
|---|---:|---:|
| sunny | 3.0 | 1.5 |
| cloudy | 2.0 | 1.0 |
| terrible | 1.0 | 0.5 |

After softmax, the approximate probabilities become:

<box gap={3}>
  <box gap={1}>
    <row align="center" justify="between">
      **sunny**
      <text color="secondary" size="sm">50.6%</text>
    </row>
    <box background="surface-tertiary" radius="md" height="10px" clip>
      <box background="#2563EB" height="10px" width="50.6%" radius="md" />
    </box>
  </box>
  <box gap={1}>
    <row align="center" justify="between">
      **cloudy**
      <text color="secondary" size="sm">30.7%</text>
    </row>
    <box background="surface-tertiary" radius="md" height="10px" clip>
      <box background="#2563EB" height="10px" width="30.7%" radius="md" />
    </box>
  </box>
  <box gap={1}>
    <row align="center" justify="between">
      **terrible**
      <text color="secondary" size="sm">18.6%</text>
    </row>
    <box background="surface-tertiary" radius="md" height="10px" clip>
      <box background="#2563EB" height="10px" width="18.6%" radius="md" />
    </box>
  </box>
</box>

Now `cloudy` and `terrible` have a greater chance of being selected than they had at low temperature.

**Result:** The model can produce more varied and less predictable output.

### When Is High Temperature Useful?

- Creative writing
- Brainstorming
- Generating alternative ideas
- Exploring different possible phrasings

Higher temperature can also increase the likelihood of irrelevant or incoherent output.

*The probabilities above are illustrative and may differ slightly due to rounding.*

---

## 6. Compare Different Temperature Values

Using the same example logits of `[3, 2, 1]`, the distribution changes as follows:

| Temperature | Sunny | Cloudy | Terrible |
|---:|---:|---:|---:|
| 0.5 | 86.7% | 11.7% | 1.6% |
| 1.0 | 66.5% | 24.5% | 9.0% |
| 2.0 | 50.6% | 30.7% | 18.6% |

<text color="secondary" size="sm">Percentages may not sum to exactly 100% because of rounding.</text>

Notice the pattern:

- As temperature decreases toward zero, the highest-logit token becomes increasingly dominant.
- At temperature 1, the original logits go directly into softmax.
- As temperature increases, the distribution becomes flatter.
- At very high temperatures, the probabilities approach a uniform distribution across the available vocabulary, assuming finite logits.

---

## 7. Interactive Temperature Simulator

Change the temperature to see how the probabilities of our three example tokens change.

{@body
const [temp, setTemp] = DIL.useState(1);
const logits = [3, 2, 1];
const tokens = ["sunny", "cloudy", "terrible"];
const exps = logits.map(v => Math.exp(v / temp));
const total = exps.reduce((sum, v) => sum + v, 0);
const probs = exps.map(v => v / total * 100);
}
<box border radius="xl" padding={4} gap={4}>
  <row align="center" justify="between">
    <title size="lg">Temperature</title>
    <title size="xl" color="default" tabularNums>{temp.toFixed(1)}</title>
  </row>
  <slider min={0.2} max={3} step={0.1} value={temp} onChange={setTemp} marks={[{"value":0.2,"label":"0.2 — Low"},{"value":1,"label":"1.0 — Standard"},{"value":3,"label":"3.0 — High"}]} />
  <divider />
  {#each tokens as token, i}
    <box gap={2} key={token}>
      <row align="center" justify="between">
        <text weight="medium">{token}</text>
        <title size="md" tabularNums>{probs[i].toFixed(1)}%</title>
      </row>
      <box background="surface-tertiary" radius="md" height="12px" clip>
        <box background="#0D9488" radius="md" height="12px" width={`${probs[i]}%`} />
      </box>
    </box>
  {/each}
  <text color="secondary" size="sm">These probabilities are calculated from the example logits [3, 2, 1]. They are not outputs from a live LLM.</text>
  {#if temp < 0.7}
    **Observation:** The highest-scoring token dominates the distribution.
  {:else if temp <= 1.3}
    **Observation:** The model still favors the highest-scoring token, while alternatives retain meaningful probabilities.
  {:else}
    **Observation:** The distribution is flatter, so lower-scoring alternatives become more likely.
  {/if}
</box>

---

## 8. Does Temperature Change Which Token Has the Highest Probability?

For any finite set of logits and a positive temperature, **temperature alone does not change the ranking of tokens**.

Suppose the original logits are:

```text
sunny    = 3.0
cloudy   = 2.0
terrible = 1.0
```

Dividing all logits by the same positive number preserves their order.

```text
Original ranking:
sunny > cloudy > terrible

After low temperature:
sunny > cloudy > terrible

After high temperature:
sunny > cloudy > terrible
```

The probabilities change, but the ranking remains the same.

This means `sunny` remains the most probable token in our example at every positive temperature.

However, the token that is actually generated may differ because a sampling method can select a lower-probability token.

### What If We Use Greedy Decoding?

Greedy decoding selects the highest-probability token at each step.

Because temperature alone preserves the ranking, applying positive temperature scaling before greedy selection does not change the selected token, assuming no other processing or tie-breaking changes.

Temperature is primarily useful when the decoding strategy uses probabilities to sample tokens.

---

## 9. Temperature vs Greedy Decoding vs Sampling

These concepts are related, but they are not the same.

| Concept | Purpose |
|---|---|
| Temperature | Adjusts the sharpness of the probability distribution |
| Greedy decoding | Always selects the highest-probability token |
| Sampling | Randomly selects a token according to a probability distribution |
| Top-K sampling | Restricts sampling to the K highest-scoring candidate tokens |
| Top-P sampling | Restricts sampling to a candidate set based on cumulative probability |

For example, if the distribution is:

```text
sunny    = 70%
cloudy   = 20%
terrible = 10%
```

Greedy decoding always selects `sunny`.

Sampling may select `sunny`, `cloudy`, or `terrible`, with the corresponding probabilities.

If temperature changes the distribution to:

```text
sunny    = 50%
cloudy   = 30%
terrible = 20%
```

sampling becomes more varied, even though `sunny` remains the highest-probability token.

---

## 10. Can Temperature Be Zero?

Some interfaces allow users to specify `temperature = 0`.

Mathematically, the formula \(z_i/T\) is undefined at exactly zero. Implementations generally treat zero temperature as a request for deterministic or greedy-style selection, or handle it through a special case.

Therefore:

- Positive temperature: scales logits before softmax.
- Temperature near zero: concentrates probability on the highest-logit token.
- Temperature exactly zero: typically handled specially by the generation implementation.

Zero temperature does not mean the model stops predicting. It means the implementation generally avoids ordinary random sampling.

---

## 11. Does Temperature Affect Training?

Temperature is commonly discussed as a generation setting during inference.

### During Training

The model normally uses its logits to calculate a training loss, such as cross-entropy, against the correct next tokens. Standard training does not require the same generation temperature setting.

### During Inference

The model produces logits, and the generation procedure may apply temperature before sampling the next token.

```text
TRAINING
--------
Input tokens
     |
     v
Model forward pass
     |
     v
Logits
     |
     v
Loss calculation
     |
     v
Backpropagation and parameter updates


INFERENCE
---------
Prompt tokens
     |
     v
Model forward pass
     |
     v
Logits
     |
     v
Temperature scaling (optional)
     |
     v
Probability distribution
     |
     v
Token selection
```

During ordinary inference, temperature does not update the model's learned parameters.

---

## 12. Common Misconceptions

### ❌ High temperature makes the model smarter.

Temperature changes token-selection probabilities. It does not increase the model's intelligence or knowledge.

### ❌ Low temperature guarantees correct answers.

A low temperature makes selection more predictable, but the highest-probability continuation can still be incorrect.

### ❌ High temperature always produces creative text.

It can encourage variety, but it can also produce incoherent or irrelevant text.

### ❌ Temperature changes the model's learned weights.

Temperature scaling during generation does not change the learned parameters.

### ❌ Temperature alone changes the ranking of tokens.

Positive temperature scaling preserves the ranking of logits. It changes the probability gaps, not their order.

### ❌ Every LLM uses the same default temperature.

Defaults and supported ranges depend on the model, API, application, and generation implementation.

---

## 13. 🧠 Simple Mental Model

Imagine three candidates for the next token:

- `sunny` is the strongest candidate.
- `cloudy` is the second strongest.
- `terrible` is the weakest.

Temperature controls how strongly the probability distribution favors the strongest candidate.

```text
LOW TEMPERATURE
sunny    █████████████████
cloudy   ██
terrible ▏

HIGH TEMPERATURE
sunny    ██████████
cloudy   ██████
terrible ████
```

The strongest candidate remains the strongest, but the weaker candidates receive a greater share of the probability at higher temperatures.

**Remember:** Temperature changes the probability distribution used for token selection; it does not change the model's learned knowledge.

---

## 14. Key Takeaways

- Temperature controls how concentrated or flat the next-token probability distribution is.
- It is applied to logits before softmax.
- Lower positive temperatures favor the highest-logit tokens more strongly.
- Higher temperatures make lower-logit alternatives more likely under sampling.
- Positive temperature scaling alone preserves token ranking.
- Greedy decoding ignores the probability differences when choosing a token because it always takes the highest-probability candidate.
- Temperature is a generation setting, not a model-training update.
- Temperature works alongside other decoding methods, including top-K and top-P sampling.
