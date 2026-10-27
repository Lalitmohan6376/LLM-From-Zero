# 🧠 LLM From Zero

### Understand How a Large Language Model Is Built

> **From raw text to a complete Transformer-based LLM**

**📚 Current Status:** Theory Only
**💻 Implementation:** Coming Soon

---

## 🌟 About This Repository

**LLM From Zero** is a step-by-step learning repository designed to explain how a modern Transformer-based Large Language Model is constructed, trained, and used for text generation.

This repository does not begin with implementation.

It begins with understanding.

The learning journey gradually moves from the basic idea of an LLM to tokenization, architecture, Transformers, decoder-only models, training, inference, and finally the complete LLM pipeline.

### 🎯 The Core Goal

By the end of this repository, you should be able to look at a Transformer-based LLM and understand **what is happening at every major stage**.

---

# 🗺️ Learning Journey

```text
📚 Understand LLMs
        │
        ▼
📝 Understand Text & Tokenization
        │
        ▼
🔢 Understand Token IDs
        │
        ▼
🏗️ Understand LLM Architecture
        │
        ▼
🤖 Understand Transformers
        │
        ▼
🧩 Build a Decoder-Only Transformer
        │
        ▼
🎓 Train the LLM
        │
        ▼
✨ Generate Text
        │
        ▼
🧠 Understand the Complete LLM
```

---

# 🎯 Goal of the Repository

The goal is not simply to learn how to **use** an existing LLM.

The goal is to understand how an LLM is **constructed internally**.

This repository focuses on:

* 🧠 Understanding what an LLM actually is
* 📝 Understanding how text enters an LLM
* 🔤 Understanding tokenization
* 🔢 Understanding token IDs and representations
* 🏗️ Understanding LLM architecture
* 👀 Understanding attention
* 🤖 Understanding the Transformer
* 🧩 Understanding decoder-only architecture
* 🎓 Understanding how an LLM is trained
* ✨ Understanding how an LLM generates text
* 🔄 Understanding the complete flow from input to output

---

# 📁 Repository Structure

The repository is divided into eight major learning stages.

