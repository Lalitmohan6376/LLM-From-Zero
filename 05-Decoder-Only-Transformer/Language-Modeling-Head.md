🧠 Language Modeling Head

1. What is a Language Modeling Head?

The Language Modeling Head (LM Head) is the final layer of a language model that converts the Transformer’s hidden representations into scores for every token in the vocabulary.



In a decoder-only LLM, the basic flow is:

Input Text
    ↓
Tokenization
    ↓
Token IDs
    ↓
Token Embeddings
    ↓
Transformer Blocks
    ↓
Final Hidden States
    ↓
Language Modeling Head
    ↓
Logits
    ↓
Probability Distribution
    ↓
Next Token


The LM Head connects the internal representation of the Transformer to the model's vocabulary.

2. Why Do We Need an LM Head?

The Transformer does not directly output words or tokens.



After passing through all Transformer blocks, the model has a representation for each position in the sequence.



For example:

"The cat is"


After the Transformer:

Position 1 → hidden representation
Position 2 → hidden representation
Position 3 → hidden representation


These hidden representations contain information produced by the Transformer.



But we still need to answer:

Which token should come next?

The Language Modeling Head converts the hidden representation into scores for all possible vocabulary tokens.

Hidden Representation
        ↓
Language Modeling Head
        ↓
Scores for Vocabulary
        ↓
Logits


3. Hidden States Before the LM Head

Suppose the model has:



Vocabulary size = 50,000

Hidden dimension = 768

Sequence length = 10



The Transformer may produce:

[10 × 768]


This means there is one 768-dimensional hidden representation for each of the 10 token positions.



Conceptually:

Token 1 → [768 values]
Token 2 → [768 values]
Token 3 → [768 values]
...
Token 10 → [768 values]


The LM Head converts these representations into vocabulary-sized outputs.

[10 × 768]
      ↓
Language Modeling Head
      ↓
[10 × 50,000]


Now every position has a score for every vocabulary token.

4. What Does the LM Head Produce?

The LM Head normally produces logits.



A logit is a raw numerical score for a possible token.



For example:

Token        Logit
-------------------
"cat"        2.1
"dog"        1.7
"car"       -0.5
"the"        3.4
"runs"       0.8


These values are not probabilities yet.



The model can convert them into probabilities using Softmax.

Hidden State
     ↓
LM Head
     ↓
Logits
     ↓
Softmax
     ↓
Probabilities


5. Basic Mathematical Idea

Suppose the final hidden representation is:

h


The LM Head can be represented as a linear projection:

z = hW + b


Where:



h = hidden representation

W = output projection weights

b = bias

z = logits



The number of output values is equal to the vocabulary size.



If:

hidden dimension = 768
vocabulary size = 50,000


then the output projection maps:

768 → 50,000


So:

[768]
   ↓
LM Head
   ↓
[50,000]


Each of the 50,000 values represents the score of one vocabulary token.

6. Why Vocabulary Size Matters

The output dimension of the LM Head is connected to the vocabulary size.



Suppose:

Vocabulary = 30,000 tokens


Then the LM Head produces:

30,000 logits


If:

Vocabulary = 100,000 tokens


Then it produces:

100,000 logits


Conceptually:

Hidden State
     ↓
     ├── Token 1 score
     ├── Token 2 score
     ├── Token 3 score
     ├── ...
     └── Token 100,000 score


The model then uses these scores to determine the next-token distribution.

7. LM Head and Softmax

The LM Head produces logits.



Softmax converts the logits into a probability distribution.



The simplified formula is:

P(token) = softmax(logits)


For example:

Logits:

cat     2.5
dog     1.8
car     0.2
tree   -0.5


After Softmax:

Token     Probability
---------------------
cat          0.57
dog          0.28
car          0.10
tree         0.05


The probabilities sum approximately to:

1.0


The model can then select a token according to the chosen decoding strategy.

8. LM Head Does Not Directly Generate Text

The LM Head itself does not produce a sentence.



It produces numerical scores.



The complete process is:

Transformer
    ↓
Hidden State
    ↓
LM Head
    ↓
Logits
    ↓
