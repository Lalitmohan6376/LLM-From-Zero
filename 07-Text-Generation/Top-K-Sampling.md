# 🎯 Top-K Sampling in LLMs

## 1. What Is Top-K Sampling?

**Top-K sampling is a text-generation technique that restricts the next-token candidates to the K tokens with the highest scores or probabilities. The model then samples the next token from those candidates.**

Here, **K represents the number of candidate tokens allowed for sampling.**

For example, suppose an LLM predicts these possible next tokens:

| Token | Probability |
|---|---:|
| sunny | 40% |
| cloudy | 25% |
| rainy | 18% |
| windy | 10% |
| snowy | 7% |

If we set \(K=3\), only the three highest-probability tokens remain eligible:

- `sunny`
- `cloudy`
- `rainy`

The other candidates, `windy` and `snowy`, are excluded from this sampling step.

The model then samples one token from the remaining three.

---

## 2. Where Does Top-K Sampling Fit in the Generation Pipeline?

Top-K sampling is applied after the model produces logits. In a typical generation pipeline, the logits are adjusted and filtered before a token is selected.

```text
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
        Probability Scores
                |
                v
         Top-K Filtering
                |
                v
     Keep K Highest-Scoring Tokens
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

This diagram shows one common conceptual ordering. Actual implementations may apply filtering and probability transformations in a different order.

**Important:** Top-K filtering does not retrain the model or change its learned parameters. It restricts the candidates available during token selection.

---

## 3. How Does Top-K Sampling Work?

Let's understand the complete process using a simple example.

Suppose the model predicts the next token after this prompt:

> The weather today is...

The model produces the following probability distribution:

| Token | Original Probability |
|---|---:|
| sunny | 40% |
| cloudy | 25% |
| rainy | 18% |
| windy | 10% |
| snowy | 7% |

All five probabilities sum to 100%.

### Step 1: Choose a K Value

Suppose we choose:

\[
K=3
\]

This means we want to keep only the three highest-scoring candidates.

### Step 2: Rank the Candidates

The model already has scores for the possible next tokens.

```text
1. sunny    → 40%
2. cloudy   → 25%
3. rainy    → 18%
4. windy    → 10%
5. snowy    →  7%
```

### Step 3: Keep the Top K Tokens

Since \(K=3\), we retain:

```text
sunny  → 40%
cloudy → 25%
rainy  → 18%
```

The remaining tokens are excluded:

```text
windy  → Excluded
snowy  → Excluded
```

Their probabilities are effectively set to zero for this sampling step.

### Step 4: Renormalize the Probabilities

The retained probabilities add up to:

\[
40+25+18=83\%
\]

They no longer sum to 100%, so we normalize them to create a valid probability distribution.

The formula is:

\[
P_i'=\frac{P_i}{\sum_{j\in K}P_j}
\]

Where:

- \(P_i\) = original probability of a retained token
- \(\sum_{j\in K}P_j\) = sum of probabilities for the retained candidates
- \(P_i'\) = normalized probability after filtering

The new probabilities are approximately:

| Token | Original Probability | New Probability |
|---|---:|---:|
| sunny | 40% | 48.2% |
| cloudy | 25% | 30.1% |
| rainy | 18% | 21.7% |
| windy | 10% | 0% |
| snowy | 7% | 0% |

Now the probabilities of the three retained tokens sum to approximately 100%.

### Step 5: Sample the Next Token

The model randomly selects a token according to the new probability distribution.

For example:

- `sunny` has approximately a 48.2% chance.
- `cloudy` has approximately a 30.1% chance.
- `rainy` has approximately a 21.7% chance.

The model might select `cloudy` even though `sunny` has the highest probability.

That is the key difference between sampling and greedy decoding.

---

## 4. Interactive Top-K Simulator

Change the K value to see which candidates remain eligible and how their probabilities are redistributed.

{@body
const [k, setK] = DIL.useState(3);
const candidates = [
  {token:"sunny", p:40},
  {token:"cloudy", p:25},
  {token:"rainy", p:18},
  {token:"windy", p:10},
  {token:"snowy", p:7}
];
const total = candidates.slice(0,k).reduce((sum,item) => sum + item.p, 0);
}
<box border radius="xl" padding={4} gap={4}>
  <row align="center" justify="between">
    <title size="lg">K value</title>
    <title size="xl" tabularNums>{k}</title>
  </row>
  <slider min={1} max={5} step={1} value={k} onChange={setK} marks={[{"value":1,"label":"K = 1"},{"value":3,"label":"K = 3"},{"value":5,"label":"K = 5"}]} />
  <divider />
  {#each candidates as item,i}
    <box key={item.token} gap={1}>
      <row align="center" justify="between">
        <row align="center" gap={2}>
          <text weight="medium">{item.token}</text>
          {#if i < k}
            <badge color="success">Included</badge>
          {:else}
            <badge>Excluded</badge>
          {/if}
        </row>
        <text tabularNums>{i < k ? `${(item.p/total*100).toFixed(1)}%` : "0%"}</text>
      </row>
      <box background="surface-tertiary" radius="md" height="10px" clip>
        <box background={i < k ? "#0D9488" : "#9CA3AF"} radius="md" height="10px" width={`${i < k ? item.p/total*100 : 0}%`} />
      </box>
    </box>
  {/each}
  <text color="secondary" size="sm">The original probabilities are 40%, 25%, 18%, 10%, and 7%. Displayed probabilities are renormalized over the retained candidates.</text>
  {#if k === 1}
    **Observation:** Only `sunny` remains. Sampling becomes equivalent to greedy selection for this example.
  {:else if k === 5}
    **Observation:** All five candidates remain. Top-K filtering removes nothing.
  {:else}
    **Observation:** Only the top {k} candidates can be sampled. The remaining candidates receive zero probability.
  {/if}
</box>

---

## 5. What Happens When We Change K?

The K value controls how many candidates are available for sampling.

| K Value | Effect |
|---|---|
| \(K=1\) | Only the highest-scoring token remains |
| \(K=2\) | Only the two highest-scoring tokens remain |
| \(K=3\) | Only the three highest-scoring tokens remain |
| Larger K | More candidate tokens remain eligible |
| K covers the entire vocabulary | No candidates are removed |

### Small K

A small K restricts the model to a narrow set of high-scoring candidates.

This generally makes the output more constrained and predictable, although sampling among multiple retained tokens can still produce different outputs.

### Large K

A larger K gives the model more candidate tokens.

This can increase variety, but it also permits lower-probability candidates that might be less suitable in context.

**Remember:** A larger K does not guarantee better creativity or better-quality text.

---

## 6. What Happens When K = 1?

When \(K=1\), only the highest-scoring token survives filtering.

```text
Original candidates:

sunny  → 40%
cloudy → 25%
rainy  → 18%
windy  → 10%
snowy  →  7%

After Top-K filtering (K = 1):

sunny  → 100%
cloudy →   0%
rainy  →   0%
windy  →   0%
snowy  →   0%
```

There is only one eligible candidate, so sampling must select `sunny`.

For this token-selection step, Top-1 behaves like greedy decoding, assuming the same logits and no other processing changes the candidate ranking.

However, the complete generated sequence may still depend on other settings and implementation details.

---

## 7. Top-K Sampling vs Greedy Decoding

Both methods favor high-probability tokens, but they select tokens differently.

| Feature | Greedy Decoding | Top-K Sampling |
|---|---|---|
| Candidate tokens | All tokens are considered | Only the top K remain eligible |
| Token selection | Always selects the highest-probability token | Samples from the retained candidates |
| Randomness | No randomness in token selection | Usually stochastic when multiple candidates have nonzero probability |
| Variety | More predictable | Can produce more varied output |
| K parameter | Not required | Required |
| Main behavior | Always takes the current best candidate | Allows alternatives among the best K candidates |

### Example

Suppose the probabilities are:

```text
sunny  → 40%
cloudy → 25%
rainy  → 18%
windy  → 10%
snowy  →  7%
```

**Greedy decoding:** Always selects `sunny`.

**Top-K sampling with K = 3:** Can select `sunny`, `cloudy`, or `rainy`, according to their renormalized probabilities.

The highest-probability token remains the most likely selection, but it is no longer guaranteed to be selected.

---

## 8. Top-K Sampling vs Temperature

Temperature and Top-K sampling control different aspects of generation.

| Feature | Temperature | Top-K Sampling |
|---|---|---|
| Main purpose | Changes the sharpness of the distribution | Restricts the candidate set |
| Changes probabilities? | Yes | Yes, after filtering and renormalization |
| Excludes candidates? | No, not by itself at positive temperature | Yes, all candidates outside the top K |
| Main parameter | Temperature \(T\) | Candidate count \(K\) |
| Can be combined? | Yes | Yes |

### Temperature Example

Temperature changes the relative probabilities of candidates before selection. With positive temperature alone, all finite-logit candidates remain eligible.

### Top-K Example

Top-K explicitly removes candidates outside the selected set.

### Using Both Together

A generation system may apply temperature and Top-K filtering together:

```text
Model logits
     |
     v
