# 📦 Training Sequences

After training data has been tokenized, the resulting token IDs need to be organized into sequences that can be used to train an LLM.

A **training sequence** is an ordered series of tokens that the model processes together as one training example.

The basic flow is:

```text
Training Text
      ↓
Tokenization
      ↓
Token IDs
      ↓
Training Sequences
      ↓
Input / Target
      ↓
Batches
      ↓
LLM Training
```

Training sequences are the bridge between tokenized data and the actual training process.

---

## 1. What Is a Training Sequence?

A training sequence is a group of token IDs arranged in their original order.

For example:

```text
Text:

The cat is sleeping.
```

After tokenization, it might become:

```text
[101, 245, 37, 892, 13]
```

This sequence contains five tokens.

The model can use this sequence to learn relationships between the tokens and predict the next token.

---

## 2. Why Do We Need Training Sequences?

A document can contain thousands or millions of tokens.

The model usually cannot process an unlimited number of tokens at once.

Therefore, tokenized data is organized into manageable sequences.

For example:

```text
Long Document
      ↓
Tokenization
      ↓
Thousands of Token IDs
      ↓
Split into Training Sequences
      ↓
Sequence 1
Sequence 2
Sequence 3
...
```

Each sequence can then be processed by the model.

---

# 3. Example of a Long Token Sequence

Suppose a document becomes:

```text
[12, 45, 67, 89, 23, 91, 44, 76, 18, 55, 32, 81]
```

If the selected sequence length is 4, it could be organized as:

```text
Sequence 1:
[12, 45, 67, 89]

Sequence 2:
[23, 91, 44, 76]

Sequence 3:
[18, 55, 32, 81]
```

The sequence length of each example is 4.

The numbers are only illustrative.

---

# 4. Sequence Length

**Sequence length** is the number of tokens contained in a training sequence.

For example:

```text
[12, 45, 67, 89]
```

has:

```text
Sequence length = 4
```

Another example:

```text
[12, 45, 67, 89, 23, 91, 44, 76]
```

has:

```text
Sequence length = 8
```

Sequence length is measured in **tokens**, not words or characters.

---

# 5. Sequence Length vs Context Window

These concepts are related but should not be treated as exactly the same.

### Sequence Length

The number of tokens in a particular training example.

```text
Sequence:
[12, 45, 67, 89]

Length = 4
```

### Context Window

The maximum amount of tokenized context that a model can handle in a given configuration.

For example:

```text
Context window = 8,192 tokens
```

A training sequence may be shorter than the model's maximum context length.

Depending on the training setup, sequences may also be constructed to use the model's available context length.

---

# 6. Why Sequence Length Matters

Sequence length affects several parts of LLM training.

It affects:

* 🧠 How much context the model sees
* 💾 Memory usage
* ⚡ Computation
* 📦 Batch size
* 🔄 Number of training examples
* 🔍 Attention computation

For Transformer self-attention, the number of token-to-token relationships grows roughly with the square of sequence length.

Conceptually:

```text
More tokens per sequence
        ↓
More attention relationships
        ↓
More computation and memory
```

This is one reason sequence length is an important training decision.

---

# 7. Creating Sequences from Tokenized Data

Suppose tokenized training data is:

```text
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
```

If we choose a sequence length of 5:

```text
Sequence 1:
[10, 20, 30, 40, 50]

Sequence 2:
[60, 70, 80, 90, 100]
```

The original order is preserved.

This allows the model to learn relationships between nearby and longer-range tokens within each sequence.

---

# 8. Sequence Construction from Documents

Training data may contain many documents:

```text
Document A
Document B
Document C
Document D
```

After tokenization:

```text
Document A → Token IDs
Document B → Token IDs
Document C → Token IDs
Document D → Token IDs
```

These tokenized documents can then be organized into training sequences.

The exact method depends on the training pipeline.

A simplified view is:

```text
Documents
    ↓
Tokenization
    ↓
Tokenized Documents
    ↓
Sequence Construction
    ↓
Training Sequences
```

---

# 9. Preserving Token Order

Token order is extremely important.

Consider:

```text
"The dog chased the cat."
```

and:

```text
"The cat chased the dog."
```

The same general words appear, but their order changes the meaning.

Therefore, a training sequence preserves the order of tokens:

```text
Token 1 → Token 2 → Token 3 → Token 4 → ...
```

