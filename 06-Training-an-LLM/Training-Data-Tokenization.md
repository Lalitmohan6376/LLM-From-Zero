🔤 Training Data Tokenization

Before an LLM can train on text, the text needs to be converted into a form that the model can process.



This process is called tokenization.



The basic flow is:

Training Data
     ↓
Text
     ↓
Tokenization
     ↓
Tokens
     ↓
Token IDs
     ↓
Training Sequences
     ↓
LLM Training


Tokenization connects prepared training data to the numerical input that the Transformer can process.

1. What Is Training Data Tokenization?

Training data tokenization is the process of converting training text into tokens and then into numerical token IDs.



For example:

Text:
"The cat is sleeping."


might become:

Tokens:
["The", " cat", " is", " sleeping", "."]


Then the tokenizer assigns an ID to each token:

Token IDs:
[101, 245, 37, 892, 13]


The exact tokens and IDs depend on the tokenizer.



The LLM does not directly receive the original text.



It receives numerical representations derived from the token IDs.

2. Why Is Tokenization Needed?

Neural networks operate on numerical data.



Raw text contains characters and words:

The cat is sleeping.


The model needs numbers:

[101, 245, 37, 892, 13]


So tokenization creates the bridge:

Human-readable text
        ↓
      Tokens
        ↓
    Token IDs
        ↓
 Numerical model input


3. Training Data Before Tokenization

Before tokenization, the training data has usually gone through preparation steps.



A simplified pipeline is:

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
Prepared Text
   ↓
Tokenization


This means tokenization is generally part of a larger data-processing pipeline.

4. Text Becomes Tokens

A tokenizer divides text into smaller units called tokens.



For example:

Input:
"I love machine learning."


A tokenizer might produce:

["I", " love", " machine", " learning", "."]


Another tokenizer could split the same text differently.



For example:

["I", " love", " machine", " learn", "ing", "."]


There is no single universal tokenization.



The result depends on the tokenizer and vocabulary.

5. Tokens Are Not Always Words

A common misunderstanding is:

One token = one word.

That is not necessarily true.



A token can be:

Word
Subword
Character
Punctuation
Number
Code fragment
Special token


For example:

"unbelievable"


could potentially be represented as:

["un", "believ", "able"]


The exact split depends on the tokenizer.

6. Subword Tokenization

Modern language models commonly use tokenization methods based on subword units or related approaches.



Subword tokenization provides a balance between:

Very large vocabulary
        ↕
Very long sequences


It allows common pieces to be reused across many words.



For example:

play
playing
played
player


may share token pieces depending on the tokenizer.



This can help the tokenizer handle words that are rare or not explicitly present as complete vocabulary entries.

7. Tokenizer Vocabulary

A tokenizer has a vocabulary containing the tokens it knows.



For example:

Vocabulary

ID      Token
----------------
0       <PAD>
1       <UNK>
2       the
3       cat
4       machine
5       learning
...


The actual vocabulary of a modern LLM can be much larger.



Each token has an associated numerical ID.

8. Token IDs

After tokenization, each token is converted into a numerical identifier.



Example:

Text:
"The cat sleeps."


Tokens:

["The", " cat", " sleeps", "."]


Token IDs:

[101, 245, 892, 13]


These numbers are identifiers, not semantic values.



For example:

Token ID 245


does not inherently mean:

"cat"


The tokenizer simply assigns that ID to a particular token.

9. Token IDs Are Tokenizer-Specific

Token IDs are not universal.



For example:

Tokenizer A

"cat" → 245


while:

Tokenizer B

"cat" → 781


Both can be correct.



The ID only has meaning within its tokenizer vocabulary.



Therefore:

Token ID numbers should not be compared across different tokenizers as if they represented universal meanings.

10. Special Tokens

Training data may also contain special tokens.



Examples include:

<PAD>
<UNK>
<BOS>
<EOS>
<SEP>
<MASK>


The exact special tokens depend on the tokenizer and model.



They can provide structural information to the model or training pipeline.



For example:

<BOS> The cat sleeps <EOS>


Here:

BOS → beginning of sequence
EOS → end of sequence


Not every LLM uses the same special tokens.

11. Tokenization of Long Text

Training documents can be much longer than the sequence length used for one training example.



For example:

Long Document
      ↓
Tokenization
      ↓
Thousands of Tokens
      ↓
Split into Training Sequences


A simplified example:

Token IDs:

[12, 45, 67, 89, 23, 91, 44, 76, 18, 55, ...]


may be divided into smaller sequences:

Sequence 1:
[12, 45, 67, 89]

Sequence 2:
[23, 91, 44, 76]

