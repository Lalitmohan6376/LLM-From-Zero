# ⚖️ LLM Training vs Inference

Training and inference are two fundamental processes in the lifecycle of a Large Language Model (LLM).

**Training teaches the model by updating its parameters, while inference uses the trained model to generate predictions.**

Both processes use many of the same neural network components, including embeddings, Transformer blocks, and the language modeling head. However, their objectives and workflows are different.

This document explains how training and inference work, how they differ, and how they connect.

---

## 1. What Is Training?

Training is the process of adjusting a model's parameters using data so that it improves at a particular learning objective.

For a typical causal language model, the objective is to predict the next token from the preceding context.

For example, given:

```text id="x7k2pm"
Input:
"The sun rises in the"

Target:
"east"
```

The model processes the input and predicts a distribution over possible next tokens.

If the correct token receives a low probability, the loss will generally be higher. The training algorithm uses gradients and an optimizer to adjust the model's trainable parameters.

### Training pipeline

```text id="n5w8ka"
Training Data
      |
      v
Tokenization
      |
      v
Training Sequences
      |
      v
Inputs and Target Tokens
      |
      v
Forward Pass
      |
      v
Logits
      |
      v
Loss Calculation
      |
      v
Backpropagation
      |
      v
Optimizer Updates Parameters
      |
      v
Improved Parameters
      |
      +---- Repeat
```

The process repeats over many batches and training steps.

---

## 2. What Is Inference?

Inference is the process of using a model's existing parameters to make predictions for an input.

For a GPT-style LLM, inference commonly involves generating text one token at a time.

For example:

```text id="m9v4qb"
Prompt:
"The sun rises in the"

          |
          v

Model predicts:
" east"

          |
          v

Updated sequence:
"The sun rises in the east"

          |
          v

Predict another token or stop
```

The example is illustrative. The model's actual output depends on its parameters, context, and generation settings.

### Inference pipeline

```text id="j3k8wy"
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
Transformer Blocks
      |
      v
Logits
      |
      v
Token Selection
      |
      v
Append Selected Token
      |
      v
Repeat Until Stopped
      |
      v
Generated Text
```

During ordinary inference, the model's learned parameters remain fixed. The input context and temporary inference state can change as tokens are generated.

---

## 3. The Most Important Difference

The key distinction is whether the model is learning from target data or using its current parameters to make predictions.

<box gap={3}>
  <row align=start gap={3}>
    <box background="surface-secondary" radius="lg" padding={3} align=center justify=center size="52px">
      <icon name="graduation-cap" size="2xl" />
    </box>
    <box flex="1" gap={1}>
      **Training — Learning**

      The model predicts target tokens, calculates loss, computes gradients, and updates its parameters using an optimizer.
    </box>
  </row>
  <divider color="subtle" />
  <row align=start gap={3}>
    <box background="surface-secondary" radius="lg" padding={3} align=center justify=center size="52px">
      <icon name="message-square-text" size="2xl" />
    </box>
    <box flex="1" gap={1}>
      **Inference — Prediction**

      The model processes a prompt, predicts the next token, and generates output without updating its learned parameters.
    </box>
  </row>
</box>

Both processes can perform a forward pass. The difference is what happens after the model produces its predictions.

---

## 4. Side-by-Side Comparison

| Aspect | Training | Inference |
|---|---|---|
| Main purpose | Learn from data | Produce predictions |
| Input | Training examples | Prompt or other model input |
| Targets | Usually available for supervised next-token prediction | Not required for ordinary generation |
| Forward pass | Yes | Yes |
| Logits | Compared with target tokens through a loss function | Used to select the next token |
| Loss calculation | Used for optimization | Not required for ordinary generation |
| Backpropagation | Calculates gradients | Not used for ordinary generation |
| Optimizer | Updates trainable parameters | Does not update parameters |
| Parameter state | Changes during optimization | Remains fixed during ordinary inference |
| Token generation | Not the primary goal of standard pretraining | Often generates tokens autoregressively |
| KV cache | Depends on the training implementation | Commonly used during generation |
| Memory needs | Includes activations and training-related state | Depends on model weights, context, cache, and implementation |
| Typical cost | High for large-scale training | Depends on model size, prompt, output length, and hardware |

The details vary by architecture and implementation, but the learning-versus-prediction distinction remains fundamental.

---

## 5. What Happens Inside the Model in Both Processes?

Training and inference often use the same core architecture.

```text id="q4n8vx"
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
```

This is the shared forward-pass path for a typical decoder-only LLM.

The main difference appears after the logits are calculated.

### During training

```text id="w6j2ka"
Logits
   |
   v
Compare with Target Tokens
   |
   v
Calculate Loss
   |
   v
Backpropagation
   |
   v
Update Parameters
```

### During inference

```text id="c8m5vy"
Logits
   |
   v
Apply Decoding Settings
   |
   v
Select Next Token
   |
   v
Update Context
   |
   v
Repeat
```

