# 🎯 Input and Target

During LLM training, tokenized training sequences are divided into **input tokens** and **target tokens**.

For a decoder-only language model, the target is usually the **next token** for each position in the input sequence.

The basic idea is:

```text id="itflow1"
Token Sequence
      ↓
Shift by One Position
      ↓
Input        Target
  ↓             ↓
Model       Expected Output
      ↓
   Prediction
      ↓
     Loss
```

This simple shifting process is the foundation of **next-token prediction** training.

---

# 1. What Is the Input?

The **input** is the sequence of tokens given to the model.

For example:

```text id="itinput1"
[The] [cat] [is] [sleeping]
```

The model receives these tokens as its input.

After tokenization, they are represented by token IDs:

```text id="itinput2"
[101, 245, 37, 892]
```

These IDs are then converted into embeddings before entering the Transformer.

---

# 2. What Is the Target?

The **target** is the token that the model is expected to predict.

For next-token prediction, the target sequence is shifted one position to the left compared with the input.

For example:

```text id="ittarget1"
Input:
[The] [cat] [is]

Target:
[cat] [is] [sleeping]
```

The model learns:

```text id="ittarget2"
The       → cat
The cat   → is
The cat is → sleeping
```

---

# 3. The One-Position Shift

Suppose the complete token sequence is:

```text id="shift1"
[The] [cat] [is] [sleeping]
```

We create:

```text id="shift2"
Input:
[The] [cat] [is]

Target:
[cat] [is] [sleeping]
```

Notice that the target is shifted by one position.

This is why the process is often called **shifted language modeling**.

---

# 4. Token ID Example

Suppose the tokenizer produces:

```text id="shift3"
[101, 245, 37, 892, 13]
```

The input can be:

```text id="shift4"
[101, 245, 37, 892]
```

The target becomes:

```text id="shift5"
[245, 37, 892, 13]
```

The model therefore has four prediction positions.

```text id="shift6"
101  → 245
245  → 37
37   → 892
892  → 13
```

The actual token IDs here are only illustrative.

---

# 5. Why Are Input and Target Shifted?

The goal of a decoder-only language model is to learn:

> Given the tokens so far, predict the next token.

For example:

```text id="predict1"
"The"
 ↓
"cat"
```

Then:

```text id="predict2"
"The cat"
 ↓
"is"
```

Then:

```text id="predict3"
"The cat is"
 ↓
"sleeping"
```

The shifted input-target arrangement allows all of these prediction tasks to be represented inside one sequence.

---

# 6. One Sequence Creates Multiple Training Examples

Consider:

```text id="multi1"
[The] [cat] [is] [sleeping]
```

It provides several prediction tasks:

```text id="multi2"
The
 ↓
cat

The cat
   ↓
   is

The cat is
      ↓
   sleeping
```

Instead of creating three completely separate examples, the model can process the sequence together.

This makes Transformer training efficient.

---

# 7. Input and Target Alignment

The input and target have corresponding positions.

Example:

```text id="align1"
Input:   [The] [cat] [is] [sleeping]
Target:  [cat] [is] [sleeping] [next]
```

Conceptually:

```text id="align2"
Input Position       Target

The          ─────→  cat
cat          ─────→  is
is           ─────→  sleeping
sleeping     ─────→  next token
```

The last target depends on how the training sequence is constructed.

For a sequence taken from a longer token stream, the next token may come immediately after the sequence.

---

# 8. Complete Sequence Example

Suppose the token sequence is:

```text id="complete1"
[The] [cat] [is] [sleeping] [on] [the] [sofa]
```

We can create:

```text id="complete2"
Input:
[The] [cat] [is] [sleeping] [on] [the]

Target:
[cat] [is] [sleeping] [on] [the] [sofa]
```

The model learns:

```text id="complete3"
The                    → cat
The cat                → is
The cat is             → sleeping
The cat is sleeping    → on
The cat is sleeping on → the
...
```

Each input position has a corresponding target token.

---

# 9. Input and Target Using Token IDs

Suppose:

```text id="ids1"
Tokens:

[The] [cat] [is] [sleeping] [on]
```

become:

```text id="ids2"
[101, 245, 37, 892, 44]
```

Then:

```text id="ids3"
Input:
[101, 245, 37, 892]

Target:
[245, 37, 892, 44]
```

The model receives the input IDs and is trained to predict the target IDs.

---

# 10. What Happens Inside the Model?

The simplified training flow is:

```text id="inside1"
Input Token IDs
       ↓
Token Embeddings
       ↓
Positional Information
       ↓
Decoder-Only Transformer
       ↓
Hidden Representations
       ↓
Language Model Head
       ↓
Logits
       ↓
Compare With Target
       ↓
Loss
```

The target is used to determine how correct the model's predictions are.

---

