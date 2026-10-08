📦 Batches

A batch is a group of training sequences processed together during one training step.



Instead of sending one training sequence to the LLM at a time, training usually processes multiple sequences together.

Training Dataset
       ↓
Training Sequences
       ↓
     Batches
       ↓
  Forward Pass
       ↓
     Loss
       ↓
 Backpropagation
       ↓
   Optimizer
       ↓
Parameter Update


Batches are mainly used to make training more efficient and practical on modern hardware such as GPUs and TPUs.

1. What Is a Batch?

Suppose we have many training sequences:

Sequence 1
Sequence 2
Sequence 3
Sequence 4
Sequence 5
Sequence 6
Sequence 7
Sequence 8


We can group them into batches:

Batch 1
 ├── Sequence 1
 ├── Sequence 2
 ├── Sequence 3
 └── Sequence 4

Batch 2
 ├── Sequence 5
 ├── Sequence 6
 ├── Sequence 7
 └── Sequence 8


If each batch contains 4 sequences:

Batch Size = 4


2. Why Do We Use Batches?

Training an LLM on one sequence at a time is usually inefficient.



Modern hardware is designed to perform many numerical operations in parallel.



Instead of:

Sequence 1 → Model
Sequence 2 → Model
Sequence 3 → Model
Sequence 4 → Model


we can process:

┌───────────────┐
│ Sequence 1    │
│ Sequence 2    │
│ Sequence 3    │
│ Sequence 4    │
└───────────────┘
        ↓
      Model


This allows the hardware to perform many computations together.

3. Batch Size

Batch size is the number of training sequences included in one batch.



For example:

Batch Size = 4


means:

4 training sequences
        ↓
     One batch


Another example:

Batch Size = 32


means:

32 training sequences
        ↓
      One batch


Batch size is a training configuration, not a property of the language itself.

4. Simple Example

Suppose the dataset contains 12 training sequences:

S1
S2
S3
S4
S5
S6
S7
S8
S9
S10
S11
S12


With:

Batch Size = 4


we get:

Batch 1:
S1 S2 S3 S4

Batch 2:
S5 S6 S7 S8

Batch 3:
S9 S10 S11 S12


So:

12 sequences ÷ 4 sequences per batch = 3 batches


5. Batch and Sequence Are Different

These two concepts are often confused.

Sequence

A sequence is an ordered collection of tokens.



Example:

[The] [cat] [is] [sleeping]


Batch

A batch is a collection of sequences.

Batch
 ├── [The] [cat] [is] [sleeping]
 ├── [A] [dog] [is] [running]
 ├── [The] [bird] [is] [flying]
 └── [The] [sun] [is] [bright]


So:

Sequence = tokens
Batch = multiple sequences


6. Batch Size vs Sequence Length

These are two different dimensions.



Suppose:

Batch Size = 4
Sequence Length = 8


Then conceptually:

             Sequence Length
              ←──────────→

Batch 1   [t1 t2 t3 t4 t5 t6 t7 t8]
Batch 2   [t1 t2 t3 t4 t5 t6 t7 t8]
Batch 3   [t1 t2 t3 t4 t5 t6 t7 t8]
Batch 4   [t1 t2 t3 t4 t5 t6 t7 t8]


The input token tensor can be represented as:

[B, N]


where:



B = batch size

N = sequence length



For this example:

[4, 8]


7. Batch Size and Sequence Length Together

A training batch can therefore be viewed as:

Batch
   ↓
Multiple sequences
   ↓
Each sequence contains multiple tokens


For example:

Batch Size = 3
Sequence Length = 5

        Token positions
        1  2  3  4  5

Seq 1  [A][B][C][D][E]
Seq 2  [F][G][H][I][J]
Seq 3  [K][L][M][N][O]


Shape:

[3, 5]


8. Batches During LLM Training

For a causal language model, each sequence normally contains input and target tokens.



For example:

Original sequence:

[The] [cat] [is] [sleeping]


Input:

[The] [cat] [is]


Target:

[cat] [is] [sleeping]


With multiple sequences:

Inputs:
[The] [cat] [is]
[A]   [dog] [is]
[The] [sun] [is]

Targets:
[cat] [is] [sleeping]
[dog] [is] [running]
[sun] [is] [bright]


These can be processed as one batch.

9. Batch Shape

Suppose:

Batch Size = 3
Sequence Length = 4


The input IDs may have shape:

[3, 4]


For example:

[
  [101, 245, 37, 892],
  [101, 781, 64, 932],
  [101, 512, 29, 745]
]


Each row represents one sequence.

Row 1 → Sequence 1
Row 2 → Sequence 2
Row 3 → Sequence 3


10. From Token IDs to Embeddings

The batch of token IDs is passed into the embedding layer.



Conceptually:

Input IDs
[B, N]
   ↓
Token Embeddings
   ↓
[B, N, D]


Where:



B = batch size

N = sequence length

D = model hidden/embedding dimension



For example:

Input:
[32, 128]

Embedding dimension:
768

Representation:
[32, 128, 768]


This is an illustrative example.

11. Batch Through the Transformer

The batch then moves through the Transformer blocks.

Input IDs
    ↓
Embeddings
    ↓
Transformer Block 1
    ↓
Transformer Block 2
    ↓
Transformer Block 3
    ↓
...
    ↓
Final Transformer Block


The batch dimension remains part of the computation.



For example:

[B, N, D]
   ↓
Transformer
   ↓
[B, N, D]


The exact internal tensor shapes vary across components, but the batch represents multiple sequences being processed together.

12. Batch Through the Output Layer

The final hidden representations are converted into vocabulary logits.



Conceptually:

[B, N, D]
     ↓
Language Model Head
     ↓
[B, N, V]


Where:



B = batch size

N = sequence length

D = hidden dimension

V = vocabulary size



For example:

[B, N, D]
     ↓
[4, 8, 768]
     ↓
[4, 8, 50,000]


The vocabulary size here is only an illustrative example.

13. Loss for a Batch

Each sequence produces predictions for its target tokens.



Conceptually:

Batch
 ↓
Predictions
 ↓
Compare with Targets
 ↓
Per-token Losses
 ↓
Batch Loss


For example:

Sequence 1 Loss = 1.2
Sequence 2 Loss = 0.8
Sequence 3 Loss = 1.5
Sequence 4 Loss = 1.0


A training setup can aggregate these losses, commonly by taking an average over valid prediction positions.

Batch Loss
≈ average of relevant token losses


The exact reduction can depend on the training implementation.

14. Why Average the Loss?

Suppose one batch contains many prediction positions.



If we simply added all losses together, the numerical value would depend strongly on how many valid tokens were included.



Averaging provides a more consistent scale.



Conceptually:

Token Losses
     ↓
Aggregation
     ↓
Batch Loss


The exact loss reduction can vary by implementation.

15. Backpropagation on a Batch

After calculating the batch loss:

Batch Loss
    ↓
Backpropagation
    ↓
Gradients


The gradients are calculated using the batch's predictions and targets.



These gradients represent the combined training signal from the examples in that batch.

16. Parameter Update After a Batch

After gradients are calculated:

Batch
 ↓
Forward Pass
 ↓
Loss
 ↓
Backpropagation
 ↓
Gradients
 ↓
Optimizer
 ↓
Parameter Update


So one batch is commonly associated with one optimizer update when gradient accumulation is not being used.



This gives a useful mental model:

One batch → one training step → one parameter update

However, gradient accumulation can intentionally change this relationship.

17. What Is a Training Step?

A training step generally refers to one optimizer update.



In the simplest setup:

One Batch
    ↓
Forward Pass
    ↓
Loss
    ↓
Backpropagation
    ↓
Optimizer
    ↓
One Parameter Update


Therefore:

1 batch ≈ 1 training step


when there is no gradient accumulation.

18. Batches and Parameter Updates

Suppose we have:

Dataset = 1000 sequences
Batch Size = 100


Then:

1000 ÷ 100 = 10 batches


A simplified training process is:

Batch 1 → Update
Batch 2 → Update
Batch 3 → Update
Batch 4 → Update
Batch 5 → Update
Batch 6 → Update
Batch 7 → Update
Batch 8 → Update
Batch 9 → Update
Batch 10 → Update


So there are approximately:

10 training steps


for that pass through the dataset, assuming all sequences are used once and there is no additional batching behavior.

19. What Happens When the Dataset Is Not Divisible?

Suppose:

Dataset = 10 sequences
Batch Size = 4


The batches could be:

Batch 1 → 4 sequences
Batch 2 → 4 sequences
Batch 3 → 2 sequences


The final batch is smaller.



Training frameworks can handle this in different ways.



For example, a training loader may:



Keep the smaller final batch

Drop the final incomplete batch



The choice depends on the training setup.

20. Shuffling the Dataset

Training sequences are often shuffled before batching.



For example, without shuffling:

Batch 1 → S1 S2 S3 S4
Batch 2 → S5 S6 S7 S8


With shuffling:

Batch 1 → S7 S2 S9 S1
Batch 2 → S5 S8 S3 S6


Shuffling can help prevent the model from seeing training examples in the same fixed order every time.



The exact data-ordering strategy depends on the training setup.

21. Batch Size and Memory

Larger batches generally require more memory.



For example:

Small Batch
     ↓
Less memory

Large Batch
     ↓
More memory


This is because more sequences and their intermediate activations need to be processed.



For Transformer models, memory usage also depends heavily on:



Sequence length

Model size

Number of layers

Hidden dimension

Attention implementation

Precision

Optimizer state

Activation storage



So batch size is only one part of total memory usage.

22. Batch Size and Speed

A larger batch can allow hardware to perform more work in parallel.



Conceptually:

Very Small Batch
       ↓
Less parallel work


Larger Batch
       ↓
More parallel work


However, larger is not automatically better.



At some point:

Larger Batch
    ↓
Memory pressure
    ↓
Possible slowdown / out-of-memory


The useful batch size depends on the hardware and training configuration.

23. Batch Size and Learning Behavior

Batch size can also affect the optimization process.



A smaller batch gives gradients based on fewer examples.



A larger batch gives gradients based on more examples.



Conceptually:

Small Batch
    ↓
Gradient based on fewer examples


Large Batch
    ↓
Gradient based on more examples


Larger batches can produce a more averaged gradient estimate, while smaller batches can introduce more variation between updates.

24. Batch Size Is Not Context Window

These concepts are completely different.

Batch size

Number of sequences processed together.

Batch Size = 32


Context window

Maximum number of tokens the model can process as context for a given input.

Context Window = 8,192 tokens


Therefore:

Batch Size
    ↓
How many sequences?

Context Window
    ↓
How many tokens can one sequence contain?


25. Batch Size Is Not Sequence Length

Another important distinction:

Batch Size
= Number of sequences


Sequence Length
= Number of tokens in each sequence


Example:

Batch Size = 8
Sequence Length = 512


means:

8 sequences
×
512 tokens per sequence


Conceptually:

8 rows
512 token positions per row


26. Batch Size Is Not Vocabulary Size

These are unrelated.

Batch Size
= number of sequences processed together


Vocabulary Size
= number of tokens known by the tokenizer/model vocabulary


For example:

Batch Size = 16
Vocabulary Size = 50,000


These numbers describe completely different things.

27. Padding in Batches

Different sequences may have different lengths.



For example:

Sequence 1:
[The] [cat] [is]

Sequence 2:
[The] [dog] [is] [running]

Sequence 3:
[Birds] [can] [fly]


To create a rectangular batch tensor, shorter sequences may be padded:

[The]   [cat] [is] [PAD]
[The]   [dog] [is] [running]
[Birds] [can] [fly] [PAD]


A mask can indicate which positions are padding.



For causal language-model training, the exact padding and masking strategy depends on the implementation.

28. Padding Does Not Represent Real Text

A padding token is used to make sequences compatible with a batch shape.



For example:

[The] [cat] [is] [PAD]


[PAD] does not mean the original sentence actually contained that token.



It is structural information used by the training system.

29. Batch Processing With Variable-Length Sequences

