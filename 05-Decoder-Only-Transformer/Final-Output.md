📤 Final Output

📌 Introduction

After the input passes through all Transformer Blocks in a decoder-only LLM, the model has a final hidden representation.



This representation is not yet a predicted word or token.



It must pass through the Language Model Head to produce scores for the vocabulary.



The simplified flow is:

Input Text
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
Final Hidden States
    ↓
Language Model Head
    ↓
Logits
    ↓
Probability Distribution
    ↓
Next Token


The final output stage converts the internal representation produced by the Transformer into something that can be used for next-token prediction.

1. 🧠 What Is the Final Output?

The final output of the Transformer stack is a set of hidden representations.



For a sequence of tokens:

The | cat | is | sleeping


the Transformer produces a representation for each position.



Conceptually:

The       → Vector
cat       → Vector
is        → Vector
sleeping  → Vector


These vectors are called hidden states or hidden representations.



They contain information produced by the Transformer layers.

2. 📦 Final Hidden States

Suppose:

Batch Size = B
Sequence Length = N
Hidden Dimension = D


The final hidden-state tensor can be represented as:

[B, N, D]


For example:

[2, 128, 768]


means:

2   → sequences in the batch
128 → tokens per sequence
768 → hidden features per token


The exact dimensions depend on the model.

3. 🔄 Final Transformer Block Output

The final Transformer Block produces:

Final Hidden States


The architecture can be viewed as:

Embedding
    ↓
Block 1
    ↓
Block 2
    ↓
Block 3
    ↓
...
    ↓
Block N
    ↓
Final Hidden States


At this point, the model has processed the sequence through the entire Transformer stack.



But it has not yet produced vocabulary scores.

4. ❓ Are Hidden States the Final Prediction?

No.



This is an important distinction.



The final hidden states are internal representations.



They are not directly:

"cat"
"dog"
"sleeping"


Instead:

Final Hidden State
        ↓
Language Model Head
        ↓
Vocabulary Scores
        ↓
Next Token


So:

Final Hidden State ≠ Final Token


5. 🎯 Language Model Head

The final hidden representation is passed through a Language Model Head, often implemented as a linear projection to the vocabulary size.



Conceptually:

Final Hidden State
        ↓
Linear Projection
        ↓
Vocabulary Logits


If the vocabulary contains:

50,000 tokens


then the output layer can produce approximately:

50,000 logits


for a prediction position.

6. 📊 From Hidden State to Logits

Suppose one token position has a hidden representation:

h


The language model head applies a learned projection:

z = hW + b


where:

h = hidden representation
W = output projection weights
b = bias, if used
z = logits


The resulting vector has one score for each vocabulary token.



For example:

Vocabulary:

cat       → 1.2
dog       → 3.4
sleeping  → 5.7
running   → 2.1
...


These values are logits.

7. 🔢 What Are Logits?

A logit is a raw numerical score produced by the output layer.



Logits are not probabilities.



For example:

cat        → 1.2
dog        → 3.4
sleeping   → 5.7
running    → 2.1


The larger score indicates that the model assigns a higher relative preference to that token before probability conversion.



But:

5.7 ≠ 57% probability


Logits must be converted into a probability distribution.

8. 🎲 Logits to Probabilities

Softmax can convert logits into probabilities.



Conceptually:

Logits
  ↓
Softmax
  ↓
Probabilities


For example:

cat        → 0.05
dog        → 0.12
sleeping   → 0.73
running    → 0.10


The probabilities sum to approximately:

1.0


The probability distribution covers the model's vocabulary.

9. 📐 Softmax

For logits:

z₁, z₂, z₃, ..., zᵥ


softmax produces:

P(i) = exp(zᵢ) / Σ exp(zⱼ)


where:

P(i) = probability of token i


The output probabilities are positive and sum to 1.



In practical generation systems, logits may first be modified by techniques such as temperature or filtered using top-k/top-p before the final token is selected.

10. 🧠 Which Hidden State Is Used?

For autoregressive generation, the model generally uses the representation at the current prediction position, typically the last relevant position in the sequence.



For example:

Input:

The cat is


The model processes the sequence and uses the relevant final-position representation to predict:

sleeping


Conceptually:

The     → Hidden State
cat     → Hidden State
is      → Hidden State
                 ↓
        Current Prediction Position
                 ↓
              Logits
                 ↓
            Next Token


During training, logits can be produced for multiple sequence positions simultaneously.

11. 🏋️ Final Output During Training

During training, the model usually predicts the next token at many positions in parallel.



Example:

Input:

