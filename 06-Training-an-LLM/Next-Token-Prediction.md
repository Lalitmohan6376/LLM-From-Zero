# 🔮 Next-Token Prediction

Next-Token Prediction is the **core learning objective of a decoder-only Large Language Model (LLM)**.

The basic idea is simple:

> Given the tokens that came before, predict what token should come next.

For example:

```text
Input:
The cat is

Target:
sleeping
```

The model learns to predict the next token based on the previous tokens.

---

## 1. What Is Next-Token Prediction?

Next-token prediction means predicting the **next token in a sequence**.

For example:

```text
The cat is sleeping
```

The model can create several prediction tasks:

```text
The        → cat
The cat    → is
The cat is → sleeping
```

The model is not necessarily predicting complete words.

It predicts **tokens**, which may be:

* Words
* Subwords
* Characters
* Punctuation
* Special tokens

The exact tokenization depends on the tokenizer.

---

## 2. Simple Example

Consider:

```text
The cat is
```

The model receives:

```text
The cat is
```

It produces a probability distribution for possible next tokens:

```text
sleeping    → 0.70
hungry      → 0.10
running     → 0.08
small       → 0.05
...
```

The model then uses a decoding strategy to select a token.

For example:

```text
sleeping
```

The generated text becomes:

```text
The cat is sleeping
```

The process can then continue.

---

## 3. Next-Token Prediction During Training

During training, the model does not simply receive text and generate forever.

Instead, the training data is converted into **input and target sequences**.

Example:

```text
Original sequence:

The cat is sleeping
```

After shifting by one token:

```text
Input:

The cat is

Target:

cat is sleeping
```

This creates multiple prediction tasks:

```text
The        → cat
The cat    → is
The cat is → sleeping
```

The model makes predictions and compares them with the correct target tokens.

---

## 4. Input and Target

For causal language modeling:

```text
Input  = tokens given to the model
Target = expected next tokens
```

Example:

```text
Input:

[The] [cat] [is]

Target:

[cat] [is] [sleeping]
```

The positions are aligned like this:

```text
Input:   The      cat      is
          ↓        ↓       ↓
Target:  cat      is       sleeping
```

So the model is solving three prediction problems at the same time.

---

## 5. Why Is the Target Shifted?

Suppose the sequence is:

```text
The cat is sleeping
```

We want the model to learn:

```text
The        → cat
The cat    → is
The cat is → sleeping
```

Therefore:

```text
Input:

The cat is
```

and:

```text
Target:

cat is sleeping
```

The target is shifted one position to the left relative to the original sequence.

This is called **shifted input-target training**.

---

## 6. Token IDs

Before entering the Transformer, text is tokenized and converted into token IDs.

For example:

```text
Text:

The cat is sleeping
```

Could become:

```text
Tokens:

[The] [cat] [is] [sleeping]
```

Then:

```text
Token IDs:

[101, 245, 37, 892]
```

These numbers are only an example.

Actual token IDs depend on the tokenizer and its vocabulary.

The training data may therefore look like:

```text
[101, 245, 37, 892]
```

The model works with these token IDs through embeddings and Transformer layers.

---

## 7. Complete Training Flow

The simplified training process is:

```text
Raw Text
   ↓
Tokenization
   ↓
Token IDs
   ↓
Training Sequence
   ↓
Input + Target
   ↓
Token Embeddings
   ↓
Positional Information
   ↓
Transformer Blocks
   ↓
Logits
   ↓
Probability Distribution
   ↓
Compare with Target
   ↓
Loss
   ↓
Backpropagation
   ↓
Parameter Updates
```

This process is repeated many times during training.

---

## 8. What Does the Model Actually Predict?

The model does not directly output a word.

The final layer produces **logits for the vocabulary**.

Suppose the vocabulary contains:

```text
10,000 tokens
```

For one prediction position, the model can produce:

```text
10,000 logits
```

Each logit represents a score for one possible token.

Conceptually:

```text
Hidden Representation
        ↓
   Language Model Head
        ↓
      Logits
        ↓
     Softmax
        ↓
 Probabilities for all tokens
```

Example:

```text
Token        Probability
------------------------
sleeping       0.70
running        0.12
hungry         0.08
playing        0.05
...
```

---