Training uses prediction errors to improve the model. Inference uses predictions to produce an output.

---

## 6. Forward Pass During Training vs Inference

A forward pass means passing input data through the neural network to calculate outputs.

### Training forward pass

During causal language-model training, a sequence can be processed in parallel with a causal mask. The model commonly calculates logits at multiple positions.

For example:

```text id="b4k7nz"
Input:
[The] [cat] [is]

Targets:
[cat] [is] [sleeping]

             |
             v

Model calculates predictions
for the eligible positions.

             |
             v

Compare predictions with targets.
```

The targets are shifted relative to the inputs so that each position predicts the next token.

The resulting loss is used to calculate gradients.

### Inference forward pass

During inference, the model initially processes the prompt to calculate the next-token prediction.

After selecting a token, the system appends it to the sequence and predicts another token.

```text id="r9m3wx"
Prompt:
"The cat"

     |
     v

Predict:
" is"

     |
     v

Context:
"The cat is"

     |
     v

Predict:
" sleeping"
```

With KV caching, subsequent decoding steps can reuse previously computed attention keys and values instead of recomputing all earlier attention information.

---

## 7. Why Does Training Need Backpropagation?

A forward pass calculates predictions, but predictions alone do not update the model.

Training needs a way to determine how the trainable parameters contributed to the loss.

Backpropagation calculates gradients:

\[
\nabla_\theta L
\]

Where:

- \(L\) = loss
- \(\theta\) = trainable model parameters

The optimizer uses these gradients to update the parameters.

A simplified gradient descent update is:

\[
\theta_{\text{new}}
=
\theta_{\text{old}}
-
\eta\nabla_\theta L
\]

Here, \(\eta\) is the learning rate.

Real LLM training commonly uses optimizers such as AdamW, whose updates are more involved than this simplified equation.

### Does inference need backpropagation?

Ordinary inference does not need backpropagation because it is not trying to update the learned parameters. It only needs to calculate predictions and, when generating text, select tokens.

This is one of the main reasons inference has a different computational workflow from training.

---

## 8. Loss During Training vs Inference

Loss measures how well predictions match target tokens.

For next-token prediction, cross-entropy loss is commonly used:

\[
L=-\log P(\text{correct token})
\]

For example, if the correct token has a predicted probability of \(0.8\):

\[
L=-\log(0.8)\approx0.223
\]

A lower loss indicates that the model assigned more probability to the correct target on that example.

### During training

Loss is used to calculate gradients and update the model's parameters.

### During inference

Ordinary text generation does not require target tokens, so it does not need a loss calculation for the generation loop.

Loss can still be calculated during evaluation if reference targets are available. Therefore, loss is not exclusive to training; it simply is not necessary for ordinary generation.

---

## 9. Parameter Updates vs Context Updates

This is an important distinction.

### Parameter updates during training

Training changes the model's learned numerical parameters.

```text id="f5m8vy"
Old Parameters
      |
      v
Calculate Gradients
      |
      v
Optimizer Update
      |
      v
New Parameters
```

The new parameters are used in subsequent training steps.

### Context updates during inference

Inference changes the sequence of tokens being processed, not the model's learned parameters.

```text id="z7p3ka"
Current Context:
"The cat"

      |
      v

Selected Token:
" is"

      |
      v

Updated Context:
"The cat is"
```

The model then uses the updated context to calculate the next prediction.

The KV cache may also change during inference, but that is temporary state rather than a learned parameter update.

**Remember:** Training updates parameters; inference updates the generated sequence and its temporary state.

---

## 10. Training and Inference Memory Requirements

Training and inference have different memory requirements because they perform different operations.

### Training memory

Training commonly needs memory for:

- Model parameters
- Intermediate activations needed for backpropagation
- Gradients
- Optimizer state
- Input batches and other training data

The exact memory requirements depend on the architecture, precision, optimizer, sequence length, batch size, and training techniques.

### Inference memory

Inference commonly needs memory for:

- Model parameters
- Input and intermediate representations
- KV cache, when enabled
- Temporary buffers used by the implementation

During autoregressive generation, the KV cache can grow as the context grows.

### Comparison

| Factor | Training | Inference |
|---|---|---|
| Parameter storage | Required | Required |
| Gradients | Usually required | Not required for ordinary generation |
| Optimizer state | Required for optimizers that maintain it | Not required for ordinary generation |
| Backpropagation activations | Often retained or recomputed as needed | Not needed for backpropagation |
| KV cache | Implementation-dependent | Commonly used during generation |
| Memory pattern | Includes training state | Includes inference state and potentially growing cache |

Inference is often less memory-intensive than full training, but a large model or long context can still require substantial resources.

---

## 11. Why Is Training Usually More Expensive?

Full model training usually requires more computation and memory than generating a small number of tokens with the same model.

Training includes:

1. Forward-pass computation.
2. Loss calculation.
3. Backpropagation through the network.
4. Optimizer updates.
5. Storage or management of training-related state.

