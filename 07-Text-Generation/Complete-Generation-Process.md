# 🔄 Complete Generation Process in LLMs

## 1. Introduction

Text generation is the process through which a Large Language Model (LLM) produces text in response to a prompt.

Most GPT-style LLMs generate text **one token at a time**, repeatedly predicting and selecting the next token until a stopping condition is met.

For example, a user enters:

> Explain artificial intelligence in simple words.

The LLM processes the prompt, calculates the probability distribution for the next token, selects a token, and repeats the process until it has generated a response.

This process is called **autoregressive text generation**.

In this document, we will connect the concepts learned throughout the text-generation section into one complete workflow.

---

## 2. The Complete Text-Generation Pipeline

```text id="genpipeline01"
             User Prompt
                  |
                  v
          1. Tokenization
                  |
                  v
            2. Token IDs
                  |
                  v
        3. Input Embeddings
                  |
                  v
       4. Positional Information
                  |
                  v
        5. Transformer Blocks
                  |
                  v
        6. Final Hidden States
                  |
                  v
       7. Language Modeling Head
                  |
                  v
               Logits
                  |
                  v
       8. Probability Calculation
                  |
                  v
       9. Decoding and Selection
                  |
                  v
          Select Next Token
                  |
                  v
       10. Check Stopping Rules
                  |
           +------+------+
           |             |
        Continue         Stop
           |             |
           v             v
     Update Context   Return Text
           |
           v
    Run Model Again
```

The process repeats for each new token.

Some details, such as temperature, Top-K, and Top-P, are optional generation settings. The exact sequence of processing steps depends on the model and implementation.

---

## 3. Step 1: User Provides a Prompt

The process begins when the user supplies an input prompt.

For example:

```text id="promptdemo01"
Explain machine learning in simple words.
```

The prompt provides the context from which the model generates a continuation.

The model does not directly process the raw characters as ordinary readable text throughout its neural network. The input must first be converted into the representation expected by the model.

---

## 4. Step 2: Tokenization

The tokenizer divides the input text into tokens according to its vocabulary and tokenization rules.

For example, the sentence:

```text id="tokendemo01"
I love AI.
```

Might be divided into:

```text id="tokendemo02"
["I", " love", " AI", "."]
```

This is an illustrative tokenization; the exact tokens depend on the tokenizer.

A token may represent a word, part of a word, punctuation, or another text unit.

The tokenizer converts the prompt into a sequence of tokens that the model can process.

---

## 5. Step 3: Convert Tokens into Token IDs

Each token is associated with an integer ID in the tokenizer's vocabulary.

For example:

```text id="idsdemo01"
Tokens:
["I", " love", " AI", "."]

Token IDs:
[40, 912, 6842, 13]
```

These numbers are illustrative and do not represent the actual IDs of a particular tokenizer.

Token IDs identify vocabulary entries. They are not semantic vectors and do not directly represent the meaning of the words.

The IDs provide the indices used to look up the corresponding token embeddings.

---

## 6. Step 4: Create Input Representations

The model converts token IDs into learned embedding vectors.

Positional information is also incorporated so the model can distinguish token positions.

Conceptually:

```text id="repdemo01"
Token IDs
    |
    v
Embedding Lookup
    |
    v
Token Vectors
    |
    v
Add or Apply Positional Information
    |
    v
Model Input Representations
```

The exact method of incorporating positional information depends on the architecture. For example, some models use learned positional embeddings, while others use mechanisms such as Rotary Positional Embeddings (RoPE).

The resulting representations are passed into the Transformer.

---

## 7. Step 5: Process the Input Through Transformer Blocks

The Transformer processes the input representations through a stack of Transformer blocks.

Within a typical decoder-only LLM, these blocks contain components such as:

- **Causal self-attention:** Lets each position use information from permitted earlier positions and itself, while blocking future positions.
- **Feed-forward networks:** Transform the representations at each position.
- **Residual connections and normalization:** Help information and gradients flow through the network.

As the input passes through these blocks, the representations become contextualized.

For example, the representation of the word `bank` can be influenced by its surrounding text:

```text id="bankdemo01"
Sentence A:
I deposited money at the bank.

Sentence B:
We sat beside the river bank.
```

The token `bank` is the same word, but its surrounding context differs. The model's contextual representation can reflect those differences.

The model uses these contextual representations to predict what should come next.

---

## 8. Step 6: Generate Logits

After the final Transformer block, the model produces a final hidden representation for each processed token position.

The language modeling head maps these representations to vocabulary-sized logits.

**Logits are raw scores for possible next tokens. They are not probabilities.**

For example, the logits for a simplified vocabulary might be:

| Candidate Token | Logit |
|---|---:|
| data | 3.2 |
| patterns | 2.4 |
| information | 1.7 |
| weather | 0.3 |

These are illustrative scores, not outputs from a real model.

During ordinary autoregressive inference, the model generally uses the logits at the last relevant position to select the next token.

The token with the highest logit is the highest-ranked candidate before any additional generation processing.

---

## 9. Step 7: Convert Logits into Probabilities

