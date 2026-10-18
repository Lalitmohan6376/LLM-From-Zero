# 🚀 Inference in an LLM

Inference is the process of using a trained Large Language Model (LLM) to generate predictions or produce an output from an input.

During training, the model learns patterns by updating its parameters. During inference, the model uses its existing parameters to process new input and generate output.

For example, when you ask an LLM:

**Prompt:** `What is Artificial Intelligence?`

The model processes your input, predicts tokens, and generates a response.

This process is called **LLM inference**.

---

## 1. 🧠 What Does Inference Mean?

Inference means running a trained model to obtain predictions.

A trained LLM has learned parameters containing patterns acquired during training. When new text is provided, the model processes that text and calculates predictions based on its current parameters.

For a GPT-style language model, inference usually involves predicting one token at a time and using the generated tokens to continue the sequence.

For example:

```text
Input:
The sun rises in the

        |
        v

Trained LLM
        |
        v

Predict the Next Token
        |
        v

"east"

        |
        v

Append the Predicted Token

        |
        v

"The sun rises in the east"
```

The example is simplified. Actual generation may involve several tokens, punctuation, and additional processing.

**Important:** Inference does not ordinarily train the model or update its learned parameters.

---

## 2. ⚖️ Training vs Inference

Training and inference both use the model's forward pass, but their purposes are different.

| Feature | Training | Inference |
|---|---|---|
| Purpose | Learn patterns from training data | Generate predictions from input |
| Model parameters | Updated during training | Normally remain unchanged |
| Forward pass | Yes | Yes |
| Loss calculation | Used to guide training | Not required for ordinary generation |
| Backpropagation | Yes | No |
| Optimizer updates | Yes | No |
| Typical input | Training sequences | Prompt or other model input |
| Typical output | Updated parameters and training metrics | Predicted or generated tokens |

### Example

During training:

```text
Input:  The sky is
Target: blue

Prediction → Loss → Gradients → Parameter Update
```

During inference:

```text
Input: The sky is

Prediction → Select Token → "blue"
```

During ordinary inference, the model generates a prediction without calculating gradients to update its parameters.

---

## 3. 🔄 Complete Inference Pipeline

An LLM inference pipeline converts the input prompt into model-ready representations, processes those representations through the Transformer, and generates output tokens.

```text id="e1a4u8"
User Input / Prompt
        |
        v
Text Tokenization
        |
        v
Token IDs
        |
        v
Token Embeddings
        |
        v
Add Positional Information
        |
        v
Transformer Blocks
        |
        v
Final Hidden Representations
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
Select the Next Token
        |
        v
Append Token to the Sequence
        |
        v
More Tokens Needed?
      /          \
    Yes           No
     |             |
     v             v
Run Again      Stop Generation
     |             |
     +----<        v
              Generated Token IDs
                     |
                     v
                 Detokenization
                     |
                     v
                Generated Text
```

This is a simplified pipeline for autoregressive, decoder-only language models. Other model architectures and inference configurations may follow different steps.

---

## 4. 💬 Step 1 — Receive the Prompt

The prompt is the input supplied to the model.

Examples:

- `Explain machine learning.`
- `Write a Python function to add two numbers.`
- `The capital of India is`
- `Summarize this paragraph.`

The model receives the text as input, but it does not process ordinary text characters directly through its Transformer layers.

The text must first be converted into the representation expected by the model.

A prompt can contain a question, an instruction, a partial sentence, or a longer conversation context.

---

## 5. 🔤 Step 2 — Convert Text into Token IDs

The tokenizer divides the input text into tokens and converts them into numerical IDs.

For example:

```text id="4q2c5k"
Prompt:
The cat is sleeping

        |
        v

Tokens:
["The", " cat", " is", " sleeping"]

        |
        v

Token IDs:
[101, 482, 318, 7291]
```

The token IDs are illustrative. A real tokenizer may produce different tokens and IDs.

The model uses these IDs to look up token embeddings.

Each token ID identifies a vocabulary entry; it is not itself a semantic vector.

