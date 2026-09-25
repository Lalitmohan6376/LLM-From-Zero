# 📍 Positional Information

Transformers process token representations using attention, but attention by itself does not automatically provide the model with the order of tokens.

For language, **order matters**.

For example:

```text
The dog chased the cat.
```

is different from:

```text
The cat chased the dog.
```

The same words can have different meanings when their positions change.

**Positional Information** gives the Transformer information about where tokens occur in a sequence.

---

# 1. Why Is Positional Information Needed?

Consider:

```text
The cat eats fish.
```

The model needs to distinguish:

```text
The   → Position 1
cat   → Position 2
eats  → Position 3
fish  → Position 4
```

Without information about position, the model would have difficulty representing the difference between:

```text
The cat eats fish.
```

and:

```text
Fish eats the cat.
```

The tokens are related, but their order is different.

Therefore:

```text
Token Information
        +
Position Information
        ↓
Richer Input Representation
```

---

# 2. The Transformer and Token Order

A Transformer processes a sequence of token representations.

For example:

```text
The   cat   is   sleeping
 ↓     ↓     ↓      ↓
T₁    T₂    T₃     T₄
```

Each token has:

* Token identity
* Position in the sequence

Conceptually:

```text
🧩 Token Representation
          +
📍 Position
          ↓
🤖 Transformer Input
```

The exact way position is represented depends on the Transformer architecture.

---

# 3. Token Information vs Position Information

These are two different types of information.

### Token Information

Answers:

> **What token is this?**

For example:

```text
cat
```

is represented by its token ID and token embedding.

### Position Information

Answers:

> **Where does this token occur?**

For example:

```text
cat → Position 2
```

So:

```text
🔤 Token
   ↓
"What is this?"

📍 Position
   ↓
"Where is it?"
```

Both can contribute to the model's representation of a sequence.

---

# 4. Positions in a Sequence

Suppose the sequence is:

```text
The cat is sleeping
```

We can conceptually assign positions:

```text
Token       Position

The         0
cat         1
is          2
sleeping    3
```

Some systems or explanations may number positions starting from `1` instead.

The important idea is not whether numbering starts at `0` or `1`.

The important idea is:

> **Each token has a position in the sequence.**

---

# 5. Token Embedding + Position

A traditional way to provide positional information is to combine token embeddings with position representations.

Conceptually:

```text
Token Embedding
      +
Position Representation
      ↓
Transformer Input
```

For example:

```text
"The"
  ↓
Token Embedding
  +
Position 0
  ↓
Input Representation
```

```text
"cat"
  ↓
Token Embedding
  +
Position 1
  ↓
Input Representation
```

And so on.

The exact mechanism varies across architectures.

---

# 6. Why Token IDs Are Not Enough

Suppose:

```text
The → 101
cat → 205
```

The Token ID `101` identifies the token `"The"`.

But it does not tell the model whether `"The"` appears:

```text
Position 0
```

or:

```text
Position 20
```

Therefore:

```text
Token ID
   ↓
Identifies the token

Position
   ↓
Identifies where the token occurs
```

These are different pieces of information.

---

# 7. Why Order Matters in Language

Consider:

```text
Dog bites man.
```

and:

```text
Man bites dog.
```

The same words are present, but the order changes the meaning.

Another example:

```text
I only ate the cake.
```

and:

```text
Only I ate the cake.
```

Changing positions can change the meaning or emphasis.

Therefore, an LLM needs some way to represent sequence position.

---

# 8. Different Ways to Represent Position

There is not one universal positional-information method.

Common approaches include:

```text
📍 Positional Information
        ↓
 ┌──────┼──────────────┐
 ↓      ↓              ↓
Learned  Sinusoidal    RoPE
Position Encoding
```

Three important examples are:

1. **Learned positional embeddings**
2. **Sinusoidal positional encoding**
3. **Rotary Position Embeddings (RoPE)**