The Transformer uses positional information to represent where tokens occur in the sequence.

---

# 10. Training Sequences and Next-Token Prediction

For a decoder-only LLM, training sequences are used for **next-token prediction**.

Suppose the sequence is:

```text
[The] [cat] [is] [sleeping]
```

The model can learn:

```text
The
 ↓
cat
```

Then:

```text
The cat
   ↓
   is
```

Then:

```text
The cat is
     ↓
 sleeping
```

This can be represented using shifted input and target sequences.

---

# 11. Input and Target Sequences

Suppose the token IDs are:

```text
[10, 20, 30, 40, 50]
```

The input can be:

```text
[10, 20, 30, 40]
```

The target can be:

```text
[20, 30, 40, 50]
```

So:

```text
Input:
10 → 20 → 30 → 40

Target:
20 → 30 → 40 → 50
```

The model predicts:

```text
10 → 20
10,20 → 30
10,20,30 → 40
10,20,30,40 → 50
```

Causal masking prevents a position from using future target information.

---

# 12. Why One Sequence Produces Multiple Training Targets

Consider:

```text
[The] [cat] [is] [sleeping]
```

The sequence provides multiple prediction positions:

```text
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

Therefore, one sequence can provide multiple training signals.

This makes next-token training efficient.

---

# 13. Parallel Training

Although the model is learning an autoregressive task, training does not require predicting one token at a time in separate forward passes.

For example:

```text
Input:
[The] [cat] [is] [sleeping]
```

with causal masking allows the model to calculate predictions for multiple positions in parallel.

Conceptually:

```text
The       → cat
The cat   → is
The cat is → sleeping
```

The causal mask ensures that each position cannot access future tokens.

This is one of the important advantages of Transformer-based training.

---

# 14. Causal Masking Inside a Training Sequence

Suppose the sequence is:

```text
[The] [cat] [is] [sleeping]
```

The attention pattern is approximately:

```text
The       → The

cat       → The, cat

is        → The, cat, is

sleeping  → The, cat, is, sleeping
```

The current token can attend to itself and previous tokens.

It cannot attend to future tokens.

Visualized as a causal mask:

```text
        The  cat  is  sleeping

The      ✓    ✗    ✗      ✗
cat      ✓    ✓    ✗      ✗
is       ✓    ✓    ✓      ✗
sleeping ✓    ✓    ✓      ✓
```

This prevents information leakage from future tokens.

---

# 15. Fixed-Length Sequences

Many training pipelines use sequences of a selected length.

For example:

```text
Sequence length = 8
```

Then:

```text
[12, 45, 67, 89, 23, 91, 44, 76]
```

is one complete sequence.

Another sequence may be:

```text
[18, 55, 32, 81, 29, 63, 71, 10]
```

Fixed-length sequences can make batching and hardware utilization easier.

However, training systems can use different sequence-construction strategies.

---

# 16. Padding

Not every piece of text naturally has the same length.

For example:

```text
Sequence 1:
[10, 20, 30, 40]

Sequence 2:
[50, 60]

Sequence 3:
[70, 80, 90]
```

To put them into the same rectangular batch, padding may be used:

```text
[10, 20, 30, 40]
[50, 60, PAD, PAD]
[70, 80, 90, PAD]
```

The padding tokens are not intended to represent normal content.

A padding mask can be used so that padding positions do not affect the relevant computation.

Not every modern LLM training pipeline relies on padding in the same way; some use packing or other strategies.

---

# 17. Sequence Packing

Instead of padding many short examples, a training pipeline can sometimes combine multiple examples into a longer sequence.

For example:

```text
Example A:
[A1, A2, A3]

Example B:
[B1, B2]

Example C:
[C1, C2, C3]
```

could potentially be packed:

```text
[A1, A2, A3, B1, B2, C1, C2, C3]
```

The exact handling of boundaries depends on the training setup.

Packing can improve the use of available sequence space by reducing unnecessary padding.

---

# 18. Document Boundaries

When multiple documents are combined, the training pipeline may need to represent document boundaries.

For example:

```text
Document A
     ↓
