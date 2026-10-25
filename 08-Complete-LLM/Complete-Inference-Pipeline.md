# 🚀 Complete LLM Inference Pipeline

Inference is the process of using a trained Large Language Model (LLM) to generate predictions from an input prompt.

During inference, the model uses its learned parameters to process the prompt, predict the next token, and generate a response. Unlike ordinary training, inference does not update the model's learned parameters.

This document explains the complete inference pipeline, from entering a prompt to receiving generated text.

---

## 1. What Is LLM Inference?

**LLM inference is the process of running a trained model to produce predictions for new inputs.**

For example, suppose a user enters:

```text id="u2a9jf"
Prompt:
"What is machine learning?"
```

The model processes the prompt and generates a response such as:

```text id="r5v8mx"
"Machine learning is a field of AI that
allows computers to learn patterns from data."
```

The response is illustrative. A model's actual output depends on its learned parameters, prompt, and generation settings.

Inference involves several connected operations:

1. Receive the input prompt.
2. Tokenize the prompt.
3. Convert token IDs into embeddings.
4. Process the input through Transformer blocks.
5. Calculate logits for the next token.
6. Apply the decoding strategy.
7. Select the next token.
8. Repeat generation until a stopping condition is reached.
9. Decode the generated tokens into readable text.

---

## 2. Complete Inference Pipeline at a Glance

```text id="p7w3kn"
                INPUT PROMPT
                     |
                     v
                  TOKENIZER
                     |
                     v
                  TOKEN IDs
                     |
                     v
              TOKEN EMBEDDINGS
                     |
                     v
            POSITIONAL INFORMATION
                     |
                     v
              TRANSFORMER BLOCKS
                     |
                     v
             FINAL HIDDEN STATES
                     |
                     v
            LANGUAGE MODELING HEAD
                     |
                     v
                   LOGITS
                     |
                     v
         DECODING / TOKEN SELECTION
                     |
                     v
              NEXT TOKEN SELECTED
                     |
                     v
             UPDATE THE SEQUENCE
                     |
                     v
          PROCESS THE UPDATED CONTEXT
                     |
                     +------ Repeat
                     |
                     v
           STOPPING CONDITION REACHED
                     |
                     v
           DECODE TOKENS INTO TEXT
                     |
                     v
              GENERATED RESPONSE
```

The model's neural network calculates predictions. The surrounding generation process selects tokens, manages stopping conditions, and converts tokens back into text.

---

## 3. Step 1 — Receive the Input Prompt

The inference pipeline begins when the model receives an input prompt.

For example:

```text id="k8v3md"
"Explain how a solar panel works."
```

The prompt provides the initial context for the model's predictions.

The prompt may be a question, an instruction, a partial sentence, or another supported input format.

The model does not necessarily know the user's intended meaning perfectly. Its output depends on the information provided, the model's learned patterns, and the way the input is represented.

### Important point

A prompt is the starting context, not the final answer. The model must process it before generating new tokens.

---

## 4. Step 2 — Tokenize the Prompt

The tokenizer converts the input text into tokens and then maps those tokens to integer IDs.

For example:

```text id="b6f4wr"
Input:
"Solar panels convert sunlight."

             |
             v

Tokens:
["Solar", " panels", " convert", " sunlight", "."]

             |
             v

Token IDs:
[312, 851, 204, 672, 14]
```

These IDs are illustrative. Different tokenizers may split the same text differently and assign different IDs.

### Why is tokenization necessary?

The neural network operates on numerical representations rather than directly processing ordinary text strings.

Token IDs identify vocabulary entries, which the embedding layer then converts into vectors.

The tokenized prompt must also fit the model's supported context and input limits, taking account of any special tokens or additional formatting.

---

## 5. Step 3 — Convert Token IDs into Embeddings

Each token ID is used to retrieve its learned embedding vector.

For example:

```text id="r9q4zs"
Token IDs:
[312, 851, 204, 672, 14]

             |
             v

Embedding Layer

312 -> [0.25, -0.14, 0.71, ...]
851 -> [0.62,  0.09, 0.18, ...]
204 -> [0.13,  0.47, 0.39, ...]
672 -> [0.41, -0.22, 0.56, ...]
14  -> [0.08,  0.33, 0.21, ...]
```

The vectors shown are illustrative.

If the prompt contains \(N\) tokens and the model's hidden dimension is \(d_{\text{model}}\), the embedding output is commonly shaped as:

\[
[N,d_{\text{model}}]
\]

For batched input, a common shape is:

\[
[B,N,d_{\text{model}}]
\]

