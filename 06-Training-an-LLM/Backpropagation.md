# 🔄 Backpropagation

Backpropagation is the process used during neural-network training to **calculate how much each model parameter contributed to the loss**.

In simple words:

> **Backpropagation calculates gradients that tell the model how its parameters should change to reduce the loss.**

It is an essential part of training an LLM.

The simplified training flow is:

```text id="b7x3qa"
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
```

---

## 1. What Is Backpropagation?

The word **backpropagation** means that information about the error is propagated backward through the network.

During the forward pass:

```text id="k4m8wp"
Input
  ↓
Model
  ↓
Prediction
  ↓
Loss
```

After calculating the loss, the model works backward:

```text id="q9v2mc"
Loss
  ↓
Backpropagation
  ↓
Gradients
  ↓
Parameters
```

The goal is to determine how changing the parameters would affect the loss.

---

## 2. Why Do We Need Backpropagation?

An LLM can contain millions, billions, or even more parameters.

For example:

```text id="m3x7qa"
Parameter 1
Parameter 2
Parameter 3
...
Parameter N
```

The model needs a systematic way to determine how these parameters should change during training.

Backpropagation provides the mathematical mechanism for calculating this information.

Without gradients, the optimizer would not know which direction to move the parameters.

---

## 3. Simple Example

Suppose the model receives:

```text id="v8k2md"
The cat is
```

The correct next token is:

```text id="x5q9pa"
sleeping
```

The model predicts:

```text id="r6m3wc"
sleeping → 0.30
running  → 0.40
playing  → 0.20
...
```

The correct token received a relatively low probability.

This produces a loss.

```text id="j7n4qx"
Prediction
    ↓
Loss
```

Now the model needs to determine:

> Which parameters contributed to this loss, and how should they change?

Backpropagation calculates the required gradients.

---

## 4. The Complete Training Loop

A simplified LLM training loop is:

```text id="p8c3mw"
Training Data
     ↓
Input + Target
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
Next Training Step
```

This process is repeated many times.

---

## 5. Forward Pass vs Backward Pass

There are two important directions during training.

### Forward Pass

Information moves from the input toward the output.

```text id="f5m9qa"
Input
  ↓
Embeddings
  ↓
Transformer Blocks
  ↓
Logits
  ↓
Loss
```

### Backward Pass

Gradient information moves backward from the loss through the model.

```text id="z3x7kc"
Loss
  ↓
Output Layer
  ↓
Transformer Blocks
  ↓
Embeddings
  ↓
Parameters
```

The backward pass is commonly associated with **backpropagation**.

---

## 6. What Is a Gradient?

A gradient tells us how a small change in a parameter would affect the loss.

For a parameter `w`, we can write:

```text id="n6q2vp"
∂Loss / ∂w
```

This means:

> How does the loss change when parameter `w` changes?

The gradient provides both a direction and a magnitude for the local change.

---

## 7. Simple Gradient Example

Suppose:

```text id="a8m4xc"
Parameter = w
Loss = L
```

The gradient is:

```text id="k7p2zr"
∂L / ∂w
```

Suppose:

```text id="r5n8qm"
∂L / ∂w = +2
```

This tells us that increasing `w` locally increases the loss.

If:

```text id="u3c9va"
∂L / ∂w = -2
```

the local relationship is in the opposite direction.

The optimizer uses this gradient information to decide how to update the parameter.

---

## 8. Why Is the Gradient Important?

The model wants to reduce the loss.

The gradient tells the optimizer which direction locally increases the loss.

The optimizer can therefore move the parameter in the opposite direction.

Conceptually:

```text id="q8m3wd"
Gradient
   ↓
Which direction increases loss?
   ↓
Move parameters in the opposite direction
   ↓
Try to reduce loss
```

This is the basic idea behind gradient-based optimization.

---

## 9. A Simple One-Parameter Example

Suppose the loss depends on one parameter:

```text id="w5x9mc"
L = f(w)
```

Imagine:

```text id="h7q2pa"
w = 5
```

and:

```text id="s4m8zx"
Gradient = +2
```

The gradient says that locally, increasing `w` would increase the loss.

A gradient-descent style update is:

```text id="k3v6nr"
w_new = w_old - learning_rate × gradient
```