Document B
```

may be separated using a special token or another boundary mechanism.

Conceptually:

```text
[Document A tokens] [END] [Document B tokens]
```

The exact method depends on the tokenizer and training design.

---

# 19. Short Documents

Suppose the desired sequence length is 8, but a document contains only 3 tokens:

```text
[12, 45, 67]
```

A training pipeline may:

* Combine it with other data
* Pad it
* Pack multiple examples
* Use a shorter sequence
* Apply another sequence-building strategy

There is no single universal solution.

---

# 20. Long Documents

Suppose a document contains many more tokens than the selected sequence length.

For example:

```text
Document
↓
50,000 tokens
```

It can be divided into smaller sequences:

```text
Sequence 1
Sequence 2
Sequence 3
...
Sequence N
```

A simplified example:

```text
50,000 tokens
      ↓
4,096-token sequences
      ↓
Many training examples
```

The exact length is model- and training-dependent.

---

# 21. Sliding Windows

Another possible strategy is to create overlapping sequences.

For example, suppose:

```text
Tokens:
[1, 2, 3, 4, 5, 6, 7, 8]
```

A simplified sliding-window approach could produce:

```text
Sequence 1:
[1, 2, 3, 4]

Sequence 2:
[3, 4, 5, 6]

Sequence 3:
[5, 6, 7, 8]
```

Here, some tokens appear in multiple sequences.

This is different from simply splitting the data into non-overlapping chunks.

Large-scale training pipelines may use other packing and sampling strategies instead.

---

# 22. Non-Overlapping Chunks vs Sliding Windows

### Non-overlapping chunks

```text
[1, 2, 3, 4]
[5, 6, 7, 8]
```

### Sliding windows

```text
[1, 2, 3, 4]
[3, 4, 5, 6]
[5, 6, 7, 8]
```

The first method does not intentionally repeat tokens between sequences.

The second method creates overlapping context.

The choice depends on the training strategy.

---

# 23. Sequence Boundaries Matter

Consider:

```text
Document A:
"The cat is sleeping."

Document B:
"The weather is sunny."
```

If they are combined carelessly:

```text
"The cat is sleeping. The weather is sunny."
```

the model may treat the transition as part of the same continuous token stream.

Depending on the training objective and data construction strategy, explicit document boundaries may be useful.

This is why sequence construction is not simply about cutting text into equal-sized pieces.

---

# 24. Training Sequences and Context

A sequence provides the model with a limited amount of context.

For example:

```text
Sequence:
[The, cat, is, sleeping]
```

The model can use information available within the sequence when predicting tokens.

For a decoder-only model, causal masking determines which positions can access which earlier positions.

Therefore:

```text
Sequence
   ↓
Context available to each position
   ↓
Next-token prediction
```

---

# 25. Training Sequences and Attention

For a sequence containing `N` tokens, self-attention compares token positions with one another, subject to masking.

Conceptually:

```text
N tokens
   ↓
N × N attention relationships
```

For example:

```text
4 tokens
   ↓
4 × 4 attention matrix
```

The matrix contains relationships between query positions and key positions.

With causal masking:

```text
Future positions are blocked.
```

This is why longer sequences can require substantially more computation and memory.

---

# 26. Training Sequences and Batches

After sequences are created, they are grouped into batches.

For example:

```text
Sequence 1 → [12, 45, 67, 89]
Sequence 2 → [34, 91, 20, 55]
Sequence 3 → [72, 18, 44, 31]
Sequence 4 → [61, 29, 77, 14]
```

A batch might contain:

```text
4 sequences
```

Conceptually:

```text
Training Sequences
        ↓
      Batch
        ↓
     Forward Pass
        ↓
       Loss
        ↓
   Parameter Update
```

---

# 27. Batch Size vs Sequence Length

These two concepts are often confused.

### Batch Size

Number of sequences processed together.

```text
Batch size = 4
```

means:

```text
4 sequences
```

are processed together.

### Sequence Length

Number of tokens in each sequence.

```text
Sequence length = 512
```

means each sequence contains 512 token positions.

So a simplified batch shape could be:

```text
[Batch Size, Sequence Length]

[4, 512]
```

This means:

```text
4 sequences
512 tokens per sequence
```

---

# 28. Training Sequence Shape

After batching, token IDs can be represented conceptually as:

```text
[B, N]
```

where:

```text
B = batch size
N = sequence length
```

For example:

```text
[B, N] = [4, 512]
```

means:

```text
4 sequences
512 token positions each
```

After embedding lookup, the representation becomes something like:

```text
[B, N, D]
```

where:

```text
D = model hidden / embedding dimension
```

For example:

```text
[4, 512, 768]
```

is an illustrative shape.

---

# 29. Training Sequences and the Transformer

Once the token IDs are organized into sequences, they can enter the model.

The simplified flow is:

```text
Training Sequence
       ↓
