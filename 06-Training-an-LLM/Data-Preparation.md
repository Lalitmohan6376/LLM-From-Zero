# 🧹 Data Preparation

Before an LLM can learn from training data, raw data needs to be prepared in a form that the model can use.

Raw data may contain unnecessary content, duplicates, formatting problems, unwanted symbols, low-quality text, or other issues.

The basic idea is:

```text id="dpflow1"
Raw Data
   ↓
Cleaning
   ↓
Filtering
   ↓
Deduplication
   ↓
Formatting
   ↓
Tokenization
   ↓
Training Sequences
   ↓
Training
```

Data preparation is an important part of the LLM training pipeline because the quality of the training data can strongly affect the quality of the resulting model.

---

## 1. What Is Data Preparation?

**Data preparation** is the process of transforming raw data into a cleaner and more suitable form for training an LLM.

Raw data is usually not ready to be directly given to the model.

For example, web data might contain:

```text
HTML
Navigation menus
Advertisements
Repeated content
Broken text
Spam
Duplicate pages
```

Data preparation attempts to remove or handle such problems before training.

---

## 2. Why Is Data Preparation Needed?

An LLM learns patterns from the data it receives during training.

If the data contains a lot of poor-quality or unwanted content, the model may spend training capacity learning patterns that are not useful.

For example:

```text
High-quality data
        ↓
Useful language patterns
        ↓
Better learning
```

Compared with:

```text
Low-quality data
        ↓
Noise + duplicates + unwanted content
        ↓
Less useful training signal
```

This does not mean that every imperfect piece of data must be removed.

Real-world datasets are complex, and preparation usually involves balancing quality, diversity, coverage, and other requirements.

---

# 3. Raw Data vs Prepared Data

### Raw Data

Raw data is collected from different sources before extensive processing.

Example:

```text
Web pages
Books
Articles
Code
Scientific papers
Documentation
Conversations
```

It may contain unwanted material.

### Prepared Data

Prepared data has gone through one or more processing steps so that it is more suitable for training.

```text
Raw Data
   ↓
Cleaning
   ↓
Filtering
   ↓
Deduplication
   ↓
Formatting
   ↓
Prepared Data
```

---

# 4. Common Sources of LLM Training Data

Large language models can be trained using many types of text.

Common examples include:

| Source             | Example                        |
| ------------------ | ------------------------------ |
| 📚 Books           | Fiction, non-fiction           |
| 🌐 Web             | Articles, websites             |
| 💻 Code            | Programming repositories       |
| 🔬 Scientific Text | Papers and technical documents |
| 📖 Documentation   | Technical documentation        |
| 💬 Conversations   | Dialogue-style datasets        |
| 📰 Articles        | News and educational content   |

The exact sources and proportions depend on the model and its training process.

---

# 5. Basic Data Preparation Pipeline

A simplified pipeline looks like this:

```text
Raw Data
   ↓
Collect Data
   ↓
Clean Data
   ↓
Filter Data
   ↓
Remove Duplicates
   ↓
Normalize / Format Data
   ↓
Tokenize Data
   ↓
Create Training Sequences
   ↓
Create Batches
   ↓
Train the LLM
```

Not every training system follows exactly the same steps or order.

---

# 6. Data Cleaning

🧹 **Data cleaning** attempts to remove or correct unwanted parts of the raw dataset.

For example, web pages can contain:

```text
HTML tags
Advertisements
Navigation menus
Tracking information
Broken characters
Repeated headers
Unwanted metadata
```

A simplified example:

### Before cleaning

```text
<header>MY WEBSITE</header>

Advertisement: BUY NOW!!!

The Transformer architecture uses attention.

<footer>Copyright 2026</footer>
```

### After cleaning

```text
The Transformer architecture uses attention.
```

The exact cleaning process depends on the source.

---

# 7. Removing Unwanted Content

Some collected data may contain content that is not useful for the intended training objective.

Examples can include:

```text
Spam
Automatically generated low-quality pages
Broken documents
Repeated boilerplate
Irrelevant metadata
```

Such content may be filtered according to the goals and policies of the training pipeline.

---

# 8. Data Filtering

Filtering means selecting data that meets certain requirements.

For example, a dataset might be filtered based on:

```text
Language
Quality
Length
Domain
Source
Safety requirements
Content type
```

A simplified example:

```text
100 Million Documents
        ↓
Quality Filtering
        ↓
70 Million Documents
```

The numbers above are only illustrative.

