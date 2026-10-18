# ⚙️ Forward Pass During Inference

The **forward pass during inference** is the process in which a trained Large Language Model (LLM) takes input representations, processes them through its Transformer layers, and calculates predictions for the next token.

During inference, the model uses its existing learned parameters. It does not ordinarily perform backpropagation or update those parameters.

For example, suppose the prompt is:

`The sun rises in the`

The model processes the prompt through its Transformer blocks and produces scores for possible next tokens, such as `east`, `west`, or `sky`.

The forward pass produces the prediction scores. A decoding strategy then determines which token to select.

---

## 1. 🧠 What Is a Forward Pass?

A forward pass is the process of passing input data through a neural network to calculate its output.

In an LLM, this means processing token representations through the model's layers until the model produces vocabulary logits.

A simplified pipeline looks like this:

```text id="v7m3qx"
Input Token IDs
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
More Transformer Blocks
       |
       v
Final Hidden Representations
       |
       v
Language Modeling Head
       |
       v
Logits for Vocabulary Tokens
```

The forward pass performs numerical calculations using the model's learned parameters.

It does not decide by itself how the generated text should be displayed or when the complete response should stop.

---

## 2. ⚖️ Forward Pass During Training vs Inference

The forward pass occurs in both training and inference, but the surrounding operations differ.

| Operation | Training | Inference |
|---|---|---|
| Process input through Transformer | Yes | Yes |
| Calculate predictions | Yes | Yes |
| Calculate training loss | Usually | Not required for ordinary generation |
| Calculate gradients | Yes, during backpropagation | No |
| Update parameters | Yes | No |
| Generate new tokens | Not the primary training objective | Commonly, for text generation |

During training, predictions are compared with target tokens so the model can calculate loss and update its parameters.

During inference, predictions are used to generate output without ordinary training updates.

**Remember:** A forward pass calculates predictions. It does not automatically mean that the model is learning or changing its parameters.

---

## 3. 🔤 Step 1 — Receive Token IDs

Before the forward pass begins, the prompt has already been tokenized.

Consider this example:

`The cat is sleeping`

A tokenizer might convert it into these illustrative token IDs:

```text id="f4j8kw"
Prompt:
"The cat is sleeping"

        |
        v

Token IDs:
[101, 482, 318, 7291]
```

These IDs are examples, not actual IDs from a specific tokenizer.

The token IDs identify vocabulary entries. They are not the numerical vectors that the Transformer processes internally.

The model first uses these IDs to retrieve their corresponding embeddings.

---

## 4. 🧩 Step 2 — Convert Token IDs into Embeddings

Each token ID selects a learned vector from the model's token embedding matrix.

Suppose the prompt contains four tokens and the model has a hidden dimension of 768.

The input IDs could have the shape:

```text id="n2z5bu"
[1, 4]
```

The embedding output could have the shape:

```text id="m7c3qa"
[1, 4, 768]
```

Here:

- `1` is the batch size.
- `4` is the sequence length.
- `768` is the illustrative hidden dimension.

Each token is now represented by a vector of numerical values.

The model can process these vectors using its neural network layers.

---

## 5. 📍 Step 3 — Incorporate Positional Information

Token order matters.

Consider:

- `The dog chased the cat.`
- `The cat chased the dog.`

The same words appear in both sentences, but their arrangement changes the meaning.

The model therefore needs positional information.

Depending on the architecture, positional information may be incorporated through learned positional embeddings, rotary positional embeddings (RoPE), or another method.

A simplified representation is:

```text id="h8w2pz"
Token Embeddings
       +
Positional Information
       |
       v
Input to Transformer
```

This diagram illustrates the general idea. Some positional methods, including RoPE, are applied within attention computations rather than simply being added to token embeddings.

The exact implementation depends on the model architecture.

---

## 6. ⚙️ Step 4 — Process the Input Through Transformer Blocks

The input representations pass through the model's stacked Transformer blocks.

A simplified decoder-only architecture looks like this:

```text id="q6y3mn"
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
More Transformer Blocks
         |
         v
Final Hidden Representations
```

Each Transformer block commonly includes:

1. Causal self-attention
2. A feed-forward network
3. Residual connections
4. Layer normalization

The exact ordering and implementation vary between architectures.

### What does causal self-attention do?