Sequence 3:
[18, 55, ...]


The exact sequence construction depends on the training setup.

12. Sequence Length

A training sequence contains a specific number of tokens.



For example:

Sequence length = 8

[12, 45, 67, 89, 23, 91, 44, 76]


The sequence length used during training can depend on:



Model architecture

Context-window configuration

Training stage

Hardware constraints

Training strategy



Sequence length is measured in tokens, not characters or words.

13. Tokenization and Context Window

The context window is also measured in tokens.



For example, if a model supports a context of:

8,192 tokens


the relevant input context is limited by that token count.



This is one reason tokenization matters.



The same text can produce different numbers of tokens with different tokenizers.



Therefore:

Same text
   ↓
Different tokenizer
   ↓
Potentially different token count


14. Training Data Tokenization Flow

The complete simplified flow is:

Prepared Training Text
          ↓
       Tokenizer
          ↓
        Tokens
          ↓
      Token IDs
          ↓
 Training Sequences
          ↓
      Input / Target
          ↓
         Batch
          ↓
       LLM Training


This is the bridge between text data and model training.

15. Tokenization Example

Consider:

"The cat is sleeping."


Step 1 — Original text

"The cat is sleeping."


Step 2 — Tokens

A tokenizer might produce:

["The", " cat", " is", " sleeping", "."]


Step 3 — Token IDs

Suppose the tokenizer maps them to:

[101, 245, 37, 892, 13]


These numbers are only illustrative.

Step 4 — Training sequence

[101, 245, 37, 892, 13]


Step 5 — Input and target

For next-token prediction:

Input:
[101, 245, 37, 892]

Target:
[245, 37, 892, 13]


The model learns to predict the next token at each position.

16. Why Input and Target Are Shifted

Suppose the token sequence is:

[The] [cat] [is] [sleeping]


The model can be trained using:

Input:
[The] [cat] [is]

Target:
[cat] [is] [sleeping]


This creates several training examples from one sequence:

The       → cat
The cat   → is
The cat is → sleeping


For a decoder-only LLM, causal masking prevents each position from using future tokens while making these predictions.

17. Tokenization Does Not Create Embeddings

Tokenization produces tokens and token IDs.



It does not itself create semantic embedding vectors.



The distinction is:

Text
 ↓
Tokenization
 ↓
Tokens
 ↓
Token IDs
 ↓
Embedding Lookup
 ↓
Vectors


For example:

Token ID:
245


can be used to look up a learned vector:

[0.12, -0.31, 0.48, ...]


The vector is an embedding.



The ID is simply an identifier.

18. Token IDs → Embeddings

After tokenization, the token IDs are passed to an embedding layer.



Conceptually:

Token IDs
    ↓
Embedding Matrix
    ↓
Token Embeddings


If:

Vocabulary size = V
Embedding dimension = D


the embedding matrix can be represented as:

V × D


Each token ID selects one row from this matrix.

19. Tokenization vs Embedding

Tokenization

Embedding

Converts text into tokens

Converts token IDs into vectors

Produces token IDs

Produces numerical vectors

Uses tokenizer vocabulary

Uses learned embedding parameters

Happens before model input

Provides model input representation

Token-level representation

Vector representation

A simplified pipeline is:

Text
 ↓
Tokenization
 ↓
Token IDs
 ↓
Embeddings
 ↓
Transformer


20. Tokenization During Training

During training, the process can be represented as:

Training Text
      ↓
Tokenization
      ↓
Token IDs
      ↓
Training Sequences
      ↓
Input / Target
      ↓
Batch
      ↓
Embeddings
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


Tokenization itself does not normally change the model's weights.



The training process updates the model parameters.

21. Is Tokenization Learned During Training?

The tokenizer and the language model are related but separate components.



A tokenizer may be trained or constructed before the main LLM training process.



For example:

Training Text
     ↓
Tokenizer Development
     ↓
Vocabulary + Tokenization Rules


Then:

Training Text
     ↓
Existing Tokenizer
     ↓
Token IDs
     ↓
LLM Training


Some tokenization algorithms learn their vocabulary or merge rules from text.



But this is different from the LLM learning its neural-network parameters.

22. BPE and Training Data

One common family of tokenization approaches is Byte-Pair Encoding (BPE).



A simplified idea is:

Initial Pieces
     ↓
Find Frequent Pairs
     ↓
Merge Pairs
     ↓
Build Vocabulary / Merge Rules
     ↓
Tokenize New Text


For example, frequent pieces might gradually be combined:

l + o
 ↓
lo

lo + w
 ↓
low


This is a simplified illustration.



Actual BPE implementations can differ, including the starting units and preprocessing rules.