The | cat | is | sleeping


The targets are shifted:

Target:

cat | is | sleeping | ...


The model can produce logits for multiple positions:

Position 1 → Predict "cat"
Position 2 → Predict "is"
Position 3 → Predict "sleeping"


The predicted distributions are compared with the target tokens to calculate the loss.

12. 🚀 Final Output During Inference

During generation, the process is different.



Suppose the prompt is:

"The cat is"


The model produces a probability distribution for the next token.



For example:

sleeping → 0.65
running  → 0.15
eating   → 0.10
sitting  → 0.05
other    → 0.05


Suppose:

sleeping


is selected.



The sequence becomes:

"The cat is sleeping"


Then the model generates another token.

13. 🔁 Autoregressive Final Output

The final output stage participates in a loop:

Context
   ↓
Transformer Stack
   ↓
Final Hidden State
   ↓
Language Model Head
   ↓
Logits
   ↓
Probability Distribution
   ↓
Select Next Token
   ↓
Add Token to Context
   ↓
Run Again


For example:

"The weather is"
        ↓
"beautiful"
        ↓
"The weather is beautiful"
        ↓
"today"
        ↓
"The weather is beautiful today"


The model repeats this process until generation stops.

14. 🧩 Complete Final-Output Pipeline

The final stages of a decoder-only LLM are:

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
Final Hidden States
       ↓
Language Model Head
       ↓
Logits
       ↓
Temperature / Sampling / Filtering
       ↓
Probability Distribution
       ↓
Next Token


Not every system applies all decoding operations in exactly this order, but the core prediction flow is based on the logits produced by the language model head.

15. 🔍 Why Does the Model Need an Output Layer?

The Transformer hidden dimension and vocabulary size are different concepts.



For example:

Hidden Dimension = 768
Vocabulary Size  = 50,000


The Transformer produces:

768-dimensional representation


But the model needs to choose from:

50,000 possible tokens


The language model head performs this mapping:

768-dimensional representation
             ↓
       Output Projection
             ↓
      50,000 vocabulary logits


This allows the model to score every vocabulary token.

16. 🧠 Output Projection

The output projection can be represented as:

Hidden State
     ↓
    W
     ↓
Vocabulary Logits


If:

h ∈ ℝᴰ


and the vocabulary size is:

V


then the output is approximately:

z ∈ ℝⱽ


So the transformation is:

D-dimensional hidden state
          ↓
V-dimensional logits


17. 🔗 Weight Tying

Some language models use weight tying.



This means the token embedding matrix and output projection weights can share parameters.



Conceptually:

Token Embedding Matrix
        ↕
Shared Parameters
        ↕
Output Projection


This is an architectural choice, not a requirement.



Therefore:

Weight Tying = Optional


Different models can use different designs.

18. 📦 Shape of the Final Output

Suppose:

Batch Size = 2
Sequence Length = 128
Vocabulary Size = 50,000


The logits during training can have a shape like:

[2, 128, 50,000]


This means:

2      → sequences
128    → positions
50,000 → vocabulary scores


During autoregressive inference, a system typically uses the logits for the current/last relevant position to select the next token.



Exact implementation details vary.

19. 📊 Hidden State vs Logits vs Probability

These three are different.

Representation

Meaning

Hidden State

Internal learned representation

Logits

Raw scores for vocabulary tokens

Probability

Normalized distribution over vocabulary tokens

The flow is:

Hidden State
     ↓
Language Model Head
     ↓
Logits
     ↓
Softmax / Decoding Processing
     ↓
Probabilities


20. 🧠 Hidden State Is Not a Word

Suppose the model produces:

[0.12, -0.45, 1.23, 0.87, ...]


This vector is not directly:

"sleeping"


It is an internal numerical representation.



The output layer converts that representation into scores over the vocabulary.

21. 🔄 Final Output in the Complete LLM

The complete architecture can now be seen as:

                     Text
                      ↓
                 Tokenization
                      ↓
                   Token IDs
                      ↓
                Token Embeddings
                      ↓
             Positional Information
                      ↓
              Transformer Block 1
                      ↓
              Transformer Block 2
                      ↓
                      ...
                      ↓
              Transformer Block N
                      ↓
              Final Hidden States
                      ↓
               Language Model Head
                      ↓
                    Logits
                      ↓
               Probability Distribution
                      ↓
                 Next Token


The final output stage connects the internal Transformer representations to the vocabulary.

22. 🎯 Example

Suppose the prompt is:

"Machine learning is"


After tokenization:

Machine | learning | is


The sequence passes through the Transformer stack.