---

## 6. 🧩 Step 3 — Create Input Representations

The token IDs are converted into learned embedding vectors. Positional information is also incorporated so the model can represent token order.

For example, if the input contains four tokens, the model might create a representation with this shape:

```text id="h3v7nw"
Token IDs
Shape: [1, 4]

        |
        v

Input Representations
Shape: [1, 4, 768]
```

Here:

- `1` represents the batch size.
- `4` represents the number of tokens.
- `768` is an illustrative hidden dimension.

The actual dimensions depend on the model architecture.

These representations are then processed by the Transformer.

---

## 7. ⚙️ Step 4 — Process the Input Through the Transformer

The input representations pass through the model's Transformer blocks.

A simplified decoder-only architecture looks like this:

```text id="m8c1zv"
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

Inside each block, causal self-attention allows each token position to use information from permitted earlier positions and itself. The feed-forward network transforms the representations at each position.

The model repeats these operations across its stacked blocks.

The final hidden representations contain context-dependent information used to produce vocabulary predictions.

**Important:** The Transformer does not directly output ordinary text. It produces numerical representations that are converted into prediction scores.

---

## 8. 📊 Step 5 — Generate Logits

The final hidden representation used for the current prediction is passed through the language modeling head.

This produces **logits**: scores for possible next tokens in the model's vocabulary.

Suppose the prompt is:

`The sun rises in the`

The model might assign illustrative logits to several candidate tokens:

| Candidate token | Example logit |
|---|---:|
| east | 4.2 |
| west | 2.1 |
| sky | 1.5 |
| morning | 0.7 |

These are example numbers, not actual model outputs.

A higher logit generally corresponds to a higher probability after softmax, relative to the other logits.

The model typically produces scores for the entire vocabulary, not just the four candidates shown here.

---

## 9. 🎲 Step 6 — Convert Logits into Probabilities

Softmax converts the logits into a probability distribution over the vocabulary.

For a vocabulary of \(V\) tokens, the model produces a probability for each candidate token.

The probabilities sum to 1:

\[
\sum_{i=1}^{V}P(t_i)=1
\]

For example:

| Candidate token | Illustrative probability |
|---|---:|
| east | 65% |
| west | 18% |
| sky | 10% |
| morning | 4% |
| Other tokens | 3% |

These probabilities are illustrative and do not correspond to the example logits above.

The model can now use a decoding strategy to select a token.

Possible strategies include:

- Greedy decoding
- Temperature-based sampling
- Top-k sampling
- Top-p sampling

These strategies influence how the next token is selected from the model's scores or probabilities.

---

## 10. ➡️ Step 7 — Select the Next Token

After calculating the next-token distribution, the inference system selects a token according to its decoding configuration.

For example:

```text id="9g4f7j"
Prompt:
The sun rises in the

        |
        v

Model Predicts:
east  → 65%
west  → 18%
sky   → 10%
...

        |
        v

Selected Token:
east

        |
        v

Updated Sequence:
The sun rises in the east
```

In greedy decoding, the token with the highest probability is selected.

With sampling-based methods, a token is selected according to a modified probability distribution. A token with a lower probability can therefore be selected.

The selection method affects the generated text, but it does not ordinarily update the model's learned parameters.

---

## 11. 🔁 Step 8 — Repeat Autoregressive Generation

For a GPT-style model, generating one token usually does not finish the entire response.

The newly generated token is appended to the existing sequence. The model then predicts another token using the updated context.

This process is called **autoregressive generation**.

Suppose the model generates the phrase `Machine learning is useful`.

```text id="v5n8qb"
Step 1

Input:
Machine learning

Predict:
is

        |
        v

Step 2

Updated Input:
Machine learning is

Predict:
useful

        |
        v

Step 3

Updated Input:
Machine learning is useful

Predict:
for

        |
        v

Step 4

Updated Input:
Machine learning is useful for

