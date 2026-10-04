📚 Training Data

1. What is Training Data?

Training data is the collection of examples used to train an LLM.



For a language model, training data mainly consists of text that the model can learn patterns from.



Examples include:

Books
Articles
Web pages
Documentation
Code
Educational material
Conversations
Scientific text
News
Other text sources


The basic idea is:

Training Data
     ↓
Tokenization
     ↓
Training Sequences
     ↓
LLM
     ↓
Predictions
     ↓
Loss
     ↓
Parameter Updates


Through this process, the model learns patterns that help it predict tokens.

2. Why is Training Data Important?

An LLM can only learn patterns from the information available during training.



For example:

Training Data
     ↓
Patterns in Data
     ↓
Learned Parameters
     ↓
Model Behavior


Therefore, the training data strongly influences:



What the model knows

Which languages it handles well

Which domains it understands better

Which writing styles it can reproduce

Which programming languages it can generate

Which biases may appear

How well it performs on different tasks



Training data is therefore one of the most important parts of building an LLM.

3. What Can Training Data Contain?

LLM training data can contain many types of text.



For example:

Books
├── Fiction
├── Non-fiction
└── Reference material

Web Data
├── Articles
├── Documentation
├── Forums
└── Educational pages

Code
├── Python
├── Java
├── C++
├── JavaScript
└── Other languages

Scientific Data
├── Papers
├── Technical documents
└── Research material


The exact sources depend on the model and its training process.

4. Text is the Main Input

A language model ultimately needs numerical input.



Raw text cannot be directly processed by the Transformer.



The training pipeline therefore begins with text:

Raw Training Text
       ↓
Tokenization
       ↓
Tokens
       ↓
Token IDs
       ↓
Training Sequences


For example:

"The cat is sleeping."


may become:

["The", " cat", " is", " sleeping", "."]


The exact tokens depend on the tokenizer.

5. Training Data is Not the Same as Training Input

It is useful to distinguish these two terms.

Training Data

The complete collection of raw material used for training.

Millions / billions of text examples


Training Input

The token sequence actually provided to the model for a particular training step.

"The cat is sleeping"
        ↓
Input tokens


So:

Training Data
      ↓
Data Preparation
      ↓
Training Sequences
      ↓
Training Input


6. A Simple Example

Suppose our training data contains:

The cat is sleeping.
The dog is running.
The bird is flying.


After tokenization, the model can process sequences such as:

The cat is sleeping
The dog is running
The bird is flying


For next-token prediction:

Input:

The cat is

Target:

sleeping


Another example:

Input:

The dog is

Target:

running


The model learns from many such examples.

7. Training Data and Next-Token Prediction

Decoder-only LLMs commonly learn through next-token prediction.



Suppose the sequence is:

The cat is sleeping


The training relationships can be viewed as:

Input              Target

The                cat
The cat            is
The cat is         sleeping


The model predicts the target token.

"The cat is"
      ↓
    LLM
      ↓
"sleeping"


The prediction is compared with the actual target.

Prediction
    ↓
Compare with Target
    ↓
Loss


8. Large-Scale Training Data

Modern LLMs are trained on very large datasets.



The amount of training data can be extremely large, often involving billions or more tokens depending on the model and training setup.



A simplified view is:

Small Dataset
     ↓
Few Training Examples

Large Dataset
     ↓
Many More Patterns


However:

More data does not automatically mean better training.

The quality, diversity, relevance, and processing of the data also matter.

9. Data Quantity vs Data Quality

Two important factors are:

Data Quantity

How much training material is available.

More examples
      ↓
More opportunities to learn patterns


Data Quality

How useful and reliable those examples are.

High-quality examples
      ↓
Better learning signals


A very large dataset containing significant amounts of:



Spam

Duplicates

Incorrect information

Low-quality text

Unwanted content



may not be as useful as its raw size suggests.



So:

Good Training
=
Data Quantity
+
Data Quality
+
Data Diversity
+
Good Training Process


10. Data Diversity

Training data can contain many different domains.



For example:

                Training Data
                     │
       ┌─────────────┼─────────────┐
       ↓             ↓             ↓
    General       Technical      Creative
      Text          Text           Text
       ↓             ↓             ↓
   Articles       Papers         Stories
   Books          Docs           Poems
   Websites       Code           Scripts


Diverse data can expose the model to different:



Vocabulary

Topics

Writing styles

Structures

Domains

Languages

Concepts



This can support broader capabilities.

11. Language Distribution

Training data can contain multiple languages.



For example:

English
Hindi
Spanish
French
German
Japanese
...


The amount of data for each language can differ significantly.



