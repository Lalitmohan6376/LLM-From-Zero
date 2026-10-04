# 🧠 What Does an LLM Learn?

## 1. Introduction

An LLM is trained on large amounts of text.

But what exactly does it **learn** from that text?

The simplest answer is:

> **An LLM learns patterns in data that help it predict the next token.**

During training, the model repeatedly sees sequences of tokens, makes predictions, compares those predictions with the actual next tokens, and updates its parameters.

```text id="intro-flow"
Training Text
     ↓
Tokenization
     ↓
Input Tokens
     ↓
LLM
     ↓
Next-Token Prediction
     ↓
Compare with Target
     ↓
Loss
     ↓
Parameter Updates
     ↓
Learned Patterns
```

The model does not store a simple list of rules such as:

```text
"cat" → "animal"
"Paris" → "France"
```

Instead, learning is distributed across a very large number of parameters.

---

# 2. The Core Learning Objective

For a decoder-only language model, the central training objective is usually **next-token prediction**.

Suppose the training text is:

```text id="objective-example"
The cat is sleeping
```

The model can create training relationships such as:

```text
Input              Target

The                cat
The cat            is
The cat is         sleeping
```

The model tries to predict the target token from the available context.

```text id="objective-flow"
"The cat is"
      ↓
     LLM
      ↓
Prediction:
"sleeping"
```

If the prediction is poor, the training process calculates a loss and updates the model parameters.

After seeing many examples, the model learns patterns that improve its predictions.

---

# 3. What Does "Learn" Mean Here?

When we say an LLM **learns**, we mean that its parameters are adjusted during training.

A model starts with parameters that do not yet produce useful language behavior.

Training repeatedly changes these parameters:

```text id="parameter-learning"
Initial Parameters
       ↓
Prediction
       ↓
Loss
       ↓
Backpropagation
       ↓
Parameter Update
       ↓
New Parameters
       ↓
Better Prediction
```

This happens over a very large number of training examples and optimization steps.

The learned information is therefore represented in the model's parameters.

---

# 4. LLMs Learn Patterns, Not Simple Rules

Consider these sentences:

```text id="patterns"
The dog is running.
The dog is sleeping.
The dog is eating.
```

The model encounters many similar patterns during training.

It can learn statistical relationships between tokens and contexts.

For example:

```text id="relationship"
"dog"
  ↓
often appears near:
"bark"
"animal"
"pet"
"running"
"eating"
```

This does not mean the model stores a simple dictionary of these relationships.

The patterns are distributed across the model's learned parameters.

---

# 5. Language Patterns

One major thing an LLM learns is how language is structured.

For example:

```text id="language-patterns"
Words
 ↓
Phrases
 ↓
Sentences
 ↓
Larger Text Structures
```

The model can learn patterns involving:

* Word combinations
* Sentence structure
* Grammar
* Punctuation
* Common expressions
* Writing styles
* Relationships between words
* Context-dependent meanings

These patterns help the model predict what tokens are likely to appear next.

---

# 6. Grammar Patterns

LLMs can learn many grammatical patterns from examples.

For example:

```text id="grammar"
She is going home.
He is going home.
They are going home.
```

From many examples, the model can learn patterns involving:

```text
Subject
   ↓
Verb
   ↓
Object / Complement
```

It does not need to be explicitly given a grammar rule such as:

```text
"Use 'is' with this type of subject."
```

The patterns can emerge from training on many examples.

---

# 7. Word and Token Relationships

The model learns relationships between tokens.

For example:

```text id="token-relations"
doctor ↔ hospital
teacher ↔ school
pilot  ↔ airplane
```

These relationships are learned through the contexts in which tokens appear.

The model does not simply memorize one fixed relationship.

The same token can have different relationships depending on context.

For example:

```text id="context-meaning"
bank near "money"
        ↓
financial institution

bank near "river"
        ↓
side of a river
```

Context is therefore extremely important.

---

# 8. Contextual Relationships

