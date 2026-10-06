# 🔄 Parameter Updates

Parameter updates are the step where the **learned values inside an LLM are changed using the gradients calculated during backpropagation**.

During training, the model repeatedly:

```text
Input Tokens
     ↓
Forward Pass
     ↓
Predictions
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

The goal is to gradually change the model's parameters so that its future predictions become better.

---

## 1. What Are Parameters?

Parameters are the numerical values inside a neural network that are learned during training.

For example:

* Weights
* Biases
* Attention projection parameters
* Feed-forward network parameters
* Embedding parameters
* Output projection parameters

A simplified model might contain:

```text
Parameter 1 = 0.50
Parameter 2 = -0.20
Parameter 3 = 1.10
Parameter 4 = 0.75
```

A real LLM contains a very large number of parameters.

These parameters are what the training process gradually adjusts.

---

# 2. Why Are Parameters Updated?

At the beginning of training, the model's parameters are usually initialized to values that do not yet produce useful language predictions.

For example:

```text
Input:
The cat is

Model prediction:
The → 20%
blue → 15%
running → 10%
...

Correct next token:
sleeping
```

The model gives a probability distribution, but the correct token may have a low probability.

The model calculates a loss.

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
Parameter Update
```

The parameters are changed so that future predictions can improve.

---

# 3. Parameter Update in Simple Terms

Think of parameter updates as:

> **Small adjustments to the model's internal numerical values that reduce the training loss.**

For example:

```text
Before training step:

weight = 0.50

After calculating gradient:

gradient = 0.20

After optimizer update:

weight = 0.48
```

The exact update depends on the optimizer and its settings.

---

# 4. Gradient and Parameter Are Different

A very important distinction:

| Concept          | Meaning                                            |
| ---------------- | -------------------------------------------------- |
| Parameter        | Value that the model learns                        |
| Loss             | Measures prediction error                          |
| Gradient         | Shows how loss changes with respect to a parameter |
| Optimizer        | Uses gradients to determine parameter updates      |
| Parameter Update | The actual change made to the parameter            |

The basic relationship is:

```text
Loss
 ↓
Gradient
 ↓
Optimizer
 ↓
Parameter Update
 ↓
New Parameter
```

---

# 5. Basic Gradient Descent Update

The simplest parameter update can be represented as:

```text
θ_new = θ_old - η × ∇L
```

Where:

* `θ_old` = current parameter
* `θ_new` = updated parameter
* `η` = learning rate
* `∇L` = gradient of the loss with respect to the parameter

The optimizer uses this information to update the parameter.

---

# 6. Simple Example

Suppose:

```text
Parameter = 0.80
Gradient = 0.30
Learning Rate = 0.10
```

Using the basic gradient descent formula:

```text
New Parameter
= 0.80 - (0.10 × 0.30)

= 0.80 - 0.03

= 0.77
```

So:

```text
Before:
0.80

After:
0.77
```

The parameter changed slightly.

This is one simple example of a parameter update.

---

# 7. What Does the Gradient Tell Us?

The gradient tells the optimizer how the loss changes when a parameter changes.

A simplified interpretation:

```text
Positive gradient
      ↓
Parameter tends to move downward

Negative gradient
      ↓
Parameter tends to move upward
```

The optimizer uses the gradient direction to decide how parameters should change.

The actual behavior can be more sophisticated for optimizers such as Adam and AdamW.

---

# 8. Learning Rate

The **learning rate** controls how large the parameter updates are.

For example:

```text
Small learning rate
        ↓
Small parameter updates
```

```text
Large learning rate
        ↓
Large parameter updates
```

### Learning rate too small

```text
Very small updates
      ↓
Training can become very slow
```

### Learning rate too large

```text
Very large updates
      ↓
Training can become unstable
```

Therefore, choosing an appropriate learning rate is important.

---

# 9. Parameter Updates During LLM Training

For an LLM, there are many parameters distributed across different components.

A simplified architecture is:

```text
Token Embeddings
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
       ↓
Language Model Head
```

Each component contains learnable parameters.