For example:

Training Data

English  ████████████████
Hindi    ███████
French   █████
German   ████
Other    █████


A model's performance can depend strongly on how much and what kind of training data it receives for each language.



More data is not the only factor; data quality and linguistic diversity also matter.

12. Domain Coverage

Training data can contain information from different domains.



Examples:

Technology
Science
Medicine
Finance
Education
Law
History
Programming
Literature
Mathematics


If a model receives substantial high-quality data from a particular domain, it may learn useful patterns from that domain.



For example:

Programming Data
       ↓
Code Patterns
       ↓
Programming-Related Capabilities


This does not guarantee expert-level performance.

13. Code as Training Data

Code can be an important part of some LLM training datasets.



For example:

def add(a, b):
    return a + b


From many code examples, a model can learn patterns involving:



Syntax

Functions

Variables

Loops

Classes

Libraries

Comments

Documentation

Common programming structures



The model can then use these learned patterns when generating code.



However:

Learned Code Patterns
       ≠
Guaranteed Correct Code


Generated code can still contain errors.

14. Web Data

Web-based text can provide a large amount of diverse material.



Examples include:

Articles
Documentation
Educational pages
Forums
Public discussions
Reference material
Websites


Web data can provide:



Large scale

Diverse topics

Multiple writing styles

Multiple languages



But raw web data can also contain:



Spam

Duplicates

Incorrect information

Low-quality pages

Advertisements

Malicious or unwanted content



Therefore, data processing and filtering are important.

15. Books and Long-Form Text

Books can provide long-form examples of language.



They may contain:

Narrative structure
Long paragraphs
Dialogue
Descriptions
Explanations
Complex vocabulary


This type of data can expose models to language patterns that are different from short web pages.



However, the exact use of books depends on the dataset, licensing, filtering, and training setup.

16. Scientific and Technical Text

Scientific and technical documents can provide specialized vocabulary and structured explanations.



Examples:

Research papers
Technical documentation
Textbooks
Engineering documents
Scientific articles


This can expose a model to patterns such as:

Problem
  ↓
Method
  ↓
Analysis
  ↓
Result
  ↓
Conclusion


Again, learning patterns from technical text does not guarantee scientific correctness.

17. Conversations and Dialogue

Some training datasets can contain conversational text.



For example:

User: What is Python?

Assistant: Python is a programming language...


Dialogue data can expose models to:



Questions

Answers

Turn-taking

Explanations

Instructions

Conversational styles



However, not every LLM is trained on the same kind of conversation data.



Also, conversational behavior can involve additional training stages beyond broad pretraining.

18. Structured vs Unstructured Text

Training data can contain different structures.

Unstructured Text

Paragraphs
Articles
Books
Stories


Structured Text

Documentation
Tables represented as text
Code
Lists
Metadata
Question-answer formats


Different structures can provide different learning signals.



The model ultimately processes the information through token sequences.

19. Raw Data is Usually Not Ready for Training

Raw data generally needs preparation before being used.



A simplified pipeline is:

Raw Data
   ↓
Collection
   ↓
Filtering
   ↓
Cleaning
   ↓
Deduplication
   ↓
Quality Processing
   ↓
Formatting
   ↓
Tokenization
   ↓
Training Sequences


The exact pipeline differs between projects.

20. Data Cleaning

Data cleaning attempts to remove or handle unwanted content.



Examples can include:

Broken text
Duplicate records
Corrupted content
Unwanted markup
Extremely low-quality content
Other unsuitable data


For example:

Raw:

<h1>Hello</h1><div>World</div>

        ↓

Cleaned:

Hello World


Cleaning methods depend on the type of data.

21. Deduplication

Large datasets can contain repeated or nearly repeated content.



For example:

Document A:
Python is a programming language.

Document B:
Python is a programming language.


If large amounts of duplicated data remain in the dataset, the training process may repeatedly see the same information.



Deduplication attempts to reduce unnecessary repetition.



It can operate at different levels, such as:

Exact duplicates
        ↓
Near duplicates
        ↓
Repeated sections


The exact methods vary.

22. Filtering

Filtering can be used to remove data that is unsuitable for a particular training objective.



Possible filtering criteria can include:



Quality

Language

Spam

Duplicates

Formatting

Relevance

Safety requirements

Dataset-specific constraints



The exact filtering policy depends on the model and training project.

23. Data Quality

Training data quality can affect the quality of learned behavior.



A simplified relationship is:

Better Data
     ↓
Better Learning Signals
     ↓
Potentially Better Model Behavior


But model quality also depends on:



Architecture

Optimization