The meaning or role of a token can depend on surrounding tokens.

Consider:

```text id="context"
"The animal went to the bank."
```

and:

```text
"The person deposited money in the bank."
```

The word **"bank"** appears in both sentences, but the surrounding context is different.

A Transformer uses contextual processing, especially through attention, to build representations that depend on the surrounding sequence.

```text id="context-flow"
Token
  +
Surrounding Context
  ↓
Contextual Representation
```

This is one reason Transformers are powerful for language modeling.

---

# 9. Semantic Patterns

LLMs can learn many patterns related to meaning.

For example:

```text id="semantic"
king
queen

Paris
France

doctor
hospital
```

These relationships are learned from patterns in the training data.

However, saying that an LLM learns "meaning" should be understood carefully.

The model learns statistical and representational patterns that are useful for language prediction.

This should not automatically be interpreted as human-like understanding.

---

# 10. Facts and World Knowledge

LLMs can also learn information that appears repeatedly or meaningfully in their training data.

For example:

```text id="facts"
The Earth orbits the Sun.
Water freezes at approximately 0°C under standard conditions.
Paris is the capital of France.
```

If such information appears in training data, the model may learn patterns that allow it to generate similar information later.

However:

> **An LLM's learned knowledge is not guaranteed to be complete, current, or correct.**

Training data can contain:

* Errors
* Contradictions
* Outdated information
* Biases
* Missing information

Therefore, a model can produce incorrect information even when it has been trained on a large amount of data.

---

# 11. Relationships Between Concepts

LLMs can learn associations between concepts.

For example:

```text id="concepts"
Python
  ↓
Programming
  ↓
Functions
  ↓
Variables
  ↓
Libraries
```

Or:

```text
Machine Learning
        ↓
Supervised Learning
        ↓
Classification
        ↓
Regression
```

These associations are learned from how concepts appear together across the training data.

The model's internal representations encode many such relationships.

---

# 12. Code Patterns

If an LLM is trained on programming code, it can learn many patterns found in code.

For example:

```python
for i in range(10):
    print(i)
```

The model can learn patterns involving:

* Programming syntax
* Function definitions
* Variables
* Loops
* Common libraries
* Code structure
* Common programming patterns
* Comments and documentation

This can allow an LLM to generate or explain code.

However, generated code can still contain bugs or security problems.

Learning code patterns does not guarantee that every generated program is correct.

---

# 13. Different Writing Styles

LLMs can learn patterns associated with different styles of writing.

For example:

```text id="styles"
Formal writing
Casual writing
Technical writing
Academic writing
Creative writing
Documentation
```

The training data can contain examples of these styles.

The model can therefore learn statistical patterns associated with them.

For example:

```text id="styleexample"
Formal:
"Please provide the requested information."

Casual:
"Can you send me the info?"
```

The model learns patterns that distinguish these forms of expression.

---

# 14. Multilingual Patterns

If the training data contains multiple languages, an LLM can learn patterns across those languages.

For example:

```text id="multilingual"
English
Hindi
French
Spanish
German
...
```

The model can learn:

* Vocabulary patterns
* Grammar patterns
* Sentence structures
* Translation relationships
* Multilingual associations

The quality depends heavily on the amount and quality of training data for each language.

A model trained mostly on one language may perform much better in that language than in a low-resource language.

---

# 15. Long-Range Relationships

Transformers can learn relationships between tokens that are far apart in a sequence.

For example:

```text id="longrange"
The scientist entered the laboratory after
several hours of travel because she needed
to continue her experiment.
```

The model may need information from earlier parts of the sequence when processing later tokens.

Self-attention allows token representations to incorporate information from other positions that are visible under the attention pattern.

In a decoder-only model, causal masking means a token can only use the current and previous positions.

---

# 16. Patterns Across Different Levels

An LLM does not learn only individual words.

It can learn patterns at different levels:

```text id="levels"
Characters / Subwords
        ↓
Tokens
        ↓
Words
        ↓
Phrases
        ↓
Sentences
        ↓
Paragraphs
        ↓
Documents
        ↓
Broader Patterns
```

These levels are not necessarily stored as separate modules.

The model's representations and parameters collectively capture many different patterns.

---

# 17. How Does the Model Learn These Patterns?

The learning process is based on optimization.

A simplified training loop is:

```text id="learning-loop"
Training Data
     ↓
Tokenization
     ↓
Input + Target
     ↓
Forward Pass
     ↓
Predicted Logits
     ↓
Loss
     ↓
Backpropagation
     ↓
Optimizer
     ↓
Parameter Update
     ↓
Repeat
```

Each update changes the model slightly.

Over many updates, the model's parameters become better at predicting tokens.

---

# 18. Parameters Are Where Learning Is Stored

An LLM can contain millions, billions, or more parameters.

Parameters include learned numerical values such as:

```text id="parameters"
Weights
Biases
Other learned parameters
```

During training:

```text id="parameter-update"
Old Parameter
     ↓
Gradient
     ↓
Optimizer
     ↓
New Parameter
```

The collection of these learned values forms the trained model.

It is therefore useful to think of the model's parameters as storing **distributed learned patterns**, rather than a simple database of facts.

---

# 19. What Does Attention Learn?

Attention helps the model determine how information from different token positions should interact.

For example:

```text id="attention"
"The animal didn't cross the road because it was tired."
```

When processing a token, attention can help combine information from relevant visible positions.

The model learns attention parameters during training.

These parameters determine how Queries, Keys, and Values are produced and processed.

However, attention weights should not automatically be interpreted as a complete explanation of what the model "understands."

---

# 20. What Does the Feed-Forward Network Learn?

The Feed-Forward Network (FFN) transforms representations at each position.

A simplified view is:

```text id="ffn-learning"
Contextual Representation
          ↓
         FFN
          ↓
Transformed Representation
```

The FFN contains learned parameters.

Together with attention and the rest of the Transformer, it helps the model build useful internal representations for prediction.

It is not accurate to assign one fixed human-readable concept to every FFN or layer.

---

# 21. Does the Model Learn Rules?

Yes, but the word **rules** needs to be used carefully.

An LLM can learn patterns that behave similarly to rules.

For example, it may learn that:

```text id="rulepattern"
"if" → often followed by a condition
```

Or:

```text
Python function
    ↓
def function_name(...)
```

But these are not necessarily stored as explicit symbolic rules.

The model generally represents learned patterns through numerical parameters.

So:

```text id="rules"
Explicit Rule System:
IF X → THEN Y

LLM:
Learned numerical patterns
       ↓
Context-dependent predictions
```

---

# 22. Does an LLM Memorize Training Data?

An LLM can memorize some parts of its training data, especially information that is repeated or distinctive.

But it is not accurate to describe all learned behavior as simple memorization.

Training can produce both:

```text id="memorization-generalization"
Memorization
     +
Pattern Learning
     +
Generalization
```

The model can sometimes generate information that was not present as an exact sentence in its training data.

It can combine learned patterns in new ways.

However, memorization and generalization can coexist, and the degree of memorization depends on the model, training process, data, and specific example.

---

# 23. Generalization

**Generalization** means using learned patterns in situations that are different from the exact training examples.

Suppose the model sees many examples of:

```text id="generalization"
"The dog is running."
"The horse is running."
"The child is running."
```

It may learn patterns associated with the structure:

```text
Subject + is + running
```

It can then generate:

```text
"The athlete is running."
```

even if that exact sentence was not seen during training.

This is a simplified example of generalization.

---

# 24. Learning From Context vs Learning During Training

Two different ideas should be separated.

### Learning During Training

The model's parameters are updated.

```text id="traininglearning"
Data
 ↓
Loss
 ↓
Parameter Updates
 ↓
Learned Model
```

### Using Context During Inference

The model uses the current input without normally changing its parameters.