```text
🧠 LLM-From-Zero/
│
├── 📁 01-Introduction-to-LLMs/
│   ├── 📄 README.md
│   ├── 🧠 What-is-an-LLM.md
│   ├── 📚 What-is-a-Language-Model.md
│   ├── ❓ Why-LLMs.md
│   ├── 🆚 LLM-vs-Traditional-Language-Models.md
│   ├── 🆚 LLM-vs-NLP.md
│   ├── 🆚 LLM-vs-Generative-AI.md
│   ├── 🆚 LLM-vs-Chatbot.md
│   ├── 📏 Small-vs-Large-Language-Models.md
│   ├── 🏛️ Foundation-Models.md
│   ├── 🤖 What-is-GPT.md
│   ├── ⚡ LLM-Capabilities.md
│   └── ⚠️ LLM-Limitations.md
│
├── 📁 02-Text-and-Tokenization/
│   ├── 📄 README.md
│   ├── 📝 How-LLMs-Process-Text.md
│   ├── 📚 Vocabulary.md
│   ├── 🔤 What-is-a-Token.md
│   ├── ✂️ Tokenization.md
│   ├── 🔡 Character-Level-Tokenization.md
│   ├── 📝 Word-Level-Tokenization.md
│   ├── 🧩 Subword-Tokenization.md
│   ├── ⚙️ Byte-Pair-Encoding.md
│   ├── 🔢 Token-IDs.md
│   ├── 🏷️ Special-Tokens.md
│   ├── 📏 Sequence.md
│   ├── 🪟 Context-Window.md
│   └── 🔄 Text-to-Model-Input.md
│
├── 📁 03-LLM-Architecture/
│   ├── 📄 README.md
│   ├── 🧠 Inside-an-LLM.md
│   ├── 📥 Input-Representation.md
│   ├── 🔢 Token-Embeddings.md
│   ├── 📍 Positional-Information.md
│   ├── 🧩 Transformer-Blocks.md
│   ├── 👀 Attention.md
│   ├── 🧠 Feed-Forward-Network.md
│   ├── 📤 Output-Layer.md
│   └── 🏗️ LLM-Architecture-Overview.md
│
├── 📁 04-Transformer/
│   ├── 📄 README.md
│   ├── ❓ Why-Transformers.md
│   ├── 🏗️ Transformer-Architecture.md
│   ├── 👀 Attention-Mechanism.md
│   ├── 🔍 Self-Attention.md
│   ├── 🔑 Query-Key-Value.md
│   ├── 🎯 Attention-Scores.md
│   ├── 🎭 Attention-Masking.md
│   ├── 🧠 Multi-Head-Attention.md
│   ├── 📍 Positional-Information.md
│   ├── 🧮 Feed-Forward-Network.md
│   ├── ➕ Residual-Connections.md
│   ├── 📏 Layer-Normalization.md
│   ├── 🧩 Transformer-Block.md
│   ├── 📥 Encoder.md
│   ├── 📤 Decoder.md
│   ├── 🔄 Encoder-Decoder-Architecture.md
│   └── 🏗️ Complete-Transformer.md
│
├── 📁 05-Decoder-Only-Transformer/
│   ├── 📄 README.md
│   ├── 🆚 Encoder-vs-Decoder.md
│   ├── ❓ Why-Decoder-Only.md
│   ├── 👀 Causal-Self-Attention.md
│   ├── 🎭 Causal-Masking.md
│   ├── 🧩 Decoder-Only-Architecture.md
│   ├── 🏗️ Transformer-Block-in-LLM.md
│   ├── 🔄 Stacking-Transformer-Blocks.md
│   ├── 📤 Final-Output.md
│   ├── 🧠 Language-Modeling-Head.md
│   └── 🤖 GPT-Style-Architecture.md
│
├── 📁 06-Training-an-LLM/
│   ├── 📄 README.md
│   ├── 🧠 What-Does-an-LLM-Learn.md
│   ├── 📚 Training-Data.md
│   ├── 🧹 Data-Preparation.md
│   ├── 🔤 Training-Data-Tokenization.md
│   ├── 🧩 Training-Sequences.md
│   ├── ↔️ Input-and-Target.md
│   ├── 🎯 Next-Token-Prediction.md
│   ├── ▶️ Forward-Pass.md
│   ├── 📉 Loss.md
│   ├── 🔄 Backpropagation.md
│   ├── ⚙️ Optimizer.md
│   ├── 🔧 Parameter-Updates.md
│   ├── 📦 Batches.md
│   ├── 🔁 Training-Iterations.md
│   ├── 📊 Validation.md
│   └── 🏁 Complete-Training-Process.md
│
├── 📁 07-Text-Generation/
│   ├── 📄 README.md
│   ├── 🚀 Inference.md
│   ├── 📝 Prompt-to-Tokens.md
│   ├── 🧠 Forward-Pass-During-Inference.md
│   ├── 📊 Logits.md
│   ├── 🎯 Probability-Distribution.md
│   ├── 🔮 Next-Token-Prediction.md
│   ├── 🔄 Autoregressive-Generation.md
│   ├── 🥇 Greedy-Decoding.md
│   ├── 🌡️ Temperature.md
│   ├── 🔝 Top-K-Sampling.md
│   ├── 🫧 Top-P-Sampling.md
│   ├── 🛑 Stopping-Generation.md
│   └── ✨ Complete-Generation-Process.md
│
├── 📁 08-Complete-LLM/
│   ├── 📄 README.md
│   ├── 🧠 Complete-LLM-Architecture.md
│   ├── 🎓 Complete-Training-Pipeline.md
│   ├── 🚀 Complete-Inference-Pipeline.md
│   ├── 🔄 Complete-Data-Flow.md
│   ├── 🆚 Training-vs-Inference.md
│   ├── 📝 Text-to-Tokens.md
│   ├── 🔢 Tokens-to-Representation.md
│   ├── 🧩 Representation-to-Transformer.md
│   ├── 🎯 Transformer-to-Prediction.md
│   ├── ✨ Prediction-to-Generated-Text.md
│   └── 🏗️ LLM-From-Zero.md
│
└── 📄 README.md
```

