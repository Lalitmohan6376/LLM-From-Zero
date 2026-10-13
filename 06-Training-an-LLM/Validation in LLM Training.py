# 🧪 Validation in LLM Training

**Validation is the process of evaluating a trained model on separate data that is not used to update its parameters during training.**

It helps us understand whether the model is learning useful patterns that generalize beyond the training examples.

During training, the model learns from training data. During validation, we check how well it performs on unseen examples without normally changing its parameters.

```text
Training Data
      ↓
Forward Pass
      ↓
Loss
      ↓
Backpropagation
      ↓
Optimizer
      ↓
Parameter Updates
      ↓
Trained Model
      │
      ▼
Validation Data
      ↓
Forward Pass
      ↓
Validation Loss
      ↓
Evaluate Performance
```

Validation helps answer an important question:

> Is the model learning patterns that generalize, or is it becoming too specialized to its training data?

---

# 1. Why Is Validation Needed?

Suppose an LLM is being trained to predict the next token.

During training, it repeatedly processes training examples and updates its parameters.

The training loss might decrease:

```text
Training Step 1 → Loss = 4.8
Training Step 2 → Loss = 4.2
Training Step 3 → Loss = 3.7
Training Step 4 → Loss = 3.1
```

This suggests that the model is improving on the training objective.

However, lower training loss does not automatically mean the model will perform well on new data.

The model might memorize parts of the training data or become overly specialized to it.

Validation helps us investigate this possibility.

---

# 2. Training Data vs Validation Data

Training data and validation data serve different purposes.

### Training Data

Used to calculate the training loss and update model parameters.

```text
Training Examples
       ↓
Forward Pass
       ↓
Training Loss
       ↓
Backpropagation
       ↓
Parameter Updates
```

### Validation Data

Used to evaluate the model without normally updating its parameters.

```text
Validation Examples
       ↓
Forward Pass
       ↓
Validation Loss
       ↓
Evaluate Generalization
```

| Training Data | Validation Data |
|---|---|
| Used to train the model | Used to evaluate the model |
| Produces training loss | Produces validation loss |
| Gradients are calculated for training | Gradients are not normally calculated |
| Optimizer updates parameters | Parameters remain unchanged |
| Used repeatedly for learning | Used to monitor performance on separate data |

The validation set should be kept separate from the training examples used for parameter updates.

---

# 3. Why Not Evaluate Only on Training Data?

Imagine a student practicing questions from one book.

The student becomes very good at answering those exact questions.

But can the student solve different questions that test the same concepts?

We need another set of questions to find out.

The same principle applies to LLM training.

```text
Training Data
      ↓
Model Learns Patterns
      ↓
Evaluate on Training Examples
      ↓
Performance May Look Good
```

But this alone does not tell us how well the model generalizes.

Validation provides another perspective:

```text
Unseen Validation Data
          ↓
    Trained Model
          ↓
   Validation Results
          ↓
Evaluate Generalization
```

**Good performance on training data alone is not enough to establish good generalization.**

---

# 4. How Is the Dataset Divided?

A dataset can be divided into separate subsets.

```text
             Complete Dataset
                    │
          ┌─────────┴─────────┐
          ▼                   ▼
     Training Data       Validation Data
          │                   │
          ▼                   ▼
   Update Parameters     Evaluate Model
```

For example, suppose a dataset contains 10,000 training examples before splitting.

An illustrative division could be:

| Subset | Percentage | Examples |
|---|---:|---:|
| Training | 90% | 9,000 |
| Validation | 10% | 1,000 |
| Total | 100% | 10,000 |

These percentages are only an example. The appropriate split depends on the dataset, training objective, and evaluation requirements.

For large-scale LLM pretraining, the data organization can be more complex than a simple random split.

---

# 5. Data Leakage During Validation

**Data leakage occurs when information that should be unavailable during evaluation influences the evaluation process.**

For example, suppose the same text appears in both training and validation data.

```text
Training Data
"The Earth revolves around the Sun."

Validation Data
"The Earth revolves around the Sun."
```

The model may have already encountered the same text during training.

Its validation performance may therefore look better than its ability to generalize to genuinely unseen text.

A simplified illustration:

```text
Duplicate or Overlapping Data
             ↓
     Training + Validation
             ↓
Potentially Misleading Results
```

To reduce this risk, data preparation may include:

- Removing exact duplicates across splits.
- Detecting near-duplicate documents where appropriate.
- Keeping related or overlapping examples in the same split when needed.
- Checking for contamination from evaluation datasets.

For LLMs, data leakage can be more subtle than exact text duplication.

