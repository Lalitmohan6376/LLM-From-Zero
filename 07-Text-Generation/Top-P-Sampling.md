# 🎯 Top-P Sampling in LLMs

## 1. What Is Top-P Sampling?

**Top-P sampling is a text-generation technique that selects a group of candidate tokens whose combined probability reaches a specified threshold, then samples the next token from that group.**

It is also called **nucleus sampling**.

The parameter \(P\) is a probability threshold between 0 and 1. Unlike Top-K sampling, which keeps a fixed number of candidates, Top-P sampling can keep a different number of candidates at each generation step.

For example, suppose an LLM predicts these next-token probabilities:

| Token | Probability |
|---|---:|
| sunny | 40% |
| cloudy | 25% |
| rainy | 18% |
| windy | 10% |
| snowy | 7% |

If we choose \(P=0.80\), we keep the highest-probability candidates until their cumulative probability reaches or exceeds 80%.

- `sunny` → 40%
- `cloudy` → 40% + 25% = 65%
- `rainy` → 65% + 18% = 83%

The retained group is `sunny`, `cloudy`, and `rainy`.

Their combined probability is 83%, which reaches the 80% threshold.

The model then samples one token from this group after renormalizing its probabilities.

---

## 2. Where Does Top-P Sampling Fit in the LLM Pipeline?

Top-P sampling is part of the token-selection process during inference.

```text id="pflow01"
           User Prompt
                |
                v
        Transformer Model
                |
                v
              Logits
                |
                v
       Apply Temperature
           (optional)
                |
                v
             Softmax
                |
                v
      Probability Distribution
                |
                v
       Sort by Probability
                |
                v
      Calculate Cumulative Sum
                |
                v
       Keep the Nucleus (Top-P)
                |
                v
      Renormalize Probabilities
                |
                v
          Sample One Token
                |
                v
       Add Token to Context
                |
                v
       Predict Next Token Again
```

This is a common conceptual ordering. Actual implementations may apply probability filtering and other transformations in a different order.

**Important:** Top-P sampling does not retrain the model or update its learned parameters. It changes which candidates are eligible for selection during generation.

---

## 3. How Does Top-P Sampling Work?

Let's understand the complete process using a simple example.

Suppose the prompt is:

> The weather today is...

The model produces this probability distribution:

| Token | Probability |
|---|---:|
| sunny | 40% |
| cloudy | 25% |
| rainy | 18% |
| windy | 10% |
| snowy | 7% |

All probabilities sum to 100%.

### Step 1: Choose a P Value

Suppose we choose:

\[
P=0.80
\]

This means the nucleus should contain the highest-probability candidates whose cumulative probability reaches at least 80%.

### Step 2: Sort the Tokens

The tokens are ranked from highest probability to lowest probability.

```text id="psort01"
1. sunny    → 40%
2. cloudy   → 25%
3. rainy    → 18%
4. windy    → 10%
5. snowy    →  7%
```

In this example, they are already sorted.

### Step 3: Calculate Cumulative Probabilities

Cumulative probability means adding the probabilities as we move down the ranked list.

| Token | Probability | Cumulative Probability |
|---|---:|---:|
| sunny | 40% | 40% |
| cloudy | 25% | 65% |
| rainy | 18% | 83% |
| windy | 10% | 93% |
| snowy | 7% | 100% |

We stop when the cumulative probability first reaches or exceeds 80%.

That happens at `rainy`, where the cumulative probability becomes 83%.

### Step 4: Keep the Nucleus

The nucleus is the selected group of tokens.

```text id="pnuc01"
P = 0.80

sunny  → 40%  ┐
cloudy → 25%  ├── Keep
rainy  → 18%  ┘

windy  → 10%  ── Exclude
snowy  →  7%  ── Exclude
```

The retained group contains three tokens.

Notice that their combined probability is 83%, not exactly 80%. The threshold is a cutoff: we include the token that causes the cumulative probability to reach or exceed P.

### Step 5: Renormalize the Probabilities

The retained probabilities add up to 83%.

To sample from this group, we normalize their probabilities so that they sum to 100%.

The formula is:

\[
P_i'=\frac{P_i}{\sum_{j\in S}P_j}
\]

Where:

- \(P_i\) is the original probability of a retained token.
- \(S\) is the set of tokens in the nucleus.
- \(\sum_{j\in S}P_j\) is the total probability of the retained tokens.
- \(P_i'\) is the new probability after normalization.

The new probabilities are approximately:

| Token | Original Probability | New Probability |
|---|---:|---:|
| sunny | 40% | 48.2% |
| cloudy | 25% | 30.1% |
| rainy | 18% | 21.7% |
| windy | 10% | 0% |
| snowy | 7% | 0% |

The retained probabilities now sum to approximately 100%.

### Step 6: Sample the Next Token

The model randomly selects one of the retained tokens according to the new probability distribution.

For example, it could select:

- `sunny` with approximately 48.2% probability
- `cloudy` with approximately 30.1% probability
- `rainy` with approximately 21.7% probability

The model might select `cloudy`, even though `sunny` has the highest probability.

That is why Top-P sampling can produce different outputs from the same prompt.

---

## 4. Interactive Top-P Simulator

Change the P threshold to see how the nucleus changes.

{@body
const [p, setP] = DIL.useState(0.8);
const candidates = [
  {token:"sunny",prob:40},
  {token:"cloudy",prob:25},
  {token:"rainy",prob:18},
  {token:"windy",prob:10},
  {token:"snowy",prob:7}
];
const retained = [];
let cumulative = 0;
for (let i = 0; i < candidates.length; i++) {
  if (cumulative < p * 100) {
    retained.push(i);
    cumulative += candidates[i].prob;
  }
}
const total = retained.reduce((sum,i) => sum + candidates[i].prob, 0);
}
<box border radius="xl" padding={4} gap={4}>
  <row align="center" justify="between">
    <title size="lg">P threshold</title>
    <title size="xl" tabularNums>{p.toFixed(2)}</title>
  </row>
  <slider min={0.1} max={1} step={0.05} value={p} onChange={setP} marks={[{"value":0.1,"label":"0.10"},{"value":0.5,"label":"0.50"},{"value":1,"label":"1.00"}]} />
  <divider />
  {#each candidates as item,i}
    <box key={item.token} gap={1}>
      <row align="center" justify="between">
        <row align="center" gap={2}>
          <text weight="medium">{item.token}</text>
          {#if retained.includes(i)}
            <badge color="success">Included</badge>
          {:else}
            <badge>Excluded</badge>
          {/if}
        </row>
        <text tabularNums>{retained.includes(i) ? `${(item.prob/total*100).toFixed(1)}%` : "0%"}</text>
      </row>
      <box background="surface-tertiary" radius="md" height="10px" clip>
        <box background={retained.includes(i) ? "#0D9488" : "#9CA3AF"} radius="md" height="10px" width={`${retained.includes(i) ? item.prob/total*100 : 0}%`} />
      </box>
    </box>
  {/each}
  <text color="secondary" size="sm">The original probabilities are 40%, 25%, 18%, 10%, and 7%. The displayed probabilities are renormalized across the retained candidates.</text>
  <text>**Nucleus size:** {retained.length} {retained.length === 1 ? "candidate" : "candidates"}</text>
  <text>**Cumulative probability retained:** {cumulative}%</text>
  {#if retained.length === 1}
    **Observation:** Only the highest-probability token remains eligible.
  {:else if retained.length === candidates.length}
    **Observation:** Every candidate is retained. Top-P filtering removes nothing.
  {:else}
    **Observation:** The nucleus contains only the highest-ranked candidates needed to reach the selected threshold.
  {/if}
</box>

---

## 5. What Happens When We Change P?

The P value controls how much cumulative probability the retained candidates must cover.

| P Value | General Effect |
|---|---|
| \(P=0.10\) | Often retains only the highest-probability token |
| \(P=0.50\) | Retains candidates until their cumulative probability reaches at least 50% |
| \(P=0.80\) | Retains candidates until their cumulative probability reaches at least 80% |
| \(P=0.95\) | Usually retains a broader set of candidates |
| \(P=1.00\) | Retains the entire distribution, assuming no additional filtering |

The exact number of retained candidates depends on the probability distribution at that generation step.

A low P value generally produces a smaller nucleus. A high P value generally produces a larger nucleus.

**Important:** P is a cumulative probability threshold, not the number of tokens.

For example, \(P=0.90\) does not mean that 90 tokens are retained or that the model generates 90% of a sentence.

---

## 6. Why Is Top-P Called Nucleus Sampling?

The word *nucleus* refers to the core group of high-probability candidates selected for sampling.

Unlike Top-K, which fixes the number of candidates, Top-P adapts the number of retained candidates to the shape of the probability distribution.

Consider two different situations.

### Situation A: One Token Is Strongly Preferred

```text id="nucA01"
Token A → 85%
Token B →  7%
Token C →  4%
Token D →  2%
Token E →  2%
```

With \(P=0.90\), the nucleus includes Token A and Token B, reaching 92%.

Only two candidates are retained.

### Situation B: Several Tokens Are Plausible

```text id="nucB01"
Token A → 25%
Token B → 22%
Token C → 20%
Token D → 18%
Token E → 15%
```

With \(P=0.90\), the nucleus includes the first four tokens, reaching 85%, then Token E to reach 100%.

All five candidates are retained.

In the second situation, more tokens are needed to reach the threshold.

This ability to adapt to the probability distribution is one of Top-P sampling's main advantages.

---

## 7. Top-P Sampling vs Top-K Sampling

Both methods filter the candidate tokens before sampling, but they use different rules.

| Feature | Top-K Sampling | Top-P Sampling |
|---|---|---|
| Main parameter | Number of tokens \(K\) | Cumulative probability threshold \(P\) |
| Selection rule | Keep the K highest-scoring tokens | Keep the highest-scoring tokens until cumulative probability reaches P |
| Number of candidates | Fixed by K, subject to implementation constraints | Can change at every generation step |
| Adapts to distribution shape | No, not through K itself | Yes |
| Excludes lower-ranked tokens | Yes | Yes, outside the nucleus |
| Can be combined with temperature | Yes | Yes |

### Example

Suppose the model produces:

```text id="kpcomp01"
sunny  → 40%
cloudy → 25%
rainy  → 18%
windy  → 10%
snowy  →  7%
```

**Top-K with \(K=3\):**

Keeps exactly the three highest-ranked candidates.

**Top-P with \(P=0.80\):**

Keeps candidates until their cumulative probability reaches at least 80%.

In this example, both methods retain `sunny`, `cloudy`, and `rainy`.

However, they will not always retain the same number of tokens.

---

## 8. Top-P Sampling vs Temperature

Temperature and Top-P control different parts of token selection.

| Feature | Temperature | Top-P Sampling |
|---|---|---|
| Main purpose | Changes probability concentration | Filters candidates using cumulative probability |
| Changes relative probabilities | Yes | Yes, after filtering and renormalization |
| Removes candidates by itself | No, for positive temperature | Yes |
| Main parameter | \(T\) | \(P\) |
| Can be combined | Yes | Yes |

### Temperature

Temperature makes the probability distribution sharper or flatter before sampling.

A lower positive temperature favors the highest-scoring tokens more strongly. A higher temperature makes the distribution flatter.

### Top-P

Top-P removes candidates outside the selected nucleus, then renormalizes the retained probabilities.

### Using Both Together

A typical conceptual pipeline is:

```text id="tpcombo01"
Model logits
     |
     v
Temperature scaling
     |
     v
Probability distribution
     |
     v
Top-P filtering
     |
     v
Renormalize probabilities
     |
     v
Sample next token
```

The exact order of operations depends on the generation implementation. Since temperature can change the probability distribution, it can also change which tokens enter the nucleus.

---

## 9. Advantages of Top-P Sampling

### 1. Adaptive Candidate Count

It can retain a small set when a few tokens dominate and a larger set when probability is distributed more broadly.

### 2. Controlled Variety

It permits sampling among plausible high-probability candidates rather than always choosing the single highest-probability token.

### 3. Excludes the Distribution's Lower-Ranked Tail

Candidates outside the nucleus cannot be selected during that step.

### 4. Works With Other Decoding Controls

Top-P can be combined with temperature and, in some implementations, Top-K filtering.

---

## 10. Limitations of Top-P Sampling

### 1. It Does Not Guarantee Better Output

The retained candidates can still be incorrect, irrelevant, or unsuitable.

### 2. P Does Not Directly Specify the Candidate Count

The number of retained tokens varies with the probability distribution.

### 3. Low P Can Restrict Variety

A small nucleus may exclude reasonable alternatives.

### 4. High P Can Retain Many Candidates

When probability is spread across many tokens, a high threshold may include a large portion of the distribution.

### 5. It Does Not Eliminate Repetition

A model can still repeat words, phrases, or ideas when using Top-P sampling.

---

## 11. Common Misconceptions

### ❌ Top-P = 0.90 means the model keeps exactly 90 tokens.

No. It means the retained candidates' cumulative probability must reach or exceed 90%.

### ❌ Top-P always keeps the same number of tokens.

No. The nucleus size changes according to the current probability distribution.

### ❌ Top-P always selects the highest-probability token.

No. It samples from the retained candidates, so a lower-probability candidate may be selected.

### ❌ Top-P changes the model's learned parameters.

No. It is a generation-time filtering technique.

### ❌ Top-P = 0.80 means the generated sentence is 80% correct.

No. P is a probability threshold for candidate selection. It is not a factual accuracy score or a measure of answer quality.

### ❌ Top-P and Top-K are the same.

No. Top-K fixes the candidate count, while Top-P uses a cumulative probability threshold.

---

## 12. 🧠 Simple Mental Model

Imagine the model has ranked all possible next tokens by probability.

Top-P sampling keeps adding the strongest candidates to a group until their combined probability reaches the chosen threshold.

```text id="nucflow01"
Rank candidate tokens
         |
         v
Start with the highest probability
         |
         v
Add the next candidate
         |
         v
Cumulative probability reaches P?
         |
         +---- No ----> Add another candidate
         |
         +---- Yes ---> Keep the nucleus
                            |
                            v
                   Renormalize probabilities
                            |
                            v
                    Sample one token
```

**The key idea:** Top-P sampling adapts the number of eligible next tokens to the model's probability distribution, then samples one token from that group.

---

## 13. Key Takeaways

- Top-P sampling is also called nucleus sampling.
- P represents a cumulative probability threshold, usually between 0 and 1.
- Candidates are ranked from highest to lowest probability.
- The nucleus includes the highest-ranked candidates needed to reach or exceed P.
- Retained probabilities are typically renormalized before sampling.
- The number of retained tokens can change at every generation step.
- Top-K uses a fixed candidate count, while Top-P uses a cumulative probability threshold.
- Temperature changes the probability distribution; Top-P filters that distribution.
- Top-P can increase variety compared with greedy decoding, but it does not guarantee correctness or prevent repetition.
