# 🔮 Next-Token Prediction in an LLM

## 1. What Is Next-Token Prediction?

**Next-token prediction is the process of predicting a likely next token based on the tokens that came before it.**

Modern GPT-style LLMs use this process as a central part of autoregressive text generation.

For example, suppose the input is:

```text
The sky is
```

The model processes the input and predicts a distribution over possible next tokens.

```text
Input:
"The sky is"

Possible next tokens:

blue      → 70%
clear     → 15%
cloudy    → 10%
green     →  4%
banana    →  1%
```

These probabilities are illustrative, not actual outputs from a particular model.

The model might select `blue` as the next token.

The sequence becomes:

```text
The sky is blue
```

The model can then predict another token using the updated sequence.

**Important:** The model predicts tokens, not necessarily complete words or sentences. A token can represent a word, part of a word, punctuation, or another piece of text.

---

## 2. How Does Next-Token Prediction Work?

A simplified next-token prediction pipeline looks like this:

```text
Input Text
    |
    v
Tokenization
    |
    v
Token IDs
    |
    v
Token Embeddings
    |
    v
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
Probability Distribution
    |
    v
Select Next Token
    |
    v
Generated Token
```

Let's understand each step.

1. **Input text:** The model receives a prompt or an existing sequence of text.
2. **Tokenization:** The tokenizer divides the text into tokens.
3. **Token IDs:** Each token is represented by a tokenizer-specific numerical ID.
4. **Token embeddings:** The IDs are mapped to learned vector representations.
5. **Transformer blocks:** The model processes the sequence using attention and other neural-network operations.
6. **Final hidden representation:** The model produces contextual representations for the processed positions.
7. **Language modeling head:** Converts a hidden representation into a score for every vocabulary token.
8. **Logits:** These are the raw scores for candidate next tokens.
9. **Probability distribution:** Softmax can convert the logits into probabilities.
10. **Token selection:** A decoding strategy chooses the next token.

The selected token can then become part of the input for the following prediction.

---

## 3. What Does the Model Actually Predict?

The model does not directly choose a complete sentence in one ordinary autoregressive generation step.

Instead, it predicts a distribution over possible next tokens.

Consider this example:

```text
Input:
"I am learning"

Possible next tokens:

Python    → 60%
machine   → 20%
about     → 10%
quickly   →  7%
banana    →  3%
```

These numbers are illustrative.

The model may select `Python`, producing:

```text
I am learning Python
```

It then predicts the next token using the updated context.

For example:

```text
Input:
"I am learning Python"

Possible next token:
"programming"
```

The process continues until the model reaches a stopping condition.

A token may be a whole word, a subword, or a special token. Therefore, predicting the next token is not always the same as predicting the next word.

---

## 4. How Does the Model Learn Next-Token Prediction?

During training, the model is given text sequences and learns to predict the next token in those sequences.

Consider this training sentence:

```text
The cat is sleeping
```

After tokenization, imagine the sentence contains these tokens:

```text
[The] [cat] [is] [sleeping]
```

For a causal language model, the training objective can be illustrated as follows:

| Available input context | Target next token |
|---|---|
| The | cat |
| The cat | is |
| The cat is | sleeping |

The model makes predictions based on the available context and compares them with the correct target tokens.

If its predictions are poor, the training process calculates a loss. Backpropagation calculates gradients, and an optimizer updates the model's parameters.

Repeated training helps the model improve its next-token predictions on the training objective.

### Training flow

```text
Training Text
      |
      v
 Token IDs
      |
      v
 Input Sequence + Shifted Targets
      |
      v
 Transformer Forward Pass
      |
      v
 Predicted Logits
      |
      v
 Compare with Correct Next Tokens
      |
      v
      Loss
      |
      v
 Backpropagation
      |
      v
 Optimizer Updates Parameters
```

The model is trained across many sequences and optimization steps.

**Important:** Training is not simply storing every sentence in a database. The optimization process changes the model's parameters so that it learns statistical patterns in the training data. Memorization can also occur.

---

## 5. How Are Inputs and Targets Shifted?

Next-token prediction uses a relationship between input tokens and their target tokens.

Consider this sequence:

```text
The cat is sleeping
```

For a simplified example, the input and targets are:

```text
Input:
[The] [cat] [is]

Target:
[cat] [is] [sleeping]
```

Each input position is trained to predict the token that follows it.

| Input position | Input token | Target token |
|---|---|---|
| 1 | The | cat |
| 2 | cat | is |
| 3 | is | sleeping |

The target sequence is shifted one token to the right compared with the input sequence.

Real training pipelines can use longer sequences, batches, padding, packed documents, and special tokens. But the core next-token relationship remains the same.

### Why is this useful?

One sequence can provide several next-token prediction targets instead of requiring a separate training example for every word or token.

During training, a causal attention mask prevents each position from using future tokens when making its prediction.

---

## 6. How Does Causal Attention Help?

A language model should not use future tokens to predict the next token during ordinary causal training.

Suppose the sequence is:

```text
The cat is sleeping
```

When predicting `is` from the context `The cat`, the model must not look ahead at `is` or `sleeping` through its causal self-attention.

The attention mask restricts which positions each token can attend to.

```text
Tokens:
[The] [cat] [is] [sleeping]

Prediction at "cat":
Can use:     The, cat
Cannot use:  is, sleeping
```

This diagram is conceptual: each position can use its own token and permitted earlier positions, but not future positions.

Causal masking allows the model to calculate predictions at multiple positions in parallel during training while preserving the correct left-to-right prediction constraint.