# 11. Input Does Not Mean "Question"

The word **input** can sometimes be confusing.

In LLM training, input does not necessarily mean a question.

The input can simply be a sequence of text tokens:

```text id="inputquestion"
"The cat is sleeping"
```

There does not need to be a question.

The model's task is to predict the next token.

---

# 12. Target Does Not Mean "Answer Text"

Similarly, the target is not necessarily a complete answer.

For next-token prediction, the target is usually the next token at each position.

For example:

```text id="targetanswer"
Input:
"The cat"

Target:
"is"
```

The target is simply what the model should predict next.

---

# 13. Causal Masking

Input and target shifting alone is not the complete story.

A decoder-only Transformer also uses **causal masking**.

Suppose the sequence is:

```text id="mask1"
[The] [cat] [is] [sleeping]
```

The model should not allow the first position to see:

```text id="mask2"
[cat] [is] [sleeping]
```

when making its prediction.

The allowed attention pattern is:

```text id="mask3"
             The   cat    is   sleeping

The          ✓     ✗      ✗      ✗
cat          ✓     ✓      ✗      ✗
is           ✓     ✓      ✓      ✗
sleeping     ✓     ✓      ✓      ✓
```

This prevents future-token information from leaking into the prediction.

---

# 14. Why Do We Need Causal Masking If We Already Have Targets?

Because the model could otherwise access future tokens through self-attention.

For example, without causal masking:

```text id="mask4"
Input:
[The] [cat] [is] [sleeping]
```

the representation for `"The"` could potentially use information from `"sleeping"`.

That would make next-token training invalid.

Therefore, two ideas work together:

```text id="mask5"
Input / Target Shift
        +
Causal Masking
        ↓
Correct Next-Token Training
```

---

# 15. Input and Target During Parallel Training

A common misconception is:

> Since the model predicts the next token, it must process one token at a time during training.

Not necessarily.

Transformers can calculate predictions for multiple positions in parallel.

For example:

```text id="parallel1"
Input:
[The] [cat] [is] [sleeping]

Targets:
[cat] [is] [sleeping] [...]
```

The model can calculate multiple prediction positions in one forward pass.

Causal masking makes sure each position only uses information available up to that position.

---

# 16. Training vs Generation

Input and target work differently during training and generation.

### During training

We already know the target tokens.

```text id="train1"
Input
  ↓
Model
  ↓
Predictions
  ↓
Compare with known targets
  ↓
Loss
  ↓
Parameter Updates
```

### During generation

The future target is not known.

```text id="generate1"
Prompt
  ↓
Model
  ↓
Predict next token
  ↓
Add token to sequence
  ↓
Predict another token
  ↓
Repeat
```

This difference is important.

---

# 17. Teacher Forcing

During autoregressive training, the model is typically given the known sequence tokens as inputs rather than requiring it to use its own previous predictions as the next input at every position.

This is commonly referred to as **teacher forcing**.

For example:

```text id="teacher1"
Correct previous tokens
        ↓
Model
        ↓
Next-token predictions
```

Instead of:

```text id="teacher2"
Model prediction
      ↓
Feed prediction back
      ↓
Next prediction
      ↓
Repeat
```

The first approach makes training much more efficient.

---

# 18. Teacher Forcing Example

Suppose the sequence is:

```text id="teacher3"
The cat is sleeping
```

During training, the model receives:

```text id="teacher4"
The
The cat
The cat is
```

and learns to predict:

```text id="teacher5"
cat
is
sleeping
```

The correct tokens are available during training.

During generation, however, the model does not know the future tokens.

---

# 19. Training Example With Multiple Positions

Suppose the token IDs are:

```text id="positions1"
[10, 20, 30, 40, 50]
```

Input:

```text id="positions2"
[10, 20, 30, 40]
```

Target:

```text id="positions3"
[20, 30, 40, 50]
```

The model produces predictions at four positions:

```text id="positions4"
Position 1 → Predict 20
Position 2 → Predict 30
Position 3 → Predict 40
Position 4 → Predict 50
```

Each prediction contributes to the training loss.

---

# 20. Logits and Targets

The Transformer does not directly output token IDs during training.

It produces **logits** for the vocabulary.

For example:

```text id="logits1"
Input position
      ↓
Hidden representation
      ↓
Language Model Head
      ↓
Vocabulary logits
```

Suppose the vocabulary contains 50,000 tokens.

For one position, the model may produce:

```text id="logits2"
[1.2, -0.4, 3.7, 0.8, ...]
```

There is one logit for each vocabulary token.

The target tells the training process which vocabulary token is correct.

---

# 21. Target and Probability Distribution

The logits can be converted into probabilities using softmax.

Conceptually:

```text id="prob1"
Logits
  ↓
Softmax
  ↓
Probability Distribution
  ↓
Compare with Target
```