Token IDs
       ↓
Embedding
       ↓
Positional Information
       ↓
Transformer Blocks
       ↓
Language Model Head
       ↓
Logits
       ↓
Next-Token Predictions
```

The sequence is therefore the basic unit of token-level context used by the Transformer during a training step.

---

# 30. What Happens Inside One Training Sequence?

Suppose we have:

```text
[The] [cat] [is] [sleeping]
```

The process is approximately:

```text
Tokens
   ↓
Token IDs
   ↓
Embeddings
   ↓
Positional Information
   ↓
Causal Self-Attention
   ↓
Feed-Forward Network
   ↓
More Transformer Blocks
   ↓
Language Model Head
   ↓
Logits
   ↓
Loss
```

The model compares its predictions with the target tokens.

---

# 31. Training Sequences Are Not the Same as Documents

A **document** is a piece of source content.

A **training sequence** is a token sequence constructed for model training.

One document can produce:

```text
Document
   ↓
Many training sequences
```

And one training sequence may potentially contain content from multiple documents, depending on the data-packing strategy.

Therefore:

```text
Document ≠ Training Sequence
```

---

# 32. Training Sequences Are Not the Same as Context Window

Another common confusion is:

```text
Training sequence = context window
```

These concepts are related but different.

A context window describes how much tokenized context a model can handle under a particular configuration.

A training sequence is an actual sequence of tokens used as a training example.

For example:

```text
Model context capability:
8,192 tokens

Training sequence:
4,096 tokens
```

This is completely possible.

---

# 33. Training Sequences Are Not Individual Words

A sequence contains tokens, not necessarily words.

For example:

```text
"unbelievable"
```

might become:

```text
["un", "believ", "able"]
```

So a sequence such as:

```text
[un, believ, able, ...]
```

contains token pieces.

The model operates on these token positions.

---

# 34. Data Ordering

Training data can be organized and sampled in different ways.

A training system may control:

```text
Document order
Sequence order
Batch order
Sampling
Shuffling
```

Shuffling training examples can help prevent the model from always seeing the same examples in the same order.

The exact data-ordering strategy depends on the training setup.

---

# 35. Epochs

An **epoch** can be thought of as one complete pass through a defined training dataset.

For example:

```text
Training Dataset
      ↓
All training sequences processed
      ↓
One Epoch
```

Then another epoch may process the data again.

However, very large LLM training runs are often described in terms of tokens processed rather than simply relying on traditional small-dataset epoch terminology.

---

# 36. Tokens Processed

For large-scale LLM training, an important quantity is the number of tokens processed.

For example:

```text
1 billion tokens
10 billion tokens
100 billion tokens
...
```

A simplified relationship is:

```text
Number of sequences
×
Tokens per sequence
≈
Tokens processed
```

Actual training pipelines can be more complex because of padding, packing, masking, repeated data, and other factors.

---

# 37. Sequence Length and Training Efficiency

Suppose we have the same total number of tokens.

### Shorter sequences

```text
Many shorter sequences
```

### Longer sequences

```text
Fewer longer sequences
```

Longer sequences provide more context per example but can increase attention-related computation and memory.

Shorter sequences can be cheaper per sequence but may provide less long-range context.

Therefore, sequence length is an important training design choice.

---

# 38. Complete Example

Suppose the original text is:

```text
"The cat is sleeping on the sofa."
```

### Step 1 — Tokenization

A tokenizer might produce:

```text
["The", " cat", " is", " sleeping", " on", " the", " sofa", "."]
```

### Step 2 — Token IDs

For illustration:

```text
[101, 245, 37, 892, 44, 67, 311, 13]
```

### Step 3 — Training Sequence

```text
[101, 245, 37, 892, 44, 67, 311, 13]
```

### Step 4 — Input

```text
[101, 245, 37, 892, 44, 67, 311]
```

### Step 5 — Target

```text
[245, 37, 892, 44, 67, 311, 13]
```

### Step 6 — Model

```text
Input
  ↓
Embeddings
  ↓
Transformer
  ↓
