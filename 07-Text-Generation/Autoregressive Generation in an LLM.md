# 🔄 Autoregressive Generation in an LLM

## 1. What Is Autoregressive Generation?

**Autoregressive generation is the process of generating text one token at a time, using the previously available tokens as context for predicting the next token.**

Modern GPT-style LLMs use this process to generate text.

For example, suppose the prompt is:

```text
I love
```

The model predicts a possible next token:

```text
coding
```

The sequence becomes:

```text
I love coding
```

Now the model uses the updated sequence to predict another token:

```text
I love coding because
```

It continues this process until it reaches a stopping condition.

### The core idea

```text
Initial Prompt
      |
      v
Predict Next Token
      |
      v
Select a Token
      |
      v
Add Token to the Sequence
      |
      v
Predict the Next Token Again
      |
      v
Repeat Until Generation Stops
```

The important idea is that **each newly generated token can influence the tokens generated after it**.

The example above illustrates the process; an actual model may generate different tokens.

---

## 2. Why Is It Called Autoregressive?

Let's break the term into two parts.

- **Auto:** The process continues using its own generated output.
- **Regressive:** The prediction depends on previously available values or elements in the sequence.

In autoregressive text generation, the model predicts the next token using the existing context, which can include tokens it generated itself.

For example:

```text
Prompt:
The cat

Step 1:
The cat is

Step 2:
The cat is sleeping

Step 3:
The cat is sleeping peacefully
```

At each step, the previously generated token becomes part of the context for the next prediction.

This is why the process is called autoregressive generation.

---

## 3. Complete Autoregressive Generation Pipeline

Let's follow the process from the user's prompt to the generated text.

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
Probability Distribution
     |
     v
Select Next Token
     |
     v
Append Token to Context
     |
     v
Check Stopping Condition
     |
     +------ Continue ------+
     |                      |
     |                      v
     |                Transformer Model
     |                      |
     |                      v
     |                Predict Again
     |
     +------ Stop ----------> Final Generated Text
```

The main steps are:

1. The user provides a prompt.
2. The tokenizer converts the prompt into token IDs.
3. The model processes the available context.
4. The language modeling head produces logits for possible next tokens.
5. The logits are converted into probabilities, usually through softmax and any configured decoding transformations.
6. A decoding strategy selects the next token.
7. The selected token is added to the sequence.
8. The model predicts again using the updated context.
9. The process continues until generation stops.

The model's learned parameters ordinarily remain fixed throughout this inference process.

---

## 4. Step-by-Step Example

Suppose the user enters:

```text
Prompt: "I am learning"
```

Imagine the model generates the following tokens.

<box border radius="xl" padding={3} gap={3}>
  <row align="start" gap={3}>
    <box background="surface-secondary" radius="lg" padding={2} align="center" justify="center" minWidth="44px">
      <title size="lg">1</title>
    </box>
    <box flex="1" gap={1}>
      **Initial prompt**

      `I am learning`

      <text color="secondary" size="sm">The model receives the prompt as its initial context.</text>
    </box>
  </row>
  <divider color="subtle" />
  <row align="start" gap={3}>
    <box background="surface-secondary" radius="lg" padding={2} align="center" justify="center" minWidth="44px">
      <title size="lg">2</title>
    </box>
    <box flex="1" gap={1}>
      **First token generated**

      `I am learning Python`

      <text color="secondary" size="sm">The model selects `Python` as the next token.</text>
    </box>
  </row>
  <divider color="subtle" />
  <row align="start" gap={3}>
    <box background="surface-secondary" radius="lg" padding={2} align="center" justify="center" minWidth="44px">
      <title size="lg">3</title>
    </box>
    <box flex="1" gap={1}>
      **Second token generated**

      `I am learning Python programming`

      <text color="secondary" size="sm">The model now predicts using the updated context, including `Python`.</text>
    </box>
  </row>
  <divider color="subtle" />
  <row align="start" gap={3}>
    <box background="surface-secondary" radius="lg" padding={2} align="center" justify="center" minWidth="44px">
      <title size="lg">4</title>
    </box>
    <box flex="1" gap={1}>
      **Third token generated**

      `I am learning Python programming online`

      <text color="secondary" size="sm">The new token is appended, and the process can continue.</text>
    </box>
  </row>
</box>

These are illustrative generation steps. Real tokenization may split words differently, so a generated token does not always correspond to one complete word.

Notice the pattern: the model does not need to generate the entire final sentence in one step. It repeatedly predicts and appends tokens.

---

## 5. How Does Each New Token Affect the Next Prediction?

This is the most important part of autoregressive generation.

Suppose the prompt is:

```text
The dog
```

The model might predict these possible next tokens:

| Candidate token | Illustrative probability |
|---|---:|
| is | 50% |
| runs | 25% |
| likes | 15% |
| sleeps | 10% |

Imagine the model selects `runs`.

The sequence becomes:

```text
The dog runs
```

The next prediction is now based on the updated context:

```text
The dog runs
```

The model might predict tokens such as `fast`, `outside`, or `away`.

The distribution has changed because the context has changed.

If the first selected token had been `sleeps` instead, the model would have received a different context and could have generated a different continuation.

**Therefore, an early token can influence the direction of the entire generated passage.**

---

## 6. How Do Logits and Probabilities Fit Into This Process?

Autoregressive generation uses the model's output scores to choose the next token.

The simplified process is:

```text
Current Context
      |
      v