Suppose the target token is:

```text id="prob2"
"cat"
```

The model should assign a high probability to `"cat"`.

The loss function measures how well the predicted distribution matches the target.

---

# 22. Cross-Entropy Loss

For next-token prediction, **cross-entropy loss** is commonly used.

Suppose the correct target is token `cat`.

The model predicts:

```text id="loss1"
cat       → 0.70
dog       → 0.15
car       → 0.05
...
```

The model gave a relatively high probability to the correct token.

The loss will therefore be lower than if the model predicted:

```text id="loss2"
cat       → 0.01
dog       → 0.60
car       → 0.20
...
```

The exact loss calculation is covered separately in the training pipeline.

---

# 23. Input and Target Shapes

Suppose:

```text id="shape1"
Batch size = 4
Sequence length = 512
```

The input token IDs can have shape:

```text id="shape2"
[4, 512]
```

The target token IDs can also have shape:

```text id="shape3"
[4, 512]
```

They are aligned position by position.

Conceptually:

```text id="shape4"
Input:
[B, N]

Target:
[B, N]
```

where:

```text id="shape5"
B = batch size
N = sequence length
```

The model then produces logits with a vocabulary dimension:

```text id="shape6"
[B, N, V]
```

where `V` is the vocabulary size.

---

# 24. Example of Shapes

Suppose:

```text id="shape7"
Batch size = 2
Sequence length = 4
Vocabulary size = 10,000
```

Then:

```text id="shape8"
Input:
[2, 4]

Target:
[2, 4]

Logits:
[2, 4, 10000]
```

This means:

```text id="shape9"
2 sequences
×
4 positions
×
10,000 possible vocabulary tokens
```

The model produces a prediction distribution for each relevant position.

---

# 25. Input and Target in a Batch

Suppose we have:

```text id="batch1"
Sequence 1:
[10, 20, 30, 40, 50]

Sequence 2:
[60, 70, 80, 90, 100]
```

The batch input can be:

```text id="batch2"
[
    [10, 20, 30, 40],
    [60, 70, 80, 90]
]
```

The batch target can be:

```text id="batch3"
[
    [20, 30, 40, 50],
    [70, 80, 90, 100]
]
```

The model processes the batch together.

---

# 26. The Last Token

Consider:

```text id="last1"
Sequence:
[10, 20, 30, 40, 50]
```

If we use:

```text id="last2"
Input:
[10, 20, 30, 40]

Target:
[20, 30, 40, 50]
```

the last input token is:

```text id="last3"
40
```

and its target is:

```text id="last4"
50
```

So the model learns:

```text id="last5"
10 → 20
20 → 30
30 → 40
40 → 50
```

The sequence provides multiple prediction positions.

---

# 27. What About the First Token?

The first token does not need a previous token from the same sequence to be represented.

For example:

```text id="first1"
Input:
[The]
```

can be used to predict:

```text id="first2"
cat
```

If a model/training setup needs an explicit beginning-of-sequence marker, a special token can be included:

```text id="first3"
<BOS> The cat is sleeping
```

The exact use of BOS or other special tokens depends on the tokenizer and model.

---

# 28. What About the End of a Sequence?

A training sequence may end at a chosen boundary.

For example:

```text id="end1"
[The] [cat] [is] [sleeping]
```

If the sequence came from a longer token stream, the next token may exist outside the displayed sequence.

Depending on the sequence construction method, the target for the final position can therefore involve a token immediately after the selected input window.

If the example is intentionally terminated, an end-of-sequence token may be used.

---

# 29. Input and Target Are Not Two Different Datasets

Another common misunderstanding is:

```text id="dataset1"
Input Dataset
+
Target Dataset
```

The target is normally derived from the same token sequence by shifting it.

For example:

```text id="dataset2"
Original:
[10, 20, 30, 40, 50]

Input:
[10, 20, 30, 40]

Target:
[20, 30, 40, 50]
```

So the input and target come from the same underlying sequence.

---

# 30. Input and Target Flow

The complete training flow can be represented as:

```text id="flow1"
Tokenized Data
      ↓
Training Sequence
      ↓
┌───────────────┐
│ Shift Sequence│
└───────┬───────┘
        ↓
 ┌────────────┐
 │   Input    │
 └─────┬──────┘
       ↓
 Transformer
       ↓
    Logits
       ↓
 Compare
       ↑
 ┌────────────┐
 │   Target   │
 └────────────┘
       ↓
      Loss
       ↓
 Backpropagation
       ↓
Parameter Updates
```

---

# 31. Complete Example

Let's use a simple sentence:

```text id="example1"
"The dog runs fast."
```

### Step 1 — Tokenization

A tokenizer might produce:

```text id="example2"
["The", " dog", " runs", " fast", "."]
```

