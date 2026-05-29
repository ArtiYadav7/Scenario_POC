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

    score_delta: Dict[str, int]


class Node(BaseModel):
    """
    One decision point in the scenario.
    """

    node_id: str

    situation: str

    choices: List[Choice]


class Scenario(BaseModel):
    """
    Complete scenario definition.
    """

    scenario_id: str

    scenario_name: str

    target_icp: str

    learning_objective: List[str]

    start_node: str

    nodes: List[Node]