Softmax / Logit Processing
    ↓
Token Selection
    ↓
Selected Token
    ↓
Repeat


For example:

"The cat"


The model might predict:

"sat"


Then the sequence becomes:

"The cat sat"


The model runs the generation process again to predict the next token.

9. LM Head During Autoregressive Generation

LLMs usually generate text one token at a time.



Suppose the input is:

"The cat"


The model processes the sequence and produces hidden states:

"The" → hidden state
"cat" → hidden state


For next-token generation, the relevant output is generally taken from the current/last position.

"The cat"
       ↓
Transformer
       ↓
Hidden state for current position
       ↓
LM Head
       ↓
Logits
       ↓
Probabilities
       ↓
"sat"


The new token is then added:

"The cat sat"


The process repeats.

10. LM Head During Training

During training, the model learns to predict the next token.



Suppose the sequence is:

The cat is sleeping


Training examples can be created as:

Input:  The cat is
Target: cat is sleeping


More precisely, for next-token prediction:

Input tokens:   The   cat   is
Target tokens:  cat   is   sleeping


The Transformer produces hidden states for the input positions.



The LM Head produces logits for the vocabulary at those positions.

Input
  ↓
Transformer
  ↓
Hidden States
  ↓
LM Head
  ↓
Logits
  ↓
Compare with Target Tokens
  ↓
Loss


The loss tells the model how different its predictions were from the target tokens.

11. Why Can Training Predict Many Positions at Once?

A decoder-only Transformer uses causal masking.



For example:

The cat is sleeping


The model must not use future tokens when predicting an earlier token.



Conceptually:

Position 1 → can see position 1
Position 2 → can see positions 1-2
Position 3 → can see positions 1-3
Position 4 → can see positions 1-4


Because of causal masking, the model can process many positions in parallel during training while preventing future-token information from leaking into the prediction.



Therefore, the LM Head can produce logits for multiple positions:

Hidden States
[B, N, D]
    ↓
LM Head
    ↓
Logits
[B, N, V]


Where:



B = batch size

N = sequence length

D = hidden dimension

V = vocabulary size

12. LM Head Shape

Suppose:

Batch size = 2
Sequence length = 8
Hidden dimension = 768
Vocabulary size = 50,000


The Transformer output is approximately:

[2, 8, 768]


The LM Head maps the final dimension:

768 → 50,000


So the logits become:

[2, 8, 50,000]


This means:

2 sequences
   ↓
8 positions per sequence
   ↓
50,000 vocabulary scores per position


13. LM Head Weight Matrix

The LM Head can be represented by a weight matrix.



For example:

Hidden Dimension = 768
Vocabulary Size = 50,000


The output projection has a conceptual shape like:

768 × 50,000


The projection transforms:

768-dimensional hidden representation


into:

50,000-dimensional vocabulary scores


The exact parameterization can vary between architectures and implementations.

14. Weight Tying

Some language models use weight tying.



Weight tying means that the input token embedding matrix and output projection weights share parameters.



Without weight tying:

Token Embedding Matrix
        ↓
     Input side

Output Projection Matrix
        ↓
     Output side


With weight tying:

       Shared Weights
        /          \
       ↓            ↓
Input Embeddings   LM Head


This can reduce the number of parameters and connect the input and output token representations.



However, weight tying is optional.



Not every language model must use it.

15. Token Embeddings vs LM Head

These two components are related but have different jobs.

Component

Main Job

Token Embedding

Converts token IDs into vectors

Transformer Blocks

Transform contextual representations

LM Head

Converts final representations into vocabulary logits

Softmax

Converts logits into probabilities

The overall flow is:

Token ID
   ↓
Embedding
   ↓
Transformer
   ↓
LM Head
   ↓
Logits
   ↓
Probability


16. LM Head vs Transformer

The Transformer and LM Head have different responsibilities.

Transformer

The Transformer processes the sequence and builds contextual representations.

Input Representations
        ↓
Transformer Blocks
        ↓
Contextual Representations


LM Head

The LM Head converts those representations into vocabulary scores.

Contextual Representation
        ↓
LM Head
        ↓
Vocabulary Logits