If:

```text id="d9p2qa"
learning_rate = 0.1
gradient = 2
```

then:

```text id="m6x8vc"
w_new = 5 - (0.1 × 2)

w_new = 4.8
```

The parameter moves in the direction intended to reduce the loss locally.

---

## 10. Backpropagation Does Not Directly Update Parameters

This is an important distinction.

Backpropagation calculates gradients.

It does not normally perform the final parameter update itself.

The simplified process is:

```text id="y4n7mc"
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

So:

```text id="c8q2vp"
Backpropagation = calculate gradients

Optimizer = use gradients to update parameters
```

---

## 11. What Does Backpropagation Calculate?

Suppose the model has parameters:

```text id="x6m3qa"
w₁
w₂
w₃
...
wₙ
```

Backpropagation calculates gradients such as:

```text id="p7v9kc"
∂L/∂w₁
∂L/∂w₂
∂L/∂w₃
...
∂L/∂wₙ
```

These gradients describe how the loss changes with respect to the model parameters.

The optimizer then uses them for parameter updates.

---

## 12. Why Does It Work Backward?

The model's output depends on many intermediate calculations.

For example:

```text id="m2x8qa"
Input
  ↓
Layer 1
  ↓
Layer 2
  ↓
Layer 3
  ↓
Output
  ↓
Loss
```

The loss depends on the output.

The output depends on Layer 3.

Layer 3 depends on Layer 2.

Layer 2 depends on Layer 1.

Therefore, to determine how each parameter affects the final loss, the calculation works backward through these dependencies.

```text id="v5q7mc"
Loss
 ↓
Layer 3
 ↓
Layer 2
 ↓
Layer 1
```

This is the basic idea behind backpropagation.

---

## 13. Chain Rule

Backpropagation relies heavily on the **chain rule** from calculus.

The chain rule allows us to calculate how a change in one quantity affects another through a sequence of operations.

For example:

```text id="n8m4za"
x → a → b → L
```

If:

```text id="r6p2xc"
a = f(x)
b = g(a)
L = h(b)
```

then:

```text id="k3q9mv"
dL/dx
=
dL/db × db/da × da/dx
```

This allows the gradient to be propagated backward through the computational chain.

---

## 14. Simple Chain Rule Example

Suppose:

```text id="w7m3qa"
x → a → L
```

where:

```text id="f8q2mc"
a = 2x
L = a²
```

Then:

```text id="p4n9vx"
dL/da = 2a

da/dx = 2
```

Using the chain rule:

```text id="z6k3rw"
dL/dx
=
dL/da × da/dx
```

Therefore:

```text id="c5m8qa"
dL/dx = 2a × 2
```

Backpropagation performs this type of chain-rule calculation across much larger computational graphs.

---

## 15. Computational Graph

A neural network can be viewed as a sequence of mathematical operations.

For example:

```text id="q8m4vd"
Input
  ↓
Linear Transformation
  ↓
Activation
  ↓
Linear Transformation
  ↓
Prediction
  ↓
Loss
```

This can be represented as a **computational graph**.

The forward pass follows the graph toward the loss.

Backpropagation moves through the graph in the reverse direction to calculate gradients.

---

## 16. Backpropagation in an LLM

An LLM contains many operations.

A simplified flow is:

```text id="x5n7qc"
Token IDs
    ↓
Embeddings
    ↓
Transformer Block
    ↓
Transformer Block
    ↓
Transformer Block
    ↓
...
    ↓
Language Model Head
    ↓
Logits
    ↓
Loss
```

During backpropagation:

```text id="m9q3za"
Loss
 ↓
Language Model Head
 ↓
Last Transformer Block
 ↓
Previous Transformer Block
 ↓
Previous Transformer Block
 ↓
...
 ↓
Embedding Parameters
```

Gradients are calculated for the trainable parameters throughout this computation.

---

## 17. Backpropagation Through the Language Model Head

Suppose the model produces:

```text id="h6x2mw"
Hidden Representation
       ↓
Language Model Head
       ↓
Logits
       ↓
Loss
```

The loss depends on the logits.

Backpropagation first calculates how the loss changes with respect to the logits.

Then it continues backward through the Language Model Head.

```text id="k4p8va"
Loss
 ↓