Causal self-attention allows each token position to use information from earlier positions and itself, while preventing it from using future tokens.

For example:

```text id="b9v4kc"
Input:
The cat is sleeping

Prediction at "The":
Can use "The"

Prediction at "cat":
Can use "The cat"

Prediction at "is":
Can use "The cat is"

Prediction at "sleeping":
Can use "The cat is sleeping"
```

This is a simplified illustration of the information available at each position in a causal Transformer.

The masking rule is important because it preserves the model's ability to predict the next token without seeing that future token at the position being evaluated.

---

## 7. 🔍 Step 5 — Understand What Happens Inside a Transformer Block

A Transformer block transforms the representations it receives.

A simplified block can be shown as:

```text id="t5w9qd"
Input Representations
         |
         v
Causal Self-Attention
         |
         v
Residual Connection
         |
         v
Normalization
         |
         v
Feed-Forward Network
         |
         v
Residual Connection
         |
         v
Normalization
         |
         v
Output Representations
```

This diagram shows one common arrangement, not the only possible one. Many modern decoder-only models use pre-normalization, where normalization occurs before the attention and feed-forward sublayers.

### Self-attention

Self-attention allows token representations to combine information from permitted positions in the sequence.

For example, while processing:

`The animal drank water because it was thirsty.`

The representation associated with `it` can use information from earlier tokens that helps establish the context.

Attention does not guarantee perfect understanding. It is a learned numerical operation that combines information across token positions.

### Feed-forward network

The feed-forward network applies learned transformations to each token position's representation.

Attention primarily enables information exchange across positions, while the feed-forward network transforms the resulting representation at each position.

The output of one block becomes the input to the next block.

---

## 8. 📊 Step 6 — Produce Final Hidden Representations

After passing through the Transformer blocks, the input has been transformed into contextual hidden representations.

These representations depend on the prompt and the model's learned parameters.

For example:

```text id="j2m7vw"
Input Tokens
[The] [sun] [rises] [in] [the]
                 |
                 v
          Transformer Blocks
                 |
                 v
      Contextual Hidden States
```

In a typical decoder-only model, there is a hidden representation for each token position.

If the input contains five tokens, the final hidden-state tensor might have the shape:

```text id="x8n4cp"
[1, 5, 768]
```

The dimensions are illustrative.

The hidden state at each position is used to calculate a prediction for the next token at that position.

During ordinary generation, the prediction associated with the final input position is generally the one used to select the next token.

---

## 9. 🎯 Step 7 — Pass the Hidden State Through the Language Modeling Head

The language modeling head converts the hidden representation into scores for possible vocabulary tokens.

Suppose the model's vocabulary contains 50,000 tokens.

The final hidden state used for prediction might be a vector of size 768, and the output head might produce 50,000 logits.

```text id="p3x7za"
Final Hidden State
Shape: [768]
       |
       v
Language Modeling Head
       |
       v
Vocabulary Logits
Shape: [50,000]
```

These dimensions are hypothetical.

Each logit is a score associated with one vocabulary token.

For example:

| Candidate token | Illustrative logit |
|---|---:|
| east | 4.2 |
| west | 2.1 |
| sky | 1.5 |
| morning | 0.7 |

These scores are illustrative and do not represent actual model output.

The language modeling head does not directly produce a readable sentence. It produces numerical scores that can be used to determine the next token.

---

## 10. 🎲 Step 8 — Use the Logits to Select a Token

After the forward pass produces logits, the inference system can convert them into probabilities and apply a decoding strategy.

For example:

```text id="r5w8nk"
Forward Pass
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
Selected Next Token
```

Common decoding methods include:

- **Greedy decoding:** Select the highest-probability token.
- **Temperature sampling:** Adjust the probability distribution before sampling.
- **Top-k sampling:** Restrict sampling to a set of high-scoring candidate tokens.
- **Top-p sampling:** Restrict sampling to a candidate set based on cumulative probability.

The decoding strategy determines how the system chooses a token from the model's predictions.

It is separate from the Transformer forward pass itself.

---

## 11. 🔁 Step 9 — Run Another Forward Pass for the Next Token

Suppose the prompt is:

`The sun rises in the`

The forward pass produces logits for the next token. Assume the system selects `east`.

The updated sequence becomes:

`The sun rises in the east`

If generation continues, the model must calculate another prediction based on the updated context.