---

# 6. What Is Validation Loss?

Validation loss measures how well the model predicts targets on the validation dataset.

For a next-token language model, the model predicts tokens and compares its predictions with the correct next tokens.

```text
Validation Input
       ↓
      LLM
       ↓
     Logits
       ↓
Next-Token Probabilities
       ↓
Compare with Correct Targets
       ↓
Validation Loss
```

Cross-entropy loss is commonly used for next-token prediction.

Conceptually:

\[
L=-\log P(\text{correct token})
\]

If the model assigns a high probability to the correct token, the loss is lower.

If it assigns a low probability to the correct token, the loss is higher.

For a validation dataset, losses from the relevant prediction positions are aggregated according to the evaluation setup.

---

# 7. Training Loss vs Validation Loss

Consider this illustrative example:

| Training Step | Training Loss | Validation Loss |
|---:|---:|---:|
| 100 | 3.8 | 4.0 |
| 200 | 3.2 | 3.5 |
| 300 | 2.7 | 3.1 |
| 400 | 2.3 | 2.9 |
| 500 | 2.0 | 3.0 |
| 600 | 1.7 | 3.3 |

The training loss continues decreasing.

However, the validation loss begins increasing after step 400.

This may indicate that the model is becoming too specialized to its training data.

The pattern is a possible sign of overfitting.

It is not conclusive proof by itself; validation data quality, distribution differences, and other training factors must also be considered.

---

# 8. What Is Overfitting?

**Overfitting occurs when a model becomes too specialized to its training data and performs less effectively on unseen examples.**

A simplified illustration:

```text
Early Training
      ↓
Training Loss Decreases
Validation Loss Decreases
      ↓
Model Generalizes Better
```

Later, the pattern might change:

```text
Continued Training
      ↓
Training Loss Decreases
Validation Loss Increases
      ↓
Possible Overfitting
```

The model may continue improving on the training examples while generalization stops improving.

Overfitting is not inevitable. Its likelihood depends on factors such as model capacity, data quality, dataset size, regularization, and training duration.

---

# 9. Understanding Loss Curves

Loss curves show how loss changes as training progresses.

<box gap={3}>
  <box border radius="lg" padding={3} gap={2}>
    **Case A: Training and validation loss both decrease**

    <AsyncImage query="machine learning training loss validation loss graph both curves decreasing epochs clean educational line chart white background" aspectRatio="16:9" width="100%" />

    <text color="secondary" size="sm">Possible interpretation: the model is improving on both the training objective and the validation data.</text>
  </box>
  <box border radius="lg" padding={3} gap={2}>
    **Case B: Training loss decreases, validation loss increases**

    <AsyncImage query="machine learning overfitting graph training loss decreasing validation loss decreasing then increasing epochs educational line chart white background" aspectRatio="16:9" width="100%" />

    <text color="secondary" size="sm">Possible interpretation: overfitting may be occurring.</text>
  </box>
</box>

These patterns are illustrative. Real loss curves can fluctuate and may not follow perfectly smooth lines.

---

# 10. Validation Does Not Update Parameters

This is one of the most important distinctions.

### During training

```text
Input
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
Parameter Updates
```

### During validation

```text
Validation Input
       ↓
  Forward Pass
       ↓
 Validation Loss
       ↓
Record Results
```

The model's parameters normally remain unchanged during validation.

Validation evaluates the current model; it does not directly train the model.

In software frameworks, validation is commonly performed with gradient calculation disabled and the model placed in evaluation mode.

Evaluation mode can change the behavior of layers such as dropout. It does not itself update model parameters.

---

# 11. When Is Validation Performed?

Validation can be performed at different intervals.

For example:

```text
Training Steps 1–100
        ↓
   Validation

Training Steps 101–200
        ↓
   Validation

Training Steps 201–300
        ↓
   Validation
```

Alternatively, validation may be performed at the end of each epoch.

The frequency depends on the training setup.

Very frequent validation can consume significant computation, especially for large language models.

Very infrequent validation may make it harder to detect problems early.

---

# 12. Validation After an Epoch

Suppose the dataset is divided into 100 batches.

```text
Epoch 1
 ├── Training Batch 1
 ├── Training Batch 2
 ├── Training Batch 3
 ├── ...
 └── Training Batch 100
             ↓
         Validation
```

After the training batches have been processed, the model can be evaluated on validation data.

The process may then repeat for another epoch.

```text
Epoch 1 → Train → Validate
Epoch 2 → Train → Validate
Epoch 3 → Train → Validate
```

Validation does not have to occur exactly once per epoch; this is simply a common approach.