```text id="inferencecontext"
Prompt
 ↓
Contextual Processing
 ↓
Prediction
```

For example, if you tell the model:

```text
"My dog's name is Max."
```

the model can use that information later in the same context.

That does **not** normally mean the model permanently changed its parameters.

---

# 25. Does an LLM Learn During Normal Chat?

In standard inference, the model normally does not update its weights after every user message.

Instead:

```text id="chat"
User Input
   ↓
Existing Trained Parameters
   ↓
Context Processing
   ↓
Response
```

The model uses its existing learned parameters plus the current context.

Parameter updates require a separate training or adaptation process.

---

# 26. What Does an LLM Not Automatically Learn?

Training on large text datasets does not guarantee that an LLM learns everything correctly.

It does not automatically guarantee:

* Perfect factual knowledge
* Perfect reasoning
* Perfect mathematics
* Perfect common sense
* Current information
* Complete knowledge
* Correct code
* Reliable predictions
* Human-like understanding

A model can produce fluent text while still being wrong.

```text id="fluency"
Fluent Output
    ≠
Guaranteed Truth
```

---

# 27. Training Data Matters

What an LLM learns depends strongly on its training data.

The training data affects:

```text id="dataimpact"
What information appears
        ↓
What patterns can be learned
        ↓
What behaviors may emerge
```

Important factors include:

* Data size
* Data quality
* Data diversity
* Language distribution
* Domain coverage
* Duplicates
* Noise
* Bias
* Filtering
* Data freshness

More data alone does not guarantee better learning.

---

# 28. Data Quality Matters

Suppose training data contains many incorrect examples.

The model can learn patterns from those examples too.

```text id="quality"
High-quality data
      ↓
Useful learning signals

Noisy / incorrect data
      ↓
Potentially noisy learning signals
```

Therefore:

> **Training quality is not determined only by the amount of data.**

Data composition and quality also matter.

---

# 29. What Does "Knowledge" Mean in an LLM?

When we say an LLM has "knowledge", this is a simplified description.

The model does not contain a traditional database where facts are stored like:

```text id="database"
Question → Answer
```

Instead, learned information is distributed across model parameters and representations.

For example:

```text id="distributed"
Training Data
      ↓
Patterns
      ↓
Learned Parameters
      ↓
Model Behavior
```

This learned information can be used during prediction.

---

# 30. What Does the Model Learn About a Sentence?

Consider:

```text id="sentence"
"The student solved the problem."
```

During training, the model can learn patterns involving:

```text
"The"
 ↓
"student"
 ↓
"solved"
 ↓
"the"
 ↓
"problem"
```

It can also learn broader relationships involving:

* Sentence structure
* Word relationships
* Grammatical patterns
* Semantic associations
* Common sequences

The model does not simply learn each sentence as an isolated object.

It learns statistical patterns across a huge collection of examples.

---

# 31. Learning Is Distributed

One important property of neural networks is that learned information is distributed across many parameters.

It is usually not possible to say:

```text id="not-simple"
Parameter 1 = grammar
Parameter 2 = mathematics
Parameter 3 = Python
```

Instead:

```text id="distributedlearning"
Many Parameters
      ↓
Many Interacting Representations
      ↓
Complex Learned Behavior
```

Different layers, attention heads, neurons, and parameters can contribute to multiple behaviors.

---

# 32. Does Bigger Model Mean More Learning?

Not automatically.

A larger model has more capacity, but performance depends on multiple factors:

```text id="scale"
Model Size
+
Training Data
+
Data Quality
+
Architecture
+
Optimization
+
Training Compute
+
Training Process
```

A larger model can potentially learn more complex patterns, but:

> **Bigger does not automatically mean better in every situation.**

---

# 33. A Simple Example of Learning

Imagine the model repeatedly sees:

```text id="simpleexample"
The sky is blue.
The ocean is blue.
The car is red.
The grass is green.
```

During training, the model learns patterns connecting contexts with likely next tokens.