```text id="z7k2wf"
Initial Prompt
"The sun rises in the"
          |
          v
Forward Pass
          |
          v
Select "east"
          |
          v
Updated Sequence
"The sun rises in the east"
          |
          v
Another Prediction
          |
          v
Continue Generating
```

The model repeats this process until it reaches a stopping condition, such as an end-of-sequence token or the configured maximum number of new tokens.

This repeated process is called autoregressive generation.

---

## 12. ⚡ Prefill and Decode: Two Stages of Inference

The forward pass is used in two important stages of many autoregressive inference systems.

### Stage A — Prefill

During prefill, the model processes the prompt tokens.

For example:

```text id="w6y3pj"
Prompt:
The sun rises in the

        |
        v

Process Prompt Tokens
        |
        v

Calculate Hidden States
        |
        v

Produce Next-Token Logits
        |
        v

Initialize KV Cache
```

The prompt tokens can generally be processed together, subject to the model's attention mask and implementation.

### Stage B — Decode

During decoding, the model generates new tokens incrementally.

```text id="c5q8mv"
Selected Token
      |
      v
Process New Token
      |
      v
Reuse Cached Keys and Values
      |
      v
Produce Next-Token Logits
      |
      v
Select Another Token
      |
      v
Repeat
```

A key-value (KV) cache stores previously computed attention keys and values. Reusing this information avoids recomputing those values for the entire previous sequence at every decoding step.

Without a KV cache, an implementation may recompute more of the previous context on each step, increasing redundant computation.

The exact caching strategy depends on the model and inference implementation.

---

## 13. 🧠 Does the Forward Pass Change the Model's Parameters?

No, not during ordinary inference.

The model uses its existing learned parameters to calculate hidden representations and logits.

For example:

```text id="u4j9sb"
Trained Model Parameters
          |
          v
Forward Pass
          |
          v
Predictions
```

There is no ordinary optimizer update in this process.

Temporary inference state, such as the current token sequence and KV cache, may change as generation continues. These temporary changes are not the same as updating the model's learned parameters.

During training, the workflow is different:

```text id="n7c4mx"
Forward Pass
      |
      v
Calculate Loss
      |
      v
Backpropagation
      |
      v
Optimizer Update
      |
      v
Updated Parameters
```

The distinction between these workflows is fundamental to understanding how LLMs operate.

---

## 14. ❗ Common Misunderstandings

### 1. Does the forward pass generate the entire response at once?

In ordinary autoregressive generation, the model predicts a next token and repeats the process to generate additional tokens.

### 2. Does the forward pass update parameters?

No. It calculates predictions. Parameter updates normally occur during training through backpropagation and an optimizer.

### 3. Does the Transformer directly output words?

No. The Transformer produces hidden representations. The language modeling head converts the relevant hidden state into vocabulary logits.

### 4. Are logits the same as probabilities?

No. Logits are scores. Softmax can convert them into a probability distribution.

### 5. Is the highest-logit token always selected?

Only with a strategy such as greedy decoding. Sampling-based strategies can select other tokens.

### 6. Does every token attend to every other token?

Not in a causal decoder-only Transformer. Each position is prevented from accessing future positions through causal masking.

### 7. Does inference always recompute the entire prompt?

Not necessarily. Optimized systems often use a KV cache to reuse previous attention keys and values.

### 8. Is the forward pass the same as the complete inference pipeline?

No. The forward pass calculates model outputs. The complete inference pipeline also includes input preparation, token selection, repeated generation, stopping rules, and decoding the resulting token IDs into text.

---

## 15. 🧠 Final Mental Model

Remember the forward pass in this order:

1. **Token IDs** — receive the numerical input.
2. **Embeddings** — look up learned token vectors.
3. **Positional information** — represent token order.
4. **Transformer blocks** — apply causal attention and feed-forward transformations.
5. **Hidden states** — obtain contextual representations.
6. **Language modeling head** — convert the relevant hidden state into vocabulary logits.
7. **Token selection** — use a decoding strategy to select the next token.
8. **Repeat** — run another prediction step when more output is needed.

The central idea is:

**Input Representations → Transformer Blocks → Hidden States → Logits → Next-Token Prediction**

The forward pass is the computation at the heart of inference. It transforms the model's input into predictions, while the surrounding generation system decides which tokens to produce and when to stop.
