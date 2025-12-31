# **Instructor Test Plan – Counter-Factual Scenario Generator

## 1. Objective of This Test Plan

The purpose of this test plan is to allow an instructor or evaluator to:

* Verify that the system runs correctly
* Confirm that **exactly 10 counter-factual scenarios** are generated
* Validate that outputs are **divergent, structured, and constrained**
* Gain confidence that the project meets all stated requirements

No code modification is required to execute this test.

---

## 2. System Prerequisites

Before starting the test, ensure:

* Windows OS
* Python 3.9+
* Internet connectivity
* Valid OpenAI API key
* Project folder cloned or downloaded

---

## 3. PowerShell Windows Required

### **Total PowerShell windows required: 2**

| Window       | Purpose                      |
| ------------ | ---------------------------- |
| PowerShell-1 | Run the FastAPI server       |
| PowerShell-2 | Run test scripts / API calls |

No additional terminals are required.

---

## 4. Pre-Test Setup (MANDATORY)

### Step 1: Navigate to Project Root

In **PowerShell-1**:

```powershell
cd path\to\project\root
```

(Example: `dse-counterfactual-engine`)

---

### Step 2: Verify Environment Variable

Ensure `.env` file exists in project root:

```text
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxx
```

Without this, the system will not generate outputs.

---

### Step 3: Start the API Server

In **PowerShell-1**, run:

```powershell
uvicorn app.main:app --reload
```

Expected output:

```
INFO:     Uvicorn running on http://127.0.0.1:8000
```

☑ Leave this window **open and running**.

---

## 5. Test Execution (Instructor Actions)

All tests below are run from **PowerShell-2**.

---

## 6. Core Functional Test (MANDATORY)

### Test Case 1 – Basic Generation Test

**Purpose:**
Verify that the system generates exactly 10 scenarios.

**Command to run:**

```powershell
$response = Invoke-RestMethod -Method Post `
  -Uri "http://127.0.0.1:8000/generate?concept=Cultural Drift"

$response.scenarios.Count
```

**Expected Result:**

```
10
```

✔ Confirms scenario count enforcement
✔ Confirms API is functioning

---

## 7. Output Quality Test (Instructor Review)

### Test Case 2 – Inspect Generated Scenarios

Run:

```powershell
$response.scenarios
```

Instructor should verify manually:

* Exactly **10 scenarios**
* Most begin with **“What if” / “Why not”**
* No explanations or summaries
* Each scenario explores a **different mechanism**
* No repeated reasoning pattern

☑ Passing this test confirms **divergence and novelty**

---

## 8. Stress Test (Instructor Choice)

### Test Case 3 – Abstract Concept Test

**Purpose:**
Ensure system handles abstract concepts.

Run:

```powershell
Invoke-RestMethod -Method Post `
  -Uri "http://127.0.0.1:8000/generate?concept=Power Legitimacy"
```

Expected behavior:

* System responds without error
* Still produces 10 scenarios
* Scenarios remain counter-factual

---

## 9. Maximum Scenario Validation Test

### Test Case 4 – Attempt to Break Constraint

Instructor may try **multiple concepts sequentially**, e.g.:

```powershell
Invoke-RestMethod -Method Post `
  -Uri "http://127.0.0.1:8000/generate?concept=Invisible Consent"
```

Observation:

* System **never produces more or fewer than 10 scenarios**
* Confirms validation enforcement

---

## 10. Failure Handling (Optional Observation)

If the LLM output violates constraints internally:

* The system **regenerates automatically**
* Instructor does **not see invalid output**

This demonstrates **robustness by design**, not prompt reliance.

---

## 11. Test Completion Criteria

The instructor can consider the system **SUCCESSFUL** if:

* API starts without error
* All test calls return exactly 10 scenarios
* Outputs are divergent and non-repetitive
* No manual intervention is required
* System behaves consistently across multiple concepts

---

## 12. Instructor-Safe Explanation (If Asked)

You may state **verbatim**:

> “The system enforces structural and semantic constraints through post-generation validation and regeneration, ensuring consistent output despite probabilistic LLM behavior.”

---

## 13. Summary

| Item                      | Result              |
| ------------------------- | ------------------- |
| PowerShell windows needed | 2                   |
| Pre-test setup required   | Minimal             |
| Code changes needed       | None                |
| Manual judgment required  | Output quality only |
| Satisfaction level        | High                |

---

### End of Test Plan