## 9. Logits vs Probabilities

### Logits

Logits are raw scores produced by the model.

Example:

```text
sleeping → 4.2
running  → 2.1
hungry   → 1.5
```

These are **not probabilities**.

### Probabilities

Softmax converts logits into a probability distribution.

Conceptually:

```text
Logits
  ↓
Softmax
  ↓
Probabilities
```

For example:

```text
sleeping → 0.70
running  → 0.12
hungry   → 0.08
...
```

The probabilities across the vocabulary sum to approximately:

```text
1.0
```

---

## 10. How Does the Model Know the Correct Answer?

During training, the correct next token is already known from the training sequence.

Example:

```text
Input:

The cat is

Correct target:

sleeping
```

Suppose the model predicts:

```text
sleeping → 0.70
running  → 0.10
hungry   → 0.05
...
```

The training process checks how well the predicted distribution matches the correct target.

This difference is represented using a **loss function**.

---

## 11. Loss

For language-model training, **cross-entropy loss** is commonly used.

The loss measures how well the model predicted the correct token.

Conceptually:

```text
Prediction
    +
Correct Target
    ↓
Compare
    ↓
Loss
```

If the model gives high probability to the correct token:

```text
Correct token probability = 0.90
```

the loss is relatively low.

If the model gives very low probability to the correct token:

```text
Correct token probability = 0.01
```

the loss is relatively high.

The model uses this loss to update its parameters.

---

## 12. One Sequence Creates Multiple Training Tasks

Consider:

```text
I love machine learning
```

The model can learn:

```text
I                → love
I love           → machine
I love machine   → learning
```

So one sequence provides several next-token prediction examples.

This is one reason language-model training can use large amounts of text efficiently.

---

## 13. Causal Masking

Next-token prediction requires an important restriction.

When predicting a token, the model must **not see future tokens**.

For example:

```text
The cat is sleeping
```

When predicting:

```text
is
```

the model can use:

```text
The
cat
```

but it should not use:

```text
sleeping
```

Otherwise, the model would already have access to the answer.

This is why decoder-only LLMs use **causal self-attention**.

---

## 14. Causal Attention Example

Consider:

```text
The cat is sleeping
```

The attention pattern can conceptually look like:

```text
             Can attend to
             ↓

The          The

cat          The  cat

is           The  cat  is

sleeping     The  cat  is  sleeping
```

A token can attend to itself and previous tokens, but not future tokens.

This prevents future information from leaking into the prediction.

---

## 15. Why Can Training Still Be Parallel?

At first, it may seem that next-token prediction must always happen one token at a time.

During **training**, that is not necessary.

Consider:

```text
Input:

The cat is sleeping
```

The model can process the sequence in parallel while causal masking controls which information each position can access.

Conceptually:

```text
The        → cat
The cat    → is
The cat is → sleeping
```

These prediction positions can be processed together.

The causal mask ensures that each position only uses allowed previous information.

This makes Transformer training highly parallelizable.

---

## 16. Next-Token Prediction During Inference

During inference, the situation is different.

Suppose the user enters:

```text
The cat
```

The model predicts the next token:

```text
The cat → is
```

Now the generated token becomes part of the input:

```text
The cat is
```

The model predicts again:

```text
The cat is → sleeping
```

Then:

```text
The cat is sleeping → .
```

This continues until generation stops.

---

## 17. Autoregressive Generation

This repeated process is called **autoregressive generation**.

The model:

1. Reads the current context.
2. Predicts the next token.
3. Selects a token.
4. Adds that token to the sequence.
5. Predicts the next token again.
6. Repeats.

Diagram:

```text
Prompt
  ↓
Tokenize
  ↓
Transformer
  ↓
Predict next token
  ↓
Add token to sequence
  ↓
Transformer
  ↓
Predict next token
  ↓
Add token
  ↓
Repeat
```

For example:

```text
Prompt:
The cat

       ↓

Predict:
is

       ↓

The cat is

       ↓

Predict:
sleeping

       ↓

The cat is sleeping

       ↓

Predict:
.
```

---

## 18. Training vs Inference

Next-token prediction works differently during training and inference.