Logits
```

### Step 7 — Loss

The model compares its predicted tokens with:

```text
[245, 37, 892, 44, 67, 311, 13]
```

The loss measures how well the model predicted the target tokens.

---

# 39. Complete Training Sequence Pipeline

The complete process can be visualized as:

```text
┌──────────────────────────┐
│       Training Text      │
└────────────┬─────────────┘
             ↓
┌──────────────────────────┐
│       Tokenization       │
└────────────┬─────────────┘
             ↓
┌──────────────────────────┐
│        Token IDs         │
└────────────┬─────────────┘
             ↓
┌──────────────────────────┐
│  Sequence Construction   │
└────────────┬─────────────┘
             ↓
┌──────────────────────────┐
│    Training Sequences    │
└────────────┬─────────────┘
             ↓
┌──────────────────────────┐
│      Input / Target      │
└────────────┬─────────────┘
             ↓
┌──────────────────────────┐
│         Batches          │
└────────────┬─────────────┘
             ↓
┌──────────────────────────┐
│     Embedding Layer      │
└────────────┬─────────────┘
             ↓
┌──────────────────────────┐
│   Decoder-Only           │
│   Transformer            │
└────────────┬─────────────┘
             ↓
┌──────────────────────────┐
│    Next-Token Logits     │
└────────────┬─────────────┘
             ↓
┌──────────────────────────┐
│           Loss           │
└──────────────────────────┘
```

---

# 40. Common Misunderstandings

### ❌ "A training sequence is always one document."

No.

A document can produce multiple sequences, and sequences can sometimes be packed from multiple examples.

---

### ❌ "Every sequence must have exactly the same natural text length."

No.

Sequences may be padded, packed, truncated, or constructed using other strategies depending on the training pipeline.

---

### ❌ "Sequence length means number of words."

No.

Sequence length is measured in tokens.

---

### ❌ "The model predicts the entire sequence at once without masking."

Not for a standard causal decoder-only language model.

Causal masking prevents each position from accessing future tokens.

---

### ❌ "Longer sequences are always better."

No.

Longer sequences provide more context but generally increase computation and memory requirements.

---

### ❌ "Batch size and sequence length are the same."

No.

```text
Batch size
= number of sequences

Sequence length
= number of tokens per sequence
```

---

### ❌ "Sequence construction happens before tokenization."

Usually, text is tokenized first and then organized into token sequences, although real data pipelines can have more complex implementations.

---

# 41. Simple Mental Model 🧠

Think of training data as a very long stream of tokens.

```text
Huge Token Stream
──────────────────────────────────────────→

[1][2][3][4][5][6][7][8][9][10][11][12]...
```

The training pipeline organizes this stream into manageable sequences:

```text
Sequence 1
[1][2][3][4]

Sequence 2
[5][6][7][8]

Sequence 3
[9][10][11][12]
```

Then each sequence is shifted into input and target:

```text
Input:
[1][2][3]

Target:
[2][3][4]
```

The model learns to predict the next token while causal masking prevents future information from leaking into earlier positions.

---

# 42. Key Takeaways 📌

* 📦 A **training sequence** is an ordered group of token IDs used as a training example.
* 🔤 Training sequences are created after tokenization.
* 🔢 Sequence length is measured in tokens.
* 🧩 Long documents can be divided into multiple training sequences.
* ✂️ Sequence construction can use chunks, packing, padding, or other strategies.
* 🎯 Input and target sequences are shifted for next-token prediction.
* 🔒 Causal masking prevents future tokens from being used when predicting earlier positions.
* ⚡ Multiple prediction positions can be processed in parallel during Transformer training.
* 📦 Multiple sequences can be grouped into a batch.
* 📊 Batch size and sequence length are different dimensions.
* 🧠 Longer sequences provide more context but generally require more computation and memory.
* 📄 A document is not necessarily the same thing as a training sequence.
* 🌐 A training sequence can potentially contain content from multiple documents depending on the data pipeline.
* 🔄 Training sequences connect tokenized text to the Transformer training process.

The core idea is:

```text
Training Text
      ↓
Tokenization
      ↓
Token IDs
      ↓
Training Sequences
      ↓
Input / Target
      ↓
Batches
      ↓
Embeddings
      ↓
Transformer
      ↓
Next-Token Prediction
      ↓
Loss
      ↓
Parameter Updates
```