Inference usually performs the forward computation and generation-related operations without backpropagation or optimizer updates.

However, total cost depends on the workload. Generating a long response, serving many requests, or processing large batches can make inference computationally expensive as well.

Training a model from scratch can require substantial hardware and time, while inference can often be run with fewer resources.

---

## 12. Pretraining vs Fine-Tuning vs Inference

Training itself includes different stages. Two important training stages are pretraining and fine-tuning.

| Stage | Purpose | What happens to parameters? |
|---|---|---|
| Pretraining | Learn broad patterns from large-scale data | Parameters are updated |
| Fine-tuning | Adapt an existing model to a specific objective or behavior | Selected trainable parameters are updated |
| Inference | Use the trained model to make predictions | Parameters remain fixed during ordinary inference |

### Pretraining

A base language model commonly learns through next-token prediction on a large and diverse collection of training text.

### Fine-tuning

A pretrained model can be trained further on instruction-response examples or other task-specific data.

For example, supervised fine-tuning teaches a model to produce responses matching desired examples.

### Inference

Once a suitable model is available, inference uses its current parameters to respond to prompts or make predictions.

Inference is not another name for fine-tuning. They have different purposes.

---

## 13. Interactive Example: Training or Inference?

Use the examples below to check the distinction.

{@body const [scenario,setScenario] = DIL.useState("a")}
<box border radius="xl" padding={4} gap={3}>
  <text color="secondary" size="sm">Choose a scenario</text>
  <radio-group value={scenario} onChange={setScenario} direction="col">
    <radio value="a">A model predicts the next token, calculates loss, and updates its weights.</radio>
    <radio value="b">A model receives a prompt and generates an answer without changing its weights.</radio>
    <radio value="c">A model calculates validation loss on held-out text without updating its weights.</radio>
    <radio value="d">A model appends a selected token to its current prompt and predicts another token.</radio>
  </radio-group>
  <divider color="subtle" />
  {#if scenario === "a"}
    <text color="success" weight="medium"><icon name="check-circle" size="sm" inline /> Training</text>
    The loss and optimizer update indicate that the model is learning from the training example.
  {:else if scenario === "b"}
    <text color="success" weight="medium"><icon name="check-circle" size="sm" inline /> Inference</text>
    The model is using its existing parameters to generate an answer.
  {:else if scenario === "c"}
    <text color="success" weight="medium"><icon name="check-circle" size="sm" inline /> Evaluation</text>
    This is validation or evaluation, not a parameter-training step. The model calculates a metric without updating its weights.
  {:else}
    <text color="success" weight="medium"><icon name="check-circle" size="sm" inline /> Inference</text>
    The system is updating the generated context and continuing autoregressive generation, not updating the learned parameters.
  {/if}
</box>

---

## 14. Common Misconceptions

**Misconception 1: Training and inference use completely different neural networks.**

They often use the same core architecture. The workflow around the forward pass differs.

**Misconception 2: A forward pass always means training.**

A forward pass occurs during both training and inference. It simply calculates the network's outputs.

**Misconception 3: Inference changes the model's learned weights.**

Ordinary inference does not update the model's parameters. Context and temporary cache state may change.

**Misconception 4: Loss is never calculated during inference.**

Loss is unnecessary for ordinary generation, but it can be calculated during evaluation when reference targets are available.

**Misconception 5: Backpropagation and optimizer updates are the same operation.**

Backpropagation calculates gradients. The optimizer uses gradients to update trainable parameters.

**Misconception 6: Inference is always cheap.**

Inference avoids the ordinary training update process, but large models, long prompts, long outputs, and high request volumes can still be expensive.

**Misconception 7: Fine-tuning and inference are the same.**

Fine-tuning is a training process that updates parameters. Inference uses the resulting model to make predictions.

---

## 15. Complete Comparison — Final Summary

```text id="h8w4mq"
                  LLM LIFECYCLE
                       |
             +---------+---------+
             |                   |
             v                   v
         TRAINING             INFERENCE
             |                   |
             v                   v
        Input Data            Input Prompt
             |                   |
             v                   v
        Forward Pass          Forward Pass
             |                   |
             v                   v
           Logits               Logits
             |                   |
             v                   v
       Calculate Loss       Select Next Token
             |                   |
             v                   v
      Backpropagation       Update Context
             |                   |
             v                   v
      Update Parameters      Repeat Generation
             |                   |
             v                   v
      Learned Parameters     Generated Output
```

The most important difference is what happens after predictions are calculated:

- **Training:** Predictions are compared with targets, loss is calculated, gradients are computed, and an optimizer updates parameters.
- **Inference:** Predictions are used to make decisions, such as selecting the next token, while the learned parameters remain fixed.

Remember this simple rule:

**Training changes what the model has learned through parameter updates. Inference uses what the model has learned to produce predictions.**

Understanding this distinction provides the foundation for understanding pretraining, supervised fine-tuning, evaluation, and autoregressive text generation.