Where \(B\) is the batch size.

The embedding vectors are learned numerical representations. They are not the same as the token IDs or the final contextual representations produced by the Transformer.

---

## 6. Step 4 — Incorporate Positional Information

The model needs information about token order because word order can change meaning.

Compare:

```text id="t6h2pk"
"The dog chased the cat."

"The cat chased the dog."
```

The same words appear in different orders, but the meaning differs.

The architecture therefore incorporates positional information using a method appropriate to the model.

Common approaches include:

- Learned positional embeddings
- Sinusoidal positional encodings
- Rotary Position Embedding (RoPE)

These approaches work differently. For example, a model using learned positional embeddings may add positional vectors to token embeddings, while a RoPE-based model incorporates positional information into attention computations.

After the appropriate input preparation, the representations can enter the Transformer blocks.

---

## 7. Step 5 — Process the Prompt Through Transformer Blocks

The Transformer blocks perform the main neural network computations during inference.

A typical decoder-only Transformer block contains:

- Causal self-attention
- A feed-forward network
- Residual connections
- Normalization layers

The exact ordering depends on the architecture.

```text id="z8m3vk"
Input Representations
          |
          v
   Causal Self-Attention
          |
          v
    Residual Connection
          |
          v
   Feed-Forward Network
          |
          v
    Residual Connection
          |
          v
    Output Representations
```

This is a simplified view, not a universal ordering of all operations.

### 7.1 Causal self-attention

Causal self-attention allows each token to use information from permitted positions in the context while preventing access to future positions.

During inference, the model uses the prompt tokens available so far.

For example:

```text id="g4w2ns"
Tokens:
[The] [cat] [is]

When processing "The":
Available context -> [The]

When processing "cat":
Available context -> [The] [cat]

When processing "is":
Available context -> [The] [cat] [is]
```

During the initial prompt-processing stage, implementations can process the prompt's token positions together while applying causal masking.

### 7.2 Feed-forward network

After attention, the feed-forward network applies learned transformations to the token representations.

Attention combines information across permitted token positions. The feed-forward network transforms each position's representation through learned linear and nonlinear operations.

### 7.3 Stacking multiple blocks

A typical LLM contains multiple Transformer blocks. Each block transforms the representations produced by the previous block.

```text id="e3v7hm"
Prompt Representations
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
    Transformer Block N
          |
          v
   Final Hidden Representations
```

The resulting representations incorporate information from the available context and patterns learned during training.

---

## 8. Step 6 — Process the Final Hidden State

After the final Transformer block, the architecture may apply a final normalization layer.

The resulting hidden representations are passed to the language modeling head.

During initial prompt processing, the model can calculate hidden states for multiple token positions. However, when choosing the next token in ordinary autoregressive generation, the relevant logits are generally taken from the last available position.

For example:

```text id="d8v2ma"
Prompt:
"The sky is"

             |
             v

Transformer Output:
Hidden state for "The"
Hidden state for "sky"
Hidden state for "is"

             |
             v

Use the last position's
hidden state to predict
the next token.
```

The hidden states are numerical vectors, not readable text or final token probabilities.

---

## 9. Step 7 — Generate Logits

The language modeling head maps the final hidden representation to a score for each token in the model's vocabulary.

These scores are called **logits**.

A simplified expression is:

\[
z=hW_{\text{out}}+b
\]

Where:

- \(h\) = hidden representation at the prediction position
- \(W_{\text{out}}\) = output projection weights
- \(b\) = optional bias
- \(z\) = vocabulary logits

Suppose the model's vocabulary contains 50,000 tokens. The output for one prediction position contains 50,000 scores.

An illustrative output might be:

| Candidate token | Logit |
|---|---:|
| ` blue` | 3.8 |
| ` clear` | 2.7 |
| ` cloudy` | 1.9 |
| ` green` | 0.4 |

These scores are examples, not actual outputs from a real model.

The logits are raw scores. They are not probabilities and do not need to sum to one.

---

## 10. Step 8 — Convert Logits into Probabilities

A softmax function can convert logits into a probability distribution:

\[
P_i=\frac{e^{z_i}}{\sum_{j=1}^{V}e^{z_j}}
\]

Where:

- \(z_i\) is the logit for candidate token \(i\).
- \(V\) is the vocabulary size.
- \(P_i\) is the resulting probability.

For example:

| Candidate token | Illustrative probability |
|---|---:|
| ` blue` | 60% |
| ` clear` | 25% |
| ` cloudy` | 10% |
| Other candidates combined | 5% |
| **Total** | **100%** |

These values are illustrative.