Transformer Blocks
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
Decoding Strategy
      |
      v
Selected Token
```

### Logits

Logits are raw scores assigned to possible vocabulary tokens.

### Probability distribution

Softmax commonly converts the logits into normalized probabilities.

### Decoding strategy

The decoding strategy determines how the next token is selected.

| Strategy | Behavior |
|---|---|
| Greedy decoding | Chooses the highest-probability token |
| Sampling | Samples according to the probability distribution |
| Top-K sampling | Restricts candidates to the K highest-scoring tokens |
| Top-P sampling | Restricts candidates according to cumulative probability |

Temperature can also change the probability distribution before sampling.

The chosen token becomes part of the context for the next generation step.

---

## 7. What Happens Inside the Transformer During Generation?

The model must process the available context to predict the next token.

Consider this input:

```text
The sky is
```

A simplified view of the processing is:

```text
Input Tokens
     |
     v
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
Final Hidden Representation
     |
     v
Language Modeling Head
     |
     v
Next-Token Logits
```

The diagram shows three blocks only for illustration. Real models can contain many more.

Within the Transformer blocks:

- Causal self-attention uses the permitted context to build contextual representations.
- Feed-forward networks transform representations at each position.
- Residual connections and normalization help organize the computations.

The final hidden representation at the last position is typically mapped to vocabulary logits for the next-token prediction.

The model then selects a token and continues the generation process.

---

## 8. What Is Causal Masking's Role?

Causal masking prevents a token position from attending to future positions through causal self-attention.

During generation, future tokens have not yet been generated, so the model cannot use them as part of the current context.

For example:

```text
Available context:

[The] [cat] [is]

Unknown future:

[sleeping] [...]
```

The model predicts the next token using the available context, without looking at the unknown future tokens.

During training, causal masking also ensures that a position cannot access future tokens in the training sequence through the masked attention operation.

This is essential for training a model to predict the next token without leaking the answer into its prediction.

---

## 9. Does the Model Reprocess the Entire Sequence Every Time?

Conceptually, every next-token prediction depends on the current sequence. However, efficient implementations do not necessarily recompute every previous attention key and value from scratch.

There are two important stages.

### Prefill

During prefill, the model processes the prompt's existing tokens.

For example:

```text
Prompt:
Explain machine learning
```

The model processes the prompt and prepares the information needed for generation.

### Decode

During decoding, the model generates new tokens one at a time.

For example:

```text
Prompt:
Explain machine learning

Generated token 1:
Machine

Generated token 2:
learning

Generated token 3:
is
```

These generated tokens are illustrative.

### KV cache

Many Transformer implementations use a **KV cache** to store previously computed attention keys and values.

Instead of recomputing all past keys and values at every step, the model can reuse the cached values and calculate the new token's contribution.

```text
Prompt
  |
  v
Prefill
  |
  v
Store Attention Keys and Values
  |
  v
Generate One Token
  |
  v
Reuse KV Cache + Process New Token
  |
  v
Generate Another Token
  |
  v
