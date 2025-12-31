# Counter-Factual Scenario Generator

## Overview

The **Counter-Factual Scenario Generator** is a system that generates **counter-factual, divergent scenarios** from a single input concept.
Unlike summarization or explanation models, DSE focuses on **mechanism-level divergence**, exploring how a concept may evolve under different causal pressures, incentive structures, and system failure modes.

The system exposes a **FastAPI endpoint** that returns **exactly 10 structured scenarios** per request.

---

## Key Capabilities

* Generates **exactly 10 counter-factual scenarios**
* Enforces **structural and semantic constraints**
* Encourages **divergent, non-obvious reasoning**
* Implements **output validation + regeneration**
* JSON-based API for easy integration
* Designed with **robustness over prompt-only reliance**

---

## Architecture

```
User Concept
   ↓
FastAPI Endpoint
   ↓
Prompt Construction
   ↓
LLM Generation
   ↓
Validation & Regeneration
   ↓
Structured JSON Output
```

### Why Validation Matters

Instruction-tuned LLMs are known to violate soft constraints (e.g., asking questions, adding explanations).
To mitigate this, DSE applies **post-generation validation** and **controlled regeneration**, ensuring outputs adhere to required structure and intent.

This mirrors **industry-standard LLM deployment practices**.

---

## Project Structure

```
dse-counterfactual-engine/
│
├── app/
│   ├── main.py
│   ├── core/
│   │   ├── llm_client.py     # LLM generation + regeneration
│   │   ├── validator.py      # Hard constraint enforcement
│   │
│   └── schemas/
│
├── requirements.txt
├── README.md
├── .gitignore
└── LICENSE
```

---

## Installation

### 1. Clone the Repository

```bash
git clone <repo-url>
cd dse-counterfactual-engine
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Environment Variable

Create a `.env` file:

```
OPENAI_API_KEY=your_api_key_here
```

Or set it in your shell session.

---

## Running the API

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

Server will be available at:

```
http://127.0.0.1:8000
```

API documentation:

```
http://127.0.0.1:8000/docs
```

---

## Example Usage

### PowerShell (Windows)

```powershell
Invoke-RestMethod -Method Post `
  -Uri "http://127.0.0.1:8000/generate?concept=Cultural Drift"
```

### Sample Response

```json
{
  "concept": "Cultural Drift",
  "scenarios": [
    "What if cultural drift accelerated due to...",
    "Why not cultural drift slow when...",
    "... (total 10 scenarios)"
  ]
}
```

---

## Constraint Enforcement

Each response is validated against the following rules:

* Exactly **10 scenarios**
* At least **7** begin with *“What if”* or *“Why not”*
* No explanations, summaries, or learning goals
* No interrogative (`?`) framing
* Mechanism-level focus (rate, lock-in, selection, direction)
* Regeneration applied if validation fails

If all regeneration attempts fail, the system returns the best available output and logs the limitation.

---

## Known Limitations

* Instruction-tuned LLMs may occasionally revert to academic or interrogative phrasing.
* LoRA fine-tuning biases generation but does not fully override base model priors.
* Perfect enforcement of abstract counter-factual reasoning is not guaranteed.

These limitations are **explicitly acknowledged** and mitigated via validation logic.

---

## Technologies Used

* Python
* FastAPI
* OpenAI API
* Custom validation logic
* Controlled regeneration strategies

---

## License

This project is released under the **MIT License**.

---

## Final Note

This repository represents a **robust, defensible implementation** of a Divergent Scenario Engine, prioritizing **engineering reliability**, **constraint enforcement**, and **transparent limitations** over prompt-only claims of perfection.

Author:
Neeraj Bhatia
Ask Me Anything