| Training                                    | Inference                                    |
| ------------------------------------------- | -------------------------------------------- |
| Correct target is known                     | Correct next token is unknown                |
| Input and target are prepared               | Model generates its own tokens               |
| Many positions can be processed in parallel | Generation is autoregressive                 |
| Loss is calculated                          | Usually no training loss is required         |
| Parameters are updated                      | Parameters normally stay fixed               |
| Causal mask prevents future-token access    | Model only has the current available context |

The same trained model is used for both.

---

## 19. Teacher Forcing

During training, the model is given the correct previous tokens from the training sequence.

This is commonly described as **teacher forcing**.

Example:

```text
Correct sequence:

The cat is sleeping
```

The model receives:

```text
The
The cat
The cat is
```

and learns:

```text
cat
is
sleeping
```

During inference, however, the model does not have the correct future sequence.

It must use its own generated tokens.

---

## 20. What Happens If the Model Makes a Mistake?

Suppose the prompt is:

```text
The cat is
```

The model predicts:

```text
running
```

instead of:

```text
sleeping
```

During inference, the generated sequence becomes:

```text
The cat is running
```

The next prediction is then based on:

```text
The cat is running
```

So an earlier generated token can influence later predictions.

This is why generation is sequential.

---

## 21. Choosing the Next Token

The model produces probabilities for many possible tokens.

The highest-probability token is not always selected.

Different decoding strategies can be used, such as:

```text
Greedy Decoding
Temperature
Top-K Sampling
Top-P Sampling
```

For example:

```text
sleeping → 0.70
running  → 0.15
playing  → 0.10
...
```

A decoding strategy determines how the final token is selected from the model's output distribution.

---

## 22. Next-Token Prediction Is More Than Predicting Common Words

The model uses the entire available context when making a prediction.

For example:

```text
The capital of France is
```

The model may assign a high probability to:

```text
Paris
```

The prediction depends on learned patterns and the context provided to the model.

Another example:

```text
Machine learning is a field of
```

Possible prediction:

```text
artificial intelligence
```

The model is using relationships learned during training.

---

## 23. What Does the Model Learn From This Objective?

Although the training objective is simple:

```text
Predict the next token
```

learning to perform this task across large and diverse datasets can lead to learning many useful patterns.

The model can learn patterns related to:

* Grammar
* Syntax
* Word relationships
* Context
* Semantics
* Facts and concepts
* Code patterns
* Writing styles
* Multilingual patterns
* Long-range relationships

These capabilities emerge from learning patterns across large amounts of training data.

However, next-token prediction does **not** mean the model has human-like understanding.

---

## 24. Parameters Are Updated During Training

When the prediction is incorrect or not confident enough, the loss provides a signal for changing the model's parameters.

The simplified process is:

```text
Input
  ↓
Model
  ↓
Prediction
  ↓
Loss
  ↓
Backpropagation
  ↓
Gradients
  ↓
Optimizer
  ↓
Parameter Updates
```

The updated parameters can improve future predictions.

This process happens repeatedly across many training examples.

---

## 25. Complete Next-Token Training Example

Suppose the training sequence is:

```text
The movie was excellent
```

After tokenization:

```text
[The] [movie] [was] [excellent]
```

Create input and target:

```text
Input:

[The] [movie] [was]

Target:

[movie] [was] [excellent]
```

The model processes the input:

```text
Input IDs
   ↓
Token Embeddings
   ↓
Positional Information
   ↓
Transformer Blocks
   ↓
Hidden Representations
   ↓
Language Model Head
   ↓
Logits
   ↓
Probabilities
```

Predictions:

```text
Position 1:
The → movie

Position 2:
The movie → was

Position 3:
The movie was → excellent
```

The predictions are compared with:

```text
[movie] [was] [excellent]
```

The loss is calculated.

Then:

```text
Loss
 ↓
Backpropagation
 ↓
Gradients
 ↓
Optimizer
 ↓
Updated Parameters
```

---

## 26. Complete Next-Token Inference Example

Suppose the user provides:

```text
The movie
```

### Step 1: Tokenization

```text
The movie
   ↓
Tokens
```

### Step 2: Token IDs

```text
Tokens
   ↓
Token IDs
```

### Step 3: Model Input

```text
Token IDs
   ↓
Embeddings + Positional Information
```

### Step 4: Transformer

