# 🔤 Prompt to Tokens in an LLM

Before a Large Language Model (LLM) can process a prompt, the text must be converted into tokens and then into numerical token IDs.

This process is called **tokenization and token-to-ID conversion**.

For example, when you enter:

`Explain Artificial Intelligence`

The model does not directly pass these raw characters into its Transformer layers. A tokenizer first converts the text into tokens, and each token is mapped to an ID from the tokenizer's vocabulary.

These IDs are then used to create the numerical representations that the model processes.

---

## 1. 🧠 What Is a Prompt?

A prompt is the text or other supported input provided to a model to request a prediction or response.

Examples:

- `What is machine learning?`
- `Write a Python program to add two numbers.`
- `The sun rises in the`
- `Explain how a Transformer works.`

The prompt may be a question, an instruction, a partial sentence, or a longer conversation.

Before a text prompt can be processed by a language model, it usually passes through a tokenizer.

---

## 2. 🔄 The Complete Prompt-to-Tokens Process

Consider this prompt:

`The cat is sleeping.`

The conversion process looks like this:

```text id="w9k2md"
Original Prompt
"The cat is sleeping."
        |
        v
Tokenizer
        |
        v
Token Pieces
["The", " cat", " is", " sleeping", "."]
        |
        v
Vocabulary Lookup
        |
        v
Token IDs
[101, 482, 318, 7291, 13]
```

The token pieces and IDs above are illustrative. A real tokenizer may divide the same text differently and assign different IDs.

The important point is that **tokens are the pieces of text, while token IDs are the numerical identifiers assigned to those pieces**.

The resulting IDs are ready to be used in the model's input pipeline.

---

## 3. 🔍 Step 1 — Start with Raw Text

Suppose the user enters:

`I love machine learning.`

At this stage, the prompt is ordinary text made up of characters.

```text id="c7f4qx"
I love machine learning.
```

A human can immediately read this sentence. A neural network, however, operates on numerical representations.

The tokenizer converts the text into units that the model's vocabulary can represent.

The tokenizer does not decide what answer the model should give. Its job is to convert the input into the token format expected by the model.

---

## 4. ✂️ Step 2 — Split the Text into Tokens

A token can represent:

- A complete word
- Part of a word
- Punctuation
- A character or byte-related unit, depending on the tokenizer
- A special token used for structure or control

For example, a tokenizer might represent:

`I love machine learning.`

as:

```text id="s8k3jp"
["I", " love", " machine", " learning", "."]
```

Notice that some tokens include a leading space. Certain tokenizers encode spaces as part of token pieces rather than treating every space as a separate token.

Another tokenizer could split the same sentence differently. For example, it might divide `learning` into smaller pieces.

**There is no universal tokenization for all LLMs.** The result depends on the tokenizer and its vocabulary.

---

## 5. 🧩 Step 3 — Understand How a Word Can Become Multiple Tokens

A token does not always equal a complete word.

Consider the word:

`unhappiness`

One tokenizer might represent it as a single token, while another might divide it into pieces such as:

```text id="j3p8wm"
["un", "happiness"]
```

Or it might split it into smaller pieces, depending on its vocabulary.

This flexibility is useful because a tokenizer does not need a separate vocabulary entry for every possible word.

It can represent many uncommon words by combining smaller, reusable pieces.

### Why not make every word a single token?

A word-level vocabulary would need to contain a huge number of words, including rare words, new names, spelling variations, and technical terms.

Subword tokenization provides a practical compromise between vocabulary size and sequence length.

---

## 6. 📚 Step 4 — Map Tokens to Token IDs

After tokenization, each token piece is mapped to a numerical identifier in the tokenizer's vocabulary.

For example:

| Token | Illustrative token ID |
|---|---:|
| `I` | 41 |
| ` love` | 827 |
| ` machine` | 4921 |
| ` learning` | 6132 |
| `.` | 13 |

These values are examples only. Actual IDs depend on the vocabulary.

The resulting sequence is:

```text id="r4u8zn"
Tokens:
["I", " love", " machine", " learning", "."]

        |
        v

Token IDs:
[41, 827, 4921, 6132, 13]
```

The tokenizer's vocabulary defines the mapping between token pieces and IDs.

### Are token IDs meaningful numbers?

No. Token IDs are identifiers, not numerical measures of meaning.

For example, token ID `827` is not inherently more important or more meaningful than token ID `41`.

The numbers simply allow the model to look up the corresponding entries in its embedding matrix.

---

## 7. 🔢 Step 5 — Token IDs Become Model Input

Token IDs are the output of the text-to-ID conversion stage, but they are not normally the final representations processed by the Transformer.

The model uses the IDs to retrieve learned token embeddings.

For example:

```text id="k6z3bv"
Token IDs
[41, 827, 4921, 6132, 13]
        |
        v
Embedding Lookup
        |
        v
Numerical Vectors
        |
        v
Add or Incorporate
Positional Information
        |
        v
Transformer Blocks
```

Each token ID selects a corresponding vector from the embedding matrix.

The embedding vectors contain learned numerical values. They are different from token IDs.

For example, if a model uses a hidden dimension of 768, each token embedding has 768 numerical components. This dimension is illustrative, not universal.

Positional information is also incorporated so the model can represent the order of tokens.

---

## 8. 🎯 Step 6 — Why Tokenization Matters During Inference

Tokenization determines how a prompt is represented before the model processes it.

It affects several important aspects of inference.

### A. Number of tokens

Consider these two prompts:

- `AI`
- `Artificial Intelligence`

The longer phrase uses more characters, but the exact token count depends on the tokenizer.

Character count and token count are not the same thing.

### B. Context-window usage

Models have a maximum supported context length, measured in tokens.

The prompt, conversation history, and generated output may all consume part of that token budget.

A prompt that contains fewer characters does not necessarily use fewer tokens than another prompt.

### C. Processing cost

Token count can influence memory requirements, processing time, and inference cost.

The exact relationship depends on the architecture, implementation, hardware, and whether the prompt is processed in a batch.

### D. Handling unfamiliar text

Subword or byte-based tokenization can represent many words and strings that do not appear as complete entries in the vocabulary.

However, uncommon text may still require many tokens, and tokenization does not guarantee that the model will understand or answer questions about it correctly.

---

## 9. 🛠️ Special Tokens in Prompts

Some LLM systems use special tokens to mark structural boundaries or control how input and output are interpreted.

Examples of common special-token roles include:

- Beginning or ending a sequence
- Separating messages
- Marking the end of an assistant turn
- Identifying a special section of content
- Representing padding in a batch

The exact tokens and their meanings depend on the model and its tokenizer.

For example, a chat-oriented model may receive a structured representation that distinguishes a user message from an assistant message.

Conceptually:

```text id="t5w7yn"
Message Structure
        |
        v
Special Tokens + Message Content
        |
        v
Tokenizer-Specific Token IDs
        |
        v
Model Input
```

Not every model uses the same special tokens, and not every prompt requires every type of boundary marker.

Special tokens are part of the model's input format, not ordinary words that must appear in every prompt.

---

## 10. 🔁 Does the Same Prompt Always Produce the Same Token IDs?

For a fixed text prompt, the same compatible tokenizer configuration will generally produce the same token IDs.

However, different tokenizers can produce different token sequences for the same text.

For example:

```text id="a2m6fx"
Prompt:
"Artificial Intelligence"

Tokenizer A:
["Artificial", " Intelligence"]

Tokenizer B:
["Artificial", " Intel", "ligence"]
```

These splits are hypothetical.

The resulting token IDs would also differ because each tokenizer has its own vocabulary and mapping.

This is why a model must generally be used with the tokenizer and input-format conventions it was designed for.

Using an incompatible tokenizer can produce incorrect input representations even if the original text looks identical.

---

## 11. 🧪 Complete Example: Prompt to Token IDs