23. Different Tokenizers Produce Different Training Inputs

Consider:

"I am learning transformers."


Tokenizer A might produce:

["I", " am", " learning", " transformers", "."]


Tokenizer B might produce:

["I", " am", " learn", "ing", " transform", "ers", "."]


Therefore:

Same Text
    ↓
Different Tokenizer
    ↓
Different Tokens
    ↓
Different Token IDs
    ↓
Different Model Input


This is one reason tokenizer design is an important part of an LLM system.

24. Token Count and Training Cost

Tokenization affects how much text becomes a sequence of tokens.



Suppose:

Document A → 1,000 tokens
Document B → 1,500 tokens


The number of tokens influences how much sequence data the model processes.



More tokens generally mean more computation during training.



For Transformer-based models, attention also has an important relationship with sequence length because attention compares positions across the sequence.



Therefore, efficient tokenization can matter for training efficiency.

25. Tokenization and Multilingual Text

Different languages can tokenize differently.



For example:

English:
"machine learning"


may require a certain number of tokens.



Another language may require a different number of tokens to represent a similar amount of information.



This can affect:

Token count
Sequence length
Training efficiency
Context usage


A multilingual tokenizer therefore needs to support the languages included in the model's training setup.

26. Tokenization and Code

Tokenizers can also process programming code.



For example:

def add(a, b):
    return a + b


can be split into tokens representing:

Keywords
Identifiers
Operators
Punctuation
Whitespace-related pieces


The exact tokenization depends on the tokenizer.



This allows language models trained on code to process programming languages using the same general token → ID pipeline.

27. Tokenization and Numbers

Numbers can also be split into multiple tokens.



For example:

2026


might be represented as:

["20", "26"]


or another tokenization.



The exact result depends on the tokenizer vocabulary.



Therefore:

One visible number does not necessarily correspond to one token.

28. Tokenization and Punctuation

Punctuation can also become tokens.



For example:

Hello, world!


could contain tokens representing:

Hello
,
world
!


or different combinations depending on the tokenizer.



Punctuation therefore contributes to token count.

29. Tokenization and Whitespace

Some tokenizers represent whitespace as part of a token.



For example:

["Hello", " world"]


Here, the second token includes the leading space.



This is one reason tokenization cannot always be understood simply as splitting text on spaces.

30. Special Tokens in Training

Special tokens can help represent sequence boundaries or other structure.



For example:

<BOS> The cat is sleeping <EOS>


could become:

[1, 101, 245, 37, 892, 2]


where:

1 → <BOS>
2 → <EOS>


The actual IDs and special-token design depend on the tokenizer/model.

31. Padding

When multiple sequences have different lengths, some training systems use padding.



For example:

Sequence 1:
[12, 45, 67, 89]

Sequence 2:
[34, 91]

Sequence 3:
[72, 18, 44]


They may be padded to the same length:

[12, 45, 67, 89]
[34, 91, PAD, PAD]
[72, 18, 44, PAD]


A padding mask can then prevent padding positions from being treated as normal content.



However, training pipelines do not all handle padding in exactly the same way.

32. Tokenization and Batches

After tokenization and sequence construction, examples can be grouped into batches.

Tokenized Data
      ↓
Sequences
      ↓
Batch 1
Batch 2
Batch 3
...


For example:

Batch 1

Sequence 1 → [12, 45, 67, 89]
Sequence 2 → [34, 91, 20, 55]
Sequence 3 → [72, 18, 44, 31]


The batch is then processed by the model.

33. Tokenization Is Usually Deterministic

For a fixed tokenizer and configuration, the same input text will normally produce the same tokenization.



For example:

Input:
"The cat"


with a fixed tokenizer:

"The cat"
   ↓
["The", " cat"]
   ↓
[101, 245]


The result is normally reproducible.



The tokenizer does not randomly decide a different tokenization every time under ordinary deterministic operation.

34. Tokenization vs Text Chunking

These are different processes.

Tokenization

Converts text into tokens:

Text
 ↓
Tokens


Chunking

Divides tokenized data into training sequences:

Many Tokens
 ↓
Sequence 1
Sequence 2
Sequence 3
...


Together:

Text
 ↓
Tokenization
 ↓
Long Token Sequence
 ↓
Chunking / Sequence Construction
 ↓
Training Sequences


35. Complete Training Data Tokenization Pipeline

The complete process can be visualized as:

┌─────────────────────────┐
│     Prepared Text       │
└────────────┬────────────┘
             ↓
┌─────────────────────────┐
│        Tokenizer        │
└────────────┬────────────┘
             ↓
┌─────────────────────────┐
│         Tokens          │
└────────────┬────────────┘
             ↓