The final representation at the relevant position is:

Final Hidden State


The language model head produces:

Token        Logit
-------------------
powerful     2.1
useful       3.7
important    2.9
fun          1.2
...


After probability conversion:

useful       → 0.42
important    → 0.25
powerful     → 0.18
fun          → 0.05
...


Suppose the model selects:

useful


The generated text becomes:

"Machine learning is useful"


The model can then continue predicting the next token.

23. 🛑 When Does Generation Stop?

The model does not necessarily generate forever.



Generation can stop because of:

End-of-Sequence Token

The model may generate a special end token.

<EOS>


Maximum Token Limit

The system may stop after reaching a configured generation limit.

Application-Level Stopping Rule

An application can stop generation based on its own rules.



For example:

Stop when:
"###"


The exact stopping behavior depends on the model and generation system.

24. 🎲 Token Selection

After obtaining logits, the system needs to choose the next token.



Possible approaches include:

Greedy Decoding

Choose the highest-scoring token.

Highest probability
       ↓
    Next Token


Temperature

Adjust the sharpness of the distribution.

Top-K Sampling

Keep only the top K candidates.

Top-P Sampling

Keep the smallest group of tokens whose cumulative probability reaches a chosen threshold.



These are decoding strategies, not additional Transformer Blocks.

25. ⚠️ Common Misunderstandings

❌ "The final Transformer Block directly outputs a word."

No.



It produces hidden representations.

Final Block
   ↓
Hidden States
   ↓
Language Model Head
   ↓
Logits
   ↓
Next Token


❌ "Logits are probabilities."

No.



Logits are raw scores.



They can be converted into probabilities using softmax.

❌ "The model always chooses the token with the highest probability."

Not necessarily.



Greedy decoding does this, but sampling-based methods can select another token according to the configured strategy.

❌ "The entire vocabulary is generated as output."

No.



The model produces scores over the vocabulary, and the generation system selects a token from that distribution.

❌ "Every position is ignored except the last position during training."

No.



During training, the model can produce predictions for many positions in parallel.



During autoregressive inference, the current/last relevant position is typically used to generate the next token.

❌ "The output layer is the same thing as the Transformer."

No.



The Transformer produces hidden representations.



The output layer maps those representations to vocabulary logits.

26. 🗺️ Final Output Mental Model

The easiest way to remember this stage is:

Final Transformer Block
          ↓
   "What does this
    representation contain?"
          ↓
   Language Model Head
          ↓
   "How strongly does
    each vocabulary token
    fit as the next token?"
          ↓
        Logits
          ↓
     Probabilities
          ↓
     Token Selection
          ↓
      Next Token


27. 🔗 Complete Decoder-Only Flow

Putting everything together:

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
            ┌──────────────────────┐
            │ Transformer Block 1  │
            └──────────────────────┘
                        ↓
            ┌──────────────────────┐
            │ Transformer Block 2  │
            └──────────────────────┘
                        ↓
                        ...
                        ↓
            ┌──────────────────────┐
            │ Transformer Block N  │
            └──────────────────────┘
                        ↓
               Final Hidden States
                        ↓
                Language Model Head
                        ↓
                      Logits
                        ↓
               Decoding / Softmax
                        ↓
                   Next Token
                        ↓
                Add to Context
                        ↓
                     Repeat


This is the bridge between the Transformer stack and text generation.

28. 🧠 One-Line Definition

The final output stage of a decoder-only LLM takes the final hidden representations from the Transformer stack, projects them to vocabulary logits, and uses those scores to predict the next token.

29. 🎯 Key Takeaways

📤 The final Transformer Block produces hidden representations, not words.

🧠 These hidden representations contain the information produced by the Transformer stack.

🔗 A Language Model Head maps the hidden representation to vocabulary-sized logits.

📊 Logits are raw scores, not probabilities.

🎲 Softmax can convert logits into a probability distribution.

🎯 The generation system uses the resulting distribution to select the next token.

🔁 The selected token is added to the sequence and the process repeats.

🏋️ During training, predictions can be produced for many positions in parallel.

🚀 During autoregressive inference, the current/last relevant position is typically used to generate the next token.

⚡ KV caching can make repeated inference more efficient.

🧩 Weight tying between embeddings and output projection is possible but optional.

🛑 Generation can stop because of an end token, token limit, or application-defined stopping rule.



The complete final stage is:

Final Hidden States
        ↓
Language Model Head
        ↓
Logits
        ↓
Probability Distribution
        ↓
Token Selection
        ↓
Next Token
        ↓
Generated Text