A softmax function can convert logits into a probability distribution.

The formula is:

\[
P_i=\frac{e^{z_i}}{\sum_j e^{z_j}}
\]

Where:

- \(z_i\) is the logit of a candidate token.
- \(e^{z_i}\) is the exponential of that logit.
- The denominator sums the exponentials of the logits across the vocabulary.
- \(P_i\) is the resulting probability.

For example:

```text id="probdemo01"
Candidate token probabilities:

data          → 50%
patterns      → 25%
information   → 15%
weather       → 10%
```

These probabilities are illustrative and sum to 100%.

The model assigns probabilities to possible next tokens. The generation strategy determines how those probabilities are used to select a token.

---

## 10. Step 8: Apply Decoding Strategies

The probability distribution can be used directly or modified by generation settings before the next token is selected.

Common decoding methods include:

| Method | How It Works |
|---|---|
| Greedy decoding | Selects the highest-probability token |
| Temperature | Changes the sharpness of the probability distribution |
| Top-K sampling | Retains the K highest-scoring candidates |
| Top-P sampling | Retains candidates until their cumulative probability reaches a chosen threshold |
| Stopping conditions | Determine when generation should end |

These methods serve different purposes.

### Greedy Decoding

Greedy decoding selects the highest-probability token at every step.

It is predictable but does not explore alternative candidates when choosing a token.

### Temperature

Temperature modifies logits before probability calculation in a typical implementation.

Lower positive temperatures concentrate probability more strongly on high-scoring tokens. Higher temperatures make the distribution flatter.

### Top-K Sampling

Top-K sampling retains a fixed number of the highest-scoring candidates, then samples from the retained group.

### Top-P Sampling

Top-P sampling retains the highest-ranked candidates until their cumulative probability reaches or exceeds the selected threshold, then samples from that group.

### Combining Decoding Methods

A system may combine temperature with Top-K or Top-P sampling.

The exact processing order and supported settings depend on the generation implementation.

**Important:** Decoding strategies control token selection. They do not change the model's learned parameters.

---

## 11. Step 9: Select the Next Token

After applying the chosen generation strategy, the system selects a token.

Suppose the prompt is:

```text id="nextprompt01"
Machine learning learns from
```

The model might assign these example probabilities:

```text id="nextprob01"
data       → 55%
experience → 25%
examples   → 15%
weather    →  5%
```

With greedy decoding, `data` is selected because it has the highest probability.

With sampling, one of the eligible tokens may be selected according to the processed probability distribution.

The selected token becomes part of the generated continuation.

---

## 12. Step 10: Add the Token to the Context

After selecting a token, the generation system appends it to the existing sequence.

For example:

```text id="appenddemo01"
Original prompt:
Machine learning learns from

Selected token:
data

Updated sequence:
Machine learning learns from data
```

The model then uses the updated context to predict the next token.

This is the central idea behind autoregressive generation: **each newly generated token can influence the tokens generated after it.**

---

## 13. Step 11: Run the Model Again

The model repeats the prediction-and-selection process using the updated context.

Consider this simplified example:

```text id="iterdemo01"
Initial prompt:
Machine learning learns from

Iteration 1:
Machine learning learns from data

Iteration 2:
Machine learning learns from data and

Iteration 3:
Machine learning learns from data and identifies

Iteration 4:
Machine learning learns from data and identifies patterns
```

This is an illustrative continuation, not a deterministic prediction.

In practice, the model generates token IDs, and the text shown here represents their decoded form.

Each iteration selects one or more next tokens depending on the generation implementation. Standard autoregressive decoding proceeds token by token.

### Does the Entire Prompt Get Reprocessed Every Time?

Conceptually, the model must account for the updated context at each generation step.

Many modern implementations use a **KV cache** to reuse previously computed attention keys and values instead of recomputing everything from scratch.

The KV cache improves efficiency, but it does not remove the need to calculate the new token's next-token prediction.

---

## 14. Step 12: Check Stopping Conditions

After selecting a token, the generation system checks whether an active stopping condition has been met.

Common conditions include:

### 1. End-of-Sequence Token

The model generates a recognized EOS token that signals the end of the sequence.

### 2. Stop Sequence

A configured string or token pattern appears, telling the system to stop.

### 3. Maximum New Tokens

The generated continuation reaches its configured length limit.

### 4. Other System Constraints

An application or generation framework may impose additional stopping rules.

The process continues if no stopping condition has been triggered.

```text id="stopcheck01"
Selected token
      |
      v
Check stopping conditions
      |
      +---- Condition met? ---- Yes ----> Stop
      |
      No
      |
      v
Update context
      |
      v
Generate another token
```

Reaching a token limit does not guarantee that the response is complete. Generation may stop in the middle of a sentence if the configured limit is reached.

---

## 15. Step 13: Convert Generated Tokens into Text

Once generation stops, the output token IDs are decoded into readable text.

For example:

```text id="decodeout01"
Generated token IDs:
[512, 874, 301, 92]

          |
          v

Tokenizer decoding

          |
          v

Readable text:
"AI systems learn patterns."
```