Modern architectures can also use other position-aware mechanisms.

---

# 9. Learned Positional Embeddings

One approach is to learn a vector for each position.

For example:

```text
Position 0 → Position Vector 0
Position 1 → Position Vector 1
Position 2 → Position Vector 2
Position 3 → Position Vector 3
```

These vectors are learned during training.

Conceptually:

```text
Position
   ↓
Position Embedding
   ↓
Learned Representation
```

Then the position representation can be combined with the token embedding.

For example:

```text
Token Embedding
      +
Position Embedding
      ↓
Input Representation
```

---

# 10. Example of Learned Positional Embeddings

Suppose:

```text
"The" → Position 0
"cat" → Position 1
"eats" → Position 2
```

The model may have learned:

```text
Position 0 → [0.12, 0.41, ...]
Position 1 → [0.32, 0.18, ...]
Position 2 → [0.51, 0.27, ...]
```

These numbers are illustrative.

The model learns useful positional representations during training.

---

# 11. Sinusoidal Positional Encoding

The original Transformer introduced **sinusoidal positional encoding**.

Instead of learning a separate position vector, mathematical sine and cosine functions are used to create position-dependent representations.

Conceptually:

```text
Position
   ↓
Mathematical Functions
   ↓
Sine + Cosine Values
   ↓
Position Representation
```

A simplified idea is:

```text
Position 0 → [sin(...), cos(...), sin(...), cos(...)]
Position 1 → [sin(...), cos(...), sin(...), cos(...)]
Position 2 → [sin(...), cos(...), sin(...), cos(...)]
```

The actual formula uses different frequencies across dimensions.

---

# 12. Why Use Sine and Cosine?

The sinusoidal functions create structured patterns that vary with position.

This allows the representation to change systematically as the position changes.

Conceptually:

```text
Position
   ↓
0 → Pattern A
1 → Pattern B
2 → Pattern C
3 → Pattern D
...
```

The original Transformer used this approach to provide positional information without learning a separate position embedding for every position.

---

# 13. Rotary Position Embeddings (RoPE)

**RoPE** stands for **Rotary Position Embeddings**.

It is a different approach to representing positional information.

Instead of simply adding a position vector to token embeddings, RoPE incorporates position information into the attention computation by applying position-dependent rotations to Query and Key representations.

Conceptually:

```text
Query
  +
Position
  ↓
Rotated Query

Key
  +
Position
  ↓
Rotated Key
```

Then attention is calculated using these position-aware representations.

RoPE is used by many modern Transformer-based language models.

---

# 14. Learned Positions vs Sinusoidal vs RoPE

| Method                        | Basic Idea                                                               |
| ----------------------------- | ------------------------------------------------------------------------ |
| Learned Positional Embeddings | Learn a representation for each position                                 |
| Sinusoidal Encoding           | Generate position representations using sine/cosine functions            |
| RoPE                          | Incorporate position into attention through position-dependent rotations |

The important point is:

> **Different Transformer architectures can represent positional information in different ways.**

There is no single positional method used by every LLM.

---

# 15. Absolute vs Relative Position

Positional methods can also be understood as **absolute** or **relative** approaches.

### Absolute Position

Represents the position itself.

For example:

```text
Token A → Position 5
Token B → Position 6
```

The model receives information about the individual positions.

### Relative Position

Focuses more on the relationship between positions.

For example:

```text
Token A is 2 positions before Token B.
```

This represents the distance or relationship between tokens.

Different architectures implement positional information differently.

---

# 16. Positional Information and Attention

Attention calculates relationships between token representations.

For example:

```text
Q × K
```

produces attention scores.

Position information can help the model distinguish relationships such as:

```text
nearby tokens
```

from:

```text
distant tokens
```

and can help distinguish the same tokens appearing in different positions.

Conceptually:

```text
Token Representations
        +
Position Information
        ↓
Position-Aware Representations
        ↓
Attention
        ↓
Contextual Representations
```