During training:

```text
Input
  ↓
Forward Pass
  ↓
Logits
  ↓
Loss
  ↓
Backpropagation
  ↓
Gradients for Parameters
  ↓
Optimizer
  ↓
Update Parameters
```

This happens across the trainable parameters of the model.

---

# 10. Parameters in Attention

Self-attention contains learnable projection parameters.

For example:

```text
Q = XWQ
K = XWK
V = XWV
```

Here:

* `X` = input representation
* `WQ` = Query projection parameters
* `WK` = Key projection parameters
* `WV` = Value projection parameters

These parameters can receive gradients during training.

The optimizer then updates them.

Simplified:

```text
WQ
 ↓
Gradient
 ↓
Optimizer
 ↓
Updated WQ
```

The same idea applies to other trainable parameters in attention.

---

# 11. Parameters in the Feed-Forward Network

A simplified FFN is:

```text
FFN(x) = W₂ σ(W₁x + b₁) + b₂
```

The trainable parameters include:

```text
W₁
b₁
W₂
b₂
```

During training, gradients are calculated for these parameters.

Then the optimizer updates them.

```text
W₁ ──→ Updated W₁
b₁ ──→ Updated b₁
W₂ ──→ Updated W₂
b₂ ──→ Updated b₂
```

---

# 12. Embedding Parameters Can Also Be Updated

Token embeddings are learned vectors.

Conceptually:

```text
Token ID
   ↓
Embedding Matrix
   ↓
Token Vector
```

The embedding matrix contains trainable values in many language-model training setups.

During backpropagation, gradients can flow into the relevant embedding parameters.

The optimizer can then update them.

Over training, these vectors become useful representations for tokens.

---

# 13. Output Projection Parameters

The final Transformer representation is converted into vocabulary logits.

A simplified equation is:

```text
z = hW + b
```

Where:

* `h` = hidden representation
* `W` = output projection parameters
* `b` = bias
* `z` = logits

The parameters of this output layer can also receive gradients and be updated.

Some architectures use weight tying between input embeddings and the output projection, while others do not.

---

# 14. One Complete Parameter Update

Consider a simplified training example:

```text
Input:
The cat is

Target:
sleeping
```

### Step 1 — Forward Pass

The model processes the input.

```text
The cat is
    ↓
LLM
    ↓
Logits
```

### Step 2 — Calculate Loss

The model's prediction is compared with the target.

```text
Prediction
    +
Target
    ↓
Loss
```

### Step 3 — Backpropagation

The loss is propagated backward.

```text
Loss
 ↓
Gradients
 ↓
Model Parameters
```

### Step 4 — Optimizer

The optimizer uses the gradients.

```text
Gradients
    ↓
Optimizer
```

### Step 5 — Parameter Update

The parameters are changed.

```text
Old Parameters
      ↓
Optimizer
      ↓
Updated Parameters
```

The complete process is:

```text
Input
  ↓
Forward Pass
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
  ↓
New Model Parameters
```

---

# 15. Parameter Updates Happen Repeatedly

One update is not enough to train an LLM.

The process repeats many times.

```text
Training Step 1
      ↓
Update Parameters

Training Step 2
      ↓
Update Parameters

Training Step 3
      ↓
Update Parameters

      ...

Training Step N
      ↓
Update Parameters
```

Over many training steps, the parameters gradually change.

---

# 16. Parameters Before and After Training

Conceptually:

```text
Before Training
────────────────

Model Parameters
       ↓
Random / Initial Values
       ↓
Poor Predictions
```

After many training updates:

```text
After Training
───────────────

Model Parameters
       ↓
Learned Values
       ↓
Better Language Predictions
```

The model does not manually store a rule such as:

```text
"After The cat is → sleeping"
```

Instead, training changes a very large collection of numerical parameters.

The learned information is distributed across these parameters.

---

# 17. Parameter Updates and Learning

When we say:

> "The model learns."

we mean that its parameters are being adjusted through training.

Conceptually:

```text
Training Data
      ↓
Predictions
      ↓
Loss
      ↓
Gradients
      ↓
Parameter Updates
      ↓
Changed Parameters
      ↓
Improved Predictions
```

So learning is not a separate magical process.

It is largely the result of repeatedly updating trainable parameters based on the training objective.

---

# 18. Parameter Updates Across Transformer Blocks

An LLM may contain many Transformer blocks.

For example:

```text
Input
  ↓
Block 1
  ↓
Block 2
  ↓
Block 3
  ↓
Block 4
  ↓
...
  ↓
Block N
  ↓
Output
```

Each block contains its own trainable parameters.

During backpropagation, gradients flow through the complete network.

Conceptually:

```text
Loss
 ↓
Block N
 ↓
Block N-1
 ↓
Block N-2
 ↓
...
 ↓
Block 2
 ↓
Block 1
 ↓
Embeddings
```

The optimizer can then update the corresponding parameters.

---

# 19. Parameter Updates Are Not the Same as Backpropagation

These concepts are closely connected but different.

### Backpropagation

Calculates gradients.

```text
Loss
 ↓
Backpropagation
 ↓
Gradients
```

### Optimizer

Uses gradients to determine parameter changes.

```text
Gradients
 ↓
Optimizer
 ↓
Update
```

### Parameter Update

Actually changes the parameter values.

```text
Old Parameter
      ↓
Update
      ↓
New Parameter
```

So:

```text
Backpropagation → calculates gradients

Optimizer → uses gradients

Parameter Update → changes parameters
```

---

# 20. Parameter Updates Are Not the Same as Loss

Loss tells us how wrong the model's prediction was.

For example:

```text
Loss = 2.5
```

This does not directly change the model.

Instead:

```text
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

The updated parameters can then produce a different loss on future training steps.

---

# 21. Parameter Updates Across a Batch

LLMs normally process multiple training examples together in a batch.

For example:

```text
Batch
 ├── Sequence 1
 ├── Sequence 2
 ├── Sequence 3
 └── Sequence 4
```

The model produces predictions for the batch.

A batch loss is calculated.

Then:

```text
Batch
 ↓
Forward Pass
 ↓
Batch Loss
 ↓
Backpropagation
 ↓
Gradients
 ↓
Optimizer
 ↓
Parameter Update
```

So the parameters are generally updated after processing a training batch or an effective batch assembled through techniques such as gradient accumulation.

---

# 22. One Update vs Many Updates

It is important to distinguish:

### One training step

```text
One batch
   ↓
Forward
   ↓
Loss
   ↓
Backpropagation
   ↓
Optimizer
   ↓
Parameter Update
```

### Many training steps

```text
Batch 1 → Update
Batch 2 → Update
Batch 3 → Update
Batch 4 → Update
   ...
```

Training consists of a very large number of such steps.

---

# 23. Parameters Do Not All Change by the Same Amount

Different parameters can receive different gradients.

For example:

```text
Parameter A
Gradient = 0.01

Parameter B
Gradient = 0.50

Parameter C
Gradient = -0.20
```

Therefore, their updates may be different.

Conceptually:

```text
Parameter A → small update

Parameter B → larger update

Parameter C → update in the opposite direction
```

The exact update depends on the optimizer.

---

# 24. Optimizer State

Some optimizers maintain additional information while training.

For example, Adam and AdamW maintain state associated with gradients.

Conceptually:

```text
Parameter
   +
Gradient
   +
Optimizer State
   ↓
Optimizer
   ↓
Parameter Update
```

This allows modern optimizers to use more information than simple gradient descent.

The optimizer state is separate from the model's learned parameters.

---

# 25. Parameter Updates and AdamW

AdamW is commonly used in modern Transformer training.

A simplified conceptual flow is:

```text
Loss
 ↓
Gradients
 ↓
AdamW
 ├── Uses gradient information
 ├── Uses optimizer state
 ├── Applies learning-rate scaling
 └── Applies weight decay
 ↓