So:

Transformer = representation processing

LM Head = representation → vocabulary scores


17. LM Head vs Softmax

The LM Head and Softmax are also different.

LM Head
   ↓
Logits
   ↓
Softmax
   ↓
Probabilities


LM Head

Produces raw scores.

Softmax

Converts those scores into a probability distribution.



For example:

LM Head:

cat → 4.2
dog → 2.1
car → 0.3


Then:

Softmax:

cat → 0.87
dog → 0.11
car → 0.02


So logits and probabilities should not be treated as the same thing.

18. LM Head and Next-Token Prediction

The LM Head is the final bridge between the model's internal representation and next-token prediction.



The complete conceptual process is:

Text
 ↓
Tokenization
 ↓
Token IDs
 ↓
Embeddings
 ↓
Positional Information
 ↓
Transformer Blocks
 ↓
Final Hidden State
 ↓
Language Modeling Head
 ↓
Logits
 ↓
Probability Distribution
 ↓
Next Token


This is the key role of the LM Head.

19. A Simple Example

Suppose the input is:

"The dog is"


The Transformer processes these tokens and produces a final hidden representation for the current position.



Suppose the LM Head produces:

running → 5.2
sleeping → 3.1
eating → 2.7
blue → 0.4


These are logits.



After probability conversion:

running → 0.75
sleeping → 0.13
eating → 0.10
blue → 0.02


The model can then select:

running


The sequence becomes:

"The dog is running"


The model then continues generating.

20. Generation Loop

Autoregressive generation can be represented as:

Prompt
  ↓
Tokenize
  ↓
Transformer
  ↓
LM Head
  ↓
Logits
  ↓
Probability / Sampling
  ↓
Select Next Token
  ↓
Append Token
  ↓
Transformer
  ↓
LM Head
  ↓
Next Token
  ↓
Repeat


Eventually, a stopping condition is reached.



For example:

End-of-sequence token


or:

Maximum generation length


21. LM Head and Decoding Strategies

The LM Head produces logits, but the final token selection can use different decoding strategies.



Common approaches include:

Greedy Decoding

Select the token with the highest probability.

Highest probability
        ↓
    Next Token


Temperature

Adjusts the sharpness of the probability distribution.

Logits
  ↓
Temperature
  ↓
Probabilities


Top-K

Keeps only the highest-scoring K candidate tokens.

Vocabulary
    ↓
Top-K candidates
    ↓
Selection


Top-P

Keeps a set of tokens whose cumulative probability reaches a chosen threshold.

Vocabulary
    ↓
Top-P candidates
    ↓
Selection


These are decoding/generation techniques, not separate LM Heads.

22. Why the LM Head Is Important

Without an LM Head, the Transformer produces internal representations but does not directly map them to the vocabulary.



The LM Head provides the final mapping:

Internal Representation
          ↓
Vocabulary Scores


This makes next-token prediction possible.



A useful mental model is:

Transformer:
"What information do I have about this position?"

LM Head:
"Given that information, how should I score every possible token?"


This is a simplified conceptual analogy, not a literal internal conversation.

23. Complete Architecture

A simplified decoder-only LLM can be viewed as:

                    Input Text
                        ↓
                   Tokenization
                        ↓
                    Token IDs
                        ↓
                 Token Embeddings
                        ↓
              Positional Information
                        ↓
        ┌───────────────────────────────┐
        │     Transformer Block 1       │
        │  Causal Self-Attention + FFN  │
        └───────────────────────────────┘
                        ↓
        ┌───────────────────────────────┐
        │     Transformer Block 2       │
        │  Causal Self-Attention + FFN  │
        └───────────────────────────────┘
                        ↓
                       ...
                        ↓
        ┌───────────────────────────────┐
        │     Transformer Block N       │
        │  Causal Self-Attention + FFN  │
        └───────────────────────────────┘
                        ↓
                Final Hidden States
                        ↓
              Language Modeling Head
                        ↓
                     Logits
                        ↓
                 Probability Distribution
                        ↓
                   Next Token


24. Important Distinction: Hidden State vs Logit

These are not the same thing.

Hidden State