The IDs and sentence above are illustrative.

The tokenizer's decoding rules determine how token IDs are converted back into text.

Special tokens used for stopping may be omitted from the returned text, depending on the model and implementation.

The final text is then returned to the user or passed to the application that requested it.

---

## 16. Complete Example: From Prompt to Final Response

Let's connect the entire process using a simple prompt.

**User prompt:**

> Explain machine learning in simple words.

### Step A: Process the Prompt

```text id="fullstepA"
Raw text
   |
   v
Tokenization
   |
   v
Token IDs
   |
   v
Embeddings + Positional Information
```

### Step B: Run the Transformer

```text id="fullstepB"
Input representations
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
```

### Step C: Select Tokens Repeatedly

The model predicts the next token, applies the chosen decoding strategy, and selects a token.

A simplified illustrative continuation might be:

```text id="fullstepC"
Machine
Machine learning
Machine learning is
Machine learning is a
Machine learning is a way
Machine learning is a way for
Machine learning is a way for computers
...
```

The actual model generates tokens according to its learned behavior and the configured decoding strategy.

### Step D: Stop Generation

The process ends when an active stopping condition is met.

### Step E: Return the Response

An illustrative final answer could be:

> Machine learning is a type of AI that allows computers to learn patterns from data and use those patterns to make predictions.

The model does not normally produce the entire response in one prediction. It generates a sequence of tokens through repeated next-token selection.

---

## 17. Training vs Inference During Text Generation

Text generation during inference is different from training.

| Feature | Training | Inference |
|---|---|---|
| Main goal | Learn model parameters | Generate predictions using learned parameters |
| Input | Training sequences | User prompt and generated context |
| Next-token prediction | Yes | Yes |
| Loss calculation | Used to measure prediction error | Not normally required for ordinary text generation |
| Backpropagation | Used during training | Not used for ordinary inference |
| Parameter updates | Yes | No |
| Token selection for a generated response | Not the main training objective | Central to generation |

During training, the model learns by comparing predictions against target tokens and updating parameters through optimization.

During ordinary inference, the model uses its existing parameters to generate text. Its parameters remain fixed while temporary activations and cached attention values are computed.

---

## 18. Important Concepts to Remember

### Autoregressive Generation

The model predicts and generates tokens sequentially, using the available context.

### Logits

Raw scores produced by the language modeling head for candidate vocabulary tokens.

### Probability Distribution

A distribution that assigns probabilities to candidate next tokens.

### Decoding Strategy

The rule used to select a token from the model's scores or probability distribution.

### KV Cache

A mechanism that stores previously computed attention keys and values to improve autoregressive inference efficiency.

### Stopping Conditions

Rules that determine when generation ends.

These components work together to turn an input prompt into generated text.

---

## 19. Common Misconceptions

### ❌ The model generates the complete answer in a single prediction.

No. Standard autoregressive generation repeatedly predicts and selects next tokens.

### ❌ Token IDs directly represent word meanings.

No. Token IDs identify vocabulary entries. Meaning-related information is represented through learned embeddings and contextual processing.

### ❌ The highest-probability token must always be selected.

No. Greedy decoding selects the highest-probability token, but sampling methods can select other eligible candidates.

### ❌ Temperature retrains the model.

No. Temperature changes the probability distribution used during generation; it does not update learned parameters.

### ❌ Top-K and Top-P are the same.

No. Top-K uses a candidate count, while Top-P uses a cumulative probability threshold.

### ❌ The model must recompute every previous token from scratch.

No. KV caching can reuse previously computed attention keys and values during incremental generation.

### ❌ Reaching a stopping condition means the answer is correct and complete.

No. A length limit or stop sequence can end generation even when the response is incomplete or incorrect.

---

## 20. 🧠 Simple Mental Model

Think of text generation as a repeating loop.

```text id="mentalgen01"
       PROMPT
          |
          v
    Process Tokens
          |
          v
    Run Transformer
          |
          v
    Predict Next Token
          |
          v
    Select a Token
          |
          v
    Check Stopping Rules
          |
      +---+---+
      |       |
    Stop?    No
      |       |
      v       v
  Return    Add Token
   Text     to Context
                |
                v
          Predict Again
```

The Transformer calculates what can come next. The decoding strategy determines how the next token is selected. The stopping rules determine when to finish.

**The key idea:** An LLM converts a prompt into a sequence of generated tokens through repeated prediction, token selection, context updating, and stopping checks.

---

## 21. Key Takeaways

- Text generation begins with a prompt that is tokenized and converted into model input representations.
- Transformer blocks process the input and produce contextual hidden states.
- The language modeling head produces logits for vocabulary tokens.
- Softmax can convert logits into a probability distribution.
- Greedy decoding, temperature, Top-K, and Top-P influence token selection in different ways.
- The selected token is added to the context, allowing the model to predict the next token.
- KV caching can make incremental generation more efficient.
- EOS tokens, stop sequences, and length limits can terminate generation.
- The tokenizer converts the generated token sequence back into readable text.
- During ordinary inference, the model uses its learned parameters without updating them.