> 💡 Each folder represents one major stage of the learning process, while each Markdown file focuses on a specific concept.

---

# 01️⃣ Introduction to LLMs

### 📁 `01-Introduction-to-LLMs/`

The journey starts with the most fundamental question:

> 🧠 **What exactly is an LLM?**

### 📚 Topics

* 🧠 What is an LLM?
* 📚 What is a Language Model?
* ❓ Why do we need LLMs?
* ⚙️ How do LLMs work at a high level?
* 🆚 LLM vs Traditional Language Models
* 🆚 LLM vs NLP
* 🆚 LLM vs Generative AI
* 🆚 LLM vs Chatbot
* 📏 Small Language Models vs Large Language Models
* 🏛️ Foundation Models
* 🤖 What is GPT?
* ⚡ Capabilities of LLMs
* ⚠️ Limitations of LLMs

### 🎯 Objective

Build the basic mental model required to understand everything that follows.

---

# 02️⃣ Text and Tokenization

### 📁 `02-Text-and-Tokenization/`

An LLM cannot directly process raw human language.

So the next question is:

> 📝 **How does human language become something a model can process?**

### 📚 Topics

* 📝 How LLMs process text
* 📚 Vocabulary
* 🔤 What is a Token?
* ✂️ Tokenization
* 🔡 Character-Level Tokenization
* 📝 Word-Level Tokenization
* 🧩 Subword Tokenization
* ⚙️ Byte Pair Encoding
* 🔢 Token IDs
* 🏷️ Special Tokens
* 📏 Sequence
* 🪟 Context Window
* 🔄 Text to Model Input

### 🔄 Core Flow

```text
📝 Human Text
      │
      ▼
✂️ Tokenizer
      │
      ▼
🔤 Tokens
      │
      ▼
🔢 Token IDs
      │
      ▼
🧠 Model Input
```

### 🎯 Objective

Understand how human language is transformed into numerical input for an LLM.

---

# 03️⃣ LLM Architecture

### 📁 `03-LLM-Architecture/`

Now that we understand how text enters the model, we can ask:

> 🏗️ **What is actually inside an LLM?**

### 📚 Topics

* 🧠 What is inside an LLM?
* 📥 Input Representation
* 🔢 Token Embeddings
* 📍 Positional Information
* 🧩 Transformer Blocks
* 👀 Attention
* 🧠 Feed-Forward Network
* 📤 Output Layer
* 🔄 How the Components Connect
* 🏗️ High-Level LLM Architecture

### 🧭 Architecture Overview

```text
📝 Text
   │
   ▼
🔤 Tokenization
   │
   ▼
🔢 Token IDs
   │
   ▼
🔢 Embeddings
   │
   ▼
📍 Positional Information
   │
   ▼
🧩 Transformer Blocks
   │
   ▼
📤 Output
   │
   ▼
🎯 Next Token
```

### 🎯 Objective

Create a complete high-level blueprint of an LLM before studying its components in depth.

---

# 04️⃣ Transformer

### 📁 `04-Transformer/`

🔥 The Transformer is the architectural foundation behind modern LLMs.

This section goes deeper into the individual components that make up the Transformer.

### 📚 Topics

* ❓ Why Transformers?
* 🏗️ Transformer Architecture
* 👀 Attention Mechanism
* 🔍 Self-Attention
* 🔑 Query, Key, and Value
* 🎯 Attention Scores
* 🎭 Attention Masking
* 🧠 Multi-Head Attention
* 📍 Positional Information
* 🧮 Feed-Forward Network
* ➕ Residual Connections
* 📏 Layer Normalization
* 🧩 Transformer Block
* 📥 Encoder
* 📤 Decoder
* 🔄 Encoder-Decoder Architecture
* 🏗️ Complete Transformer

### 🧩 Transformer Block

```text
             🧩 Transformer Block
                      │
                      ▼
             👀 Self-Attention
                      │
                      ▼
              ➕ Residual Connection
                      │
                      ▼
               📏 Layer Norm
                      │
                      ▼
             🧠 Feed-Forward Network
                      │
                      ▼
              ➕ Residual Connection
                      │
                      ▼
               📏 Layer Norm
                      │
                      ▼
                   📤 Output
```