Compute

Training duration

Data mixture

Parameter count

Evaluation

Other training choices



Therefore, training data is important but is not the only factor.

24. Data Contamination

Training data can sometimes overlap with evaluation or benchmark data.



This can create data contamination.



For example:

Training Dataset
       ↓
Contains benchmark example
       ↓
Model sees it during training
       ↓
Later evaluated on the same example


The resulting evaluation may not accurately measure generalization.



This is one reason dataset and benchmark construction require careful separation.

25. Training Data and Copyright

Large-scale datasets can contain material from many sources.



The legal and licensing status of training data can vary by:



Source

Country

License

Dataset construction

Intended use

Applicable law



Therefore, real-world LLM development needs appropriate legal and licensing considerations.



This repository focuses on the technical role of training data rather than providing legal advice.

26. Training Data Does Not Equal Model Memory

A common misunderstanding is:

"If something is in the training data, the model stores it exactly."

That is not necessarily true.



The model learns through optimization.

Training Data
      ↓
Optimization
      ↓
Parameter Updates
      ↓
Learned Representations


The final model does not simply contain a copy of the complete training dataset.



However, some specific training examples can sometimes be memorized or reproduced.

27. Training Data and Knowledge

Training data influences what information a model can learn.



For example:

Training Data
      ↓
Patterns + Associations
      ↓
Learned Parameters
      ↓
Model Predictions


But the model's learned knowledge can be:



Incomplete

Incorrect

Contradictory

Outdated



Therefore:

Training Data
     ≠
Perfect Knowledge


28. Training Data and Bias

Training data can contain biases present in the source material.



For example:

Source Data
     ↓
Existing Biases
     ↓
Training Process
     ↓
Potential Model Bias


Bias can come from:



Unequal representation

Historical data

Cultural patterns

Stereotypes

Dataset construction

Filtering decisions



Data processing can reduce some problems, but it cannot guarantee that all bias is removed.

29. Data Freshness

Training data has a time dimension.



Suppose a model was trained mostly on information available before a particular date.



Then some later events may not be represented in its training data.

Past Data
   ↓
Training
   ↓
Model
   ↓
Knowledge reflects training period


This is one reason an LLM's knowledge can become outdated.



A model can only learn information from training data that it actually receives.

30. Training Data vs Context Data

These two ideas are very different.

Training Data

Used to change model parameters.

Training Data
    ↓
Loss
    ↓
Parameter Updates


Context Data

Provided to a trained model during inference.

User Input
    ↓
Existing Model
    ↓
Response


The context can influence the current response without normally changing the model's parameters.

31. Training Data vs Prompt

A prompt is not automatically training data.



For example:

User:
"Explain photosynthesis."


This is normally inference input.



It is processed by the already-trained model.

Prompt
  ↓
Trained LLM
  ↓
Response


Training data is used during the training process that creates or updates the model.

32. Training Data Pipeline

A simplified LLM data pipeline looks like:

                Raw Data Sources
                       ↓
          ┌────────────┼────────────┐
          ↓            ↓            ↓
        Books        Web          Code
          ↓            ↓            ↓
          └────────────┼────────────┘
                       ↓
                  Data Cleaning
                       ↓
                   Filtering
                       ↓
                 Deduplication
                       ↓
                Quality Processing
                       ↓
                 Data Formatting
                       ↓
                  Tokenization
                       ↓
              Training Sequences
                       ↓
                Input + Targets
                       ↓
                    LLM Training


This is a simplified conceptual pipeline. Real training systems can be much more complex.

33. From Training Data to Tokens

The model ultimately works with tokens.



Suppose the raw data contains:

The cat is sleeping.


The pipeline can be:

Raw Text
   ↓
Tokenizer
   ↓
Tokens
   ↓
Token IDs
   ↓
Training Sequence


For example:

["The", " cat", " is", " sleeping", "."]


might become:

[1256, 912, 318, 8421, 13]


The exact IDs are tokenizer-specific.

34. Creating Training Sequences

Long documents cannot necessarily be fed into the model as unlimited-length sequences.



The text is organized into sequences compatible with the model's context length.



For example:

Long Document
      ↓
Tokenized Document
      ↓
Sequence 1
Sequence 2
Sequence 3
...


Conceptually:

Token 1 → Token 2 → Token 3 → ... → Token N


Each sequence can then be used for training.



The exact sequence construction strategy varies.

35. Input and Target Tokens

For next-token prediction, tokens can be shifted to create inputs and targets.



Suppose:

Tokens:

The cat is sleeping


Then:

Input:
The cat is

Target:
cat is sleeping