The distribution represents the model's predictions for the next token given the current context. It should not automatically be interpreted as a calibrated measure of factual confidence.

---

## 11. Step 9 — Select the Next Token

The generation process uses a decoding strategy to choose the next token.

Common strategies include:

| Strategy | How it works |
|---|---|
| Greedy decoding | Selects the highest-scoring token. |
| Temperature sampling | Adjusts the distribution's sharpness before sampling. |
| Top-K sampling | Restricts the candidates to the K highest-scoring tokens. |
| Top-P sampling | Restricts candidates using cumulative probability. |

For example, suppose the prompt is:

```text id="v2n9ka"
"The sky is"
```

The model may assign a high probability to the token ` blue`.

A greedy decoding configuration selects the highest-probability token. A sampling-based configuration may select another candidate.

The selected token becomes part of the sequence.

---

## 12. Step 10 — Append the Token to the Context

After the model selects a token, the generation process appends it to the existing token sequence.

Suppose the initial prompt is:

```text id="x5m7nr"
"The sky is"
```

The model selects ` blue`.

The updated sequence becomes:

```text id="a4w9kp"
"The sky is blue"
```

The model then uses the updated context to predict the following token.

This is the core idea behind **autoregressive generation**.

The newly generated token can influence the predictions of subsequent tokens because it becomes part of the available context.

---

## 13. Step 11 — Repeat Generation

The inference process repeats the prediction-and-selection loop until a stopping condition is reached.

```text id="n7q4mv"
Initial Prompt
      |
      v
Forward Pass
      |
      v
Generate Logits
      |
      v
Select Next Token
      |
      v
Append Token to Context
      |
      v
Check Stopping Conditions
      |
      +---- Continue? ---- Yes
      |                       |
      |                       v
      |                 Next Prediction
      |                       |
      +-----------------------+
      |
      No
      |
      v
Decode Generated Tokens
```

A simplified example:

```text id="m3k8zr"
Initial prompt:
"The sky is"

Step 1:
"The sky is blue"

Step 2:
"The sky is blue today"

Step 3:
"The sky is blue today."

Step 4:
A stopping condition is reached.
```

The example illustrates the process; actual generation depends on the model and decoding settings.

---

## 14. Step 12 — Use the KV Cache

Generating a response token by token can involve repeated attention computations.

To reduce unnecessary work, many inference implementations use a **key-value (KV) cache**.

During attention, each token produces key and value representations. The cache stores previously computed keys and values so they can be reused during subsequent decoding steps.

Without caching, the implementation may repeatedly calculate attention information for earlier tokens.

With caching, the model can reuse that information while processing new tokens.

```text id="j6p2wx"
Initial Prompt
      |
      v
Process Prompt Tokens
      |
      v
Store Attention Keys and Values
      |
      v
Predict Next Token
      |
      v
Process New Token
      |
      v
Reuse Cached Keys and Values
      |
      v
Predict Following Token
```

The exact implementation varies across architectures and inference engines.

### Important distinction

The KV cache is temporary inference state. It is not the same as the model's learned parameters, and updating the cache does not mean the model is being trained.

---

## 15. Step 13 — Check Stopping Conditions

Generation does not continue indefinitely. The inference system checks whether an applicable stopping condition has been reached.

Common conditions include:

- **EOS token:** The model generates an end-of-sequence token.
- **Stop sequence:** The generated output matches a configured stopping pattern.
- **Maximum new tokens:** The generation limit is reached.
- **Other generation limits:** A system-defined rule ends generation.

For example:

```text id="y5r8tc"
Generated sequence:
"The sky is blue today."

             |
             v

Check stopping conditions
             |
             v

A stopping condition is reached
             |
             v

End generation
```

The **context window** limits the tokenized context the model can handle, while the **maximum-new-token setting** limits the length of a particular generation. They are related but different constraints.

---

## 16. Step 14 — Decode Tokens into Readable Text

After generation stops, the tokenizer converts the generated token IDs back into readable text.

```text id="h9v2qd"
Generated Token IDs
         |
         v
Tokenizer Decoding
         |
         v
Readable Text
         |
         v
"The sky is blue today."
```

The exact displayed text depends on the tokenizer and how the surrounding system handles special tokens, spacing, and output formatting.

Tokenization and detokenization connect the numerical model pipeline to the text users see.

---

## 17. Prompt Prefill vs. Token-by-Token Decode

Inference is often described in two main stages: **prefill** and **decode**.

### Prefill

During prefill, the model processes the prompt tokens to establish their representations and, when supported, populate the KV cache.