Updated Parameters
```

The exact AdamW update contains additional calculations, so the simple gradient-descent equation should be treated as a basic mental model rather than the complete AdamW algorithm.

---

# 26. What Happens to the Old Parameters?

The old parameter values are replaced by updated values.

Conceptually:

```text
Old Parameter
     ↓
Optimizer Update
     ↓
New Parameter
```

For example:

```text
Before:
weight = 0.80

After:
weight = 0.77
```

The next forward pass uses the updated value.

```text
Updated Parameters
        ↓
Next Training Step
        ↓
Forward Pass
```

---

# 27. Parameter Updates Improve Future Predictions

Suppose the model repeatedly sees examples containing patterns such as:

```text
The sky is blue.
The grass is green.
The sun is bright.
```

During training, the model's parameters are adjusted based on its prediction errors.

After many updates, the model may become better at predicting tokens that fit similar contexts.

The important point is:

> The model improves because its parameters are repeatedly adjusted to reduce the training objective.

---

# 28. Parameter Updates and Generalization

The objective is not simply to memorize every training example.

A well-trained model can learn patterns that help it make predictions on examples it has not seen exactly before.

Conceptually:

```text
Training Examples
      ↓
Parameter Updates
      ↓
Learned Patterns
      ↓
Predictions on New Inputs
```

However, training can also lead to memorization or overfitting, depending on the data, model, training setup, and other factors.

---

# 29. Parameter Updates and Overfitting

If a model becomes too specialized to its training data, it may perform poorly on unseen data.

Simplified:

```text
Training Performance
        ↑
        |
        |       Very good
        |
        +----------------------→
              Training
```

But validation performance may stop improving or worsen.

Therefore, training is usually monitored using validation data as well.

Parameter updates are driven by the training objective, while validation is used to evaluate how well the resulting model generalizes.

---

# 30. Parameter Updates During Inference

Normally, parameter updates do **not** happen during ordinary inference.

### Training

```text
Input
 ↓
Prediction
 ↓
Loss
 ↓
Backpropagation
 ↓
Optimizer
 ↓
Parameter Update
```

### Inference

```text
Input
 ↓
Forward Pass
 ↓
Prediction
 ↓
Generated Token
```

No normal training update is performed during inference.

This distinction is extremely important.

---

# 31. Training vs Inference

| Training             | Inference                               |
| -------------------- | --------------------------------------- |
| Uses training data   | Uses new input                          |
| Calculates loss      | Normally no training loss               |
| Backpropagation      | No backpropagation                      |
| Calculates gradients | No training gradients                   |
| Optimizer used       | Optimizer not used for normal inference |
| Parameters updated   | Parameters normally unchanged           |
| Goal is learning     | Goal is prediction/generation           |

---

# 32. Complete Parameter-Update Cycle

The complete cycle can be visualized as:

```text
                 TRAINING STEP
                      │
                      ▼
                Input Tokens
                      │
                      ▼
                 Forward Pass
                      │
                      ▼
                    Logits
                      │
                      ▼
              Next-Token Prediction
                      │
                      ▼
                     Loss
                      │
                      ▼
              Backpropagation
                      │
                      ▼
                  Gradients
                      │
                      ▼
                  Optimizer
                      │
                      ▼
             Parameter Updates
                      │
                      ▼
            Updated Model Parameters
                      │
                      ▼
              Next Training Step
```

This cycle is repeated many times.

---

# 33. Simple Numerical Example

Suppose a model has one parameter:

```text
θ = 1.00
```

The calculated gradient is:

```text
gradient = 0.40
```

Learning rate:

```text
η = 0.10
```

Using basic gradient descent:

```text
θ_new = θ_old - η × gradient
```

Therefore:

```text
θ_new = 1.00 - (0.10 × 0.40)

θ_new = 1.00 - 0.04