Logits
 ↓
Language Model Head
 ↓
Hidden Representation
```

This allows gradients to reach earlier parts of the Transformer.

---

## 18. Backpropagation Through Transformer Blocks

An LLM may contain many Transformer blocks.

For example:

```text id="r7m3qx"
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
Output
 ↓
Loss
```

During backpropagation:

```text id="p8n5zc"
Loss
 ↓
Block 4
 ↓
Block 3
 ↓
Block 2
 ↓
Block 1
 ↓
Input-side parameters
```

Each block's trainable parameters receive gradient information.

---

## 19. Backpropagation Through Attention

A Transformer block contains attention operations.

Simplified:

```text id="v6q2mc"
Input
  ↓
Q, K, V
  ↓
Attention Scores
  ↓
Softmax
  ↓
Attention Output
```

The loss ultimately depends on these computations.

Backpropagation calculates gradients through the operations involved in attention.

Conceptually:

```text id="y3m8qa"
Loss
 ↓
Attention Output
 ↓
Attention Weights / Scores
 ↓
Q, K, V
 ↓
Projection Parameters
```

This allows attention-related parameters to be updated during training.

---

## 20. Backpropagation Through the FFN

A Transformer block also contains a Feed-Forward Network.

Simplified:

```text id="c8v4nx"
Input
  ↓
Linear Layer
  ↓
Activation
  ↓
Linear Layer
  ↓
Output
```

The loss depends on the final output of the model.

Backpropagation calculates gradients through these operations as well.

```text id="z5q7ma"
Loss
 ↓
FFN Output
 ↓
Second Linear Layer
 ↓
Activation
 ↓
First Linear Layer
```

The FFN parameters can then be updated by the optimizer.

---

## 21. Backpropagation Through Residual Connections

Transformer blocks commonly use residual connections.

Simplified:

```text id="m4x9qc"
Input ────────────────┐
  ↓                   │
Attention / FFN       │
  ↓                   │
  └────── + ←─────────┘
           ↓
         Output
```

During backpropagation, gradient information flows through the operations as well as the residual path.

Residual connections help information and gradients flow through deep networks.

---

## 22. Backpropagation Through Layer Normalization

Transformer blocks also use Layer Normalization.

Simplified:

```text id="q7m2va"
Input
 ↓
Layer Normalization
 ↓
Next Operation
```

During backpropagation, gradients are calculated through the normalization operation as part of the computational graph.

The trainable parameters of LayerNorm, when present, can also receive gradients.

---

## 23. Backpropagation Through Embeddings

Token IDs are used to look up token embeddings.

For example:

```text id="n5x8mc"
Token ID
   ↓
Embedding Table
   ↓
Embedding Vector
```

The embedding vectors are trainable parameters.

During backpropagation, gradient information can reach the embedding parameters associated with the tokens involved in the computation.

Conceptually:

```text id="h3q6za"
Loss
 ↓
Transformer
 ↓
Embedding Representation
 ↓
Embedding Parameters
```

The embedding parameters can therefore be updated during training.

---

## 24. Gradient Flow Through the Network

The overall gradient flow can be simplified as:

```text id="p8m4xc"
                    Loss
                      ↓
                Output Layer
                      ↓
              Transformer Block N
                      ↓
              Transformer Block N-1
                      ↓
                     ...
                      ↓
              Transformer Block 2
                      ↓
              Transformer Block 1
                      ↓
                  Embeddings
```

Gradients flow backward through the computational graph.

---

## 25. Forward Pass and Backward Pass Together

The two passes work together.

### Forward

```text id="w6q2ma"
Input
 ↓
Model
 ↓
Prediction
 ↓
Loss
```

### Backward

```text id="v9m3xc"
Loss
 ↓
Gradients
 ↓
Parameters
```

Together:

```text id="z4k8qa"
             FORWARD
Input ─────────────────→ Loss
                           │
                           │
                           ↓
             BACKWARD
Parameters ←────────── Gradients
```

Then the optimizer updates the parameters.

---

## 26. Learning Rate

The gradient tells the optimizer the direction and magnitude of local change, but the optimizer also needs a **learning rate**.

The learning rate controls how large the parameter update should be.

A simplified update is:

```text id="q7m4vz"
New Parameter
=
Old Parameter
-
Learning Rate × Gradient
```

For example:

```text id="x3n8mc"
Old Parameter = 5.0
Gradient      = 2.0
Learning Rate = 0.1
```

Then:

```text id="a6p2qw"
New Parameter
=
5.0 - (0.1 × 2.0)