Filtering does not necessarily mean that more data is always better.

The goal is to create a useful and appropriate training mixture.

---

# 9. Language Filtering

A dataset may contain many languages.

For example:

```text
English
Hindi
Spanish
French
German
Japanese
...
```

A training pipeline may identify the language of text and use it according to the model's intended language coverage.

For example:

```text
Raw Web Data
      ↓
Language Identification
      ↓
English ──→ English Data
Hindi   ──→ Hindi Data
French  ──→ French Data
...
```

Multilingual models may intentionally include many languages.

---

# 10. Quality Filtering

Not all collected text has the same quality.

A training pipeline may use different methods to identify low-quality content.

For example:

```text
Very short pages
Spam
Repeated templates
Unreadable text
Broken documents
Low-quality generated content
```

The exact quality criteria depend on the training system.

The important idea is:

> Data preparation tries to increase the useful training signal without unnecessarily removing valuable information.

---

# 11. Deduplication

🔁 **Deduplication** means identifying and reducing duplicate or highly repeated data.

Suppose a dataset contains:

```text
Document A
Document B
Document A
Document C
Document A
```

The same document appears multiple times.

A simplified result could be:

```text
Document A
Document B
Document C
```

Real-world deduplication can be much more complex than this example.

---

# 12. Why Deduplication Matters

Repeated data can cause the model to see the same information many times.

For example:

```text
Same article
Same article
Same article
Same article
```

This is different from having diverse examples:

```text
Article A
Article B
Article C
Article D
```

Deduplication can help reduce unnecessary repetition and improve the usefulness of the training mixture.

---

# 13. Exact Duplicates vs Near Duplicates

Duplicates are not always exactly identical.

### Exact duplicate

```text
The cat is sleeping.

The cat is sleeping.
```

### Near duplicate

```text
The cat is sleeping on the sofa.

The cat is sleeping on a sofa.
```

The second pair is very similar but not exactly identical.

Large training pipelines may use different techniques to identify such repeated or highly similar content.

---

# 14. Formatting the Data

After cleaning and filtering, data may need to be converted into a consistent format.

For example:

```text
Document 1
Document 2
Document 3
...
```

may be stored in a structured dataset.

A simplified representation could be:

```text
{
    "text": "The Transformer uses attention."
}
```

The actual storage format can vary significantly between training systems.

---

# 15. Normalization

Some datasets may require normalization.

Examples include handling:

```text
Whitespace
Line breaks
Encoding issues
Formatting inconsistencies
Unicode representations
```

For example:

```text
"The   Transformer   uses attention."
```

might be normalized depending on the preprocessing rules.

However, normalization should be applied carefully.

Changing text unnecessarily can remove useful information.

---

# 16. Encoding and Character Problems

Raw datasets can sometimes contain encoding problems.

For example:

```text
Broken characters
Unexpected symbols
Incorrect Unicode
Corrupted text
```

A preparation pipeline may detect and handle such cases.

This is especially important when training on large multilingual datasets.

---

# 17. Data Contamination

⚠️ **Data contamination** occurs when information that should not be present in the training data becomes part of it.

For example, suppose a benchmark contains:

```text
Question
Answer
```

If the answer or benchmark content appears in the training data, evaluation results may become misleading.

A simplified example:

```text
Training Data
      +
Benchmark Data
      ↓
Possible Contamination
      ↓
Unreliable Evaluation
```

Training pipelines may therefore attempt to detect or reduce contamination.

---

# 18. Copyright and Licensing

Training data can also involve legal and licensing considerations.

Different sources may have different:

```text
Copyright rules
Licensing terms
Usage restrictions
Access conditions
```

Therefore, data preparation is not only a technical problem.

Large-scale model development also requires appropriate consideration of legal, ethical, and policy requirements.

---

# 19. Bias in Training Data

Training data can contain biases.

For example, data may have uneven representation of:

```text
Languages
Topics
Cultures
Viewpoints
Domains
Demographic groups
```

Because an LLM learns patterns from its training data, these patterns can influence model behavior.

Data preparation may therefore include analysis and filtering related to data quality and representation.

However, simply removing data does not automatically eliminate all forms of bias.

---

# 20. Data Diversity

A useful training dataset usually needs more than a large number of documents.

It can also benefit from diversity.

For example:

```text
Books
+
Web pages
+
Code
+
Scientific text
+
Documentation
+
Other useful sources
```

This can provide different styles, domains, and types of language.