θ_new = 0.96
```

The parameter changes from:

```text
1.00 → 0.96
```

On the next training step, the model uses:

```text
θ = 0.96
```

and the process repeats.

---

# 34. Many Parameters

A real LLM does not have one parameter.

Imagine a simplified model with:

```text
θ₁ = 0.50
θ₂ = 0.80
θ₃ = -0.20
θ₄ = 1.10
θ₅ = 0.30
```

Each parameter can have its own gradient:

```text
∂L/∂θ₁
∂L/∂θ₂
∂L/∂θ₃
∂L/∂θ₄
∂L/∂θ₅
```

The optimizer processes these gradients and updates the parameters.

Conceptually:

```text
Many Parameters
       +
Many Gradients
       ↓
    Optimizer
       ↓
Many Updated Parameters
```

This happens across the entire trainable model.

---

# 35. What Does the Model Actually Store After Training?

After training, the model contains its learned parameter values.

For example:

```text
Model
 ├── Embedding Parameters
 ├── Attention Parameters
 ├── FFN Parameters
 ├── Normalization Parameters
 ├── Output Parameters
 └── Other Architecture-Specific Parameters
```

These numerical values collectively represent what the model learned during training.

They are not simply a list of:

```text
Question → Answer
```

Instead, learned information is distributed across the model's parameters.

---

# 36. Parameter Updates Are the Core of Learning

The complete learning idea can be summarized as:

```text
Model makes prediction
        ↓
Prediction produces loss
        ↓
Loss produces gradients
        ↓
Optimizer uses gradients
        ↓
Parameters are updated
        ↓
Model behaves differently next time
        ↓
Repeat
```

Repeated parameter updates are what allow the model to gradually improve its training objective.

---

# 37. Common Misunderstandings

### ❌ "Backpropagation updates the parameters."

More precisely:

> Backpropagation calculates gradients, while the optimizer uses those gradients to update parameters.

---

### ❌ "The loss directly changes the parameters."

Loss provides the training error signal.

The process is:

```text
Loss
 ↓
Gradients
 ↓
Optimizer
 ↓
Parameter Update
```

---

### ❌ "Every parameter changes by the same amount."

Different parameters can have different gradients and optimizer states, so their updates can differ.

---

### ❌ "The optimizer stores the model's knowledge."

The optimizer helps update the model during training.

The learned model information is represented primarily through the model's parameters.

---

### ❌ "Parameters are updated during normal text generation."

Normally, inference does not update the model's parameters.

```text
Training → parameters change

Inference → parameters normally stay fixed
```

---

### ❌ "One parameter update trains the model."

LLM training requires a very large number of training steps.

---

### ❌ "A parameter is a rule written in English."

A parameter is a numerical value.

The model's behavior emerges from interactions among a very large number of such values.

---

# 38. Simple Mental Model

Think of training an LLM like repeatedly adjusting a huge collection of numerical controls.

```text
Prediction
    ↓
"How wrong was I?"
    ↓
Loss
    ↓
"Which parameters contributed to the error?"
    ↓
Gradients
    ↓
"How should I adjust them?"
    ↓
Optimizer
    ↓
Adjust Parameters
    ↓
Try Again
```

After many repetitions, the model's parameters are adjusted toward values that produce better predictions for the training objective.

---

# 39. Complete LLM Training Flow

Putting everything together:

```text
Raw Training Data
       ↓
Data Preparation
       ↓
Tokenization
       ↓
Token IDs
       ↓
Training Sequences
       ↓
Input + Target
       ↓
Forward Pass
       ↓
Logits
       ↓
Next-Token Predictions
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
       ↓
Updated Model
       ↓
Repeat for Many Training Steps
```

This is the central training loop of a neural language model.

---

# 🔑 Key Takeaways

* **Parameters are the numerical values learned by the model.**
* **Parameter updates change those values during training.**
* Backpropagation calculates **gradients**.
* The optimizer uses gradients to determine **updates**.
* The learning rate controls the scale of updates.
* Different parameters can receive different updates.
* Attention, FFN, embeddings, and output layers can contain trainable parameters.
* Parameter updates happen repeatedly across many training steps.
* The model improves by repeatedly adjusting parameters based on the training loss.
* Normal inference does not update model parameters.
* Learned information is distributed across a very large number of parameters.
* Parameter updates are a fundamental mechanism through which the model learns from training data.