Conceptually:

Input Tokens:
[The, cat, is]

Target Tokens:
[cat, is, sleeping]


The model predicts the target tokens from the input context.



Causal masking ensures that each prediction cannot use future target information.

36. Batch Formation

Training usually processes multiple sequences together in batches.



For example:

Batch
├── Sequence 1
├── Sequence 2
├── Sequence 3
└── Sequence 4


Conceptually:

Training Sequences
       ↓
     Batch
       ↓
    Model
       ↓
Predictions


Batching allows efficient computation on GPUs and other accelerators.

37. Training Data and the Transformer

The training data does not directly modify the Transformer.



Instead:

Training Data
      ↓
Tokenization
      ↓
Input + Target
      ↓
Transformer
      ↓
Predictions
      ↓
Loss
      ↓
Gradients
      ↓
Parameter Updates


The Transformer parameters gradually change during training.



This is how the model learns from the data.

38. What Makes Good Training Data?

There is no single perfect dataset, but useful training data generally benefits from:

High Quality
     +
Useful Diversity
     +
Good Coverage
     +
Appropriate Filtering
     +
Low Unnecessary Duplication


Depending on the goal, it may also need:



Multiple languages

Domain-specific content

High-quality code

Long-form text

Technical material

Different writing styles



The ideal mixture depends on the model's intended use.

39. Training Data Is a Mixture

A large language model may be trained using a mixture of different data sources.



Conceptually:

              Training Mixture
                    │
      ┌─────────────┼─────────────┐
      ↓             ↓             ↓
    Web           Books          Code
      ↓             ↓             ↓
    Docs        Literature     Programs
      ↓             ↓             ↓
      └─────────────┼─────────────┘
                    ↓
              Training Dataset


The proportions and sources can vary significantly between models.

40. Data Quality and Model Behavior

The relationship can be summarized as:

Training Data
      ↓
What the model can observe
      ↓
What patterns can be learned
      ↓
What behaviors may become possible


But the final behavior also depends on:

Architecture
+
Optimization
+
Training Procedure
+
Model Scale
+
Data


So the model is not simply a direct copy of its training data.

41. A Simple Real-World Analogy

Imagine teaching a student using thousands of books.

Books
Articles
Examples
Exercises
Explanations


The student does not simply memorize every page.



Instead, they may learn:

Vocabulary
Grammar
Concepts
Relationships
Patterns
Problem-solving strategies
Writing styles


An LLM is fundamentally different from a human learner, but this analogy can help explain the basic idea of learning patterns from many examples.



The model learns through numerical optimization rather than human experience.

42. Complete Training Data Flow

The overall flow can be remembered as:

Raw Data
   ↓
Clean and Filter
   ↓
Deduplicate
   ↓
Prepare Data
   ↓
Tokenize
   ↓
Create Token IDs
   ↓
Build Training Sequences
   ↓
Create Input + Target
   ↓
Batch the Data
   ↓
Train the LLM
   ↓
Calculate Loss
   ↓
Update Parameters
   ↓
Learned Model


43. Simple Mental Model

Think of training data as the learning material for an LLM.

Training Data
      ↓
Examples of Language
      ↓
Token Sequences
      ↓
Next-Token Prediction
      ↓
Loss
      ↓
Parameter Updates
      ↓
Learned Patterns


The model does not simply copy the training data.



Instead, training changes its parameters so that the model becomes better at predicting tokens from context.

44. Key Takeaways

📚 Training data is the collection of examples used to train an LLM.

📝 LLM training data is primarily text, but can include many types of textual material such as books, web pages, documentation, code, and scientific text.

🔤 Raw text is converted into tokens and token IDs before entering the model.

🎯 Decoder-only LLMs commonly use training data for next-token prediction.

🧹 Raw data usually requires cleaning, filtering, deduplication, and other preparation.

🌍 Data diversity affects the range of patterns the model can learn.

🏷️ Domain and language coverage can affect model capabilities.

⚖️ Data quality matters as much as, and sometimes more than, simply increasing data quantity.

🧠 Training data does not become a simple database inside the model; learning is represented through model parameters.

🔄 Training data changes parameters through loss, backpropagation, and optimization.

⚠️ Training data can contain errors, bias, duplicates, outdated information, and other problems.

🚫 Training data is different from the context or prompt provided during normal inference.

🚀 The basic data-to-model path is:

Raw Data
   ↓
Cleaning + Filtering
   ↓
Tokenization
   ↓
Training Sequences
   ↓
Input + Target
   ↓
LLM
   ↓
Loss
   ↓
Parameter Updates
   ↓
Learned Model