Predict:
prediction
```

The generated tokens in this example are illustrative.

At each step, the model predicts a continuation based on the available context. During generation, the context includes both the original prompt and the tokens generated so far, subject to the model's context-window limit and any generation constraints.

The model repeats this process until a stopping condition is reached.

---

## 12. 🛑 Step 9 — Stop Generation

Inference needs a rule for deciding when to stop generating tokens.

Common stopping conditions include:

- The model generates an end-of-sequence token.
- A configured maximum number of new tokens is reached.
- A configured stop sequence is detected.
- The application or generation system stops the request.

For example:

```text id="m9v4zt"
Prompt
  |
  v
Generate Token
  |
  v
Append Token
  |
  v
Check Stopping Condition
  |
  +---- Continue ----> Generate Another Token
  |
  +---- Stop --------> Finish Output
```

A model does not necessarily stop when it produces a grammatically complete sentence. The generation system follows its configured stopping rules.

---

## 13. 📝 Step 10 — Convert Token IDs into Text

After generation stops, the generated token IDs are decoded into readable text.

For example:

```text id="f4q6wj"
Generated Token IDs:
[482, 318, 7291]

        |
        v

Tokenizer Decoding

        |
        v

Text:
cat is sleeping
```

The IDs are illustrative.

Detokenization reconstructs text from the generated tokens. Depending on the tokenizer, the decoded text may include spaces, punctuation, or special-token handling.

The final text is then returned to the user or to the application that requested the model output.

---

## 14. ⚡ Why Inference Can Be Expensive

Even though inference does not normally update model parameters, it still requires computation.

The model must process input representations through its Transformer blocks and calculate token predictions.

Inference cost depends on factors such as:

- Model size and architecture
- Prompt length
- Number of generated tokens
- Batch size
- Hardware and memory bandwidth
- Precision and quantization
- Attention implementation
- Whether a key-value (KV) cache is used

### Why does output length matter?

Autoregressive generation usually predicts tokens sequentially. Each new token depends on the existing context, so generating a long response requires multiple prediction steps.

Longer outputs therefore generally require more inference work than shorter outputs, all else being equal.

---

## 15. 🚀 KV Cache During Inference

During autoregressive generation, the model repeatedly uses information from previous tokens.

Without caching, some implementations would recompute attention keys and values for earlier tokens at every generation step.

A **key-value cache (KV cache)** stores previously computed attention keys and values so they can be reused as new tokens are generated.

```text id="c8m2ya"
First Forward Pass
       |
       v
Compute Keys and Values
       |
       v
Store in KV Cache
       |
       v
Generate Next Token
       |
       v
Process New Token
       |
       v
Reuse Cached Keys and Values
       |
       v
Generate Another Token
```

The precise implementation varies, but the cache generally reduces redundant computation during autoregressive decoding.

The cache is not the same as the model's learned parameters. It stores intermediate information for a particular inference context and is generally discarded when that context is no longer needed.

KV caching can improve generation speed, but it consumes memory. Its memory requirements generally grow with the number of cached tokens and the model's attention configuration.

---

## 16. 🧪 Does Inference Use the Entire Context Every Time?

Conceptually, each next-token prediction depends on the available context, subject to causal masking and the model's architecture.

However, an optimized implementation does not necessarily recompute every previous token's key and value representations at every step.

Two common stages are:

**Prefill:** The model processes the prompt and establishes the initial representations and cache.

**Decode:** The model generates tokens one at a time, typically reusing cached key-value information.

```text id="y7k3pd"
Prompt
  |
  v
PREFILL
Process Prompt Tokens
  |
  v
Create KV Cache
  |
  v
DECODE
Generate Token 1
  |
  v
Generate Token 2
  |
  v
Generate Token 3
  |
  v