Repeat
```

The KV cache improves generation efficiency, particularly for long contexts. It stores intermediate attention information; it does not update the model's learned parameters.

The exact caching and computation strategy depends on the implementation.

---

## 10. When Does Autoregressive Generation Stop?

The process does not continue indefinitely. Generation normally stops when a configured condition is met.

Common stopping conditions include:

- **End-of-sequence token:** The model generates a token that signals the end of the sequence.
- **Maximum generation length:** The allowed number of new tokens has been reached.
- **Application-defined stop sequence:** A configured sequence indicates that generation should end.
- **Other runtime limits:** The surrounding system may impose additional constraints.

The precise stopping rules depend on the model and generation setup.

```text
Predict Next Token
        |
        v
  Append Token
        |
        v
 Stop Condition Met?
      /       \
    No         Yes
    |            |
    v            v
Generate Again  Finish
```

The prompt itself does not necessarily count as newly generated text. Many generation interfaces set a separate limit for the number of new tokens.

---

## 11. Autoregressive Generation vs Training

Autoregressive generation is closely related to next-token prediction during training, but the processes serve different purposes.

| Aspect | Training | Autoregressive inference |
|---|---|---|
| Main purpose | Learn model parameters | Generate new text |
| Input | Training sequences | Prompt and previously generated tokens |
| Target next tokens | Known from the training data | Usually unknown in advance |
| Loss calculation | Used to measure prediction errors | Not normally needed for ordinary generation |
| Parameter updates | Yes | No |
| Token processing | Multiple positions can be processed in parallel during training | New output tokens are generally generated sequentially |
| Context | Training sequence and its targets | Current prompt plus generated tokens |

During training, the model can compute predictions for many positions in parallel, while causal masking preserves the left-to-right prediction constraint.

During ordinary autoregressive inference, the next token must be selected before that token can become part of the context for the following token.

That dependency is why generating many tokens is inherently sequential, even though individual Transformer operations can use parallel computation.

---

## 12. Advantages and Limitations

### Advantages

- **Flexible output:** Can generate paragraphs, code, explanations, summaries, and other token sequences.
- **Context-dependent generation:** Each prediction can use the preceding context.
- **Incremental output:** Text can be streamed to a user as tokens are generated.
- **Controllable decoding:** Greedy decoding, sampling, temperature, and filtering affect generation behavior.

### Limitations

- **Sequential dependency:** Each new token generally depends on the previously generated sequence.
- **Error propagation:** An early mistake can influence later tokens.
- **Repetition:** The model may repeat words, phrases, or ideas.
- **Factual errors:** Fluent output is not necessarily correct.
- **Context limits:** The model can only use the context supported by its architecture and generation setup.

Autoregressive generation is a powerful text-generation method, but it does not guarantee that every output will be coherent, accurate, or useful.

---

## 13. Common Misconceptions

| Misconception | Correct explanation |
|---|---|
| The model generates a complete paragraph in one ordinary generation step. | It typically selects one next token per generation step. |
| Every token represents a complete word. | Tokens may represent words, subwords, punctuation, or special symbols. |
| The model's parameters are updated after every generated token. | Ordinary inference does not perform training updates. |
| The highest-probability token is always selected. | Sampling can select another token. |
| The model always recomputes every previous token's attention keys and values. | KV caching can reuse previously computed keys and values. |
| The model knows the entire future sentence before generating it. | Each prediction uses the available context; future generated tokens are not known in advance. |
| Autoregressive generation guarantees accurate text. | The process can still produce incorrect or inconsistent output. |

---

## 🧠 Simple Mental Model

Think of autoregressive generation as completing a sentence step by step.

```text
Start:
"I want to"

Step 1:
"I want to learn"

Step 2:
"I want to learn AI"

Step 3:
"I want to learn AI because"

Step 4:
"I want to learn AI because it"
```

Each step uses the sequence available at that moment to predict the next token.

The actual tokens depend on the model and decoding settings.

**Remember this cycle:**

```text
Context
   |
   v
Predict
   |
   v
Select Token
   |
   v
Append Token
   |
   v
Repeat
```

## ✅ Key Takeaways

- Autoregressive generation produces text one token at a time.
- Each next-token prediction uses the currently available context.
- Logits and probabilities help determine which token can be selected.
- The selected token is appended to the sequence and can influence subsequent predictions.
- Causal masking prevents access to future positions through causal self-attention.
- Prefill processes the prompt; decoding generates new tokens.
- KV caching reuses previously computed attention keys and values.
- Generation stops when a configured stopping condition is reached.
- During ordinary inference, the model's learned parameters remain fixed.