= 4.8
```

The learning rate is an important training hyperparameter.

---

## 27. Gradient Descent

The basic optimization idea is called **gradient descent**.

The model tries to move its parameters toward values that reduce the loss.

Conceptually:

```text id="m8q3xa"
Current Parameters
       ↓
Calculate Loss
       ↓
Calculate Gradients
       ↓
Move Parameters
       ↓
New Parameters
       ↓
Repeat
```

Backpropagation provides the gradients needed for this process.

---

## 28. Backpropagation vs Gradient Descent

These concepts are related but not identical.

### Backpropagation

Calculates gradients of the loss with respect to model parameters.

### Gradient Descent

Uses gradient information to update parameters in a direction intended to reduce the loss.

So:

```text id="c7m2vx"
Backpropagation
      ↓
Gradients
      ↓
Gradient-Based Optimization
      ↓
Parameter Updates
```

In modern LLM training, optimizers such as Adam or AdamW are commonly used rather than plain gradient descent.

---

## 29. Backpropagation vs Optimizer

These are also different.

| Concept             | Main Job                                   |
| ------------------- | ------------------------------------------ |
| **Loss**            | Measures prediction error                  |
| **Backpropagation** | Calculates gradients                       |
| **Gradient**        | Describes how loss changes with parameters |
| **Optimizer**       | Uses gradients to update parameters        |
| **Learning Rate**   | Controls update size                       |

Complete flow:

```text id="x9q4mw"
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
Updated Parameters
```

---

## 30. Why Backpropagation Is Important for LLMs

LLMs contain a very large number of trainable parameters.

Training requires a scalable method for determining how these parameters should change.

Backpropagation provides the gradient calculation needed for this.

Without an efficient way to calculate gradients, training large neural networks would be extremely difficult.

---

## 31. Backpropagation and Multiple Tokens

During LLM training, a sequence contains multiple prediction positions.

For example:

```text id="v5m8qa"
The        → cat
The cat    → is
The cat is → sleeping
```

Each prediction contributes to the overall loss.

Conceptually:

```text id="j3q7mc"
Token Loss 1
Token Loss 2
Token Loss 3
      ↓
Sequence / Batch Loss
      ↓
Backpropagation
      ↓
Gradients
```

The gradients reflect the combined training objective.

---

## 32. Backpropagation and Batches

LLMs normally train using batches.

For example:

```text id="n8x4vp"
Sequence 1 → Loss
Sequence 2 → Loss
Sequence 3 → Loss
Sequence 4 → Loss
```

These losses contribute to the batch loss.

Then:

```text id="q6m2za"
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

This is repeated for many batches.

---

## 33. What Happens to the Parameters?

Suppose an LLM has parameters:

```text id="f4x8mc"
θ₁
θ₂
θ₃
...
θₙ
```

Backpropagation calculates:

```text id="m7q3va"
∂L/∂θ₁
∂L/∂θ₂
∂L/∂θ₃
...
∂L/∂θₙ
```

The optimizer then uses these gradients to update the parameters.

Conceptually:

```text id="p9c5xw"
Old Parameters
      ↓
Gradient Information
      ↓
Optimizer
      ↓
New Parameters
```

The updated parameters are then used for the next training step.

---

## 34. Backpropagation Does Not Mean "Sending the Answer Back"

The name can sometimes be confusing.

Backpropagation does **not** mean that the correct answer is sent backward through the model.

Instead, information about the loss is propagated backward in the form of gradient calculations.

The target is used to calculate the loss.

The loss is then used to calculate gradients.

```text id="z6m2qa"
Target
  ↓
Loss
  ↓
Gradients
  ↓
Parameter Updates
```

---

## 35. Backpropagation and Causal Masking

Causal masking controls what information each token can use during the forward pass.

For example:

```text id="w8q4mc"
The cat is sleeping
```

When predicting `is`, the model cannot use `sleeping`.

Causal masking prevents this information leakage during the forward computation.

