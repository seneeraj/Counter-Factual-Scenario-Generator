from pydantic import BaseModel, Field
from typing import List

class Scenario(BaseModel):
    id: int = Field(..., ge=1, le=10)
    text: str = Field(..., min_length=10)

class ScenarioResponse(BaseModel):
    concept: str
    scenarios: List[Scenario]

    def validate_count(self):
        if len(self.scenarios) != 10:
            raise ValueError("Exactly 10 scenarios are required")