### 🎯 Objective

Understand how individual components combine to create a Transformer block and how multiple blocks form a Transformer architecture.

---

# 05️⃣ Decoder-Only Transformer

### 📁 `05-Decoder-Only-Transformer/`

Now we connect the general Transformer architecture to GPT-style language models.

The key question is:

> 🤖 **How does a Transformer become a decoder-only LLM?**

### 📚 Topics

* 🆚 Encoder vs Decoder
* ❓ Why Decoder-Only Architecture?
* 👀 Causal Self-Attention
* 🎭 Causal Masking
* 🧩 Decoder-Only Architecture
* 🏗️ Transformer Block Inside an LLM
* 🔄 Stacking Transformer Blocks
* 📤 Final Output
* 🧠 Language Modeling Head
* 🤖 GPT-Style Architecture

### 🏗️ GPT-Style Architecture

```text
📝 Input Text
      │
      ▼
✂️ Tokenizer
      │
      ▼
🔢 Token IDs
      │
      ▼
🔢 Token Embeddings
      │
      ▼
📍 Positional Information
      │
      ▼
┌─────────────────────┐
│ 🧩 Transformer Block │
└─────────────────────┘
      │
      ▼
┌─────────────────────┐
│ 🧩 Transformer Block │
└─────────────────────┘
      │
      ▼
┌─────────────────────┐
│ 🧩 Transformer Block │
└─────────────────────┘
      │
      ▼
       ...
      │
      ▼
🧠 Language Modeling Head
      │
      ▼
📊 Logits
      │
      ▼
🎯 Next Token
```

### 🎯 Objective

Understand how a decoder-only Transformer forms the core architecture of GPT-style LLMs.

---

# 06️⃣ Training an LLM

### 📁 `06-Training-an-LLM/`

An architecture alone does not understand language.

The model must learn patterns from training data.

The central learning task is:

> 🎯 **Predict the next token.**

### 📚 Topics

* 🧠 What Does an LLM Learn?
* 📚 Training Data
* 🧹 Data Preparation
* 🔤 Training Data Tokenization
* 🧩 Training Sequences
* ↔️ Input and Target
* 🎯 Next-Token Prediction
* ▶️ Forward Pass
* 📉 Loss
* 🔄 Backpropagation
* ⚙️ Optimizer
* 🔧 Parameter Updates
* 📦 Batches
* 🔁 Training Iterations
* 📊 Validation
* 🏁 Complete Training Process

### 🔄 Training Pipeline

```text
📚 Training Data
       │
       ▼
🧹 Data Preparation
       │
       ▼
🔤 Tokenization
       │
       ▼
🧩 Training Sequences
       │
       ▼
↔️ Input + Target
       │
       ▼
🧠 LLM
       │
       ▼
🎯 Prediction
       │
       ▼
📉 Loss
       │
       ▼
🔄 Backpropagation
       │
       ▼
⚙️ Optimizer
       │
       ▼
🔧 Parameter Update
       │
       ▼
🔁 Repeat
       │
       ▼
🧠 Trained LLM
```

### 🎯 Objective

Understand how an untrained Transformer learns language patterns through repeated next-token prediction and parameter updates.

---

# 07️⃣ Text Generation

### 📁 `07-Text-Generation/`

The model has now been trained.

But how does it actually generate text?

> ✨ **How does an LLM generate one token at a time?**

### 📚 Topics

* 🚀 Inference
* 📝 Prompt to Tokens
* 🧠 Forward Pass During Inference
* 📊 Logits
* 🎯 Probability Distribution
* 🔮 Next-Token Prediction
* 🔄 Autoregressive Generation
* 🥇 Greedy Decoding
* 🌡️ Temperature
* 🔝 Top-K Sampling
* 🫧 Top-P Sampling
* 🛑 Stopping Generation
* ✨ Complete Text Generation Process

### ✨ Generation Pipeline