### Important idea

> More data does not automatically mean better data.

Both **quantity and quality** matter.

---

# 21. Data Mixture

Large LLMs may be trained using a mixture of different types of data.

For example:

```text
             ┌── Books
             │
             ├── Web
Raw Data ────┼── Code
             │
             ├── Scientific Text
             │
             └── Documentation
                     ↓
               Data Preparation
                     ↓
                Data Mixture
```

The exact mixture depends on the model and its training goals.

---

# 22. Tokenization Comes After Data Preparation

Once the text has been prepared, it can be passed through a tokenizer.

The simplified flow is:

```text
Prepared Text
     ↓
Tokenizer
     ↓
Tokens
     ↓
Token IDs
```

For example:

```text
"The cat sleeps."
```

might become:

```text
["The", " cat", " sleeps", "."]
```

and then:

```text
[ID₁, ID₂, ID₃, ID₄]
```

The exact tokens and IDs depend on the tokenizer.

---

# 23. From Token IDs to Training Sequences

Tokenized data is usually organized into sequences suitable for training.

For example:

```text
Token IDs:

[12, 45, 91, 37, 82, 16, 54, 29]
```

A sequence may contain a fixed or otherwise selected number of tokens.

For example:

```text
[12, 45, 91, 37]
[82, 16, 54, 29]
```

The exact sequence construction depends on the training setup and context length.

---

# 24. Input and Target

For next-token prediction, the sequence is shifted to create inputs and targets.

Example:

```text
Tokens:

The cat is sleeping
```

Simplified token sequence:

```text
[The] [cat] [is] [sleeping]
```

Input:

```text
[The] [cat] [is]
```

Target:

```text
[cat] [is] [sleeping]
```

The model learns:

```text
The       → cat
The cat   → is
The cat is → sleeping
```

This allows multiple next-token prediction positions to be trained from one sequence.

---

# 25. Batching

Training usually processes multiple sequences together.

For example:

```text
Sequence 1
Sequence 2
Sequence 3
Sequence 4
       ↓
     Batch
       ↓
     Model
```

A batch allows hardware such as GPUs to process many training examples together.

Batch size is different from context-window size.

### Batch size

How many training examples are processed together.

### Context window

How many tokens the model can process as context for a sequence.

---

# 26. Complete Data Preparation Flow

The complete simplified process can be visualized as:

```text
┌─────────────────────┐
│     Raw Data        │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│      Cleaning       │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│      Filtering      │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│    Deduplication    │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│ Formatting /        │
│ Normalization       │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│     Tokenization    │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│   Training          │
│    Sequences        │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│       Batches       │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│    LLM Training     │
└─────────────────────┘
```

---

# 27. Data Preparation Is Not the Same as Training

These stages are different.

### Data Preparation

```text
Raw Data
   ↓
Clean
   ↓
Filter
   ↓
Deduplicate
   ↓
Format
   ↓
Tokenize
   ↓
Create Sequences
```

### Model Training

```text
Training Sequences
       ↓
Forward Pass
       ↓
Predictions
       ↓
Loss
       ↓
Backpropagation
       ↓
Parameter Updates
```

Data preparation creates the training material.

Training updates the model's parameters using that material.

---

# 28. What Happens to the Prepared Data?

After preparation, the data is ready to participate in the training process.

The simplified flow is:

```text
Prepared Data
      ↓
Token IDs
      ↓
Training Sequences
      ↓
Batches
      ↓
Transformer
      ↓
Predictions
      ↓
Loss
      ↓
Backpropagation
      ↓
Parameter Updates
```

The model gradually changes its parameters so that its predictions become better according to the training objective.

---

# 29. Important Distinction: Data vs Model Knowledge

The training dataset and the trained model are not the same thing.

```text
Training Data
      ↓
Training Process
      ↓
Updated Parameters
      ↓
Trained Model
```

The model does not simply store the entire training dataset as a searchable database.

Training changes the numerical parameters of the model.

Some information can be memorized, while other information is represented through learned patterns and generalizations.

---

# 30. Data Preparation Does Not Have One Universal Recipe

Different LLM projects can use different preparation pipelines.

For example:

```text
Model A
Raw Data
 ↓
Cleaning
 ↓
Filtering
 ↓
Tokenization
```

while another system might use:

```text
Model B
Raw Data
 ↓
Cleaning
 ↓
Language Filtering
 ↓
Quality Filtering
 ↓
Deduplication
 ↓
Formatting
 ↓
Tokenization
```