If given:

```text
"The sky is"
```

it may assign a high score to:

```text
blue
```

The important point is that the model learned numerical parameters that make this prediction likely.

It did not receive a hard-coded rule saying:

```text
IF subject = sky
THEN output = blue
```

---

# 34. Learning Is More Than Next-Token Memorization

Although the training objective is often next-token prediction, the model can learn many useful internal patterns as a consequence.

These can include:

```text id="emergentpatterns"
Language structure
     ↓
Contextual relationships
     ↓
Concept associations
     ↓
Code patterns
     ↓
Style patterns
     ↓
Multilingual relationships
     ↓
Other statistical regularities
```

The model is optimized for prediction, but the internal representations that help prediction can support many capabilities.

---

# 35. Why Can Next-Token Prediction Produce Broad Capabilities?

This is one of the most important ideas in understanding LLMs.

Suppose a model must predict the next token in many different types of text:

```text id="broadtraining"
Books
Articles
Web pages
Code
Documentation
Conversations
Questions
Answers
Scientific text
...
```

To predict tokens well, the model benefits from learning many patterns present in those sources.

Therefore, a simple objective:

```text id="objective"
Predict the next token
```

can lead to rich internal representations.

However, this does not mean every capability is guaranteed or perfectly reliable.

---

# 36. What the LLM Learns: A Layered View

A useful conceptual view is:

```text id="layered"
Raw Text
   ↓
Token Patterns
   ↓
Language Patterns
   ↓
Contextual Relationships
   ↓
Concept Associations
   ↓
Broader Statistical Patterns
   ↓
Prediction Behavior
```

These should not be interpreted as strict separate stages where one layer only learns one category.

They are a conceptual way to understand the kinds of patterns that can emerge from training.

---

# 37. Complete Learning Process

The complete simplified learning process is:

```text id="complete"
Large-Scale Training Data
          ↓
      Tokenization
          ↓
   Training Sequences
          ↓
   Input + Target Tokens
          ↓
    Transformer Model
          ↓
      LM Head
          ↓
        Logits
          ↓
    Next-Token Prediction
          ↓
         Loss
          ↓
    Backpropagation
          ↓
      Optimizer
          ↓
    Parameter Updates
          ↓
   Learned Parameters
          ↓
   Learned Patterns
          ↓
 Better Predictions
```

This process is repeated many times.

---

# 38. Simple Mental Model

The easiest way to remember what an LLM learns is:

```text id="mental"
The model sees many examples of language.

        ↓

It tries to predict the next token.

        ↓

Its prediction is compared with the actual token.

        ↓

The error is used to update its parameters.

        ↓

After many updates, the model learns
patterns that help it predict language.
```

So:

> **An LLM primarily learns numerical representations and patterns that help it predict tokens from context.**

---

# 39. Key Takeaways

* 🧠 An LLM learns patterns from large amounts of training data.
* 🎯 The core objective of a decoder-only LLM is usually next-token prediction.
* 🔢 Learning happens by updating model parameters during training.
* 📝 The model can learn language, grammar, contextual relationships, semantic associations, code patterns, styles, and other statistical regularities.
* 🌍 It can learn information present in its training data, but that information is not guaranteed to be complete, current, or correct.
* 🧩 Learned information is distributed across many parameters rather than stored as a simple database.
* 🔄 Training changes model parameters; normal inference generally does not.
* 📚 Training data quality, diversity, and composition strongly affect what the model learns.
* 🧠 Next-token prediction can lead to broad capabilities because predicting diverse text benefits from learning many underlying patterns.
* ⚠️ Learning patterns does not guarantee human-like understanding, perfect reasoning, or factual accuracy.
* 🚀 The core learning loop is:

```text id="final-loop"
Training Data
     ↓
Prediction
     ↓
Loss
     ↓
Backpropagation
     ↓
Parameter Update
     ↓
Learned Patterns
     ↓
Better Prediction
```
