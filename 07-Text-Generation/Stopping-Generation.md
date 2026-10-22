# 🛑 Stopping Generation in LLMs

## 1. What Is Stopping Generation?

**Stopping generation is the process of deciding when an LLM should stop producing new tokens.**

An LLM typically generates text one token at a time. Without a stopping condition, the generation process could continue until it reaches a configured limit or another stopping rule.

Stopping conditions help the model finish its response at an appropriate point.

For example, suppose a user asks:

> What is machine learning?

The model might generate:

> Machine learning is a branch of AI that enables computers to learn patterns from data.

After completing the answer, generation should stop instead of continuing to produce unrelated text.

---

## 2. Where Does Stopping Generation Fit in the Pipeline?

Stopping conditions are checked during the autoregressive generation loop.

```text id="stopflow01"
           User Prompt
                |
                v
        Tokenize the Prompt
                |
                v
        Transformer Model
                |
                v
          Generate Logits
                |
                v
       Select the Next Token
                |
                v
       Append Token to Context
                |
                v
      Check Stopping Conditions
                |
         +------+------+
         |             |
      Stop? No         Yes
         |             |
         v             v
   Generate Again   Return Output
```

If no stopping condition has been met, the model continues generating tokens.

If a stopping condition is met, generation ends.

---

## 3. Why Does an LLM Need Stopping Conditions?

A language model predicts likely next tokens. Its next-token prediction mechanism does not automatically guarantee that every response will end at the exact point a user expects.

Stopping conditions provide boundaries for generation.

They help with:

- **Response completion:** Stop when the model indicates that its response is finished.
- **Length control:** Prevent excessively long output.
- **Structured output:** Stop after a particular delimiter or marker when appropriate.
- **Resource management:** Limit the time and computation spent generating tokens.
- **Application control:** End generation when the required output has been produced.

Different applications may use different stopping rules.

---

## 4. End-of-Sequence Token

One common stopping mechanism is a special token that indicates the end of a sequence.

It is often called an **EOS token**, meaning *End of Sequence*.

A tokenizer or model may represent it using a token such as `</s>` or another model-specific special token. The exact token depends on the model and its tokenizer.

### Example

Suppose the model generates:

```text id="eosdemo01"
Machine learning helps computers
learn patterns from data.
<EOS>
```

The EOS token indicates that the generated sequence has ended.

The generation system recognizes this token and stops producing further tokens for that sequence.

### Important Details

- EOS is a token, not merely a punctuation mark.
- Different models can use different end-of-sequence tokens.
- A model may generate an EOS token as part of its learned behavior.
- The generation system must recognize the relevant token as a stopping condition.

An EOS token is not the same as a period. A period is ordinary text punctuation unless the tokenizer and model define it otherwise.

---

## 5. Stop Sequences

Another stopping mechanism is a **stop sequence**.

A stop sequence is a configured string or token pattern that tells the generation system to stop when the specified sequence appears.

For example, an application might configure:

```text id="stopseq01"
Stop sequence: <END>
```

If the model produces:

```text id="stopseq02"
The answer is 42.
<END>
Additional generated text...
```

The generation system can stop when it detects `<END>`.

The exact matching behavior depends on the implementation. Stop sequences may be handled through token matching or text matching, and the matched sequence may or may not be included in the returned output.

### Where Are Stop Sequences Useful?

- Generating structured responses
- Separating sections in a custom format
- Ending a response at a designated marker
- Controlling output from models used in applications

**Important:** A stop sequence is not necessarily a special token built into the model. It can be a string configured by the application.

---

## 6. Maximum New Tokens

A generation system can also stop after producing a specified maximum number of new tokens.

For example:

```text id="maxnew01"
Maximum new tokens = 5

Prompt:
The capital of France is

Generated tokens:
Paris | is | the | capital | of

Stop: Maximum reached
```

Here, the generation process stops because it has reached the configured limit, even though the sentence is incomplete.

This illustrates an important difference: reaching a length limit does not necessarily mean the model has finished its answer naturally.

### Prompt Tokens vs New Tokens

Suppose the prompt contains 100 tokens and the generation limit is 50 new tokens.

```text id="tokencount01"
Prompt tokens:       100
Maximum new tokens:   50
------------------------
Potential total:     150 tokens
```

The limit of 50 new tokens applies to the generated continuation, not necessarily to the entire prompt-plus-response sequence.

Actual total sequence limits and other configuration settings may impose additional constraints.

---

## 7. Maximum Sequence Length and Context Window

An LLM also has a context-window limit, which determines how many tokens it can process within a supported context.

The context can include the prompt and previously generated tokens.

For example:

```text id="ctxstop01"
Maximum supported context: 4,096 tokens

Prompt:               3,900 tokens
Generated continuation: 196 tokens
-----------------------------------
Total:                4,096 tokens
```

In this simplified example, the sequence reaches the context limit after generating 196 tokens.

The exact behavior depends on the model and generation system. Some systems may stop, truncate input, or manage the context in other ways.