┌─────────────────────────┐
│       Token IDs         │
└────────────┬────────────┘
             ↓
┌─────────────────────────┐
│ Sequence Construction   │
└────────────┬────────────┘
             ↓
┌─────────────────────────┐
│    Input / Target       │
└────────────┬────────────┘
             ↓
┌─────────────────────────┐
│         Batches         │
└────────────┬────────────┘
             ↓
┌─────────────────────────┐
│     Embedding Layer     │
└────────────┬────────────┘
             ↓
┌─────────────────────────┐
│   Transformer Training  │
└─────────────────────────┘


36. Training Data Tokenization vs Inference Tokenization

Tokenization happens in both training and inference.

During training

Training Text
     ↓
Tokenizer
     ↓
Token IDs
     ↓
Training Sequences
     ↓
Model


During inference

User Prompt
     ↓
Tokenizer
     ↓
Token IDs
     ↓
Model
     ↓
Generated Token
     ↓
Tokenizer Decoder
     ↓
Text


The important difference is what happens after tokenization.



During training, the tokenized data is used to calculate loss and update parameters.



During inference, tokenized input is used to generate output without normally updating the model parameters.

37. Detokenization

The reverse process is often called detokenization or decoding.



For example:

Token IDs
   ↓
Tokens
   ↓
Text


Example:

[101, 245, 37, 892]
        ↓
["The", " cat", " is", " sleeping"]
        ↓
"The cat is sleeping"


The exact process depends on the tokenizer.

38. Complete Text-to-Training Flow

Putting everything together:

                    Training Data
                         ↓
                   Prepared Text
                         ↓
                     Tokenizer
                         ↓
                       Tokens
                         ↓
                     Token IDs
                         ↓
                Sequence Construction
                         ↓
                   Input / Target
                         ↓
                       Batches
                         ↓
                  Embedding Lookup
                         ↓
               Positional Information
                         ↓
              Decoder-Only Transformer
                         ↓
                  Next-Token Logits
                         ↓
                       Loss
                         ↓
                  Backpropagation
                         ↓
                 Parameter Updates


This is the connection between the training dataset and the learning process.

39. Common Misunderstandings

❌ "Tokenization means splitting every sentence into words."

No.



Tokens can be words, subwords, punctuation, characters, code pieces, or special tokens.

❌ "Every word is one token."

No.



A word can be one token or multiple tokens.

❌ "Token IDs contain the meaning of the token."

No.



Token IDs are identifiers assigned by the tokenizer.

❌ "Tokenization creates embeddings."

No.



Tokenization produces tokens and IDs.



Embedding lookup converts IDs into vectors.

❌ "All LLMs use the same tokenizer."

No.



Different models can use different tokenizers and vocabularies.

❌ "Tokenization is the same as chunking."

No.



Tokenization converts text into tokens.



Chunking or sequence construction organizes those tokens into training examples.

❌ "The tokenizer learns the same things as the LLM."

No.



Tokenizer construction and LLM parameter training are separate processes.

40. Simple Mental Model 🧠

Think of tokenization as translating human language into a form the model can process.

Human Text
    ↓
Tokenizer
    ↓
Small Pieces
    ↓
Token IDs
    ↓
Vectors
    ↓
Transformer


The important distinction is:

Text
 ↓
Tokens
 ↓
Token IDs
 ↓
Embeddings
 ↓
Transformer


Each stage has a different job.

41. Key Takeaways 📌

🔤 Tokenization converts training text into tokens.

🔢 Tokens are converted into token IDs.

🧩 A token can be a word, subword, punctuation mark, code piece, number, or special token.

📚 Modern LLMs commonly use subword-based or related tokenization approaches.

🆔 Token IDs are tokenizer-specific identifiers, not semantic meanings.

📖 A tokenizer has a vocabulary containing its available tokens.

✂️ Long tokenized data is organized into training sequences.

🎯 Input and target sequences are shifted for next-token prediction.

📦 Training sequences are grouped into batches.

🧠 Token IDs are converted into embeddings before entering the Transformer.

🔄 Tokenization is different from embedding and sequence chunking.

🌍 Different tokenizers can produce different token counts for the same text.

⚙️ Tokenization affects sequence length, context usage, and training computation.

🔁 During inference, generated token IDs are eventually decoded back into text.



The core flow is:

Training Text
      ↓
Tokenization
      ↓
Tokens
      ↓
Token IDs
      ↓
Training Sequences
      ↓
Input / Target
      ↓
Batches
      ↓
Embeddings
      ↓
Transformer
      ↓
Next-Token Prediction
      ↓
Loss
      ↓
Parameter Updates