With methods such as RoPE, positional information is incorporated more directly into the attention computation rather than simply added to the input embeddings.

---

# 17. What Happens Without Positional Information?

Suppose the input is:

```text
The cat eats fish.
```

The model needs to represent:

```text
The → before cat
cat → before eats
eats → before fish
```

If there is no mechanism that provides sequence-order information, the model has much less information about the ordering of tokens.

This is especially important because self-attention itself allows tokens to interact based on their representations.

Therefore:

```text
Self-Attention
        +
Position Information
        ↓
Sequence-Aware Processing
```

---

# 18. Positional Information Is Not Token Meaning

A position representation does not tell the model:

```text
Position 2 = "cat"
```

The token embedding provides information associated with the token.

The positional mechanism provides information about its location or positional relationship.

So:

```text
🧩 Token Embedding
→ Token-related information

📍 Positional Information
→ Position-related information
```

They serve different purposes.

---

# 19. Positional Information Is Not the Token ID

These are also different.

For example:

```text
"cat" → Token ID 205
```

This tells the tokenizer/model which vocabulary entry is being referenced.

But:

```text
Position = 3
```

tells where that token occurs in the current sequence.

Therefore:

```text
Token ID ≠ Position
```

---

# 20. A Simple Example

Consider:

```text
The cat sleeps.
```

Conceptually:

```text
Token       Token Information       Position

The         🧩 Embedding            📍 0
cat         🧩 Embedding            📍 1
sleeps      🧩 Embedding            📍 2
```

These two types of information can then contribute to the Transformer input:

```text
"The"    → Token Information + Position Information
"cat"    → Token Information + Position Information
"sleeps" → Token Information + Position Information
```

The exact combination depends on the positional method.

---

# 21. Traditional Input Representation

With a learned or sinusoidal positional representation, a simplified formulation is:

```text
Input Representation
=
Token Embedding
+
Position Representation
```

For each token:

```text
Xᵢ = E(tokenᵢ) + Pᵢ
```

where:

```text
E(tokenᵢ) → Token Embedding
Pᵢ         → Position Representation
Xᵢ         → Input Representation
```

This is a simplified representation of architectures that combine position and token embeddings this way.

Not every modern architecture uses this exact formulation.

---

# 22. Positional Information Through the Transformer

After positional information has been incorporated, the representations enter the Transformer blocks.

Conceptually:

```text
📝 Text
   ↓
🔤 Tokenization
   ↓
🔢 Token IDs
   ↓
🧩 Token Embeddings
   ↓
📍 Positional Information
   ↓
🔄 Transformer Block
   ↓
🔄 Transformer Block
   ↓
🔄 Transformer Block
   ↓
📊 Final Representation
```

The model can now process token relationships while retaining information about sequence position.

---

# 23. Positional Information and Contextual Representations

Before attention:

```text
Token Embedding
+
Position Information
```

After attention and other Transformer operations:

```text
Contextual Representation
```

For example:

```text
Token
  ↓
Token Embedding
  ↓
Position Information
  ↓
Self-Attention
  ↓
Feed-Forward Network
  ↓
Contextual Representation
```

The contextual representation contains information influenced by the surrounding sequence.

---

# 24. Position and Sequence Length

Positions are tied to the sequence.

For example:

```text
Sequence:

The cat is sleeping
```

has four token positions:

```text
0   1   2   3
↓   ↓   ↓   ↓
The cat  is sleeping
```

If another token is added:

```text
The cat is sleeping peacefully
```

there is now another position:

```text
0   1   2   3   4
```

Therefore, positional information is closely related to sequence length.

---

# 25. Positional Information During Training

During training, token sequences are converted into representations that include or otherwise incorporate positional information.

Simplified flow:

```text
📚 Training Text
      ↓
🔤 Tokenization
      ↓
🔢 Token IDs
      ↓
🧩 Token Embeddings
      ↓
📍 Position Information
      ↓
🔄 Transformer
      ↓
🎯 Next-Token Prediction
      ↓
📉 Loss
      ↓
🔄 Backpropagation
```

