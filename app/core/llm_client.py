import os
import re
from typing import List
from openai import OpenAI

from app.core.validator import validate_dse_output


class OpenAILLMClient:
    """
    LLM client with output validation + controlled regeneration
    for Divergent Scenario Engine (DSE).
    """

    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def generate(self, prompt: str, max_attempts: int = 2) -> List[str]:
        """
        Generate exactly 10 counter-factual scenarios.
        Applies validation and regenerates if constraints are violated.
        """

        last_text = None

        for attempt in range(max_attempts):
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You generate counter-factual scenarios that are "
                            "declarative, mechanism-focused, and structurally valid."
                        ),
                    },
                    {"role": "user", "content": prompt},
                ],
                temperature=1.1,          # encourage divergence
                top_p=0.9,
            )

            text = response.choices[0].message.content.strip()
            last_text = text

            # Apply hard validation
            if validate_dse_output(text):
                return self._parse_scenarios(text)

        # Fallback: return best-effort output (documented limitation)
        return self._parse_scenarios(last_text)

    def _parse_scenarios(self, text: str) -> List[str]:
        """
        Extract numbered scenarios and return first 10 clean items.
        """
        lines = []
        for line in text.split("\n"):
            line = line.strip()
            if re.match(r"^\d+\.", line):
                cleaned = re.sub(r"^\d+\.\s*", "", line)
                lines.append(cleaned)

        return lines[:10]
