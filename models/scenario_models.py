from pydantic import BaseModel
from typing import List, Dict


class Choice(BaseModel):
    """
    A single option the learner can choose.
    """

    choice_id: str

    text: str

    consequence: str

    next_node: str

    competency_effects: Dict[str, int]


class Node(BaseModel):
    """
    One decision point in the scenario.
    """

    node_id: str
     
    state_type: str

    situation: str

    choices: List[Choice]

class Outcome(BaseModel):
    outcome_id: str
    title: str
    description: str
    business_impact: str    


class Scenario(BaseModel):
    scenario_id: str

    scenario_name: str

    target_icp: str

    role: str

    industry: str

    difficulty: str # beginner/intermediate/advanced

    estimated_duration: int

    learning_skills: List[str]

    start_node: str

    nodes: List[Node]

    outcomes: List[Outcome]