There are different ways to handle variable-length sequences.



Common approaches include:



Padding

Grouping similar-length sequences

Packing sequences

Dynamic batching



The exact method depends on the training system.



The important idea is:

The model needs an efficient way to process multiple token sequences together.

30. Gradient Accumulation

Sometimes the available GPU memory cannot fit the desired effective batch size.



Gradient accumulation can help.



Instead of updating parameters after every small batch:

Small Batch 1
     ↓
Calculate Gradients

Small Batch 2
     ↓
Calculate Gradients

Small Batch 3
     ↓
Calculate Gradients

Small Batch 4
     ↓
Calculate Gradients


the gradients can be accumulated before the optimizer update.



Conceptually:

Small Batch 1 → Gradients
                    ↓
Small Batch 2 → Gradients
                    ↓
Small Batch 3 → Gradients
                    ↓
Small Batch 4 → Gradients
                    ↓
              Optimizer
                    ↓
            Parameter Update


This allows several smaller batches to contribute to one optimizer update.

31. Effective Batch Size

With gradient accumulation, we can distinguish:

Micro-batch

The smaller batch processed at one time.

Effective batch size

The total number of training examples contributing to one optimizer update.



For example:

Micro-batch size = 8
Gradient accumulation steps = 4


Then conceptually:

Effective Batch Size
= 8 × 4
= 32 sequences


This is a simplified calculation assuming the batches are combined directly and ignoring other implementation details.

32. Batch vs Micro-Batch

Without gradient accumulation:

Batch
 ↓
Optimizer Update


With gradient accumulation:

Micro-batch 1
      ↓
Micro-batch 2
      ↓
Micro-batch 3
      ↓
Micro-batch 4
      ↓
Optimizer Update


So the term batch can sometimes be used differently depending on the training implementation.



For a beginner mental model:

Micro-batch = data processed in one forward/backward pass

Effective batch = data contributing to one optimizer update


33. Batches and Training Steps

Without gradient accumulation:

Batch 1 → Step 1
Batch 2 → Step 2
Batch 3 → Step 3
Batch 4 → Step 4


With gradient accumulation:

Micro-batch 1
Micro-batch 2
Micro-batch 3
Micro-batch 4
       ↓
     Step 1


This distinction becomes important when calculating training steps.

34. Batches and Epochs

An epoch means one complete pass through the training dataset.



Suppose:

Dataset = 1000 sequences
Batch Size = 100


Then one epoch contains approximately:

10 batches


So:

Epoch 1
 ├── Batch 1
 ├── Batch 2
 ├── Batch 3
 ├── ...
 └── Batch 10


After these batches, the model has processed the dataset once.

35. Multiple Epochs

If training uses 3 epochs:

Epoch 1
 ├── Batch 1
 ├── Batch 2
 └── ...

Epoch 2
 ├── Batch 1
 ├── Batch 2
 └── ...

Epoch 3
 ├── Batch 1
 ├── Batch 2
 └── ...


The model sees the training dataset multiple times.



The parameters continue to be updated across these training steps.

36. Batches and Data Order

If the dataset is shuffled between epochs, the model may see a different ordering of sequences in each epoch.



For example:

Epoch 1:
S1 → S2 → S3 → S4

Epoch 2:
S3 → S1 → S4 → S2


This can reduce dependence on one fixed ordering.



The exact behavior depends on the data loader and training configuration.

37. Batches and Training Efficiency

Batches allow training systems to take advantage of parallel computation.



The basic idea is:

Many sequences
      ↓
One batch
      ↓
Parallel computation
      ↓
Efficient hardware utilization


This is particularly important for large Transformer models because their computations involve large matrix operations that GPUs and TPUs can execute efficiently.

38. A Complete Example

Suppose we have:

Training sequences = 1,000
Batch size = 10
Sequence length = 128


Then:

1,000 sequences
      ↓
100 batches


Each batch contains:

10 sequences
×
128 tokens


Input shape:

[10, 128]


After embeddings:

[10, 128, D]


After the Transformer:

[10, 128, D]


After the language-model head:

[10, 128, V]