Backpropagation then calculates gradients through the resulting computational graph.

So these concepts have different roles:

```text id="h5m9vx"
Causal Masking
      ↓
Controls information flow

Backpropagation
      ↓
Calculates gradient flow
```

---

## 36. Backpropagation and Training Mode

Backpropagation is part of the training process.

During training:

```text id="c3x7qa"
Forward Pass
      ↓
Loss
      ↓
Backward Pass
      ↓
Gradients
      ↓
Optimizer
      ↓
Parameter Update
```

During normal inference:

```text id="m8q2vc"
Forward Pass
      ↓
Prediction
      ↓
Token Selection
```

The model normally does not calculate training gradients or update its parameters during ordinary inference.

---

## 37. What Is the Backward Pass?

The **backward pass** is the process of computing gradients starting from the loss and moving backward through the computational graph.

For example:

```text id="q5n8ma"
Forward:

Input → Layer 1 → Layer 2 → Output → Loss


Backward:

Loss → Layer 2 → Layer 1 → Gradients
```

Backpropagation is the algorithmic process used to efficiently perform these gradient calculations.

---

## 38. Vanishing and Exploding Gradients

During backpropagation, gradients can sometimes become:

* Very small
* Very large

These problems are known as:

```text id="x7m3qc"
Vanishing Gradients
Exploding Gradients
```

Very small gradients can make learning difficult.

Very large gradients can make training unstable.

Modern neural-network architectures and training techniques are designed to help manage these problems.

Transformer architectures use components such as:

* Residual connections
* Layer normalization
* Carefully designed initialization
* Appropriate optimizers
* Learning-rate strategies

These can help make large-scale training more stable.

---

## 39. Why Residual Connections Help

A deep Transformer may contain many blocks:

```text id="r4q8mx"
Block 1
 ↓
Block 2
 ↓
Block 3
 ↓
...
 ↓
Block N
```

Without suitable architectural design, gradient flow through very deep networks can become difficult.

Residual connections provide additional paths through the network.

Conceptually:

```text id="k6m2qa"
Input ────────────────┐
  ↓                   │
Transformation        │
  ↓                   │
  └────── + ←─────────┘
           ↓
         Output
```

This can help information and gradients flow through deep networks.

---

## 40. Backpropagation Does Not Require Manual Derivatives for Every Parameter

Modern deep-learning frameworks automatically calculate gradients using **automatic differentiation**.

Examples include:

* PyTorch autograd
* TensorFlow automatic differentiation

Conceptually:

```text id="p3x8qa"
Forward Computation
       ↓
Computational Graph
       ↓
Automatic Differentiation
       ↓
Gradients
```

The developer does not normally calculate every derivative manually.

---

## 41. Automatic Differentiation

Automatic differentiation keeps track of mathematical operations performed during the forward computation.

When the backward pass is requested, the framework uses those operations to calculate gradients.

Simplified:

```text id="m7q2vc"
x
 ↓
Operation 1
 ↓
Operation 2
 ↓
Operation 3
 ↓
Loss
```

Backward:

```text id="z8n4qa"
Loss
 ↓
Gradient through Operation 3
 ↓
Gradient through Operation 2
 ↓
Gradient through Operation 1
```

This makes gradient calculation practical for large neural networks.

---

## 42. Backpropagation in a Simple Neural Network

Consider:

```text id="c5m8vx"
Input
  ↓
Layer 1
  ↓
Layer 2
  ↓
Output
  ↓
Loss
```

Forward pass:

```text id="q3n7ma"
Input
 ↓
Layer 1
 ↓
Layer 2
 ↓
Prediction
 ↓
Loss
```

Backward pass:

```text id="h8x2qc"
Loss
 ↓
Layer 2 gradients
 ↓
Layer 1 gradients
 ↓
Parameter gradients
```

Then:

```text id="w6m4qa"
Optimizer
 ↓
Updated Parameters
```

An LLM follows the same fundamental idea, but on a much larger computational graph.

---

## 43. Backpropagation in a Decoder-Only LLM

A simplified decoder-only LLM can be represented as:

```text id="n9q3mx"
Token IDs
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
Transformer Block N
    ↓
Language Model Head
    ↓
Logits
    ↓
Loss
```

Backpropagation works backward:

```text id="v5m8qa"
Loss
 ↓
Language Model Head
 ↓
Transformer Block N
 ↓
Transformer Block N-1
 ↓
...
 ↓
Transformer Block 1
 ↓
Embeddings
```

Gradients are calculated for the trainable parameters throughout these components.

---

## 44. Complete LLM Training Step

One complete training step can be simplified to:

### Step 1: Input

```text id="q8m3va"
Training Sequence
```

### Step 2: Forward Pass

```text id="x5n7mc"
Input
 ↓
Transformer
 ↓
Logits
```

### Step 3: Loss

```text id="m2q9za"
Logits + Targets
       ↓
      Loss
```

### Step 4: Backpropagation

```text id="c7v4mx"
Loss
 ↓
Gradients
```

### Step 5: Optimizer

```text id="p8n3qa"
Gradients
 ↓
Optimizer
```

### Step 6: Update

```text id="z6m5vc"
Updated Parameters
```

Then the next training step begins.

---

## 45. Complete Training Loop

The entire process can be represented as:

```text id="y4q8mc"
                 Training Data
                       ↓
                 Input + Target
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
                Next Training Step
                       ↺
```

This loop runs over many batches and training iterations.

---

## 46. Common Misunderstandings

### ❌ "Backpropagation updates the model parameters."

Not directly.

Backpropagation calculates gradients.

The optimizer uses those gradients to update parameters.

---

### ❌ "Backpropagation is the same as gradient descent."

No.

Backpropagation calculates gradients.

Gradient-based optimization uses those gradients to update parameters.

---

### ❌ "Backpropagation only happens in the final layer."

No.

Gradients are propagated backward through the computational graph and can reach parameters throughout the model.

---

### ❌ "Backpropagation changes the input tokens."

No.

It calculates gradients for trainable parameters.

The input training data is not modified by backpropagation.

---

### ❌ "The correct answer is sent backward."

Not exactly.

The target is used to calculate the loss, and the loss is then used to calculate gradients.

---

### ❌ "Backpropagation happens during normal text generation."

Normally, no.

Ordinary inference does not require parameter updates or training gradients.

---

### ❌ "Every gradient is manually calculated by the programmer."

No.

Deep-learning frameworks commonly use automatic differentiation.

---

### ❌ "A gradient tells the exact best value for a parameter."

No.

A gradient provides local information about how the loss changes with respect to a parameter.

The optimizer uses this information to decide the update.

---

## 47. Simple Mental Model

Imagine a student receives a score after answering a question.

```text id="m8q4va"
Answer
  ↓
Score
  ↓
Find what went wrong
  ↓
Determine how to improve
  ↓
Change approach
```

For an LLM:

```text id="x3n7mc"
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

The important idea is:

> **Loss tells us how wrong the prediction was, and backpropagation calculates how the model's parameters contributed to that loss.**

---

## 48. One-Line Difference

Remember these four concepts:

```text id="q6m3za"
Loss
→ How wrong was the prediction?

Backpropagation
→ How does the loss depend on the parameters?

Gradient
→ How does changing a parameter affect the loss?

Optimizer
→ How should the parameters be updated?
```

Together:

```text id="v8x2mc"
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
Updated Parameters
```

---

## 49. Key Takeaways

* **Backpropagation is used to calculate gradients during neural-network training.**
* It starts from the loss and works backward through the computational graph.
* The forward pass produces the prediction and loss.
* The backward pass calculates gradients.
* Backpropagation relies on the **chain rule** of calculus.
* Gradients describe how the loss changes with respect to model parameters.
* The optimizer uses gradients to update the parameters.
* Backpropagation itself does not perform the final parameter update.
* In an LLM, gradients can flow through:

  * Language Model Head
  * Transformer blocks
  * Attention
  * Feed-Forward Networks
  * Layer Normalization
  * Residual paths
  * Embeddings
* Multiple token losses can contribute to the overall training loss.
* Backpropagation is performed during training, not ordinary inference.
* Modern deep-learning frameworks use automatic differentiation to calculate gradients efficiently.
* The basic training cycle is:

```text id="n5q8ma"
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
Parameter Updates
```

* Repeating this process over large amounts of training data allows the model's parameters to learn useful patterns for next-token prediction.