```text
📝 Prompt
    │
    ▼
🔤 Tokenization
    │
    ▼
🔢 Token IDs
    │
    ▼
🧠 Decoder-Only LLM
    │
    ▼
📊 Logits
    │
    ▼
🎯 Probability Distribution
    │
    ▼
🔮 Select Next Token
    │
    ▼
➕ Add Token
    │
    ▼
🧠 Run Model Again
    │
    ▼
🔮 Select Next Token
    │
    ▼
🔄 Repeat
    │
    ▼
✨ Generated Text
```

### 🎯 Objective

Understand autoregressive text generation and how decoding strategies influence the generated output.

---

# 08️⃣ Complete LLM

### 📁 `08-Complete-LLM/`

🏁 This is where everything comes together.

The final section connects the complete architecture, training pipeline, inference process, and data flow.

### 📚 Topics

* 🧠 Complete LLM Architecture
* 🎓 Complete Training Pipeline
* 🚀 Complete Inference Pipeline
* 🔄 Complete Data Flow
* 🆚 Training vs Inference
* 📝 Text to Tokens
* 🔢 Tokens to Representation
* 🧩 Representation to Transformer
* 🎯 Transformer to Prediction
* ✨ Prediction to Generated Text
* 🏗️ Complete LLM From Zero

---

# 🔄 Complete LLM Flow

```text
                         🧠 LLM
                           │
              ┌────────────┴────────────┐
              │                         │
              ▼                         ▼
        🎓 TRAINING                🚀 INFERENCE
              │                         │
              ▼                         ▼
       📚 Training Data              📝 Prompt
              │                         │
              ▼                         ▼
       🔤 Tokenization             🔤 Tokenization
              │                         │
              ▼                         ▼
        🔢 Token IDs                🔢 Token IDs
              │                         │
              ▼                         ▼
       🧩 Model Input              🧩 Model Input
              │                         │
              ▼                         ▼
      🤖 Decoder-Only LLM       🤖 Decoder-Only LLM
              │                         │
              ▼                         ▼
        🎯 Prediction              🎯 Next Token
              │                         │
              ▼                         ▼
           📉 Loss                 ➕ Add Token
              │                         │
              ▼                         │
      🔄 Backpropagation              │
              │                         │
              ▼                         │
      ⚙️ Parameter Update             │
              │                         │
              ▼                         │
        🧠 Trained LLM               🔄 Repeat
              │                         │
              └────────────┬────────────┘
                           ▼
                    ✨ Generated Text
```

---

# 🗺️ Complete Learning Path

The entire repository follows a deliberate progression.

```text
01️⃣ Introduction to LLMs
              │
              ▼
02️⃣ Text and Tokenization
              │
              ▼
03️⃣ LLM Architecture
              │
              ▼
04️⃣ Transformer
              │
              ▼
05️⃣ Decoder-Only Transformer
              │
              ▼
06️⃣ Training an LLM
              │
              ▼
07️⃣ Text Generation
              │
              ▼
08️⃣ Complete LLM
```

Each stage depends on the concepts introduced before it.

The purpose is not to memorize isolated definitions.

The purpose is to gradually build one connected mental model.

---

# 🚫 What This Repository Does Not Cover

This project intentionally stays focused on the **core construction and understanding of a Transformer-based LLM**.

The following topics are outside the current scope:

* 🚫 RAG
* 🚫 AI Agents
* 🚫 Tool Calling
* 🚫 Vector Databases
* 🚫 Embedding Search Systems
* 🚫 Chatbot Development
* 🚫 LLM Applications
* 🚫 Prompt Engineering
* 🚫 Deployment
* 🚫 APIs
* 🚫 LangChain
* 🚫 LangGraph
* 🚫 Production Infrastructure
* 🚫 Cloud Deployment
* 🚫 UI and Frontend Development

These technologies are part of the broader LLM ecosystem, but they are not required for understanding the fundamental construction of a Transformer-based LLM.

---

# 📐 Mathematics

Mathematics is intentionally kept separate from the initial conceptual structure.

The primary learning path focuses on:

```text
🧠 Concept
    │
    ▼
🏗️ Architecture
    │
    ▼
🔄 Data Flow
    │
    ▼
🎓 Training
    │
    ▼
✨ Generation
```

Detailed mathematical derivations can be introduced later.

Potential future topics include:

* 📐 Vector Representations
* 🔢 Matrix Operations
* ✖️ Dot Products
* 👀 Attention Calculations
* 📊 Softmax
* 📉 Cross-Entropy Loss
* 📈 Gradient Descent
* 🔄 Backpropagation
* ⚙️ Parameter Updates

---

# 💻 Implementation Status

## 🚧 Current Version

The current repository is **theory-focused**.

```text
📚 Theory
   │
   ▼
🏗️ Architecture
   │
   ▼
🔄 Data Flow
```

There is currently no complete implementation.

---

## 🔜 Future Implementation

The implementation phase will follow the same conceptual progression.

```text
📚 Theory
    │
    ▼
🧪 Small Experiments
    │
    ▼
🔬 Component Implementation
    │
    ▼
👀 Attention Implementation
    │
    ▼
🤖 Transformer Implementation
    │
    ▼
🧩 Decoder-Only LLM
    │
    ▼
🎓 Training
    │
    ▼
✨ Text Generation
```

The goal is to understand each component before combining everything into a complete model.

---

# 🛠️ Future Technology Stack

The implementation phase may use the following technologies:

| Technology          | Purpose                                       |
| ------------------- | --------------------------------------------- |
| 🐍 **Python**       | Core implementation                           |
| 🔢 **NumPy**        | Numerical operations and tensor concepts      |
| 🔥 **PyTorch**      | Neural network and Transformer implementation |
| 🤗 **Hugging Face** | Tokenization and model ecosystem where useful |
| 📊 **Matplotlib**   | Visualizations and experiments                |

> ⚠️ The technology stack is not part of the current theoretical implementation and may evolve as the project develops.

---

# 🌱 What This Repository Will Become

The long-term goal is to evolve the repository from a theory-first resource into a complete learning and implementation project.

```text
📚 THEORY
    +
💻 IMPLEMENTATION
    +
🧪 EXPERIMENTS
    +
📊 VISUALIZATIONS
```

Eventually, the repository should allow a learner to follow the complete journey:

```text
📝 Raw Text
      │
      ▼
🔤 Tokenization
      │
      ▼
🔢 Token IDs
      │
      ▼
🧩 Token Representation
      │
      ▼
🤖 Transformer
      │
      ▼
🧠 Decoder-Only Architecture
      │
      ▼
🎓 Training
      │
      ▼
🧠 Trained LLM
      │
      ▼
✨ Text Generation
```

---

# 🚀 Project Vision

LLM From Zero is built around one central idea:

> **Don't just use an LLM. Understand what is happening inside it.**

This repository is not about learning how to call an existing LLM API.

It is about answering a deeper question:

> 🧠 **How does an LLM actually work, and how can we build one from the ground up?**

The project aims to break down the construction of a Transformer-based LLM into understandable stages so that the complete system can eventually be viewed as one connected pipeline.

---

# 📊 Project Status

| Component                   | Status         |
| --------------------------- | -------------- |
| 🧠 LLM Introduction         | 🟢 Available   |
| 📝 Text and Tokenization    | 🟢 Theoretical |
| 🏗️ LLM Architecture        | 🟢 Theoretical |
| 🤖 Transformer              | 🟢 Theoretical |
| 🧩 Decoder-Only Transformer | 🟢 Theoretical |
| 🎓 LLM Training             | 🟢 Theoretical |
| ✨ Text Generation           | 🟢 Theoretical |
| 🧠 Complete LLM             | 🟢 Theoretical |
| 💻 Coding Implementation    | 🟡 Coming Soon |
| 🧪 Experiments              | 🟡 Coming Soon |
| 📊 Visualizations           | 🟡 Coming Soon |

---

# 🌌 From Zero to LLM

```text
🧠 Understand
      │
      ▼
🔍 Break It Down
      │
      ▼
🔗 Connect the Concepts
      │
      ▼
💻 Build It
      │
      ▼
🎓 Train It
      │
      ▼
✨ Generate With It
```

---

## 🧠 LLM From Zero

**Understand it. Break it down. Build it. Train it. Generate with it.**

A theory-first journey into the internal construction of Transformer-based Large Language Models.