During generation, the model receives the available context and predicts the next token without access to unknown future tokens.

---

## 7. Logits and Probabilities in Next-Token Prediction

The model's language modeling head produces logits.

For example:

| Candidate token | Logit |
|---|---:|
| blue | 3.0 |
| clear | 2.0 |
| cloudy | 1.0 |

These are example logits, not probabilities.

Applying softmax produces a probability distribution approximately like this:

| Candidate token | Probability |
|---|---:|
| blue | 66.5% |
| clear | 24.5% |
| cloudy | 9.0% |
| **Total** | **100%** |

The probability distribution gives a normalized view of the model's relative next-token predictions.

A decoding strategy then selects a token.

- **Greedy decoding:** Selects the highest-probability token.
- **Sampling:** Selects a token randomly according to the distribution.
- **Top-K sampling:** Restricts candidates to the K highest-scoring tokens before sampling.
- **Top-P sampling:** Restricts candidates using cumulative probability before sampling.

Temperature can also adjust the distribution before selection.

Therefore, the model's highest-probability prediction and its actual generated token are not always the same.

---

## 8. What Happens During Inference?

During inference, a trained model uses next-token prediction to generate text.

Suppose the prompt is:

```text
I love
```

The model processes the prompt and predicts the next token.

```text
Prompt:
I love
   |
   v
Model predicts:
coding
   |
   v
Updated sequence:
I love coding
   |
   v
Model predicts:
because
   |
   v
Updated sequence:
I love coding because
   |
   v
Model predicts:
it
```

This example illustrates the process, not a guaranteed output.

The model repeatedly predicts one next token at a time. The selected token becomes part of the context for the next prediction.

During ordinary inference, the model's learned parameters remain fixed. It does not perform optimizer updates after every generated token.

### The inference loop

```text
          Prompt
             |
             v
      Process Context
             |
             v
      Predict Next Token
             |
             v
       Select a Token
             |
             v
     Append to Context
             |
             v
       Stop Condition?
          /      \
        No        Yes
        |           |
        v           v
  Predict Again   Finish
```

The loop ends when a stopping condition is reached, such as a suitable end-of-sequence token or a generation limit.

---

## 9. Training vs Inference

Next-token prediction is central to both training and inference, but the purpose differs.

| Aspect | Training | Inference |
|---|---|---|
| Main goal | Improve model parameters | Generate predictions using trained parameters |
| Input | Training sequences | User prompt and previously generated tokens |
| Target tokens | Available from the training data | Usually unknown in advance |
| Logits | Produced at training positions | Used to predict the next token |
| Loss | Calculated against known targets | Not normally required for ordinary generation |
| Parameter updates | Yes, through optimization | No, during ordinary inference |
| Token generation | Predictions are compared with targets | Selected tokens are appended to the context |

During training, the model learns through repeated prediction, loss calculation, and parameter updates.

During inference, it uses what it learned to produce new token sequences.

---

## 10. Does Next-Token Prediction Mean the Model Only Learns Grammar?

No.

To predict tokens across varied text, a model can learn patterns involving:

- Grammar and sentence structure.
- Relationships between words and concepts.
- Facts and associations present in training data.
- Programming-language syntax.
- Common reasoning patterns.
- Different writing styles and formats.
- Relationships across longer contexts.

However, next-token prediction does not guarantee that every learned pattern is correct or that every generated answer is reliable.

The training objective is to predict tokens. The capabilities that emerge depend on the model architecture, training data, scale, optimization, and other training choices.

A model can generate convincing text while still making factual errors or struggling with unfamiliar problems.

---

## 11. Common Misconceptions

| Misconception | Correct explanation |
|---|---|
| The model predicts a complete sentence in one ordinary generation step. | Autoregressive generation typically selects one next token per step. |
| A token is always a complete word. | Tokens may be words, subwords, punctuation, or special tokens. |
| The model always selects the highest-probability token. | Sampling and other decoding methods can select a different candidate. |
| Next-token prediction happens only during inference. | It is also the central training objective for many autoregressive LLMs. |
| The model can use future tokens during causal prediction. | Causal masking prevents access to future positions through causal self-attention. |
| Training only memorizes sentences. | Training updates parameters to learn patterns, though memorization can also occur. |
| Generating a likely token guarantees a correct answer. | Likelihood under the model does not guarantee factual correctness. |
| The model's parameters change after every generated token. | Ordinary inference generates tokens without updating learned parameters. |

---

## 🧠 Simple Mental Model

Imagine that an LLM is repeatedly completing this sentence:

```text
The weather is
```

First, it scores possible next tokens and selects one:

```text
The weather is sunny
```

Then it uses the updated context to predict another token:

```text
The weather is sunny today
```

The same process continues until generation stops.

The core cycle is:

```text
Context
   |
   v
Predict Next Token
   |
   v
Select Token
   |
   v
Update Context
   |
   v
Repeat
```

**The key idea:** Next-token prediction is the process that allows an autoregressive LLM to generate text one token at a time.

## ✅ Key Takeaways

- Next-token prediction estimates the next token based on the available context.
- The language modeling head produces logits for possible vocabulary tokens.
- Softmax can convert logits into a probability distribution.
- A decoding strategy selects the next token.
- The selected token is added to the context for the following prediction.
- During training, predictions are compared with known target tokens, and model parameters are updated.
- During ordinary inference, the model generates tokens without updating its learned parameters.
- Repeating this process enables an LLM to generate sentences, paragraphs, code, and other text.