### Maximum New Tokens vs Context Window

| Feature | Maximum New Tokens | Context Window |
|---|---|---|
| Controls | Length of the generated continuation | Amount of context the model can handle |
| Counts prompt tokens? | Usually no, when configured as a new-token limit | Yes, prompt and relevant generated tokens contribute |
| Main purpose | Bound response length | Bound the model's supported input context |
| Guarantees a natural ending? | No | No |

These are related limits, but they are not interchangeable.

---

## 8. The Model Can Predict an End Token

During training, many autoregressive language models learn to predict the next token in sequences that may include an end-of-sequence marker.

For example, a training sequence might look like:

```text id="eostraining01"
Input:
The sun rises in the

Target:
east <EOS>
```

This is a simplified illustration of next-token prediction. In practice, training sequences may contain many tokens and EOS placement depends on how the data is prepared.

The model learns patterns associated with when sequences end.

During inference, it can assign probability to an EOS token. If the generation system selects that token and recognizes it as a stopping token, generation can terminate.

**Important:** The model's learned end-token behavior and the application's stopping rules work together. An application may stop generation before the model predicts EOS, for example when a maximum token limit is reached.

---

## 9. The Complete Generation Loop

Let's combine next-token prediction, token selection, and stopping conditions.

```text id="loopstop01"
Start with prompt
       |
       v
Run model forward pass
       |
       v
Get logits for next token
       |
       v
Apply decoding strategy
       |
       v
Select next token
       |
       v
Is it a recognized EOS token?
       |
       +---- Yes ----> Stop
       |
       +---- No
              |
              v
     Append token to context
              |
              v
     Has another stopping rule
          been triggered?
              |
       +------+------+
       |             |
      Yes            No
       |             |
       v             v
      Stop      Predict again
```

Other stopping conditions, such as a stop sequence or maximum-token limit, can also terminate the loop.

The process repeats until a stopping condition is satisfied.

---

## 10. Multiple Stopping Conditions Can Work Together

A generation system may use several stopping conditions at the same time.

For example:

```text id="multistop01"
Stop if any of these occurs:

1. Model generates EOS
2. Configured stop sequence appears
3. Maximum new-token limit is reached
4. Another application-defined stopping rule is triggered
```

If any active condition is satisfied, the system can stop generation.

The precise behavior depends on the framework, model API, and configuration.

### Example

Suppose the system uses:

- EOS detection
- Maximum of 200 new tokens
- Stop sequence `<END>`

The model might stop after 35 tokens if it generates EOS, after 70 tokens if `<END>` appears, or at 200 tokens if neither of those conditions occurs first.

These are illustrative possibilities, not guaranteed outcomes.

---

## 11. What Happens to the Stopping Token?

The generation system may treat a stopping token differently from ordinary text tokens.

For example, an EOS token may be used to terminate generation but excluded from the final decoded response.

A configured stop sequence may also be omitted from the returned text, depending on the implementation.

```text id="stopoutput01"
Generated token sequence:
Hello there. <EOS>

Returned text:
Hello there.
```

This is one common behavior, not a universal rule.

The important distinction is between:

- **Generated token sequence:** Tokens produced internally by the model.
- **Returned text:** Text the application ultimately provides to the user.

The returned text may not contain every token involved in stopping generation.

---

## 12. Common Misconceptions

### ❌ Every LLM stops only when it generates EOS.

No. Generation can also stop because of a length limit, stop sequence, or another configured condition.

### ❌ Reaching the maximum-token limit means the answer is complete.

No. The output may end mid-sentence or before the requested task is finished.

### ❌ A period always stops generation.

No. Ordinary punctuation does not inherently terminate the generation loop.

### ❌ A stop sequence must be a special token.

No. It may be a configured text string or token pattern.

### ❌ Stopping generation changes the model's learned parameters.

No. Stopping rules control when inference ends; they do not update the model's weights.

### ❌ Every model uses the same EOS token.

No. Special tokens and their meanings depend on the tokenizer, model, and generation setup.

---

## 13. 🧠 Simple Mental Model

Think of text generation as a loop that repeatedly asks:

> What should the next token be, and should generation continue after it?

```text id="stopmental01"
Predict a token
      |
      v
Select the token
      |
      v
Check stopping conditions
      |
      +---- Stop condition met? ---- Yes ----> Finish
      |
      No
      |
      v
Add token to context
      |
      v
Repeat
```

The model generates the continuation, while the generation system monitors the stopping rules.

**The key idea:** An LLM generates text token by token, and stopping conditions determine when that process ends.

---

## 14. Key Takeaways

- Stopping generation determines when an LLM stops producing tokens.
- EOS tokens can indicate that a generated sequence has ended.
- Stop sequences allow applications to stop at configured markers.
- Maximum new tokens limits the length of the generated continuation.
- The context window limits how much context the model can handle.
- Multiple stopping conditions can be used together.
- A stopping condition can end generation even when the answer is incomplete.
- Stopping rules control inference; they do not retrain the model.