Temperature scaling
     |
     v
Probability calculation
     |
     v
Top-K filtering
     |
     v
Renormalization
     |
     v
Random token selection
```

The exact order depends on the implementation.

---

## 9. Advantages of Top-K Sampling

### 1. Removes Low-Ranked Candidates

Tokens outside the top K cannot be selected at that step.

### 2. Allows Controlled Variety

The model can select alternatives instead of always choosing the single highest-probability token.

### 3. Simple to Understand

The K parameter directly controls the maximum number of eligible candidates.

### 4. Can Be Combined With Other Methods

Top-K sampling can be combined with temperature and other generation controls.

---

## 10. Limitations of Top-K Sampling

### 1. K Is Fixed

The number of retained candidates remains K even when the probability distribution changes dramatically.

For example, one context might have a very obvious best token, while another might have many plausible alternatives. A fixed K does not adapt to this difference.

### 2. Useful Tokens Can Be Excluded

A token outside the top K might still be appropriate in context, but Top-K makes it ineligible.

### 3. Larger K Does Not Always Improve Output

Including more candidates can introduce less suitable alternatives.

### 4. It Does Not Guarantee Factual Accuracy

Top-K changes token selection, not the factual reliability of the model's predictions.

### 5. It Does Not Prevent Repetition

The model can still repeat words, phrases, or ideas even when Top-K sampling is used.

---

## 11. Common Misconceptions

### ❌ Top-K means selecting the K most recently generated tokens.

No. K refers to the number of highest-scoring candidate tokens for the current next-token selection.

### ❌ Top-K always selects the highest-probability token.

No. It retains the top K candidates and samples from them. It selects the highest-probability token only when \(K=1\), or when sampling otherwise happens to choose that token.

### ❌ Top-K changes the model's learned parameters.

No. It is a generation-time filtering technique.

### ❌ Top-K = 3 means the model generates three tokens.

No. It means up to three candidates are retained at each token-selection step. Generation may continue for many steps.

### ❌ Increasing K always makes the output better.

No. A larger K allows more alternatives, but those alternatives are not necessarily more relevant or accurate.

---

## 12. 🧠 Simple Mental Model

Imagine that an LLM has produced a list of possible next tokens.

Top-K sampling works like a shortlist:

```text
ALL CANDIDATES
     |
     v
Rank by model scores
     |
     v
Keep the top K
     |
     v
Discard the rest
     |
     v
Sample one token
```

If \(K=3\), the model keeps three candidates and samples one of them. It does not generate all three.

**The key idea:** Top-K sampling restricts the next-token choices to the K highest-scoring candidates, then samples from the remaining probability distribution.

---

## 13. Key Takeaways

- Top-K sampling is a decoding strategy used during LLM text generation.
- K is the number of highest-scoring candidate tokens retained at each step.
- Candidates outside the top K are excluded from that sampling step.
- Retained probabilities are typically renormalized to sum to 1.
- \(K=1\) behaves like greedy token selection under the same candidate ranking.
- Larger K permits more alternatives but does not guarantee better output.
- Temperature changes the distribution's sharpness, while Top-K restricts which candidates can be selected.
- Top-K sampling can be combined with temperature and other decoding strategies.