A learned internal representation produced by the Transformer.



Example:

[768 values]


Logits

Scores assigned to vocabulary tokens by the LM Head.



Example:

[50,000 values]


So:

Hidden State
     ↓
   LM Head
     ↓
   Logits


The LM Head performs the mapping between them.

25. Important Distinction: Logits vs Probability

Another important distinction:

Logits
  ↓
Softmax
  ↓
Probabilities


Logits:

[2.4, 1.2, -0.5, 3.1]


Probabilities:

[0.30, 0.09, 0.02, 0.59]


Logits can be positive or negative and do not need to sum to 1.



Probabilities are non-negative and sum to approximately 1.

26. LM Head in Training vs Inference

Stage

LM Head Role

Training

Produces logits used to calculate next-token prediction loss

Inference

Produces logits used to select/sample the next token

Generation

Repeatedly converts current hidden representation into vocabulary scores

Training

Input
 ↓
Transformer
 ↓
LM Head
 ↓
Logits
 ↓
Loss
 ↓
Backpropagation
 ↓
Parameter Updates


Inference

Prompt
 ↓
Transformer
 ↓
LM Head
 ↓
Logits
 ↓
Token Selection
 ↓
New Token


27. Does the LM Head Contain the Model's Knowledge?

The LM Head alone should not be thought of as containing all the model's knowledge.



The model's learned behavior is distributed across its parameters, including:



Embedding parameters

Attention projections

Feed-forward layers

Normalization parameters

Output projection

Other architecture-specific parameters



The Transformer builds the representation, while the LM Head maps that representation to vocabulary scores.

28. Common Misunderstandings

❌ LM Head directly produces words

Not exactly.



It produces logits for vocabulary tokens.

LM Head → Logits → Token Selection


❌ Logits are probabilities

No.

Logits → Softmax → Probabilities


❌ The LM Head is the whole output system

Not necessarily.



The LM Head is the output projection stage. Generation also involves probability processing, token selection, detokenization, and stopping logic.

❌ The LM Head understands the text by itself

No.



The Transformer produces contextual representations. The LM Head maps those representations to vocabulary scores.

❌ Every LLM uses exactly the same LM Head

No.



Architectures and implementations can differ in details such as:



Bias usage

Weight tying

Output projection implementation

Vocabulary representation

Other architecture-specific choices



The general concept remains similar.

29. Simple Mental Model

Think of the Transformer as building a rich representation of the current context.



Then:

Transformer
    ↓
"Here is the representation of the current context."
    ↓
LM Head
    ↓
"Let's score every possible vocabulary token."
    ↓
Logits
    ↓
Probability Processing
    ↓
Next Token


The LM Head is therefore the bridge from the Transformer's internal representation to the model's vocabulary.

30. Complete Flow

The complete decoder-only language-modeling flow is:

Raw Text
   ↓
Tokenization
   ↓
Token IDs
   ↓
Token Embeddings
   ↓
Positional Information
   ↓
Transformer Blocks
   ↓
Final Hidden States
   ↓
Language Modeling Head
   ↓
Vocabulary Logits
   ↓
Probability Distribution
   ↓
Token Selection
   ↓
Next Token
   ↓
Append Token
   ↓
Repeat


31. Key Takeaways

🧠 The Language Modeling Head is the final projection stage of a language model.

🔢 It converts Transformer hidden states into vocabulary-sized logits.

📊 Logits are raw scores, not probabilities.

📈 Softmax can convert logits into a probability distribution.

🎯 The resulting distribution is used for next-token prediction.

🔄 During generation, this process repeats autoregressively.

🏋️ During training, logits are compared with target tokens to calculate loss.

🔗 The LM Head connects the Transformer's internal representations to the vocabulary.

🔤 Its output dimension is related to the model's vocabulary size.

🔧 Weight tying may optionally share parameters between token embeddings and the output projection.

⚠️ The LM Head does not independently contain or represent the whole model's learned behavior.

🚀 The simplified final path is:

Transformer
    ↓
Final Hidden State
    ↓
LM Head
    ↓
Logits
    ↓
Probabilities
    ↓
Next Token
