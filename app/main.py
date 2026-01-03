from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from app.core.llm_client import OpenAILLMClient

app = FastAPI()
llm = OpenAILLMClient()

@app.post("/generate")
def generate(concept: str):
    prompt = f"""
You are a Divergent Scenario Engine.

Given a single concept, generate exactly 10 counter-factual scenarios.

Rules:
- At least 7 scenarios must begin with "What if" or "Why not"
- Do NOT explain the concept
- Do NOT add learning goals, questions, or summaries
- Each scenario must explore a different causal mechanism, incentive structure, or system failure mode
- Avoid reusing the same reasoning pattern or structural template across scenarios
- Avoid broad domains like art, food, religion, education unless they emerge indirectly from system-level effects
- Every scenario must explicitly describe how the process of cultural drift itself changes (rate, direction, lock-in, reversibility, or selection)
- Output ONLY a numbered list from 1 to 10

CONCEPT: {concept}
"""

    scenarios = llm.generate(prompt)
    return {"concept": concept, "scenarios": scenarios}