There is no single preparation pipeline that every LLM must follow exactly.

The process depends on:

* Training objective
* Data sources
* Model design
* Language coverage
* Data quality requirements
* Safety and policy requirements
* Compute resources
* Evaluation strategy

---

# 31. Simple Example

Suppose we want to train an LLM using several documents.

### Raw data

```text
Document A
Document A
Advertisement
Document B
Broken text
Document C
```

### After cleaning

```text
Document A
Document A
Document B
Document C
```

### After deduplication

```text
Document A
Document B
Document C
```

### After tokenization

```text
Document A → [12, 45, 67, 89, ...]
Document B → [34, 91, 20, 55, ...]
Document C → [72, 18, 44, 31, ...]
```

### Training sequences

```text
[12, 45, 67, 89]
[34, 91, 20, 55]
[72, 18, 44, 31]
```

### Training

```text
Sequences
    ↓
Transformer
    ↓
Next-token predictions
    ↓
Loss
    ↓
Parameter updates
```

This is the basic idea behind preparing data for LLM training.

---

# 32. Common Misunderstandings

### ❌ "Raw internet data can always be directly used."

Not necessarily.

Raw data may contain duplicates, spam, unwanted formatting, low-quality content, or other issues.

---

### ❌ "More training data always makes the model better."

Not necessarily.

Data quality, diversity, relevance, and mixture also matter.

---

### ❌ "Deduplication means removing everything similar."

Not necessarily.

Deduplication aims to reduce unnecessary repetition, but deciding what counts as a duplicate can be complex.

---

### ❌ "Tokenization is the same as data cleaning."

No.

They are different processes.

```text
Cleaning
→ improves or filters the text

Tokenization
→ converts text into tokens
```

---

### ❌ "Data preparation and model training are the same."

No.

Data preparation creates usable training material.

Training updates model parameters.

---

### ❌ "The model stores the training dataset inside its parameters."

Not in the simple database-like sense.

The model learns numerical patterns through parameter updates. It can also memorize some training information.

---

# 33. Complete LLM Data Pipeline

The broader pipeline can be represented as:

```text
                RAW DATA
                   ↓
          Data Preparation
                   ↓
        Clean / Filter / Deduplicate
                   ↓
              Formatting
                   ↓
              Tokenization
                   ↓
             Token IDs
                   ↓
          Training Sequences
                   ↓
                Batches
                   ↓
          ┌─────────────────┐
          │ Transformer LLM │
          └────────┬────────┘
                   ↓
            Next-Token
             Prediction
                   ↓
                 Loss
                   ↓
           Backpropagation
                   ↓
          Parameter Updates
                   ↓
            Trained LLM
```

This connects data preparation to the complete LLM training process.

---

# 34. Simple Mental Model 🧠

Think of data preparation like preparing study material before teaching a student.

```text
Raw Books / Documents
        ↓
Remove unnecessary material
        ↓
Organize useful material
        ↓
Remove unnecessary repetition
        ↓
Convert into a format the student can use
        ↓
Teach
```

For an LLM:

```text
Raw Data
   ↓
Prepare Data
   ↓
Tokenize
   ↓
Create Training Sequences
   ↓
Train the Model
```

The model can only learn from the training signal it receives.

---

# 35. Key Takeaways 📌

* 🧹 **Data preparation** converts raw data into a more suitable form for LLM training.
* 🧼 Cleaning removes or handles unwanted content and formatting problems.
* 🔍 Filtering selects data according to quality, language, domain, or other requirements.
* 🔁 Deduplication reduces unnecessary repeated data.
* 📝 Formatting and normalization help create consistent training material.
* 🔤 Tokenization converts prepared text into tokens and token IDs.
* 📦 Token IDs are organized into training sequences and batches.
* 🎯 Input and target sequences are shifted for next-token prediction.
* ⚙️ Prepared data is used during the model training process.
* 🧠 Training updates model parameters; data preparation itself does not train the model.
* 🌍 Data quality, diversity, and mixture matter—not only the amount of data.
* ⚠️ Data preparation can also involve contamination, bias, copyright/licensing, safety, and policy considerations.
* 🔄 The exact preparation pipeline varies between LLMs and training setups.

The core idea is:

```text
Raw Data
   ↓
Prepare
   ↓
Tokenize
   ↓
Create Training Sequences
   ↓
Train the LLM
   ↓
Learned Parameters
```