```text
Input Representation
   ↓
Transformer Blocks
```

### Step 5: Output

```text
Final Hidden State
   ↓
Language Model Head
   ↓
Logits
   ↓
Probabilities
```

### Step 6: Select Token

Suppose the model selects:

```text
was
```

The sequence becomes:

```text
The movie was
```

The process repeats.

---

## 27. Complete Autoregressive Loop

The complete generation process can be represented as:

```text
              ┌─────────────────────┐
              │      Input Text     │
              └──────────┬──────────┘
                         ↓
                  Tokenization
                         ↓
                    Token IDs
                         ↓
              Transformer Processing
                         ↓
                     Logits
                         ↓
                  Probabilities
                         ↓
                 Select Next Token
                         ↓
                Add Token to Input
                         ↓
                 Stop Condition?
                    ↙       ↘
                  No         Yes
                  ↓           ↓
          Repeat Generation  Output
```

The newly generated token becomes part of the context for the next prediction.

---

## 28. Next-Token Prediction and Context

The model does not make a prediction using only the immediately previous token.

For example:

```text
The small brown cat is
```

The prediction can use the available context:

```text
The
small
brown
cat
is
```

The Transformer uses causal self-attention to combine information from allowed previous positions.

So:

```text
Next-token prediction
        ↓
Uses available context
        ↓
Causal self-attention
        ↓
Contextual representation
        ↓
Vocabulary prediction
```

---

## 29. Context Window

The model can only process a limited number of tokens within its context at one time.

This limit is called the **context window**.

For example, if a model has a context window of:

```text
8,000 tokens
```

it cannot directly process an arbitrarily large sequence as one context.

The exact context-window size depends on the model and system.

Context window and next-token prediction are closely related because the available context influences the next-token prediction.

---

## 30. Next-Token Prediction Is Token-Based

It is important to remember:

> The model predicts tokens, not necessarily complete words.

For example, a word could be split into multiple tokens:

```text
unbelievable
```

could conceptually become:

```text
un
believ
able
```

The exact tokenization depends on the tokenizer.

The model may therefore generate:

```text
un
```

then:

```text
believ
```

then:

```text
able
```

The final text is reconstructed from the generated tokens.

---

## 31. Token-Level Prediction vs Word Prediction

These terms are sometimes used interchangeably for simplicity, but they are not exactly the same.

### Word prediction

```text
The cat is → sleeping
```

### Token prediction

```text
The cat is → next token
```

The next token might be:

```text
sleep
```

or:

```text
ing
```

or another tokenizer-specific piece.

Therefore, modern LLMs generally perform **next-token prediction** rather than strictly next-word prediction.

---

## 32. Why Next-Token Prediction Works Well With Transformers

Transformers are well suited for next-token prediction because they can:

* Process many training positions in parallel
* Use self-attention to combine contextual information
* Handle long sequences within the context window
* Scale to large datasets and models
* Use GPU/TPU-friendly matrix operations

Causal masking ensures that parallel training does not reveal future tokens.

---

## 33. Next-Token Prediction and the Transformer

The complete relationship is:

```text
Next-Token Prediction
        ↓
Training Objective
        ↓
Transformer
        ↓
Contextual Representations
        ↓
Language Model Head
        ↓
Vocabulary Logits
        ↓
Probability Distribution
        ↓
Next Token
```

The Transformer is the architecture that processes the context.

The next-token objective tells the model **what prediction task to learn**.

---

## 34. Important Distinction: Architecture vs Objective

These two ideas are related but different.

### Transformer

Describes the model architecture and its components:

```text
Attention
FFN
Residual Connections
Layer Normalization
```

### Next-Token Prediction

Describes the training objective:

```text
Given previous tokens → predict next token
```

So:

```text
Transformer = How the model processes information

Next-token prediction = What the language model is trained to predict
```

---

## 35. Next-Token Prediction Does Not Mean Simple Guessing

It may sound like the model is simply guessing the next word.

In reality, the prediction is produced through many learned transformations:

```text
Token IDs
   ↓
Embeddings
   ↓
Positional Information
   ↓
Causal Self-Attention
   ↓
Feed-Forward Networks
   ↓
Repeated Transformer Blocks
   ↓
Final Hidden Representation
   ↓
Language Model Head
   ↓
Vocabulary Logits
   ↓
Probability Distribution
```