The positional mechanism itself may contain learned parameters depending on the architecture.

---

# 26. Positional Information During Inference

During text generation, the model also needs positional information for the tokens in the current context.

For example:

```text
The cat is
```

The model needs to know the positions of:

```text
The → 0
cat → 1
is  → 2
```

When a new token is generated:

```text
The cat is sleeping
```

the new token occupies the next position.

The exact implementation depends on the positional method and inference architecture.

---

# 27. Positional Information and Causal Attention

In decoder-only LLMs, positional information works together with causal self-attention.

```text
🧩 Token Representations
          ↓
📍 Position Information
          ↓
🔑 Query, Key, Value
          ↓
📊 Attention Scores
          ↓
🎭 Causal Mask
          ↓
🎲 Softmax
          ↓
🎯 Attention Output
```

The causal mask determines which positions are allowed to interact.

Positional information provides information about position and positional relationships.

These are different mechanisms.

```text
📍 Position
   ↓
Where / relative position?

🎭 Mask
   ↓
Which positions are allowed?
```

---

# 28. Positional Information vs Attention Masking

These concepts are often confused.

| Positional Information                                   | Attention Masking                                  |
| -------------------------------------------------------- | -------------------------------------------------- |
| Provides position-related information                    | Restricts attention connections                    |
| Helps represent token order                              | Controls which positions may interact              |
| Can use learned vectors, sinusoidal encoding, RoPE, etc. | Can use causal, padding, or other masks            |
| Does not simply mean allowed/blocked                     | Represents allowed/blocked attention relationships |
| Part of position-aware processing                        | Applied to attention scores                        |

Simple distinction:

```text
📍 Position Information
        ↓
"Where are the tokens?"

🎭 Attention Mask
        ↓
"Which tokens can attend to which?"
```

---

# 29. Positional Information vs Token Embeddings

| Token Embeddings                                                             | Positional Information                          |
| ---------------------------------------------------------------------------- | ----------------------------------------------- |
| Represents token-related information                                         | Represents position-related information         |
| Obtained from token IDs through an embedding lookup in typical architectures | Generated or learned using a positional method  |
| Example: `"cat"`                                                             | Example: position `3`                           |
| Provides token representation                                                | Provides sequence-order information             |
| Learned in typical embedding layers                                          | May be learned or fixed depending on the method |

Together, they can form a position-aware input representation.

---

# 30. Positional Information vs Contextual Representation

These are also different.

### Positional Information

Provides information about position.

```text
📍 Position
```

### Contextual Representation

Produced after Transformer processing and influenced by surrounding tokens.

```text
🧠 Context + Token + Position
        ↓
📊 Contextual Representation
```

Simplified:

```text
Token Embedding
      +
Position Information
      ↓
Transformer
      ↓
Contextual Representation
```

---

# 31. Positional Information in Multi-Head Attention

Multi-Head Attention uses multiple attention heads.

Each head calculates relationships between token representations.

Position information can influence these relationships.

For example:

```text
Input
 ↓
Position-Aware Representation
 ↓
┌────────┬────────┬────────┐
↓        ↓        ↓
Head 1   Head 2   Head 3 ... Head N
↓        ↓        ↓
Attention Patterns
```

With RoPE, positional information is incorporated directly into the Query and Key representations used by attention.

Therefore, the exact way position enters Multi-Head Attention depends on the architecture.

---

# 32. Absolute Position Example

Suppose:

```text
The cat is sleeping
```

with positions:

```text
The       → 0
cat       → 1
is        → 2
sleeping  → 3
```

An absolute positional method represents these individual positions.

Conceptually:

```text
Position 0
Position 1
Position 2
Position 3
```

The model can use this information while processing the sequence.

---

# 33. Relative Position Example

Suppose:

```text
The cat is sleeping
```

and consider:

```text
cat
```

and:

```text
sleeping
```

Their positions are:

```text
cat       → 1
sleeping  → 3
```

Their relative distance is:

```text
3 - 1 = 2
```

A relative-position approach focuses on relationships such as:

```text
"How far apart are these positions?"
```

Different architectures implement relative position differently.

---

# 34. RoPE at a High Level

RoPE can be understood at a high level as making Query and Key representations position-aware through rotations.

Simplified:

```text
Query
  ↓
Position-Dependent Rotation
  ↓
Position-Aware Query

Key
  ↓
Position-Dependent Rotation
  ↓
Position-Aware Key
```

Then:

```text
Position-Aware Q
        ×
Position-Aware K
        ↓
Attention Scores
```

This allows positional relationships to influence attention.

The mathematical details of RoPE can be studied separately from this conceptual overview.

---

# 35. Positional Information Does Not Mean the Model "Reads" Positions Like Humans

The model does not literally think:

```text
"The word cat is at position 2."
```

Instead, positional information is represented numerically and incorporated into the computations.

The model processes numerical representations such as:

```text
🧩 Vectors
   +
📍 Position-Dependent Information
   ↓
🔄 Mathematical Operations
```

So "the model knows the position" is a useful simplification, not a description of human-like awareness.

---

# 36. Complete Positional Information Flow

The complete high-level flow is:

```text
📝 Human Text
      ↓
🔤 Tokenization
      ↓
🔢 Token IDs
      ↓
🧩 Token Embeddings
      ↓
📍 Positional Information
      ↓
🤖 Position-Aware Representations
      ↓
👀 Self-Attention
      ↓
🧠 Feed-Forward Network
      ↓
🔄 More Transformer Blocks
      ↓
📊 Contextual Representations
      ↓
🎯 Output Layer
      ↓
📈 Logits
      ↓
🔤 Next Token
```

Depending on the architecture, the positional information may be added to embeddings or incorporated at a later stage such as attention.

---

# 37. Simple Mental Model

Think of token embeddings as answering:

> **"What token is this?"**

And positional information as answering:

> **"Where is this token in relation to the sequence?"**

For example:

```text
🧩 Token
   +
📍 Position
   ↓
📊 Position-Aware Representation
   ↓
👀 Attention
   ↓
🧠 Contextual Representation
```

A simple way to remember it:

```text
🧩 Token Information
        +
📍 Position Information
        ↓
🤖 Transformer
        ↓
🧠 Contextual Representation
```

---

# 38. Key Takeaways

* 📍 **Positional Information gives Transformers information about token order and position.**
* 🧩 Token embeddings represent token-related information.
* 📍 Position information represents where tokens occur or how positions relate.
* 🔢 Token IDs and positions are different things.
* 👀 Self-attention alone does not automatically provide a universal representation of sequence order.
* 🧠 The original Transformer used sinusoidal positional encoding.
* 📚 Learned positional embeddings are another approach.
* 🔄 RoPE is a modern approach that incorporates position into attention through rotations of Query and Key representations.
* 📏 Positional methods can represent absolute positions, relative relationships, or both depending on the architecture.
* 🎭 Positional information is different from attention masking.
* 🔗 Position information can influence attention relationships.
* 🧠 After Transformer processing, token representations become contextual representations influenced by surrounding tokens.
* ⚙️ The exact positional mechanism varies between Transformer architectures.
* ⚠️ Positional information is numerical information used by the model; it is not human-like awareness of position.

The central idea is:

```text
📝 Text
   ↓
🔤 Tokens
   ↓
🔢 Token IDs
   ↓
🧩 Token Embeddings
   +
📍 Positional Information
   ↓
🤖 Position-Aware Representation
   ↓
👀 Attention
   ↓
🧠 Contextual Representation
```

**Positional Information = information that helps the Transformer represent where tokens occur and how their positions relate within a sequence.**