The prompt's positions can generally be processed together, subject to causal masking and the architecture's implementation.

### Decode

During decode, the model repeatedly processes the newly generated token using the existing context and cached attention information when available.

Each step produces predictions for another token.

| Aspect | Prefill | Decode |
|---|---|---|
| Main input | Initial prompt | Newly generated token or tokens |
| Purpose | Process the initial context | Generate subsequent tokens |
| Computation | Processes prompt positions | Repeated prediction steps |
| KV cache | Often initialized or populated | Commonly reused and extended |
| Output | Initial next-token prediction and cached state | Next-token predictions during generation |

This distinction helps explain why prompt processing and generating a long response have different computational characteristics.

---

## 18. Training vs. Inference

Training and inference use many of the same neural network components, but their purposes differ.

| Aspect | Training | Inference |
|---|---|---|
| Main goal | Learn from training data | Produce predictions |
| Input | Training sequences | Prompt and generated context |
| Forward pass | Yes | Yes |
| Logits | Calculated for training prediction positions | Used to select the next token |
| Loss | Used to evaluate training predictions | Not required for ordinary text generation |
| Backpropagation | Used to calculate gradients | Not used for ordinary generation |
| Optimizer updates | Update trainable parameters | Not performed during ordinary inference |
| Token selection | Not usually the main training objective | Central to autoregressive generation |
| KV cache | Depends on training setup | Commonly used for efficient decoding |

During training, the model learns by adjusting parameters to reduce loss.

During ordinary inference, the trained parameters remain fixed while the context and temporary inference state change.

---

## 19. What Affects Inference Performance?

Inference speed and memory requirements depend on several factors.

### Model size

Models with more parameters often require more memory and computation, although architecture and implementation also matter.

### Prompt length

Longer prompts generally require more work during prefill and can increase KV cache memory requirements.

### Generated output length

Generating more tokens requires more decode steps in autoregressive generation.

### Batch size

Processing multiple requests together can improve hardware utilization, but increases memory requirements and may affect latency.

### Precision and hardware

Numerical precision, GPU memory bandwidth, available compute, and hardware capabilities affect speed and memory use.

### KV caching

KV caching reduces repeated attention computations during autoregressive decoding, but consumes additional memory.

### Decoding settings

Sampling and filtering methods can add processing overhead. Their effect depends on the implementation and vocabulary size.

No single factor determines inference speed in every situation.

---

## 20. Common Misconceptions

**Misconception 1: Inference trains the model again.**

Ordinary inference uses the trained parameters without updating them.

**Misconception 2: The model predicts an entire response in one step.**

Autoregressive generation generally selects one new token at a time, repeating the prediction process.

**Misconception 3: Logits are probabilities.**

Logits are raw scores. Softmax or another configured transformation can produce a probability distribution.

**Misconception 4: The tokenizer generates the answer.**

The tokenizer converts text into tokens and token IDs, and later converts generated IDs back into text. The neural network calculates predictions.

**Misconception 5: The KV cache stores the model's knowledge.**

The KV cache stores intermediate attention information for the current inference context. It is not a permanent knowledge database.

**Misconception 6: The highest-probability token always produces the best complete response.**

Greedy decoding makes a locally highest-probability choice at each step. That does not guarantee the best overall sequence.

**Misconception 7: More generated tokens always mean a better answer.**

Longer outputs can contain useful detail, but they can also introduce repetition, irrelevant content, or errors.

---

## 21. Complete Inference Pipeline — Final Summary

The entire process can be divided into three connected stages.

### Stage A — Prepare the input

```text id="w2n8cy"
Input Prompt
     |
     v
Tokenization
     |
     v
Token IDs
     |
     v
Embeddings
     |
     v
Positional Information
```

### Stage B — Predict and generate

```text id="c8m5vx"
Transformer Blocks
       |
       v
Final Hidden Representation
       |
       v
Language Modeling Head
       |
       v
Logits
       |
       v
Decoding Strategy
       |
       v
Select Next Token
       |
       v
Append Token to Context
       |
       v
Repeat
```

### Stage C — Finish the response

```text id="k4r9sz"
Check Stopping Conditions
          |
          v
Stop Generation
          |
          v
Decode Token IDs
          |
          v
Readable Output Text
```

The core idea is that **inference uses a trained model to repeatedly predict and select tokens until the generation process ends.**

Remember the complete sequence:

**Prompt → Tokenization → Embeddings → Transformer Blocks → Logits → Token Selection → Context Update → Repeated Generation → Stopping Condition → Decoded Text**

This is the foundation for understanding how a trained LLM turns an input prompt into a generated response.