The final distribution represents the model's learned prediction over possible next tokens.

---

## 36. Common Misunderstandings

### ❌ "The model predicts the next word only."

Not necessarily.

Modern LLMs generally predict the next **token**.

---

### ❌ "Token IDs contain meaning."

No.

Token IDs are identifiers assigned by a tokenizer.

The semantic representation is learned through embeddings and subsequent model processing.

---

### ❌ "The model can see the whole answer during training."

Causal masking prevents each prediction position from using future tokens.

---

### ❌ "The model generates the entire response at once."

Autoregressive generation normally produces tokens sequentially.

---

### ❌ "Next-token prediction means the model only looks at the previous token."

No.

It can use the available context within the context window.

---

### ❌ "The model always selects the highest-probability token."

Not necessarily.

Different decoding strategies can be used.

---

### ❌ "The training objective is complicated."

The core objective is conceptually simple:

```text
Predict the next token.
```

The complexity comes from the model architecture, scale, data, optimization, and training process.

---

## 37. Simple Mental Model

Think of the model as repeatedly completing a sequence:

```text
The
 ↓
The cat
 ↓
The cat is
 ↓
The cat is sleeping
 ↓
The cat is sleeping today
```

At every step:

```text
Current Context
      ↓
   Transformer
      ↓
Next-Token Probabilities
      ↓
Select Token
      ↓
Add Token
      ↓
Repeat
```

That is the basic idea behind autoregressive text generation.

---

## 38. Complete Conceptual Flow

The complete next-token prediction process can be summarized as:

```text
                 TRAINING

              Training Text
                    ↓
               Tokenization
                    ↓
                Token IDs
                    ↓
             Training Sequence
                    ↓
             Input + Target
                    ↓
              Token Embeddings
                    ↓
          Positional Information
                    ↓
         Decoder-Only Transformer
                    ↓
            Causal Self-Attention
                    ↓
             Feed-Forward Network
                    ↓
             Multiple Blocks
                    ↓
          Final Hidden Representations
                    ↓
          Language Model Head
                    ↓
                 Logits
                    ↓
               Probabilities
                    ↓
          Compare with Target
                    ↓
                   Loss
                    ↓
             Backpropagation
                    ↓
            Parameter Updates
```

During inference:

```text
                 INFERENCE

                  Prompt
                    ↓
               Tokenization
                    ↓
                Token IDs
                    ↓
         Decoder-Only Transformer
                    ↓
          Final Hidden Representation
                    ↓
          Language Model Head
                    ↓
                 Logits
                    ↓
              Probabilities
                    ↓
            Select Next Token
                    ↓
          Add Token to Sequence
                    ↓
                 Repeat
                    ↓
              Generated Text
```

---

## 39. Training vs Generation in One Example

Suppose the original text is:

```text
The sky is blue
```

### During training

The model learns:

```text
The          → sky
The sky      → is
The sky is   → blue
```

The correct targets are known.

```text
Prediction
     ↓
Compare with target
     ↓
Loss
     ↓
Update parameters
```

### During generation

The user may provide:

```text
The sky is
```

The model predicts:

```text
blue
```

Then:

```text
The sky is blue
```

The model predicts the next token again.

The model continues until a stopping condition is reached.

---

## 40. Key Takeaways

* **Next-token prediction is a core objective used to train decoder-only language models.**
* The model predicts the next **token**, not necessarily the next word.
* Training uses **input and target sequences** created by shifting tokens.
* The model produces **logits** for possible vocabulary tokens.
* Softmax can convert logits into a probability distribution.
* The predicted distribution is compared with the correct target using a loss function.
* The loss is used for **backpropagation and parameter updates**.
* **Causal masking** prevents future tokens from being used when making a prediction.
* Training can process many positions in parallel because causal masking controls information flow.
* During inference, generated tokens are added back to the sequence.
* Repeated next-token prediction produces **autoregressive text generation**.
* The model can use available context, not just the immediately previous token.
* The Transformer provides the architecture for processing contextual information.
* Next-token prediction provides the learning objective.
* Next-token prediction is simple as an objective, but learning it at large scale can produce powerful language capabilities.