Let's follow one prompt through the entire conversion stage.

**Prompt:**

`The sky is blue.`

<box gap={3}>
  <row align=start gap={3}>
    <box background="surface-secondary" radius="lg" padding={3} align=center justify=center size="44px">
      <icon name="message-square-text" size="xl" />
    </box>
    <box flex="1" gap={1}>
      **Step 1 — Raw text**

      <text color="secondary" size="sm">The original text supplied to the model.</text>

      `The sky is blue.`
    </box>
  </row>
  <divider color="subtle" />
  <row align=start gap={3}>
    <box background="surface-secondary" radius="lg" padding={3} align=center justify=center size="44px">
      <icon name="scissors" size="xl" />
    </box>
    <box flex="1" gap={1}>
      **Step 2 — Tokenization**

      <text color="secondary" size="sm">The tokenizer splits the text into vocabulary pieces.</text>

      `["The", " sky", " is", " blue", "."]`
    </box>
  </row>
  <divider color="subtle" />
  <row align=start gap={3}>
    <box background="surface-secondary" radius="lg" padding={3} align=center justify=center size="44px">
      <icon name="list-ordered" size="xl" />
    </box>
    <box flex="1" gap={1}>
      **Step 3 — Token IDs**

      <text color="secondary" size="sm">Each token is replaced by its vocabulary ID.</text>

      `[101, 731, 318, 2045, 13]`

      <text color="secondary" size="xs">Illustrative IDs only.</text>
    </box>
  </row>
  <divider color="subtle" />
  <row align=start gap={3}>
    <box background="surface-secondary" radius="lg" padding={3} align=center justify=center size="44px">
      <icon name="layers" size="xl" />
    </box>
    <box flex="1" gap={1}>
      **Step 4 — Model representations**

      <text color="secondary" size="sm">Token IDs are used to retrieve embeddings, and positional information is incorporated.</text>

      `Token IDs → Embeddings → Transformer`
    </box>
  </row>
</box>

The conversion from text to IDs prepares the prompt for the model. The Transformer then processes those representations to calculate predictions.

---

## 12. ❗ Common Misunderstandings

### 1. Is a token always a complete word?

No. A token can be a word, subword, punctuation mark, or another unit defined by the tokenizer.

### 2. Are token IDs the same as embeddings?

No. Token IDs identify vocabulary entries. Embeddings are learned numerical vectors associated with those entries.

### 3. Does tokenization generate the answer?

No. Tokenization converts the input into the model's expected representation. The trained model generates predictions.

### 4. Does every LLM use the same tokenizer?

No. Tokenizers and vocabularies vary between models.

### 5. Is one word always equal to one token?

No. Some words map to one token; others map to multiple tokens.

### 6. Are token IDs ordered by meaning?

No. Their numerical values are identifiers, not a semantic ranking.

### 7. Does a larger token count always mean more information?

No. Token count measures the number of tokens, not the amount or quality of information.

### 8. Can tokenization affect inference cost?

Yes. Token count can influence context usage, memory, and computation.

### 9. Does the model process only the prompt's original tokens?

No. During autoregressive generation, newly generated tokens are appended to the sequence and used as context for subsequent predictions.

### 10. Does tokenization guarantee that a model can handle every possible string perfectly?

No. A tokenizer may represent unfamiliar strings using smaller pieces or bytes, but the model can still produce incorrect or unreliable predictions.

---

## 13. 🧠 Final Mental Model

Remember this conversion process:

1. **Prompt** — receive the original text.
2. **Tokenization** — split the text into token pieces.
3. **Vocabulary lookup** — map each token to its ID.
4. **Token IDs** — create a numerical sequence.
5. **Embedding lookup** — convert IDs into learned vectors.
6. **Positional information** — incorporate token order.
7. **Transformer** — process the input representations.

The central idea is:

**Text → Tokens → Token IDs → Embeddings → Transformer**

Tokenization is the bridge between human-readable text and the numerical input representation used by a language model.