---

# 13. Validation and Model Checkpoints

A checkpoint is a saved version of the model at a particular point during training.

For example:

```text
Training Step 1,000
         ↓
     Checkpoint A
         ↓
      Validation

Training Step 2,000
         ↓
     Checkpoint B
         ↓
      Validation

Training Step 3,000
         ↓
     Checkpoint C
         ↓
      Validation
```

Comparing validation results can help determine which checkpoint performs best according to a chosen evaluation metric.

For example:

| Checkpoint | Validation Loss |
|---|---:|
| A | 2.8 |
| B | 2.3 |
| C | 2.5 |

In this example, checkpoint B has the lowest validation loss among the three.

However, the lowest validation loss does not guarantee the best performance on every downstream task.

---

# 14. What Is Early Stopping?

**Early stopping** is a training strategy that stops training when validation performance no longer improves according to a chosen rule.

For example:

```text
Step 1,000 → Validation Loss = 3.0
Step 2,000 → Validation Loss = 2.6
Step 3,000 → Validation Loss = 2.3
Step 4,000 → Validation Loss = 2.4
Step 5,000 → Validation Loss = 2.6
```

The best observed validation loss occurred at step 3,000.

A training procedure using early stopping might stop after validation has failed to improve for a specified number of evaluations.

The exact stopping rule depends on the setup.

Early stopping is one possible use of validation; it is not mandatory in every LLM training run.

---

# 15. Validation and Generalization

**Generalization** refers to how well a model performs on data beyond the examples used to fit its parameters.

Validation provides an estimate of generalization when its data is appropriately separated and representative of the intended evaluation setting.

```text
Training Examples
       ↓
Parameter Learning
       ↓
Trained Model
       ↓
Unseen Validation Examples
       ↓
Estimate Generalization
```

However, validation results are only useful to the extent that the validation data represents the situations where the model will be evaluated or used.

If the validation distribution differs significantly from the training distribution, performance may also differ.

---

# 16. Validation Loss Is Not the Same as Accuracy

These metrics measure different things.

### Validation Loss

Measures the quality of predicted probabilities relative to the correct targets.

### Accuracy

Measures the proportion of predictions that are correct under a particular decision rule.

For next-token prediction, token accuracy can be calculated by checking whether the highest-scoring predicted token matches the target token.

Consider:

| Model | Probability Assigned to Correct Token | Prediction |
|---|---:|---|
| A | 0.90 | Correct |
| B | 0.40 | Correct |

Both models predict the correct token, but model A assigns it a higher probability and therefore has a lower cross-entropy loss for that prediction.

This shows why accuracy and loss are not interchangeable.

For LLMs, evaluation may also include perplexity and task-specific metrics.

---

# 17. What Is Perplexity?

Perplexity is a metric commonly used to evaluate language models.

It is derived from the average negative log-likelihood, or cross-entropy loss, under a specified evaluation setup.

For a compatible token-level cross-entropy value:

\[
\text{Perplexity}=e^{L}
\]

where \(L\) is the average cross-entropy loss calculated using natural logarithms.

For example:

```text
Average Cross-Entropy Loss = 2.0

Perplexity = e²
           ≈ 7.39
```

Lower perplexity generally indicates that the model assigns higher probability to the observed evaluation tokens.

However, perplexity comparisons are most meaningful when models are evaluated on comparable data using compatible tokenization and evaluation procedures.

Perplexity alone does not measure every capability of an LLM.

---

# 18. Validation in Large Language Model Pretraining

LLM pretraining can involve enormous datasets and substantial computational resources.

A simplified pipeline is:

```text
Prepared Training Data
          ↓
     Tokenization
          ↓
   Training Sequences
          ↓
        Batches
          ↓
   Repeated Training
          ↓
      Validation
          ↓
 Monitor Loss and Metrics
```

Validation can help monitor whether the model continues improving on held-out text.

For large-scale pretraining, teams may use dedicated validation datasets, carefully chosen evaluation intervals, and additional benchmark evaluations.

The exact procedure depends on the model and training objective.

---

# 19. Validation Data Must Remain Separate

Validation data should not be used to calculate the gradients that update the model during ordinary training.

The distinction is:

```text
Training Data
      ↓
Gradients
      ↓
Parameter Updates
```

Compared with:

```text
Validation Data
      ↓
Evaluation
      ↓
No Direct Parameter Updates
```

However, there is an important nuance.

If developers repeatedly use validation results to select checkpoints, adjust hyperparameters, or make training decisions, those results influence the overall development process.

That is why a separate **test set** is often reserved for final evaluation.