### Step 2 — Token IDs

Suppose:

```text id="example3"
[101, 250, 51, 732, 13]
```

### Step 3 — Input

```text id="example4"
[101, 250, 51, 732]
```

### Step 4 — Target

```text id="example5"
[250, 51, 732, 13]
```

### Step 5 — Prediction Tasks

```text id="example6"
101 → 250
250 → 51
51  → 732
732 → 13
```

### Step 6 — Model

```text id="example7"
Input IDs
    ↓
Embeddings
    ↓
Transformer Blocks
    ↓
Hidden States
    ↓
Language Model Head
    ↓
Logits
```

### Step 7 — Loss

The predicted distributions are compared with:

```text id="example8"
[250, 51, 732, 13]
```

The resulting loss is used to update the model parameters.

---

# 32. Why This Training Method Is Powerful

A single long sequence can provide many next-token prediction tasks.

For example:

```text id="power1"
Token 1 → Token 2
Token 2 → Token 3
Token 3 → Token 4
Token 4 → Token 5
...
```

Therefore, a large collection of token sequences can provide a very large number of training signals.

This is the central idea behind autoregressive language-model training.

---

# 33. Input and Target During Inference

During normal inference, there is no known target sequence.

For example, the user provides:

```text id="infer1"
"The cat"
```

The model predicts:

```text id="infer2"
"is"
```

Then the sequence becomes:

```text id="infer3"
"The cat is"
```

The model predicts again:

```text id="infer4"
"sleeping"
```

Then:

```text id="infer5"
"The cat is sleeping"
```

This continues until a stopping condition is reached.

So:

```text id="infer6"
Training:
Known Input + Known Target

Inference:
Input + Model-Generated Next Token
```

---

# 34. Training vs Inference

| Training                                        | Inference                                  |
| ----------------------------------------------- | ------------------------------------------ |
| Target tokens are known                         | Future tokens are unknown                  |
| Input and target are created from training data | Input comes from a prompt/current sequence |
| Predictions are compared with targets           | Predicted tokens are selected/generated    |
| Loss is calculated                              | Normally no training loss is used          |
| Parameters are updated                          | Parameters are normally not updated        |
| Multiple positions can be trained in parallel   | Generation is autoregressive               |

---

# 35. Common Misunderstandings

### ❌ "The target is the whole answer."

Not necessarily.

For a causal language model, the target is typically the next token at each prediction position.

---

### ❌ "Input and target are completely different datasets."

No.

They are normally created by shifting the same token sequence.

---

### ❌ "The model only predicts one token during training."

No.

Predictions for many positions can be computed in parallel.

---

### ❌ "The model can see the future target during training."

Not through the attention mechanism in a properly configured causal decoder.

Causal masking prevents future-token information from being used.

---

### ❌ "The target is converted into an embedding and given to the Transformer."

The target is used as the expected output for calculating the training loss. It is not normally provided to the model as future-token information.

---

### ❌ "Input means a question."

No.

Input can be any training text sequence.

---

### ❌ "Target means a human-written answer."

Not for ordinary next-token pretraining.

The target is generally the next token in the training sequence.

---

# 36. Simple Mental Model 🧠

Imagine reading a sentence one token at a time and asking:

> What should come next?

For:

```text id="mental1"
The cat is sleeping
```

we create:

```text id="mental2"
The       → cat
The cat   → is
The cat is → sleeping
```

The model sees the left side and learns to predict the right side.

That is the basic idea of input and target construction for causal language-model training.

---

# 37. Key Takeaways 📌

* 🎯 **Input** is the token sequence given to the model.
* 🏷️ **Target** is the expected next token at each prediction position.
* 🔄 The target sequence is created by shifting the original token sequence by one position.
* 🧩 One sequence can create many next-token prediction tasks.
* 🔒 Causal masking prevents future tokens from leaking into earlier predictions.
* ⚡ Multiple prediction positions can be processed in parallel during training.
* 🧠 The Transformer produces logits, not directly the target token IDs.
* 📊 The target is used to calculate the training loss.
* 📦 Input and target normally have matching batch and sequence dimensions.
* 🔢 Input and target are derived from the same underlying token sequence.
* 👨‍🏫 Teacher forcing allows training to use the known correct previous tokens.
* 🔄 During inference, future target tokens are not known; the model generates them step by step.
* ⚙️ The resulting loss is used for backpropagation and parameter updates.

The core idea is:

```text id="finalflow"
Token Sequence
      ↓
Shift by One Position
      ↓
Input              Target
[The] [cat] [is]   [cat] [is] [sleeping]
      ↓
      Transformer
           ↓
         Logits
           ↓
    Compare With Target
           ↓
          Loss
           ↓
    Backpropagation
           ↓
   Parameter Updates
```