Continue Until Stopping
```

Prefill can process multiple prompt tokens together, while decode commonly processes each newly generated token incrementally.

This distinction helps explain why prompt processing and token generation can have different performance characteristics.

---

## 17. 🧠 Does the Model Learn During Inference?

During ordinary inference, the model's trainable parameters remain unchanged.

For example, suppose a trained model contains a parameter with the value:

\[
\theta=0.42
\]

It uses that parameter to process a prompt and generate a response.

Ordinary inference does not update the parameter through an optimizer step. It simply uses the existing value to calculate predictions.

However, the inference process can maintain temporary state, such as:

- KV cache
- Current token sequence
- Generation scores
- Application-level conversation history

These temporary values are different from changing the model's learned parameters.

A system can also be designed to update or fine-tune a model using new data, but that is a separate training or adaptation process.

---

## 18. 🔗 Complete Example: From Prompt to Response

Suppose a user enters:

`What is machine learning?`

The inference pipeline works conceptually as follows:

| Step | Operation | Result |
|---|---|---|
| 1 | Receive prompt | `What is machine learning?` |
| 2 | Tokenize text | A sequence of token IDs |
| 3 | Create representations | Embeddings with positional information |
| 4 | Run Transformer | Context-dependent hidden representations |
| 5 | Produce logits | Scores for vocabulary tokens |
| 6 | Convert scores | Probability distribution |
| 7 | Select token | One next token |
| 8 | Append token | Updated input sequence |
| 9 | Repeat | More generated tokens |
| 10 | Stop generation | A stopping condition is met |
| 11 | Decode tokens | Readable response text |

The final response could begin:

`Machine learning is a branch of artificial intelligence...`

The exact response depends on the model's learned parameters, prompt, decoding configuration, and any other constraints applied by the surrounding system.

The model does not necessarily retrieve a prewritten answer. In ordinary autoregressive generation, it constructs the output through successive token predictions.

---

## 19. ❗ Common Misunderstandings

### 1. Is inference the same as training?

No. Training updates model parameters; ordinary inference uses the existing parameters to make predictions.

### 2. Does inference require a forward pass?

Yes. The model must process its input to produce predictions.

### 3. Does the model generate an entire paragraph in one prediction?

In ordinary autoregressive generation, the model predicts tokens sequentially. It can process multiple prompt tokens together during prefill, but new output tokens are generally generated one at a time.

### 4. Is the most probable token always selected?

No. Greedy decoding selects the highest-probability token, but sampling methods can select other tokens.

### 5. Does softmax generate the final text?

No. Softmax converts logits into probabilities. A decoding strategy selects tokens, and the tokenizer decodes those tokens into text.

### 6. Does the model's knowledge change after every prompt?

Not during ordinary inference. Its learned parameters remain unchanged, although temporary context and cache state can change.

### 7. Is the KV cache permanent memory?

No. It stores intermediate attention information for an inference context; it is not the same as persistent learned knowledge.

### 8. Can a trained model produce an incorrect answer during inference?

Yes. A trained model can generate incorrect, misleading, incomplete, or poorly formatted responses. Training does not guarantee that every prediction is correct.

### 9. Does a longer prompt always improve the response?

No. Additional context can help when it is relevant, but irrelevant or conflicting information may not improve the result. The model is also limited by its context window.

### 10. Does inference always require the Internet?

No. A model can run locally or on a remote server. Internet access depends on how the model is hosted and what surrounding services the application uses.

---

## 20. 🧠 Final Mental Model

Remember the inference process in this order:

1. **Prompt** — receive the input text.
2. **Tokenization** — convert text into token IDs.
3. **Representation** — create embeddings and incorporate positional information.
4. **Transformer** — process the input through the model's layers.
5. **Logits** — calculate scores for possible next tokens.
6. **Probabilities** — convert scores into a distribution when needed.
7. **Token selection** — choose the next token using the decoding strategy.
8. **Autoregressive loop** — append the token and generate another when needed.
9. **Stopping** — stop when a configured condition is met.
10. **Detokenization** — convert generated token IDs into readable text.

The central idea is:

**Prompt → Token IDs → Transformer → Next-Token Prediction → Repeat → Generated Text**

Training teaches the model by updating its parameters. Inference uses those trained parameters to generate predictions without ordinary training updates.