---

# 20. Training vs Validation vs Test Data

These three subsets have different purposes.

| Dataset | Main Purpose | Used for Gradient Updates? |
|---|---|---|
| Training | Learn model parameters | Yes |
| Validation | Monitor performance and guide development choices | No |
| Test | Final evaluation of the selected model | No |

A simplified pipeline:

```text
             Dataset
                │
       ┌────────┼────────┐
       ▼        ▼        ▼
   Training  Validation  Test
       │        │         │
       ▼        ▼         ▼
    Learning  Monitoring  Final
    Parameters Performance Evaluation
```

The test set should ideally remain untouched during model selection and hyperparameter tuning.

Repeatedly making decisions based on test results can make the test evaluation less independent.

Not every LLM training pipeline uses exactly this three-way split, but the distinction is fundamental to reliable evaluation.

---

# 21. Validation and Hyperparameters

Hyperparameters are settings chosen for the training process rather than ordinary model parameters learned directly through gradient descent.

Examples include:

- Learning rate
- Batch size
- Number of training steps
- Weight decay
- Model configuration

Validation results can help compare different choices.

For example:

| Experiment | Learning Rate | Validation Loss |
|---|---:|---:|
| A | 0.001 | 2.9 |
| B | 0.0005 | 2.5 |
| C | 0.0001 | 2.7 |

In this illustrative example, experiment B has the lowest validation loss.

That does not mean its learning rate is universally best. The result depends on the model, dataset, optimizer, schedule, and other settings.

---

# 22. Validation Does Not Guarantee Correct Answers

A model can have good validation loss and still produce incorrect or misleading answers.

For example, validation loss may measure next-token prediction on held-out text, while a downstream task requires:

- Reliable factual answers
- Mathematical accuracy
- Following instructions
- Correct code generation
- Safe behavior
- Strong performance across languages

These capabilities require suitable evaluation methods.

```text
Good Validation Loss
        ↓
Evidence of Improvement
        ↓
Not a Guarantee of Perfect Behavior
```

Validation loss is useful, but it is not a complete measure of LLM quality.

---

# 23. Common Misunderstandings

### ❌ "Validation is another training batch."

Validation uses separate evaluation data and normally does not update model parameters.

### ❌ "Lower training loss always means a better model."

Training loss measures performance on training data. It does not, by itself, establish generalization.

### ❌ "Validation loss must decrease at every evaluation."

No. Validation loss can fluctuate or increase.

### ❌ "Validation and test data are the same."

Validation supports development and model selection. Test data is reserved for a more independent final evaluation.

### ❌ "Validation always prevents overfitting."

Validation can help detect signs of overfitting, but it does not automatically prevent it.

### ❌ "The lowest validation loss guarantees the best model for every task."

No. It identifies the best result under that particular validation metric and dataset.

### ❌ "Validation data can never influence training decisions."

Validation data should not directly provide gradients for ordinary parameter updates, but its results can influence choices such as checkpoint selection and hyperparameter tuning.

### ❌ "Good validation loss means the model understands everything."

No. Validation loss measures a specific prediction objective, not every aspect of model capability.

---

# 🧠 Simple Mental Model

Imagine a student preparing for an exam.

```text
Training Data
      ↓
Practice and Learn
      ↓
Improve Knowledge
```

Then the student answers a separate set of questions:

```text
Validation Data
      ↓
Check Performance
      ↓
Identify Possible Problems
```

The validation questions do not directly teach the student during that evaluation. They help measure how well the student performs on questions not used for practice.

For an LLM:

```text
Training
   ↓
Parameter Updates
   ↓
Validation
   ↓
Measure Performance
   ↓
Choose How to Proceed
```

---

# 🔑 Key Takeaways

- **Validation evaluates a model on separate data that is not used for its ordinary parameter updates.**
- Training data is used to learn model parameters.
- Validation data is used to monitor performance and estimate generalization.
- Validation loss measures prediction error on held-out examples.
- Lower validation loss is generally desirable when comparing compatible evaluations.
- Training loss decreasing while validation loss increases can indicate overfitting.
- Validation does not normally involve backpropagation or optimizer updates.
- Validation can be performed after a chosen number of training steps or at the end of an epoch.
- Validation results can help with checkpoint selection, early stopping, and hyperparameter tuning.
- Perplexity is derived from average cross-entropy loss and is commonly used to evaluate language models.
- Validation loss does not guarantee strong performance on every downstream task.
- Test data should ideally be reserved for final evaluation.
- Data leakage can make validation results misleading.
- Validation is an important part of monitoring and evaluating LLM training.