Then:

Predictions
    ↓
Targets
    ↓
Loss
    ↓
Backpropagation
    ↓
Gradients
    ↓
Optimizer
    ↓
Parameter Update


This process repeats for all 100 batches.

39. Complete Batch Training Flow

The complete flow can be represented as:

Training Data
      ↓
Prepared Text
      ↓
Tokenization
      ↓
Token IDs
      ↓
Training Sequences
      ↓
Shuffle / Organize Data
      ↓
Create Batches
      ↓
┌───────────────────────────┐
│ Batch of Training         │
│ Sequences                 │
└───────────────────────────┘
      ↓
Input + Target
      ↓
Forward Pass
      ↓
Logits
      ↓
Loss
      ↓
Backpropagation
      ↓
Gradients
      ↓
Optimizer
      ↓
Parameter Update
      ↓
Next Batch


40. Batch Size and Hardware

The appropriate batch size depends on the available hardware and the model.



Factors include:



GPU/TPU memory

Model parameter count

Sequence length

Hidden dimension

Number of Transformer layers

Numerical precision

Activation memory

Optimizer memory

Attention implementation



Therefore, there is no single batch size that is best for every LLM.

41. Why Not Always Use the Largest Possible Batch?

A larger batch is not automatically better.



If the batch becomes too large:

Batch Size ↑
     ↓
Memory Usage ↑
     ↓
Possible Out-of-Memory Error


Large batch sizes can also change the optimization behavior and may require appropriate learning-rate or training adjustments.



The goal is to choose a batch configuration that works well with the training objective and available resources.

42. Common Misunderstandings

❌ "A batch is one token sequence."

No.

Sequence = one ordered group of tokens

Batch = group of sequences


❌ "Batch size means number of tokens."

Usually, batch size means the number of sequences/examples processed together.



The total number of tokens also depends on sequence length.



For fixed-length sequences:

Tokens per batch
≈ Batch Size × Sequence Length


❌ "Batch size and context window are the same."

No.

Batch Size → number of sequences

Context Window → number of tokens available in a sequence/context


❌ "Every batch always has exactly the same number of sequences."

Not necessarily.



The final batch can be smaller unless the training system drops it or handles it differently.

❌ "A larger batch always gives better training."

No.



Batch size affects memory, computation, gradient estimates, optimization behavior, and potentially training efficiency.

❌ "A batch update means each sequence gets its own parameter update."

Normally, the batch contributes to a combined loss/gradient, and the optimizer performs a shared parameter update.

❌ "Gradient accumulation means the model updates after every micro-batch."

No.



With gradient accumulation, multiple micro-batches can contribute gradients before one optimizer update.

🧠 Simple Mental Model

Think of a batch as a group of students answering questions together.

One Student
    ↓
One Training Sequence


Classroom
    ↓
Many Students
    ↓
One Batch


The model processes the batch, calculates the training error, computes gradients, and then updates its parameters.

Batch
  ↓
Predictions
  ↓
Loss
  ↓
Gradients
  ↓
Optimizer
  ↓
Parameter Update


So the simplest definition is:

A batch is a group of training sequences processed together before calculating the training update.

🔑 Key Takeaways

A batch is a group of training sequences processed together.

Batch size is the number of sequences in a batch.

A sequence contains tokens; a batch contains sequences.

Batch size and sequence length are different dimensions.

A typical input tensor has shape [Batch, Sequence Length].

After embeddings, the representation is commonly [Batch, Sequence Length, Hidden Dimension].

Batches allow modern hardware to process multiple examples efficiently.

A batch produces predictions and a loss from multiple training examples.

Backpropagation calculates gradients from the batch loss.

The optimizer uses those gradients to update model parameters.

Without gradient accumulation, one batch commonly corresponds to one optimizer update.

With gradient accumulation, multiple micro-batches can contribute to one optimizer update.

Batch size affects memory usage, computation, and optimization behavior.

Batch size is different from context window, sequence length, and vocabulary size.

An epoch represents one complete pass through the training dataset.

Batching is one of the fundamental mechanisms that makes large-scale neural-network training practical.
