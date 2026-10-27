# 🔤 Text to Tokens

Before a Large Language Model (LLM) can process text, the text must be converted into a sequence of tokens.

LLMs do not directly process raw sentences as humans see them. A tokenizer divides the input text into token units, and each token is mapped to a numerical token ID that the model can process.

This document explains how raw text becomes tokens, how tokens become IDs, and how this process connects to the rest of an LLM.

---

## 1. What Does Text-to-Tokens Mean?

**Text-to-tokens is the process of dividing text into smaller units according to a tokenizer's vocabulary and rules.**

Consider this sentence:

```text
I love machine learning.
```

A tokenizer might divide it into these tokens:

```text
["I", " love", " machine", " learning", "."]
```

This is only an illustrative example. A real tokenizer may split the sentence differently, depending on its vocabulary and tokenization algorithm.

Each item in the resulting list is a token.

A token can represent:

- A complete word
- Part of a word
- Punctuation
- Whitespace combined with text
- A character or byte-level unit
- A special token used to structure the input

**Important:** A token is not necessarily a complete word.

---

## 2. The Complete Conversion Process

The conversion from text to model input has several stages.

```text
Raw Text
   |
   v
Tokenizer
   |
   v
Token Sequence
   |
   v
Token IDs
   |
   v
Token Embeddings
   |
   v
Positional Information
   |
   v
Transformer Blocks
```

For example:

<box border radius="xl" padding={3} gap={3}>
  <box gap={1}>
    <text color="secondary" size="sm">Stage 1 — Raw text</text>
    <box background="surface-secondary" radius="md" padding={3}>
      I love machine learning.
    </box>
  </box>
  <row justify="center">
    <icon name="arrow-down" size="lg" color="secondary" />
  </row>
  <box gap={1}>
    <text color="secondary" size="sm">Stage 2 — Tokens</text>
    <row gap={1} wrap="wrap">
      {#each ["I"," love"," machine"," learning","."] as token}
        <box key={token} border radius="md" padding={2}>
          <text>{token}</text>
        </box>
      {/each}
    </row>
  </box>
  <row justify="center">
    <icon name="arrow-down" size="lg" color="secondary" />
  </row>
  <box gap={1}>
    <text color="secondary" size="sm">Stage 3 — Token IDs</text>
    <row gap={1} wrap="wrap">
      {#each ["314","892","1532","4781","13"] as id}
        <box key={id} background="surface" border radius="md" padding={2}>
          <text tabularNums>{id}</text>
        </box>
      {/each}
    </row>
    <text color="secondary" size="xs">Illustrative IDs only; real IDs depend on the tokenizer.</text>
  </box>
</box>

The model uses token IDs to look up embeddings. The token IDs themselves are identifiers, not the semantic representations that the Transformer processes.

---

## 3. Step 1: Start with Raw Text

Raw text is the sentence, question, document, or other text supplied to the model.

For example:

```text
What is artificial intelligence?
```

At this stage, it is simply a text string.

The tokenizer must convert this string into units supported by its vocabulary and tokenization rules.

The exact result depends on the tokenizer. Two different models can tokenize the same sentence differently.

---

## 4. Step 2: Split the Text into Tokens

The tokenizer divides the text into a sequence of tokens.

For example, an illustrative word-oriented tokenization might produce:

```text
"What" | " is" | " artificial" | " intelligence" | "?"
```

A subword tokenizer might instead divide a word into smaller pieces if the complete word is not represented as a single token in its vocabulary.

For example, an unfamiliar word might be divided conceptually as:

```text
"un" | "fam" | "iliar"
```

This is just an illustration, not a guaranteed split from a particular tokenizer.

### Why not use only complete words?

A vocabulary containing every possible word would be difficult to maintain. New words, names, misspellings, and word variations would create additional challenges.

Subword tokenization allows tokenizers to represent many unfamiliar words using reusable pieces.

Common approaches include:

- Character-level tokenization
- Word-level tokenization
- Subword tokenization
- Byte-level tokenization

Modern LLMs commonly use subword-based tokenization or related methods.

---

## 5. Step 3: Understand the Vocabulary

A tokenizer's vocabulary is the collection of tokens it can represent directly.

For example, a simplified vocabulary might contain:

```text
Token          Token ID
-----------------------
I              101
love           205
machine        310
learning       415
.              12
```

These values are fictional and are shown only to explain the concept.

When the tokenizer encounters a recognized token, it maps that token to its associated ID.

A vocabulary may contain words, subwords, punctuation, whitespace-related pieces, and special tokens.

### Important distinction

The vocabulary is not the same as the model's knowledge.

The vocabulary determines which token units can be represented directly. The model's learned parameters encode patterns and associations acquired during training.

---

## 6. Step 4: Convert Tokens into Token IDs

Each token is mapped to a numerical identifier.

Suppose the token sequence is:

```text
["I", "love", "machine", "learning", "."]
```

An illustrative conversion could be:

```text
["I", "love", "machine", "learning", "."]
                       |
                       v
[101, 205, 310, 415, 12]
```

The resulting sequence of numbers is called the **token ID sequence**.

Mathematically, if the tokenizer produces tokens \(t_1,t_2,\ldots,t_n\), its vocabulary mapping converts them into IDs:

\[
t_1,t_2,\ldots,t_n
\longrightarrow
i_1,i_2,\ldots,i_n
\]

Each ID identifies a particular token in that tokenizer's vocabulary.

### Are token IDs meaningful numbers?

No. Token IDs are identifiers, not measurements of meaning.

For example, token ID `205` is not inherently more meaningful than token ID `101`. The numerical values do not indicate word importance, similarity, or order.

The mapping is tokenizer-specific. The same text can receive different IDs under different tokenizers.

---

## 7. Step 5: How Token IDs Connect to Embeddings

Token IDs are not usually passed into the Transformer as meaningful numerical features directly. Instead, each ID is used to retrieve a learned vector from an embedding matrix.

For example:

```text
Token ID: 101
     |
     v
Embedding Matrix
     |
     v
Learned Vector
[0.12, -0.43, 0.81, ...]
```

The vector shown is illustrative.

If the model's hidden dimension is \(d\), each token embedding has \(d\) numerical components.

For a sequence of \(n\) tokens, the embeddings can be arranged into a matrix with shape:

\[
n \times d
\]

The model then combines token representations with positional information before processing them through its Transformer blocks.

**Remember the distinction:**

| Concept | Meaning |
|---|---|
| Raw text | The original text string |
| Token | A unit produced by the tokenizer |
| Token ID | The integer identifying a token |
| Token embedding | A learned vector associated with the token ID |
| Contextual representation | A representation that develops as the token is processed in context by the Transformer |

A token's initial embedding is not the same as its final contextual representation.

---

## 8. Step 6: Special Tokens

Some tokenizers include special tokens that help mark boundaries or communicate structure.

Examples include:

- Beginning-of-sequence markers
- End-of-sequence markers
- Padding tokens
- Unknown-token markers in some tokenizers
- Instruction or message-boundary markers in certain model formats

The actual tokens and their roles vary by tokenizer and model.

For example, an illustrative sequence might be:

```text
[BOS] I love machine learning . [EOS]
```

Here, `BOS` and `EOS` represent beginning-of-sequence and end-of-sequence markers.

Not every tokenizer uses these markers in the same way, and some models do not require an explicit beginning token for every input.

Special tokens also have token IDs. If they are included in the model input, they count toward the sequence length and may use space in the context window.

---

## 9. Does Tokenization Always Produce One Token per Word?

No.

Consider the sentence:

```text
Tokenization makes language models usable.
```

A tokenizer could produce tokens that resemble whole words:

```text
["Tokenization", " makes", " language", " models", " usable", "."]
```

Another tokenizer might divide some words into smaller units.

The exact token boundaries depend on the vocabulary and tokenization algorithm.

This matters because a sentence containing 10 words does not necessarily contain 10 tokens.

A long word may produce several tokens, while punctuation or whitespace can be represented as part of neighboring tokens or as separate tokens.

### Why token count matters

Token count affects:

- How much text fits in a model's context window
- Memory and computational requirements
- Input and output token usage
- The number of prediction steps required to generate a response

Token count should therefore be measured using the tokenizer associated with the model rather than estimated only from the number of words.

---

## 10. Tokenization During Training and Inference

Tokenization is important in both training and inference.

### During training

```text
Training Text
      |
      v
Tokenizer
      |
      v
Token IDs
      |
      v
Training Sequences
      |
      v
Inputs and Targets
      |
      v
Model Training
```

The token IDs are organized into training sequences. For a causal language model, inputs and target tokens are commonly shifted so that the model learns to predict the next token.

### During inference

```text
User Prompt
      |
      v
Tokenizer
      |
      v
Prompt Token IDs
      |
      v
Model Forward Pass
      |
      v
Next-Token Prediction
      |
      v
Generated Token IDs
      |
      v
Tokenizer Decoder
      |
      v
Generated Text
```

During inference, the tokenizer converts the prompt into token IDs. After the model generates token IDs, the tokenizer's decoding process converts those IDs back into readable text.

Training and inference use the same model-compatible tokenization scheme, although the surrounding workflows differ.

---

## 11. Tokenization Is Not Text Generation

These operations are related but perform different jobs.

| Operation | What it does |
|---|---|
| Tokenization | Converts text into tokens |
| ID conversion | Maps tokens to integer IDs |
| Embedding lookup | Maps IDs to learned vectors |
| Transformer processing | Builds context-dependent representations |
| Next-token prediction | Produces scores for possible next tokens |
| Decoding strategy | Selects a token from the prediction distribution |
| Token decoding | Converts generated token IDs back into text |

The word *decoding* can refer to two different operations in LLM discussions:

1. **Generation decoding:** Selecting the next token from model predictions, using methods such as greedy decoding or sampling.
2. **Tokenizer decoding:** Converting a sequence of token IDs back into readable text.

These operations should not be confused.

---

## 12. Interactive Example: Follow the Conversion

The following example illustrates how the stages connect. The numerical IDs are fictional.

{@body const [stage,setStage] = DIL.useState("text")}
<box border radius="xl" padding={4} gap={3}>
  <text color="secondary" size="sm">Select a stage</text>
  <radio-group value={stage} onChange={setStage} direction="col">
    <radio value="text">1. Raw text</radio>
    <radio value="tokens">2. Tokens</radio>
    <radio value="ids">3. Token IDs</radio>
    <radio value="embeddings">4. Embeddings</radio>
  </radio-group>
  <divider color="subtle" />
  {#if stage === "text"}
    **Raw text**

    <box background="surface-secondary" radius="md" padding={3}>
      I love AI.
    </box>
    The original sentence before tokenization.
  {:else if stage === "tokens"}
    **Tokens**

    <row gap={2} wrap="wrap">
      {#each ["I"," love"," AI","."] as token}
        <box key={token} border radius="md" padding={2}>{token}</box>
      {/each}
    </row>
    An illustrative tokenizer has divided the sentence into four token units.
  {:else if stage === "ids"}
    **Token IDs**

    <row gap={2} wrap="wrap">
      {#each ["101","205","560","12"] as id}
        <box key={id} background="surface-secondary" radius="md" padding={3}>
          <title size="md" tabularNums>{id}</title>
        </box>
      {/each}
    </row>
    Each token is mapped to its identifier in the fictional vocabulary.
  {:else}
    **Embeddings**

    <box background="surface-secondary" radius="md" padding={3}>
      <text preserveWhitespace>{`[0.12, -0.43, 0.81, ...]\n[0.34, 0.17, -0.22, ...]\n[-0.19, 0.72, 0.11, ...]\n[0.05, -0.08, 0.26, ...]`}</text>
    </box>
    Each token ID retrieves a learned vector. Real embeddings have a model-specific dimension and values.
  {/if}
</box>

---

## 13. Common Misconceptions

**Misconception 1: One word always equals one token.**

A word may be represented by one token or several tokens. Some tokens may include whitespace or punctuation.

**Misconception 2: Token IDs contain meaning.**

Token IDs are identifiers. The model uses them to retrieve learned embeddings.

**Misconception 3: Every model uses the same tokenizer.**

Different models can use different vocabularies, algorithms, token boundaries, and ID mappings.

**Misconception 4: Tokenization is the same as embedding.**

Tokenization divides text into units. Embedding lookup converts token IDs into learned vectors.

**Misconception 5: The tokenizer generates the answer.**

The tokenizer converts between text and token representations. The language model produces predictions, and a generation procedure selects tokens.

**Misconception 6: Special tokens are always visible in normal text.**

Some special tokens are used internally or appear in structured model formats. Whether they are displayed literally depends on the tokenizer and interface.

**Misconception 7: More tokens always mean more information.**

Token count depends on tokenization. Splitting the same text into more tokens does not automatically make it more informative.

---

## 14. Complete Text-to-Tokens Flow

```text
                  RAW TEXT
                     |
                     v
                  TOKENIZER
                     |
                     v
               TOKEN SEQUENCE
                     |
                     v
                TOKEN IDs
                     |
                     v
              EMBEDDING LOOKUP
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
               CONTEXTUAL STATES
                     |
                     v
                   LOGITS
                     |
                     v
            NEXT-TOKEN SELECTION
                     |
                     v
             GENERATED TOKEN IDs
                     |
                     v
              TOKENIZER DECODING
                     |
                     v
                READABLE TEXT
```

This diagram connects text tokenization to the larger LLM workflow. The model does not jump directly from raw text to a response: text is represented as tokens and IDs, converted into vectors, processed by the neural network, and eventually converted back into text.

---

## 15. Key Takeaways

- **Text-to-tokens** converts raw text into token units.
- **Token IDs** are numerical identifiers assigned by a tokenizer.
- **Token embeddings** are learned vectors retrieved using token IDs.
- A token can represent a word, part of a word, punctuation, whitespace-related text, or another unit.
- Tokenization differs between models, so token counts and IDs are tokenizer-dependent.
- Training and inference both rely on tokenization.
- Generated token IDs must be converted back into text to produce a readable response.

The essential flow is:

**Raw text → Tokens → Token IDs → Embeddings → Transformer processing.**
